# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.35
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _numfftw3f
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


FFTW_R2HC = _numfftw3f.FFTW_R2HC
FFTW_HC2R = _numfftw3f.FFTW_HC2R
FFTW_DHT = _numfftw3f.FFTW_DHT
FFTW_REDFT00 = _numfftw3f.FFTW_REDFT00
FFTW_REDFT01 = _numfftw3f.FFTW_REDFT01
FFTW_REDFT10 = _numfftw3f.FFTW_REDFT10
FFTW_REDFT11 = _numfftw3f.FFTW_REDFT11
FFTW_RODFT00 = _numfftw3f.FFTW_RODFT00
FFTW_RODFT01 = _numfftw3f.FFTW_RODFT01
FFTW_RODFT10 = _numfftw3f.FFTW_RODFT10
FFTW_RODFT11 = _numfftw3f.FFTW_RODFT11
FFTW_FORWARD = _numfftw3f.FFTW_FORWARD
FFTW_BACKWARD = _numfftw3f.FFTW_BACKWARD
FFTW_MEASURE = _numfftw3f.FFTW_MEASURE
FFTW_DESTROY_INPUT = _numfftw3f.FFTW_DESTROY_INPUT
FFTW_UNALIGNED = _numfftw3f.FFTW_UNALIGNED
FFTW_CONSERVE_MEMORY = _numfftw3f.FFTW_CONSERVE_MEMORY
FFTW_EXHAUSTIVE = _numfftw3f.FFTW_EXHAUSTIVE
FFTW_PRESERVE_INPUT = _numfftw3f.FFTW_PRESERVE_INPUT
FFTW_PATIENT = _numfftw3f.FFTW_PATIENT
FFTW_ESTIMATE = _numfftw3f.FFTW_ESTIMATE
FFTW_ESTIMATE_PATIENT = _numfftw3f.FFTW_ESTIMATE_PATIENT
FFTW_BELIEVE_PCOST = _numfftw3f.FFTW_BELIEVE_PCOST
FFTW_DFT_R2HC_ICKY = _numfftw3f.FFTW_DFT_R2HC_ICKY
FFTW_NONTHREADED_ICKY = _numfftw3f.FFTW_NONTHREADED_ICKY
FFTW_NO_BUFFERING = _numfftw3f.FFTW_NO_BUFFERING
FFTW_NO_INDIRECT_OP = _numfftw3f.FFTW_NO_INDIRECT_OP
FFTW_ALLOW_LARGE_GENERIC = _numfftw3f.FFTW_ALLOW_LARGE_GENERIC
FFTW_NO_RANK_SPLITS = _numfftw3f.FFTW_NO_RANK_SPLITS
FFTW_NO_VRANK_SPLITS = _numfftw3f.FFTW_NO_VRANK_SPLITS
FFTW_NO_VRECURSE = _numfftw3f.FFTW_NO_VRECURSE
FFTW_NO_SIMD = _numfftw3f.FFTW_NO_SIMD
fftwf_malloc = _numfftw3f.fftwf_malloc
fftwf_free = _numfftw3f.fftwf_free
fftwf_execute = _numfftw3f.fftwf_execute
fftwf_destroy_plan = _numfftw3f.fftwf_destroy_plan
fftwf_cleanup = _numfftw3f.fftwf_cleanup
fftwf_flops = _numfftw3f.fftwf_flops
fftwf_print_plan = _numfftw3f.fftwf_print_plan
fftwf_fprint_plan = _numfftw3f.fftwf_fprint_plan
fftwf_plan_dft_1d = _numfftw3f.fftwf_plan_dft_1d
fftwf_plan_dft_2d = _numfftw3f.fftwf_plan_dft_2d
fftwf_plan_dft_3d = _numfftw3f.fftwf_plan_dft_3d
fftwf_plan_dft = _numfftw3f.fftwf_plan_dft
fftwf_plan_guru_dft = _numfftw3f.fftwf_plan_guru_dft
fftwf_execute_dft = _numfftw3f.fftwf_execute_dft
fftwf_plan_guru_split_dft = _numfftw3f.fftwf_plan_guru_split_dft
fftwf_execute_split_dft = _numfftw3f.fftwf_execute_split_dft
fftwf_plan_dft_r2c_1d = _numfftw3f.fftwf_plan_dft_r2c_1d
fftwf_plan_dft_r2c_2d = _numfftw3f.fftwf_plan_dft_r2c_2d
fftwf_plan_dft_r2c_3d = _numfftw3f.fftwf_plan_dft_r2c_3d
fftwf_plan_dft_r2c = _numfftw3f.fftwf_plan_dft_r2c
fftwf_plan_many_dft_r2c = _numfftw3f.fftwf_plan_many_dft_r2c
fftwf_plan_guru_dft_r2c = _numfftw3f.fftwf_plan_guru_dft_r2c
fftwf_execute_dft_r2c = _numfftw3f.fftwf_execute_dft_r2c
fftwf_plan_guru_split_dft_r2c = _numfftw3f.fftwf_plan_guru_split_dft_r2c
fftwf_execute_split_dft_r2c = _numfftw3f.fftwf_execute_split_dft_r2c
fftwf_plan_dft_c2r_1d = _numfftw3f.fftwf_plan_dft_c2r_1d
fftwf_plan_dft_c2r_2d = _numfftw3f.fftwf_plan_dft_c2r_2d
fftwf_plan_dft_c2r_3d = _numfftw3f.fftwf_plan_dft_c2r_3d
fftwf_plan_dft_c2r = _numfftw3f.fftwf_plan_dft_c2r
fftwf_plan_many_dft_c2r = _numfftw3f.fftwf_plan_many_dft_c2r
fftwf_plan_guru_dft_c2r = _numfftw3f.fftwf_plan_guru_dft_c2r
fftwf_execute_dft_c2r = _numfftw3f.fftwf_execute_dft_c2r
fftwf_plan_guru_split_dft_c2r = _numfftw3f.fftwf_plan_guru_split_dft_c2r
fftwf_execute_split_dft_c2r = _numfftw3f.fftwf_execute_split_dft_c2r
fftwf_plan_r2r_1d = _numfftw3f.fftwf_plan_r2r_1d
fftwf_plan_r2r_2d = _numfftw3f.fftwf_plan_r2r_2d
fftwf_plan_r2r_3d = _numfftw3f.fftwf_plan_r2r_3d
fftwf_plan_r2r = _numfftw3f.fftwf_plan_r2r
fftwf_plan_many_r2r = _numfftw3f.fftwf_plan_many_r2r
fftwf_plan_guru_r2r = _numfftw3f.fftwf_plan_guru_r2r
fftwf_execute_r2r = _numfftw3f.fftwf_execute_r2r
fftwf_export_wisdom_to_file = _numfftw3f.fftwf_export_wisdom_to_file
fftwf_export_wisdom_to_string = _numfftw3f.fftwf_export_wisdom_to_string
fftwf_export_wisdom = _numfftw3f.fftwf_export_wisdom
fftwf_import_system_wisdom = _numfftw3f.fftwf_import_system_wisdom
fftwf_import_wisdom_from_file = _numfftw3f.fftwf_import_wisdom_from_file
fftwf_import_wisdom_from_string = _numfftw3f.fftwf_import_wisdom_from_string
fftwf_import_wisdom = _numfftw3f.fftwf_import_wisdom
fftwf_forget_wisdom = _numfftw3f.fftwf_forget_wisdom


