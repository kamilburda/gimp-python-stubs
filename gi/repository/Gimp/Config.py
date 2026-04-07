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


class Config(__gi.Struct):
    # no doc
    def copy(self, dest, flags): # real signature unknown; restored from __doc__
        """ copy(self, dest:Gimp.Config, flags:GObject.ParamFlags) -> bool """
        return False

    def deserialize(self, scanner, nest_level, data=None): # real signature unknown; restored from __doc__
        """ deserialize(self, scanner:GLib.Scanner, nest_level:int, data=None) -> bool """
        return False

    def deserialize_file(self, file, data=None): # real signature unknown; restored from __doc__
        """ deserialize_file(self, file:Gio.File, data=None) -> bool """
        return False

    def deserialize_parasite(self, parasite, data=None): # real signature unknown; restored from __doc__
        """ deserialize_parasite(self, parasite:Gimp.Parasite, data=None) -> bool """
        return False

    def deserialize_properties(self, scanner, nest_level): # real signature unknown; restored from __doc__
        """ deserialize_properties(self, scanner:GLib.Scanner, nest_level:int) -> bool """
        return False

    def deserialize_property(self, scanner, nest_level): # real signature unknown; restored from __doc__
        """ deserialize_property(self, scanner:GLib.Scanner, nest_level:int) -> GLib.TokenType """
        pass

    def deserialize_stream(self, input, data=None): # real signature unknown; restored from __doc__
        """ deserialize_stream(self, input:Gio.InputStream, data=None) -> bool """
        return False

    def deserialize_string(self, text, data=None): # real signature unknown; restored from __doc__
        """ deserialize_string(self, text:list, data=None) -> bool """
        return False

    def duplicate(self): # real signature unknown; restored from __doc__
        """ duplicate(self) """
        pass

    def get_xcf_version(self): # real signature unknown; restored from __doc__
        """ get_xcf_version(self) -> int """
        return 0

    def is_equal_to(self, b): # real signature unknown; restored from __doc__
        """ is_equal_to(self, b:Gimp.Config) -> bool """
        return False

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def serialize(self, writer, data=None): # real signature unknown; restored from __doc__
        """ serialize(self, writer:Gimp.ConfigWriter, data=None) -> bool """
        return False

    def serialize_changed_properties(self, writer): # real signature unknown; restored from __doc__
        """ serialize_changed_properties(self, writer:Gimp.ConfigWriter) -> bool """
        return False

    def serialize_properties(self, writer): # real signature unknown; restored from __doc__
        """ serialize_properties(self, writer:Gimp.ConfigWriter) -> bool """
        return False

    def serialize_property(self, param_spec, writer): # real signature unknown; restored from __doc__
        """ serialize_property(self, param_spec:GObject.ParamSpec, writer:Gimp.ConfigWriter) -> bool """
        return False

    def serialize_property_by_name(self, prop_name, writer): # real signature unknown; restored from __doc__
        """ serialize_property_by_name(self, prop_name:str, writer:Gimp.ConfigWriter) -> bool """
        return False

    def serialize_to_fd(self, fd, data=None): # real signature unknown; restored from __doc__
        """ serialize_to_fd(self, fd:int, data=None) -> bool """
        return False

    def serialize_to_file(self, file, header=None, footer=None, data=None): # real signature unknown; restored from __doc__
        """ serialize_to_file(self, file:Gio.File, header:str=None, footer:str=None, data=None) -> bool """
        return False

    def serialize_to_parasite(self, parasite_name, parasite_flags, data=None): # real signature unknown; restored from __doc__
        """ serialize_to_parasite(self, parasite_name:str, parasite_flags:int, data=None) -> Gimp.Parasite """
        pass

    def serialize_to_stream(self, output, header=None, footer=None, data=None): # real signature unknown; restored from __doc__
        """ serialize_to_stream(self, output:Gio.OutputStream, header:str=None, footer:str=None, data=None) -> bool """
        return False

    def serialize_to_string(self, data=None): # real signature unknown; restored from __doc__
        """ serialize_to_string(self, data=None) -> str """
        return ""

    def set_xcf_version(self, xcf_version): # real signature unknown; restored from __doc__
        """ set_xcf_version(self, xcf_version:int) """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Config), '__module__': 'gi.repository.Gimp', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Config' objects>, '__weakref__': <attribute '__weakref__' of 'Config' objects>, '__doc__': None, 'copy': gi.FunctionInfo(copy), 'deserialize': gi.FunctionInfo(deserialize), 'deserialize_file': gi.FunctionInfo(deserialize_file), 'deserialize_parasite': gi.FunctionInfo(deserialize_parasite), 'deserialize_properties': gi.FunctionInfo(deserialize_properties), 'deserialize_property': gi.FunctionInfo(deserialize_property), 'deserialize_stream': gi.FunctionInfo(deserialize_stream), 'deserialize_string': gi.FunctionInfo(deserialize_string), 'duplicate': gi.FunctionInfo(duplicate), 'get_xcf_version': gi.FunctionInfo(get_xcf_version), 'is_equal_to': gi.FunctionInfo(is_equal_to), 'reset': gi.FunctionInfo(reset), 'serialize': gi.FunctionInfo(serialize), 'serialize_changed_properties': gi.FunctionInfo(serialize_changed_properties), 'serialize_properties': gi.FunctionInfo(serialize_properties), 'serialize_property': gi.FunctionInfo(serialize_property), 'serialize_property_by_name': gi.FunctionInfo(serialize_property_by_name), 'serialize_to_fd': gi.FunctionInfo(serialize_to_fd), 'serialize_to_file': gi.FunctionInfo(serialize_to_file), 'serialize_to_parasite': gi.FunctionInfo(serialize_to_parasite), 'serialize_to_stream': gi.FunctionInfo(serialize_to_stream), 'serialize_to_string': gi.FunctionInfo(serialize_to_string), 'set_xcf_version': gi.FunctionInfo(set_xcf_version)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Config)


