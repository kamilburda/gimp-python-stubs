# encoding: utf-8
# module gi.repository.Gimp
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GExiv2 as __gi_overrides_GExiv2
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


class ConfigInterface(__gobject.GInterface):
    # no doc
    def build_data_path(self, name): # real signature unknown; restored from __doc__
        """ build_data_path(name:str) -> str """
        return ""

    def build_plug_in_path(self, name): # real signature unknown; restored from __doc__
        """ build_plug_in_path(name:str) -> str """
        return ""

    def build_system_path(self, name): # real signature unknown; restored from __doc__
        """ build_system_path(name:str) -> str """
        return ""

    def build_writable_path(self, name): # real signature unknown; restored from __doc__
        """ build_writable_path(name:str) -> str """
        return ""

    def deserialize_return(self, scanner, expected_token, nest_level): # real signature unknown; restored from __doc__
        """ deserialize_return(scanner:GLib.Scanner, expected_token:GLib.TokenType, nest_level:int) -> bool """
        return False

    def diff(self, a, b, flags): # real signature unknown; restored from __doc__
        """ diff(a:GObject.Object, b:GObject.Object, flags:GObject.ParamFlags) -> list """
        return []

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def param_spec_duplicate(self, pspec): # real signature unknown; restored from __doc__
        """ param_spec_duplicate(pspec:GObject.ParamSpec) -> GObject.ParamSpec """
        pass

    def reset_properties(self, p_object): # real signature unknown; restored from __doc__
        """ reset_properties(object:GObject.Object) """
        pass

    def reset_property(self, p_object, property_name): # real signature unknown; restored from __doc__
        """ reset_property(object:GObject.Object, property_name:str) """
        pass

    def serialize_value(self, value, p_str, escaped): # real signature unknown; restored from __doc__
        """ serialize_value(value:GObject.Value, str:GLib.String, escaped:bool) -> bool """
        return False

    def string_append_escaped(self, string, val): # real signature unknown; restored from __doc__
        """ string_append_escaped(string:GLib.String, val:str) """
        pass

    def sync(self, src, dest, flags): # real signature unknown; restored from __doc__
        """ sync(src:GObject.Object, dest:GObject.Object, flags:GObject.ParamFlags) -> bool """
        return False

    def type_register(self, parent_type, type_name, pspecs): # real signature unknown; restored from __doc__
        """ type_register(parent_type:GType, type_name:str, pspecs:list) -> GType """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(ConfigInterface), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpConfigInterface (2362478528)>, '__dict__': <attribute '__dict__' of 'ConfigInterface' objects>, '__weakref__': <attribute '__weakref__' of 'ConfigInterface' objects>, '__doc__': None, '__gsignals__': {}, 'build_data_path': <staticmethod(gi.FunctionInfo(build_data_path))>, 'build_plug_in_path': <staticmethod(gi.FunctionInfo(build_plug_in_path))>, 'build_system_path': <staticmethod(gi.FunctionInfo(build_system_path))>, 'build_writable_path': <staticmethod(gi.FunctionInfo(build_writable_path))>, 'deserialize_return': <staticmethod(gi.FunctionInfo(deserialize_return))>, 'diff': <staticmethod(gi.FunctionInfo(diff))>, 'error_quark': <staticmethod(gi.FunctionInfo(error_quark))>, 'param_spec_duplicate': <staticmethod(gi.FunctionInfo(param_spec_duplicate))>, 'reset_properties': <staticmethod(gi.FunctionInfo(reset_properties))>, 'reset_property': <staticmethod(gi.FunctionInfo(reset_property))>, 'serialize_value': <staticmethod(gi.FunctionInfo(serialize_value))>, 'string_append_escaped': <staticmethod(gi.FunctionInfo(string_append_escaped))>, 'sync': <staticmethod(gi.FunctionInfo(sync))>, 'type_register': <staticmethod(gi.FunctionInfo(type_register))>})"
    __gdoc__ = 'Interface GimpConfigInterface\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GimpConfigInterface (2362478528)>'
    __info__ = InterfaceInfo(ConfigInterface)


