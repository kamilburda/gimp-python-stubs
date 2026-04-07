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


class WidgetPath(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> Gtk.WidgetPath
    """
    def append_for_widget(self, widget): # real signature unknown; restored from __doc__
        """ append_for_widget(self, widget:Gtk.Widget) -> int """
        return 0

    def append_type(self, type): # real signature unknown; restored from __doc__
        """ append_type(self, type:GType) -> int """
        return 0

    def append_with_siblings(self, siblings, sibling_index): # real signature unknown; restored from __doc__
        """ append_with_siblings(self, siblings:Gtk.WidgetPath, sibling_index:int) -> int """
        return 0

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gtk.WidgetPath """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_object_type(self): # real signature unknown; restored from __doc__
        """ get_object_type(self) -> GType """
        pass

    def has_parent(self, type): # real signature unknown; restored from __doc__
        """ has_parent(self, type:GType) -> bool """
        return False

    def is_type(self, type): # real signature unknown; restored from __doc__
        """ is_type(self, type:GType) -> bool """
        return False

    def iter_add_class(self, pos, name): # real signature unknown; restored from __doc__
        """ iter_add_class(self, pos:int, name:str) """
        pass

    def iter_add_region(self, pos, name, flags): # real signature unknown; restored from __doc__
        """ iter_add_region(self, pos:int, name:str, flags:Gtk.RegionFlags) """
        pass

    def iter_clear_classes(self, pos): # real signature unknown; restored from __doc__
        """ iter_clear_classes(self, pos:int) """
        pass

    def iter_clear_regions(self, pos): # real signature unknown; restored from __doc__
        """ iter_clear_regions(self, pos:int) """
        pass

    def iter_get_name(self, pos): # real signature unknown; restored from __doc__
        """ iter_get_name(self, pos:int) -> str or None """
        return ""

    def iter_get_object_name(self, pos): # real signature unknown; restored from __doc__
        """ iter_get_object_name(self, pos:int) -> str or None """
        return ""

    def iter_get_object_type(self, pos): # real signature unknown; restored from __doc__
        """ iter_get_object_type(self, pos:int) -> GType """
        pass

    def iter_get_siblings(self, pos): # real signature unknown; restored from __doc__
        """ iter_get_siblings(self, pos:int) -> Gtk.WidgetPath """
        pass

    def iter_get_sibling_index(self, pos): # real signature unknown; restored from __doc__
        """ iter_get_sibling_index(self, pos:int) -> int """
        return 0

    def iter_get_state(self, pos): # real signature unknown; restored from __doc__
        """ iter_get_state(self, pos:int) -> Gtk.StateFlags """
        pass

    def iter_has_class(self, pos, name): # real signature unknown; restored from __doc__
        """ iter_has_class(self, pos:int, name:str) -> bool """
        return False

    def iter_has_name(self, pos, name): # real signature unknown; restored from __doc__
        """ iter_has_name(self, pos:int, name:str) -> bool """
        return False

    def iter_has_qclass(self, pos, qname): # real signature unknown; restored from __doc__
        """ iter_has_qclass(self, pos:int, qname:int) -> bool """
        return False

    def iter_has_qname(self, pos, qname): # real signature unknown; restored from __doc__
        """ iter_has_qname(self, pos:int, qname:int) -> bool """
        return False

    def iter_has_qregion(self, pos, qname): # real signature unknown; restored from __doc__
        """ iter_has_qregion(self, pos:int, qname:int) -> bool, flags:Gtk.RegionFlags """
        return False

    def iter_has_region(self, pos, name): # real signature unknown; restored from __doc__
        """ iter_has_region(self, pos:int, name:str) -> bool, flags:Gtk.RegionFlags """
        return False

    def iter_list_classes(self, pos): # real signature unknown; restored from __doc__
        """ iter_list_classes(self, pos:int) -> list """
        return []

    def iter_list_regions(self, pos): # real signature unknown; restored from __doc__
        """ iter_list_regions(self, pos:int) -> list """
        return []

    def iter_remove_class(self, pos, name): # real signature unknown; restored from __doc__
        """ iter_remove_class(self, pos:int, name:str) """
        pass

    def iter_remove_region(self, pos, name): # real signature unknown; restored from __doc__
        """ iter_remove_region(self, pos:int, name:str) """
        pass

    def iter_set_name(self, pos, name): # real signature unknown; restored from __doc__
        """ iter_set_name(self, pos:int, name:str) """
        pass

    def iter_set_object_name(self, pos, name=None): # real signature unknown; restored from __doc__
        """ iter_set_object_name(self, pos:int, name:str=None) """
        pass

    def iter_set_object_type(self, pos, type): # real signature unknown; restored from __doc__
        """ iter_set_object_type(self, pos:int, type:GType) """
        pass

    def iter_set_state(self, pos, state): # real signature unknown; restored from __doc__
        """ iter_set_state(self, pos:int, state:Gtk.StateFlags) """
        pass

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> Gtk.WidgetPath """
        pass

    def prepend_type(self, type): # real signature unknown; restored from __doc__
        """ prepend_type(self, type:GType) """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gtk.WidgetPath """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

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
        """ new() -> Gtk.WidgetPath """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(WidgetPath), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkWidgetPath (3414253584)>, '__dict__': <attribute '__dict__' of 'WidgetPath' objects>, '__weakref__': <attribute '__weakref__' of 'WidgetPath' objects>, '__doc__': None, 'new': <classmethod(gi.FunctionInfo(new))>, 'append_for_widget': gi.FunctionInfo(append_for_widget), 'append_type': gi.FunctionInfo(append_type), 'append_with_siblings': gi.FunctionInfo(append_with_siblings), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_object_type': gi.FunctionInfo(get_object_type), 'has_parent': gi.FunctionInfo(has_parent), 'is_type': gi.FunctionInfo(is_type), 'iter_add_class': gi.FunctionInfo(iter_add_class), 'iter_add_region': gi.FunctionInfo(iter_add_region), 'iter_clear_classes': gi.FunctionInfo(iter_clear_classes), 'iter_clear_regions': gi.FunctionInfo(iter_clear_regions), 'iter_get_name': gi.FunctionInfo(iter_get_name), 'iter_get_object_name': gi.FunctionInfo(iter_get_object_name), 'iter_get_object_type': gi.FunctionInfo(iter_get_object_type), 'iter_get_sibling_index': gi.FunctionInfo(iter_get_sibling_index), 'iter_get_siblings': gi.FunctionInfo(iter_get_siblings), 'iter_get_state': gi.FunctionInfo(iter_get_state), 'iter_has_class': gi.FunctionInfo(iter_has_class), 'iter_has_name': gi.FunctionInfo(iter_has_name), 'iter_has_qclass': gi.FunctionInfo(iter_has_qclass), 'iter_has_qname': gi.FunctionInfo(iter_has_qname), 'iter_has_qregion': gi.FunctionInfo(iter_has_qregion), 'iter_has_region': gi.FunctionInfo(iter_has_region), 'iter_list_classes': gi.FunctionInfo(iter_list_classes), 'iter_list_regions': gi.FunctionInfo(iter_list_regions), 'iter_remove_class': gi.FunctionInfo(iter_remove_class), 'iter_remove_region': gi.FunctionInfo(iter_remove_region), 'iter_set_name': gi.FunctionInfo(iter_set_name), 'iter_set_object_name': gi.FunctionInfo(iter_set_object_name), 'iter_set_object_type': gi.FunctionInfo(iter_set_object_type), 'iter_set_state': gi.FunctionInfo(iter_set_state), 'length': gi.FunctionInfo(length), 'prepend_type': gi.FunctionInfo(prepend_type), 'ref': gi.FunctionInfo(ref), 'to_string': gi.FunctionInfo(to_string), 'unref': gi.FunctionInfo(unref), '__new__': <staticmethod(gi.FunctionInfo(new))>, '__init__': <function nothing at 0x000002bfce305010>})"
    __gtype__ = None # (!) real value is '<GType GtkWidgetPath (3414253584)>'
    __info__ = StructInfo(WidgetPath)


