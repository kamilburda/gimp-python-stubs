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


class ConfigWriter(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new_from_fd(fd:int) -> Gimp.ConfigWriter or None
        new_from_file(file:Gio.File, atomic:bool, header:str) -> Gimp.ConfigWriter or None
        new_from_stream(output:Gio.OutputStream, header:str) -> Gimp.ConfigWriter or None
        new_from_string(string:GLib.String) -> Gimp.ConfigWriter or None
    """
    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def comment(self, comment): # real signature unknown; restored from __doc__
        """ comment(self, comment:str) """
        pass

    def comment_mode(self, enable): # real signature unknown; restored from __doc__
        """ comment_mode(self, enable:bool) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, data): # real signature unknown; restored from __doc__
        """ data(self, data:list) """
        pass

    def finish(self, footer): # real signature unknown; restored from __doc__
        """ finish(self, footer:str) -> bool """
        return False

    def identifier(self, identifier): # real signature unknown; restored from __doc__
        """ identifier(self, identifier:str) """
        pass

    def linefeed(self): # real signature unknown; restored from __doc__
        """ linefeed(self) """
        pass

    @classmethod
    def new_from_fd(cls, fd): # real signature unknown; restored from __doc__
        """ new_from_fd(fd:int) -> Gimp.ConfigWriter or None """
        pass

    @classmethod
    def new_from_file(cls, file, atomic, header): # real signature unknown; restored from __doc__
        """ new_from_file(file:Gio.File, atomic:bool, header:str) -> Gimp.ConfigWriter or None """
        pass

    @classmethod
    def new_from_stream(cls, output, header): # real signature unknown; restored from __doc__
        """ new_from_stream(output:Gio.OutputStream, header:str) -> Gimp.ConfigWriter or None """
        pass

    @classmethod
    def new_from_string(cls, string): # real signature unknown; restored from __doc__
        """ new_from_string(string:GLib.String) -> Gimp.ConfigWriter or None """
        pass

    def open(self, name): # real signature unknown; restored from __doc__
        """ open(self, name:str) """
        pass

    def print_(self, string, len): # real signature unknown; restored from __doc__
        """ print_(self, string:str, len:int) """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gimp.ConfigWriter """
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ revert(self) """
        pass

    def string(self, string): # real signature unknown; restored from __doc__
        """ string(self, string:str) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ConfigWriter), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpConfigWriter (2406244640)>, '__dict__': <attribute '__dict__' of 'ConfigWriter' objects>, '__weakref__': <attribute '__weakref__' of 'ConfigWriter' objects>, '__doc__': None, 'new_from_fd': <classmethod(gi.FunctionInfo(new_from_fd))>, 'new_from_file': <classmethod(gi.FunctionInfo(new_from_file))>, 'new_from_stream': <classmethod(gi.FunctionInfo(new_from_stream))>, 'new_from_string': <classmethod(gi.FunctionInfo(new_from_string))>, 'close': gi.FunctionInfo(close), 'comment': gi.FunctionInfo(comment), 'comment_mode': gi.FunctionInfo(comment_mode), 'data': gi.FunctionInfo(data), 'finish': gi.FunctionInfo(finish), 'identifier': gi.FunctionInfo(identifier), 'linefeed': gi.FunctionInfo(linefeed), 'open': gi.FunctionInfo(open), 'print_': gi.FunctionInfo(print), 'ref': gi.FunctionInfo(ref), 'revert': gi.FunctionInfo(revert), 'string': gi.FunctionInfo(string), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType GimpConfigWriter (2406244640)>'
    __info__ = StructInfo(ConfigWriter)


