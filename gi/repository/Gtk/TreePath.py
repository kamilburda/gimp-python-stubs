# encoding: utf-8
# module gi.repository.Gtk
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


from .TreePath import TreePath

class TreePath(TreePath):
    """
    :Constructors:
    
    ::
    
        new() -> Gtk.TreePath
        new_first() -> Gtk.TreePath
        new_from_indices(indices:list) -> Gtk.TreePath
        new_from_string(path:str) -> Gtk.TreePath
    """
    def append_index(self, index_): # real signature unknown; restored from __doc__
        """ append_index(self, index_:int) """
        pass

    def compare(self, b): # real signature unknown; restored from __doc__
        """ compare(self, b:Gtk.TreePath) -> int """
        return 0

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gtk.TreePath """
        pass

    def down(self): # real signature unknown; restored from __doc__
        """ down(self) """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_depth(self): # real signature unknown; restored from __doc__
        """ get_depth(self) -> int """
        return 0

    def get_indices(self): # real signature unknown; restored from __doc__
        """ get_indices(self) -> list """
        return []

    def is_ancestor(self, descendant): # real signature unknown; restored from __doc__
        """ is_ancestor(self, descendant:Gtk.TreePath) -> bool """
        return False

    def is_descendant(self, ancestor): # real signature unknown; restored from __doc__
        """ is_descendant(self, ancestor:Gtk.TreePath) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gtk.TreePath """
        pass

    def new_first(self): # real signature unknown; restored from __doc__
        """ new_first() -> Gtk.TreePath """
        pass

    def new_from_indices(self, indices): # real signature unknown; restored from __doc__
        """ new_from_indices(indices:list) -> Gtk.TreePath """
        pass

    def new_from_string(self, path): # real signature unknown; restored from __doc__
        """ new_from_string(path:str) -> Gtk.TreePath """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) """
        pass

    def prepend_index(self, index_): # real signature unknown; restored from __doc__
        """ prepend_index(self, index_:int) """
        pass

    def prev(self): # real signature unknown; restored from __doc__
        """ prev(self) -> bool """
        return False

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def up(self): # real signature unknown; restored from __doc__
        """ up(self) -> bool """
        return False

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
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

    def __getitem__(self, index): # reliably restored by inspect
        # no doc
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __ge__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __gt__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    def __len__(self): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __lt__(self, other): # reliably restored by inspect
        # no doc
        pass

    @staticmethod # known case of __new__
    def __new__(cls, path=0): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
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

    def __str__(self): # reliably restored by inspect
        # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gtk', '__firstlineno__': 1299, '__new__': <staticmethod(<function TreePath.__new__ at 0x000002bfcebd2a30>)>, '__init__': <function TreePath.__init__ at 0x000002bfcebd2ae0>, '__str__': <function TreePath.__str__ at 0x000002bfcebd2b90>, '__lt__': <function TreePath.__lt__ at 0x000002bfcebd2c40>, '__le__': <function TreePath.__le__ at 0x000002bfcebd2cf0>, '__eq__': <function TreePath.__eq__ at 0x000002bfcebd2da0>, '__ne__': <function TreePath.__ne__ at 0x000002bfcebd2e50>, '__gt__': <function TreePath.__gt__ at 0x000002bfcebd2f00>, '__ge__': <function TreePath.__ge__ at 0x000002bfcebd2fb0>, '__iter__': <function TreePath.__iter__ at 0x000002bfcebd3060>, '__len__': <function TreePath.__len__ at 0x000002bfcebd3110>, '__getitem__': <function TreePath.__getitem__ at 0x000002bfcebd31c0>, '__static_attributes__': (), '__doc__': None, '__hash__': None})"
    __firstlineno__ = 1299
    __gtype__ = None # (!) real value is '<GType GtkTreePath (3416385648)>'
    __hash__ = None
    __info__ = StructInfo(TreePath)
    __static_attributes__ = ()


