# encoding: utf-8
# module gi._gi
# by generator 1.147
# no doc

# imports
from gobject import GBoxed, GInterface, GPointer, GType, Warning

import enum as __enum
import gi as __gi
import gobject as __gobject


# Variables with simple values

G_MAXDOUBLE = 1.7976931348623157e+308
G_MAXFLOAT = 3.4028234663852886e+38
G_MAXINT = 2147483647
G_MAXLONG = 2147483647
G_MAXOFFSET = 9223372036854775807
G_MAXSHORT = 32767
G_MAXSIZE = 18446744073709551615
G_MAXSSIZE = 9223372036854775807
G_MAXUINT = 4294967295
G_MAXULONG = 4294967295
G_MAXUSHORT = 65535
G_MINDOUBLE = 2.2250738585072014e-308
G_MINFLOAT = 1.1754943508222875e-38
G_MININT = -2147483648
G_MINLONG = -2147483648
G_MINOFFSET = -9223372036854775808
G_MINSHORT = -32768
G_MINSSIZE = -9223372036854775808

PARAM_READWRITE = 3

SIGNAL_RUN_FIRST = 1

# functions

def add_emission_hook(*args, **kwargs): # real signature unknown
    pass

def enum_add(*args, **kwargs): # real signature unknown
    pass

def enum_register(*args, **kwargs): # real signature unknown
    pass

def flags_add(*args, **kwargs): # real signature unknown
    pass

def flags_register(*args, **kwargs): # real signature unknown
    pass

def hook_up_vfunc_implementation(*args, **kwargs): # real signature unknown
    pass

def io_channel_read(*args, **kwargs): # real signature unknown
    pass

def list_properties(*args, **kwargs): # real signature unknown
    pass

def main_context_query(*args, **kwargs): # real signature unknown
    pass

def new(*args, **kwargs): # real signature unknown
    pass

def pygobject_new_full(*args, **kwargs): # real signature unknown
    pass

def pyos_getsig(*args, **kwargs): # real signature unknown
    pass

def pyos_setsig(*args, **kwargs): # real signature unknown
    pass

def register_foreign(*args, **kwargs): # real signature unknown
    pass

def register_interface_info(*args, **kwargs): # real signature unknown
    pass

def require_foreign(*args, **kwargs): # real signature unknown
    pass

def signal_new(*args, **kwargs): # real signature unknown
    pass

def source_new(*args, **kwargs): # real signature unknown
    pass

def source_set_callback(*args, **kwargs): # real signature unknown
    pass

def spawn_async(argv, envp=None, working_directory=None, flags=0, child_setup=None, user_data=None, standard_input=None, standard_output=None, standard_error=None): # real signature unknown; restored from __doc__
    """
    spawn_async(argv, envp=None, working_directory=None,
                flags=0, child_setup=None, user_data=None,
                standard_input=None, standard_output=None,
                standard_error=None) -> (pid, stdin, stdout, stderr)
    
    Execute a child program asynchronously within a glib.MainLoop()
    See the reference manual for a complete reference.
    """
    pass

def type_register(*args, **kwargs): # real signature unknown
    pass

def variant_type_from_string(*args, **kwargs): # real signature unknown
    pass

def _gvalue_get(*args, **kwargs): # real signature unknown
    pass

def _gvalue_get_type(*args, **kwargs): # real signature unknown
    pass

def _gvalue_set(*args, **kwargs): # real signature unknown
    pass

def _install_metaclass(*args, **kwargs): # real signature unknown
    pass

# classes

from .BaseInfo import BaseInfo
from .ArgInfo import ArgInfo
from .ArrayType import ArrayType
from .Async import Async
from .Boxed import Boxed
from .CallableInfo import CallableInfo
from .CallbackInfo import CallbackInfo
from .CCallback import CCallback
from .ConstantInfo import ConstantInfo
from .Direction import Direction
from .RegisteredTypeInfo import RegisteredTypeInfo
from .EnumInfo import EnumInfo
from .ErrorDomainInfo import ErrorDomainInfo
from .FieldInfo import FieldInfo
from .FieldInfoFlags import FieldInfoFlags
from .FunctionInfo import FunctionInfo
from .FunctionInfoFlags import FunctionInfoFlags
from .Fundamental import Fundamental
from .GEnum import GEnum
from .GFlags import GFlags
from .GObject import GObject
from .GObjectWeakRef import GObjectWeakRef
from .InterfaceInfo import InterfaceInfo
from .ObjectInfo import ObjectInfo
from .Pid import Pid
from .PropertyInfo import PropertyInfo
from .PyGIDeprecationWarning import PyGIDeprecationWarning
from .PyGIWarning import PyGIWarning
from .Repository import Repository
from .RepositoryError import RepositoryError
from .ResultTuple import ResultTuple
from .ScopeType import ScopeType
from .SignalInfo import SignalInfo
from .Struct import Struct
from .StructInfo import StructInfo
from .Transfer import Transfer
from .TypeInfo import TypeInfo
from .TypeTag import TypeTag
from .UnionInfo import UnionInfo
from .UnresolvedInfo import UnresolvedInfo
from .ValueInfo import ValueInfo
from .VFuncInfo import VFuncInfo
from .VFuncInfoFlags import VFuncInfoFlags
# variables with complex values

pygobject_version = (
    3,
    56,
    0,
)

TYPE_GSTRING = None # (!) real value is '<GType GString (4105926720)>'

TYPE_INVALID = None # (!) real value is '<GType invalid (0)>'

_API = None # (!) real value is '<capsule object "gi._API" at 0x000001c5f62d13f0>'

_PyGObject_API = None # (!) real value is '<capsule object "gobject._PyGObject_API" at 0x000001c5f62d1080>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001c5f5dcfba0>'

__path__ = []

__spec__ = None # (!) real value is "ModuleSpec(name='gi._gi', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001c5f5dcfba0>)"

