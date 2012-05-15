"""Base class for AO simulation modules"""
#$Id: aobase.py,v 1.36 2009/05/11 18:19:00 ali Exp $
import threading,thread,os,sys,getopt,types
import socket, string
import util.rwlock
import Scientific.MPI as MPI
import base.dataType
#import fwdMsg

class aobase:
    """Base class for all AO simulation science modules.  Science modules
    should extend this base class, which provides default functionality.
    
    Class variables (important for simulation programmer)
     - parent - object, the predecessor (parent) object from which data is obtained.
     - idstr - string, ID string, used when parsing parameter file to determine the order in which various modules within the file are parsed.
     - debug - anything, if not none, debug messages will be printed.
    Class variables (no importance for simulation programmer)
     - inputData - the data obtained from the predecessor (parent) object.  This can be type either Numeric.ArrayType or None to work with SHM/MPI communications.
     - outputData - the data generated by this science object and returned to any sucecessor (child) objects, Numeric array or None type.
     - rank - int, the MPI rank.  Not used for much at the moment.
     - moduleName - string, the name of the science module that extends this class.
     - objID - string, moduleName+"_"+idstr.
     - myID - string, socket hostname+modulename.
     - version - float, determines whether the module prefers curry or chinese
     - selfModifiesInput - int, Not used, but was inteded to be used if the input data is modified inplace.  The correct thing to do instead is to make a copy of the input data if you intend to change it.
     - config - instance, of configuration object
    @cvar parent: predecessor (parent) object producing data
    @type parent: instance
    @cvar inputData: Data from parent object
    @type inputData: None or Numeric array
    @cvar outputData: Data produced by this module
    @type outputData: None or Numeric array
    @cvar dataValid: Whether the data in outputData is valid
    @type dataValid: Int
    @cvar newDataWaiting: Whether expecting new data from parent object
    @type newDataWaiting: Int
    @cvar generate: Whether to generate data this iteration
    @type generate: Int
    @cvar rank: MPI rank
    @type rank: Int
    @cvar idstr: ID string used when parsing parameter file
    @type idstr: String
    @cvar debug: If not None, debug messages will be printed
    @type debug: None or anything
    @cvar moduleName: Name of module
    @type moduleName: String
    @cvar objID: Module name + "_" + idstr
    @type objID: String
    @cvar myID: socket hostname + modulename
    @type myID: String
    @cvar version: Determines whether module prefers curry or chinese
    @type version: Float
    @cvar selfModifiesInput: Not used
    @type selfModifiesInput: Int
    @cvar config: Configuration object
    @type config: Instance
    """
    def __init__(self,parent,config,args={},forGUISetup=0,debug=None,idstr=None):
        """
        Create a simulation object base class.
        Arguments\n
        Parent - The object that provides data for this modules calculations.\n
        config - A configuration object with at least a .getVal("string") method.\n
        args - optional arguments as a dictionary.  Keys can include "version" (does nothing) and "idstr" which is used when searching the XML configuration file.  This idstr will be appended to the module name, and then when parsing the XML parameter file, modules with this appended idstr will be searched for a variable first.\n
        forGUISetup - Not currently used, reserved for future use.\n
        When resource sharing is mentioned, this means the ability to use one object for the calculations of many objects, ie this object will be called several times per iteration.  This allows large memory arrays to be reused.\n


        Note, input and output data should probably only be Numeric arrays or
        None values (or numarray, though not currently supported and tested).
        If you are very careful, you could use other things such as lists etc,
        though errors would then occur when these are send over shm or mpi.
        If forGUISetup==1, then not necessary to set up everything for the
        simulation - just enough to be able to provide info for the GUI.
        args is a dictionary of various arguments that can be used,
        e.g. version, v, idstr.\n\n

    

        @param parent: Parent object which provides data
        @type parent: Dict or Object
        @param config: Configuration object with getVal method.
        @type config: base.readConfig.AOXml
        @param args: Dictionary of optional arguments, currently, keys can be "idstr" (value, the idstr) and "version" (not used)
        @type args: Dictionary
        @param forGUISetup: Flag to be implemnted in the future
        @type forGUISetup: int
        @param debug: If not None, debug messages will be printed
        @type debug: Anything
        @param idstr: ID string.  Same as using args["idstr"], but less typing
        @type idstr: String
        """
        self.parent=parent
        if type(parent)==type([]):
            self.parentList=parent
        else:
            self.parentList=[parent]
        self.debug=debug
        self.inputData=None
        self.outputData=None
        self.dataValid=0
        self.generateNextTime=0.
        self.newDataWaiting=1
        self.generate=1
        #self.getNextLock=0#1
        #self.nextLock=util.rwlock.RWLock()
        self.control={}
        self.rank=MPI.world.rank
        self.idstr=[None]
        self.thisObjList=[]#list of object details when resource sharing is implemented.
        self.sentPlotsCnt=0#used when user calls plottable()...
        self.moduleName=string.split( self.__module__, "." )[-1] 
        self.objID=self.moduleName #can be used in config file if idstr defined
        self.myID=socket.gethostname()+"-"+self.moduleName
        self.version=0.001
        self.currentIdObjCnt=0#used if resource sharing is implemented, this keeps track of the current idstr to use.
        self.selfModifiesInput=0#set to one if the input data is to be
        #modified inplace.  This amoung other things means that parent can't
        #be a splitter.
        #self.busyLock=threading.Lock()#when this is acquired, updateState cannot run... (it is run as a separate thread when called by a pyro object.  This helps with synchronisation of updates...)
        if args.has_key("version"):
            self.version=args["version"]
        if args.has_key("v"):
            print "Version:",self.version
        if args.has_key("idstr"):
            if idstr==None:
                idstr=args["idstr"]
        if idstr!=None:
            if type(idstr)==type(""):
                if len(idstr)>0 and idstr[0]=="[":#its a list of idstr...
                    idlist=eval(idstr)
                    self.idstr=[]
                    for id in idlist:
                        if id!=None:
                            self.idstr.append(str(id))
                        else:
                            self.idstr.append(None)
                else:#its a single idstr
                    if len(idstr)>0:
                        self.idstr=[idstr]
                    else:
                        self.idstr=[None]
            elif type(idstr)==type([]):#its a list of idstr
                self.idstr=[]
                for id in idstr:
                    if len(str(id))>0:
                        self.idstr.append(str(id))
                    else:
                        self.idstr.append(None)
            else:#its a single idstr, convert to string.
                if len(str(idstr)):
                    self.idstr=[str(idstr)]
                else:
                    self.idstr=[None]

        if len(self.idstr)>1 or self.idstr[0]!=None:
            self.myID+="_"+str(self.idstr).replace(" ","")
            self.objID=self.moduleName+"_"+str(self.idstr[0]).replace(" ","")
        searchOrder=[self.moduleName,"globals"]
        self.config=config
        #define the order we want to search modules in the xml param file.
        if self.objID!=self.moduleName:
            searchOrder.insert(0,self.objID)
        #define the search order for the XML parameter file.
        if self.config!=None:
            self.config.setSearchOrder(searchOrder)
    def newParent(self,parent,idstr=None):
        """Sets the parent to a new object.  This should be extended by any
        science object which uses parent in its init method.
        @param parent: New parent object
        @type parent: Dict or Object
        """
        self.parent=parent

    def setGenerate(self,val):
        """Set the generate value,
        @param val: Value to which to set the generate variable
        @type val: int
        """
        self.generate=val
        
    def addNewIdObject(self,parent,idstr):
        """Add a new ID string - for resource sharing
        This should be overridden for objects that allow resource sharing.  For objects that don't, it shouldn't be used.
        Overriding this method should include all that is necessary to read the config file, and get all necessary info set up for this particular idstr.
        """
        self.idstr.append(idstr)
        self.parentList.append(parent)
        self.initialise(parent,idstr)
        return self
    def finalInitialisation(self):
        """This should probably be overridden for objects which allow resource sharing.
        For objects which don't, it can be ignored.
        Overriding should mean this sets up all the arrays that are shared - it can use data from all the idstrs to determine what the biggest array should be, and use this.
        """
        pass

    def initialise(self,parent,idstr):
        """This should be overridden for objects which allow resource sharing.
        Otherwise, it can be ignored.
        This will be called for each idstr during __init__ call, and if
        addNewIdObject() is called.
        Note, initialise is responsible for setting the search order.
        """
        pass

    def endSim(self):
        """This would be overridden, and is called when the simulation mainloop has finished.  Typically used for writing results...
        """
        pass

    def prepareNextIter(self):
        """Should be overridden by objects that allow resource sharing.
        This method is responsible for copying data from the idstr store
        into the main object.  
        """
        pass

    def endThisIter(self):
        """should be overridden by objects that allow resource sharing.
        This is responsible for copying any updated data back from the main object to the storage.
        """
        pass
    
    def doNextIter(self):
        """This is called by the ctrl.mainloop every time the object should compute new data.  This method should not be overridden.  To override, please override the generateNext or calcData methods."""

        self.prepareNextIter()
        self.generateNext()
        self.endThisIter()
        self.currentIdObjCnt=(self.currentIdObjCnt+1)%len(self.idstr)

    def generateNext(self):
        """User science module may overload this.
        This is an example of how to see whether data is valid etc. 
        Places the data from predecessor (parent) object into self.inputData,
        sets some valid flag, and ccalls a calcData method (which should
        be user defined).
        """
        if self.generate==1:
            if self.newDataWaiting:
                if self.parent.dataValid==1:
                    self.inputData=self.parent.outputData#if we alter the data, make a copy first... (not done here)
                    self.dataValid=1
                else:
                    print "Cent: Waiting for data from wfs, but not valid"
                    self.dataValid=0

            if self.dataValid:
                self.calcData()
        else:
            self.dataValid=0

    def calcData(self):
        """Dummy function to be overwridden by science module, which must perform its calculations, placing the result into self.outputData.
        """
        print "aobase: NEED TO OVERRIDE calcData function (debug=%s)"%str(self.debug)
    def getParams(self):
        """Not currently implemented or used, but reserved for future use.\n

        This should be overwridden to give details of the parameters
        required for this module, in the form of {"paramClass":Dictionary,...}
        where paramClass is used to help the user, being e.g. "telescope" or
        "turbulance" etc, which give headings in the setup GUI.  The Dictionary
        is then a dictionary of eg {"paramName":defaultValue,...}, or can be a
        further nested dictionary for subheadings etc (Francois idea).
        These params can then be placed in the config file... if not set by the
        user, the param should still be in config file as default value for
        future reference purposes.
        """
        raise Exception("WARNING: getParams() is a virtual function")
        return {}
    def getInputType(self):
        """Not currently implemented or used, but reserved for future use.\n

        Returns the input needed by this module.  Should be overwritten.
        Should return an instance of dataType class, or a list of dataType objects,
        or None if no input is required."""
        raise Exception("WARNING: getInputType() is a virtual function")
        return None
    def getOutputType(self):
        """Not currently implemented or used, but reserved for future use.\n

        Returns the output needed by this module.  Should be overwritten.
        Should return an instance of dataType, or a list of dataType objects,
        or None if no output is given."""
        raise Exception("WARNING: getOutputType() is a virtual function")
        return None
    def getInitArgs(self):
        """Not currently implemented or used, but reserved for future use.\n

        return a dictionary of parameters that can be passed to init.
        Dictionary key is the parameter name, and dictionary value is a tuple
        of (description, default value).  If there is no default value, then
        the dictionary value is a tuple of (description,).
        """
        raise Exception("WARNING: getInitArgs() is a virtual function")
        return {"parent":("parent object",),"config":("parameter file object",),"args":("arguments to be parsed",None),"forGUISetup":("Initialise bare minimum",0)}
    def plottable(self,objname="$OBJ"):
        """
        Return a XML string which contain the commands to be sent
        over a socket to obtain certain data for plotting.  The $OBJ symbol
        will be replaced by the instance name of the object - e.g.
        if scrn=mkscrns.Mkscrns(...) then $OBJ would be replaced by scrn."""
        #raise Exception("Warning: plottable() is a virtual function")
        #return {"data":"plotdata=$OBJ.data"}
        txt="""<plot title="$NAME Output data" cmd="data=$OBJ.outputData" ret="data" type="pylab" when="rpt"/>\n"""
        txt=txt.replace("$OBJ",objname)
        txt=txt.replace("$NAME",self.objID)
        return txt


            
class resourceSharer:
    """A class that is filled from the parameter file."""
    def __init__(self,parent,config,idstr,moduleName):
        self.parent=parent
        self.idstr=idstr
        self.config=config
        self.moduleName=moduleName
        if idstr!=None and len(str(idstr))>0:
            self.objID=self.moduleName+"_"+str(idstr)
            so=[self.objID,self.moduleName,"globals"]
        else:
            self.objID=self.moduleName
            so=[self.moduleName,"globals"]
        self.config.setSearchOrder(so)
