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


class TargetList(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(targets:list=None) -> Gtk.TargetList
    """
    def add(self, target, flags, info): # real signature unknown; restored from __doc__
        """ add(self, target:Gdk.Atom, flags:int, info:int) """
        pass

    def add_image_targets(self, info, writable): # real signature unknown; restored from __doc__
        """ add_image_targets(self, info:int, writable:bool) """
        pass

    def add_rich_text_targets(self, info, deserializable, buffer): # real signature unknown; restored from __doc__
        """ add_rich_text_targets(self, info:int, deserializable:bool, buffer:Gtk.TextBuffer) """
        pass

    def add_table(self, targets): # real signature unknown; restored from __doc__
        """ add_table(self, targets:list) """
        pass

    def add_text_targets(self, info): # real signature unknown; restored from __doc__
        """ add_text_targets(self, info:int) """
        pass

    def add_uri_targets(self, info): # real signature unknown; restored from __doc__
        """ add_uri_targets(self, info:int) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def find(self, target): # real signature unknown; restored from __doc__
        """ find(self, target:Gdk.Atom) -> bool, info:int """
        return False

    @classmethod
    def new(cls, targets=None): # real signature unknown; restored from __doc__
        """ new(targets:list=None) -> Gtk.TargetList """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gtk.TargetList """
        pass

    def remove(self, target): # real signature unknown; restored from __doc__
        """ remove(self, target:Gdk.Atom) """
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
        """ new(targets:list=None) -> Gtk.TargetList """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TargetList), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkTargetList (3414244848)>, '__dict__': <attribute '__dict__' of 'TargetList' objects>, '__weakref__': <attribute '__weakref__' of 'TargetList' objects>, '__doc__': None, 'new': <classmethod(gi.FunctionInfo(new))>, 'add': gi.FunctionInfo(add), 'add_image_targets': gi.FunctionInfo(add_image_targets), 'add_rich_text_targets': gi.FunctionInfo(add_rich_text_targets), 'add_table': gi.FunctionInfo(add_table), 'add_text_targets': gi.FunctionInfo(add_text_targets), 'add_uri_targets': gi.FunctionInfo(add_uri_targets), 'find': gi.FunctionInfo(find), 'ref': gi.FunctionInfo(ref), 'remove': gi.FunctionInfo(remove), 'unref': gi.FunctionInfo(unref), '__new__': <staticmethod(gi.FunctionInfo(new))>, '__init__': <function nothing at 0x000002bfce305010>})"
    __gtype__ = None # (!) real value is '<GType GtkTargetList (3414244848)>'
    __info__ = StructInfo(TargetList)


