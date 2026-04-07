# encoding: utf-8
# module gi.repository.GObject
# by generator 1.147
# no doc

# imports
from gi.repository.GLib import (Error, GError, IOCondition, IO_ERR, 
    IO_FLAG_APPEND, IO_FLAG_GET_MASK, IO_FLAG_IS_READABLE, 
    IO_FLAG_IS_SEEKABLE, IO_FLAG_IS_WRITEABLE, IO_FLAG_MASK, IO_FLAG_NONBLOCK, 
    IO_FLAG_SET_MASK, IO_HUP, IO_IN, IO_NVAL, IO_OUT, IO_PRI, IO_STATUS_AGAIN, 
    IO_STATUS_EOF, IO_STATUS_ERROR, IO_STATUS_NORMAL, OPTION_ERROR_BAD_VALUE, 
    OPTION_ERROR_FAILED, OPTION_ERROR_UNKNOWN_OPTION, OPTION_FLAG_FILENAME, 
    OPTION_FLAG_HIDDEN, OPTION_FLAG_IN_MAIN, OPTION_FLAG_NOALIAS, 
    OPTION_FLAG_NO_ARG, OPTION_FLAG_OPTIONAL_ARG, OPTION_FLAG_REVERSE, 
    SPAWN_CHILD_INHERITS_STDIN, SPAWN_DO_NOT_REAP_CHILD, 
    SPAWN_FILE_AND_ARGV_ZERO, SPAWN_LEAVE_DESCRIPTORS_OPEN, SPAWN_SEARCH_PATH, 
    SPAWN_STDERR_TO_DEV_NULL, SPAWN_STDOUT_TO_DEV_NULL, 
    filename_display_basename, filename_display_name, get_application_name, 
    get_prgname, main_context_default, main_depth, set_application_name, 
    set_prgname, source_remove, uri_list_extract_uris)

from gi._gi import (GEnum, GFlags, GObjectWeakRef, OptionContext, OptionGroup, 
    Pid, add_emission_hook, list_properties, new, signal_new, spawn_async, 
    type_register)

from gobject import GBoxed, GInterface, GPointer, GType, Warning

from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GLib as __gi_overrides_GLib
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GLib as __gi_repository_GLib
import gi._gi as __gi__gi
import gi._signalhelper as __gi__signalhelper
import gobject as __gobject


from .Value import Value

