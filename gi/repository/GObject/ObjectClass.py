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


class ObjectClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ObjectClass()
    """
    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
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

    constructed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    constructor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    construct_properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dispatch_properties_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dispose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    finalize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    notify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_construct_properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_pspecs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pdummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pspecs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ObjectClass), '__module__': 'gi.repository.GObject', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ObjectClass' objects>, '__weakref__': <attribute '__weakref__' of 'ObjectClass' objects>, '__doc__': None, 'g_type_class': <property object at 0x000001dd11e5a2f0>, 'construct_properties': <property object at 0x000001dd11e5a3e0>, 'constructor': <property object at 0x000001dd11e5a4d0>, 'set_property': <property object at 0x000001dd11e5a5c0>, 'get_property': <property object at 0x000001dd11e5a6b0>, 'dispose': <property object at 0x000001dd11e5a7a0>, 'finalize': <property object at 0x000001dd11e5a890>, 'dispatch_properties_changed': <property object at 0x000001dd11e5a9d0>, 'notify': <property object at 0x000001dd11e5aa70>, 'constructed': <property object at 0x000001dd11e5ab60>, 'flags': <property object at 0x000001dd11e5ac50>, 'n_construct_properties': <property object at 0x000001dd11e5ad40>, 'pspecs': <property object at 0x000001dd11e5ae30>, 'n_pspecs': <property object at 0x000001dd11e5af20>, 'pdummy': <property object at 0x000001dd11e5b010>, 'find_property': gi.FunctionInfo(find_property), 'install_properties': gi.FunctionInfo(install_properties), 'install_property': gi.FunctionInfo(install_property), 'list_properties': gi.FunctionInfo(list_properties), 'override_property': gi.FunctionInfo(override_property)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ObjectClass)


