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


class CClosure(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        CClosure()
    """
    def marshal_BOOLEAN__BOXED_BOXED(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_BOOLEAN__BOXED_BOXED(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_BOOLEAN__FLAGS(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_BOOLEAN__FLAGS(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_generic(self, closure, return_gvalue, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_generic(closure:GObject.Closure, return_gvalue:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_STRING__OBJECT_POINTER(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_STRING__OBJECT_POINTER(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__BOOLEAN(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__BOOLEAN(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__BOXED(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__BOXED(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__CHAR(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__CHAR(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__DOUBLE(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__DOUBLE(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__ENUM(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__ENUM(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__FLAGS(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__FLAGS(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__FLOAT(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__FLOAT(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__INT(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__INT(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__LONG(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__LONG(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__OBJECT(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__OBJECT(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__PARAM(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__PARAM(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__POINTER(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__POINTER(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__STRING(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__STRING(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__UCHAR(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__UCHAR(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__UINT(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__UINT(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__UINT_POINTER(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__UINT_POINTER(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__ULONG(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__ULONG(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__VARIANT(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__VARIANT(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
        pass

    def marshal_VOID__VOID(self, closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_VOID__VOID(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
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

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    closure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CClosure), '__module__': 'gi.repository.GObject', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'CClosure' objects>, '__weakref__': <attribute '__weakref__' of 'CClosure' objects>, '__doc__': None, 'closure': <property object at 0x000001dd11ea6840>, 'callback': <property object at 0x000001dd11ea6930>, 'marshal_BOOLEAN__BOXED_BOXED': <staticmethod(gi.FunctionInfo(marshal_BOOLEAN__BOXED_BOXED))>, 'marshal_BOOLEAN__FLAGS': <staticmethod(gi.FunctionInfo(marshal_BOOLEAN__FLAGS))>, 'marshal_STRING__OBJECT_POINTER': <staticmethod(gi.FunctionInfo(marshal_STRING__OBJECT_POINTER))>, 'marshal_VOID__BOOLEAN': <staticmethod(gi.FunctionInfo(marshal_VOID__BOOLEAN))>, 'marshal_VOID__BOXED': <staticmethod(gi.FunctionInfo(marshal_VOID__BOXED))>, 'marshal_VOID__CHAR': <staticmethod(gi.FunctionInfo(marshal_VOID__CHAR))>, 'marshal_VOID__DOUBLE': <staticmethod(gi.FunctionInfo(marshal_VOID__DOUBLE))>, 'marshal_VOID__ENUM': <staticmethod(gi.FunctionInfo(marshal_VOID__ENUM))>, 'marshal_VOID__FLAGS': <staticmethod(gi.FunctionInfo(marshal_VOID__FLAGS))>, 'marshal_VOID__FLOAT': <staticmethod(gi.FunctionInfo(marshal_VOID__FLOAT))>, 'marshal_VOID__INT': <staticmethod(gi.FunctionInfo(marshal_VOID__INT))>, 'marshal_VOID__LONG': <staticmethod(gi.FunctionInfo(marshal_VOID__LONG))>, 'marshal_VOID__OBJECT': <staticmethod(gi.FunctionInfo(marshal_VOID__OBJECT))>, 'marshal_VOID__PARAM': <staticmethod(gi.FunctionInfo(marshal_VOID__PARAM))>, 'marshal_VOID__POINTER': <staticmethod(gi.FunctionInfo(marshal_VOID__POINTER))>, 'marshal_VOID__STRING': <staticmethod(gi.FunctionInfo(marshal_VOID__STRING))>, 'marshal_VOID__UCHAR': <staticmethod(gi.FunctionInfo(marshal_VOID__UCHAR))>, 'marshal_VOID__UINT': <staticmethod(gi.FunctionInfo(marshal_VOID__UINT))>, 'marshal_VOID__UINT_POINTER': <staticmethod(gi.FunctionInfo(marshal_VOID__UINT_POINTER))>, 'marshal_VOID__ULONG': <staticmethod(gi.FunctionInfo(marshal_VOID__ULONG))>, 'marshal_VOID__VARIANT': <staticmethod(gi.FunctionInfo(marshal_VOID__VARIANT))>, 'marshal_VOID__VOID': <staticmethod(gi.FunctionInfo(marshal_VOID__VOID))>, 'marshal_generic': <staticmethod(gi.FunctionInfo(marshal_generic))>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(CClosure)