class Value(Value):
    """
    :Constructors:
    
    ::
    
        Value()
    """
    def copy(self, dest_value): # real signature unknown; restored from __doc__
        """ copy(self, dest_value:GObject.Value) """
        pass

    def dup_object(self): # real signature unknown; restored from __doc__
        """ dup_object(self) -> GObject.Object or None """
        pass

    def dup_string(self): # real signature unknown; restored from __doc__
        """ dup_string(self) -> str or None """
        return ""

    def dup_variant(self): # real signature unknown; restored from __doc__
        """ dup_variant(self) -> GLib.Variant or None """
        pass

    def fits_pointer(self): # real signature unknown; restored from __doc__
        """ fits_pointer(self) -> bool """
        return False

    def get_boolean(self): # real signature unknown; restored from __doc__
        """ get_boolean(self) -> bool """
        return False

    def get_boxed(self): # reliably restored by inspect
        # no doc
        pass

    def get_char(self): # real signature unknown; restored from __doc__
        """ get_char(self) -> int """
        return 0

    def get_double(self): # real signature unknown; restored from __doc__
        """ get_double(self) -> float """
        return 0.0

    def get_enum(self): # real signature unknown; restored from __doc__
        """ get_enum(self) -> int """
        return 0

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> int """
        return 0

    def get_float(self): # real signature unknown; restored from __doc__
        """ get_float(self) -> float """
        return 0.0

    def get_gtype(self): # real signature unknown; restored from __doc__
        """ get_gtype(self) -> GType """
        return GType

    def get_int(self): # real signature unknown; restored from __doc__
        """ get_int(self) -> int """
        return 0

    def get_int64(self): # real signature unknown; restored from __doc__
        """ get_int64(self) -> int """
        return 0

    def get_long(self): # real signature unknown; restored from __doc__
        """ get_long(self) -> int """
        return 0

    def get_object(self): # real signature unknown; restored from __doc__
        """ get_object(self) -> GObject.Object or None """
        pass

    def get_param(self): # real signature unknown; restored from __doc__
        """ get_param(self) -> GObject.ParamSpec """
        pass

    def get_pointer(self): # real signature unknown; restored from __doc__
        """ get_pointer(self) """
        pass

    def get_schar(self): # real signature unknown; restored from __doc__
        """ get_schar(self) -> int """
        return 0

    def get_string(self): # real signature unknown; restored from __doc__
        """ get_string(self) -> str or None """
        return ""

    def get_uchar(self): # real signature unknown; restored from __doc__
        """ get_uchar(self) -> int """
        return 0

    def get_uint(self): # real signature unknown; restored from __doc__
        """ get_uint(self) -> int """
        return 0

    def get_uint64(self): # real signature unknown; restored from __doc__
        """ get_uint64(self) -> int """
        return 0

    def get_ulong(self): # real signature unknown; restored from __doc__
        """ get_ulong(self) -> int """
        return 0

    def get_value(self): # reliably restored by inspect
        # no doc
        pass

    def get_variant(self): # real signature unknown; restored from __doc__
        """ get_variant(self) -> GLib.Variant or None """
        pass

    def init(self, g_type): # real signature unknown; restored from __doc__
        """ init(self, g_type:GType) -> GObject.Value """
        pass

    def init_from_instance(self, instance): # real signature unknown; restored from __doc__
        """ init_from_instance(self, instance:GObject.TypeInstance) """
        pass

    def peek_pointer(self): # real signature unknown; restored from __doc__
        """ peek_pointer(self) """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> GObject.Value """
        pass

    def set_boolean(self, v_boolean): # real signature unknown; restored from __doc__
        """ set_boolean(self, v_boolean:bool) """
        pass

    def set_boxed(self, boxed): # reliably restored by inspect
        # no doc
        pass

    def set_boxed_take_ownership(self, v_boxed=None): # real signature unknown; restored from __doc__
        """ set_boxed_take_ownership(self, v_boxed=None) """
        pass

    def set_char(self, v_char): # real signature unknown; restored from __doc__
        """ set_char(self, v_char:int) """
        pass

    def set_double(self, v_double): # real signature unknown; restored from __doc__
        """ set_double(self, v_double:float) """
        pass

    def set_enum(self, v_enum): # real signature unknown; restored from __doc__
        """ set_enum(self, v_enum:int) """
        pass

    def set_flags(self, v_flags): # real signature unknown; restored from __doc__
        """ set_flags(self, v_flags:int) """
        pass

    def set_float(self, v_float): # real signature unknown; restored from __doc__
        """ set_float(self, v_float:float) """
        pass

    def set_gtype(self, v_gtype): # real signature unknown; restored from __doc__
        """ set_gtype(self, v_gtype:GType) """
        pass

    def set_instance(self, instance=None): # real signature unknown; restored from __doc__
        """ set_instance(self, instance=None) """
        pass

    def set_int(self, v_int): # real signature unknown; restored from __doc__
        """ set_int(self, v_int:int) """
        pass

    def set_int64(self, v_int64): # real signature unknown; restored from __doc__
        """ set_int64(self, v_int64:int) """
        pass

    def set_interned_string(self, v_string=None): # real signature unknown; restored from __doc__
        """ set_interned_string(self, v_string:str=None) """
        pass

    def set_long(self, v_long): # real signature unknown; restored from __doc__
        """ set_long(self, v_long:int) """
        pass

    def set_object(self, v_object=None): # real signature unknown; restored from __doc__
        """ set_object(self, v_object:GObject.Object=None) """
        pass

    def set_param(self, param=None): # real signature unknown; restored from __doc__
        """ set_param(self, param:GObject.ParamSpec=None) """
        pass

    def set_pointer(self, v_pointer=None): # real signature unknown; restored from __doc__
        """ set_pointer(self, v_pointer=None) """
        pass

    def set_schar(self, v_char): # real signature unknown; restored from __doc__
        """ set_schar(self, v_char:int) """
        pass

    def set_static_boxed(self, v_boxed=None): # real signature unknown; restored from __doc__
        """ set_static_boxed(self, v_boxed=None) """
        pass

    def set_static_string(self, v_string=None): # real signature unknown; restored from __doc__
        """ set_static_string(self, v_string:str=None) """
        pass

    def set_string(self, v_string=None): # real signature unknown; restored from __doc__
        """ set_string(self, v_string:str=None) """
        pass

    def set_string_take_ownership(self, v_string=None): # real signature unknown; restored from __doc__
        """ set_string_take_ownership(self, v_string:str=None) """
        pass

    def set_uchar(self, v_uchar): # real signature unknown; restored from __doc__
        """ set_uchar(self, v_uchar:int) """
        pass

    def set_uint(self, v_uint): # real signature unknown; restored from __doc__
        """ set_uint(self, v_uint:int) """
        pass

    def set_uint64(self, v_uint64): # real signature unknown; restored from __doc__
        """ set_uint64(self, v_uint64:int) """
        pass

    def set_ulong(self, v_ulong): # real signature unknown; restored from __doc__
        """ set_ulong(self, v_ulong:int) """
        pass

    def set_value(self, py_value): # reliably restored by inspect
        # no doc
        pass

    def set_variant(self, variant=None): # real signature unknown; restored from __doc__
        """ set_variant(self, variant:GLib.Variant=None) """
        pass

    def steal_string(self): # real signature unknown; restored from __doc__
        """ steal_string(self) -> str or None """
        return ""

    def take_boxed(self, v_boxed=None): # real signature unknown; restored from __doc__
        """ take_boxed(self, v_boxed=None) """
        pass

    def take_string(self, v_string=None): # real signature unknown; restored from __doc__
        """ take_string(self, v_string:str=None) """
        pass

    def take_variant(self, variant=None): # real signature unknown; restored from __doc__
        """ take_variant(self, variant:GLib.Variant=None) """
        pass

    def transform(self, dest_value): # real signature unknown; restored from __doc__
        """ transform(self, dest_value:GObject.Value) -> bool """
        return False

    def type_compatible(self, src_type, dest_type): # real signature unknown; restored from __doc__
        """ type_compatible(src_type:GType, dest_type:GType) -> bool """
        return False

    def type_transformable(self, src_type, dest_type): # real signature unknown; restored from __doc__
        """ type_transformable(src_type:GType, dest_type:GType) -> bool """
        return False

    def unset(self): # real signature unknown; restored from __doc__
        """ unset(self) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """
        Default object formatter.
        
        Return str(self) if format_spec is empty. Raise TypeError otherwise.
        """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, value_type=None, py_value=None): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __subclasshook__(self, *args, **kwargs): # real signature unknown
        """
        Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        pass

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _Value__g_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.GObject', '__init__': <function Value.__init__ at 0x000001dd11de7f60>, '_Value__g_type': <property object at 0x000001dd11db3970>, 'set_boxed': <function Value.set_boxed at 0x000001dd11d98180>, 'get_boxed': <function Value.get_boxed at 0x000001dd11d98220>, 'set_value': <function Value.set_value at 0x000001dd11d982c0>, 'get_value': <function Value.get_value at 0x000001dd11d98360>, '__repr__': <function Value.__repr__ at 0x000001dd11d98400>, '__doc__': None})"
    __gtype__ = None # (!) forward: TYPE_VALUE, real value is '<GType GValue (265149856)>'
    __info__ = StructInfo(Value)


