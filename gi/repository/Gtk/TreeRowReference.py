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


class TreeRowReference(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(model:Gtk.TreeModel, path:Gtk.TreePath) -> Gtk.TreeRowReference
        new_proxy(proxy:GObject.Object, model:Gtk.TreeModel, path:Gtk.TreePath) -> Gtk.TreeRowReference
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gtk.TreeRowReference """
        pass

    def deleted(self, proxy, path): # real signature unknown; restored from __doc__
        """ deleted(proxy:GObject.Object, path:Gtk.TreePath) """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_model(self): # real signature unknown; restored from __doc__
        """ get_model(self) -> Gtk.TreeModel """
        pass

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> Gtk.TreePath or None """
        pass

    def inserted(self, proxy, path): # real signature unknown; restored from __doc__
        """ inserted(proxy:GObject.Object, path:Gtk.TreePath) """
        pass

    @classmethod
    def new(cls, model, path): # real signature unknown; restored from __doc__
        """ new(model:Gtk.TreeModel, path:Gtk.TreePath) -> Gtk.TreeRowReference """
        pass

    @classmethod
    def new_proxy(cls, proxy, model, path): # real signature unknown; restored from __doc__
        """ new_proxy(proxy:GObject.Object, model:Gtk.TreeModel, path:Gtk.TreePath) -> Gtk.TreeRowReference """
        pass

    def valid(self): # real signature unknown; restored from __doc__
        """ valid(self) -> bool """
        return False

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

    def __init__(*args, **kwargs): # reliably restored by inspect
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
        """ new(model:Gtk.TreeModel, path:Gtk.TreePath) -> Gtk.TreeRowReference """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TreeRowReference), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkTreeRowReference (3414251184)>, '__dict__': <attribute '__dict__' of 'TreeRowReference' objects>, '__weakref__': <attribute '__weakref__' of 'TreeRowReference' objects>, '__doc__': None, 'new': <classmethod(gi.FunctionInfo(new))>, 'new_proxy': <classmethod(gi.FunctionInfo(new_proxy))>, 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_model': gi.FunctionInfo(get_model), 'get_path': gi.FunctionInfo(get_path), 'valid': gi.FunctionInfo(valid), 'deleted': <staticmethod(gi.FunctionInfo(deleted))>, 'inserted': <staticmethod(gi.FunctionInfo(inserted))>, '__new__': <staticmethod(gi.FunctionInfo(new))>, '__init__': <function nothing at 0x000002bfce305010>})"
    __gtype__ = None # (!) real value is '<GType GtkTreeRowReference (3414251184)>'
    __info__ = StructInfo(TreeRowReference)


