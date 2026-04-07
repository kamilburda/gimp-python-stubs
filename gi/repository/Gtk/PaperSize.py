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


class PaperSize(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(name:str=None) -> Gtk.PaperSize
        new_custom(name:str, display_name:str, width:float, height:float, unit:Gtk.Unit) -> Gtk.PaperSize
        new_from_gvariant(variant:GLib.Variant) -> Gtk.PaperSize
        new_from_ipp(ipp_name:str, width:float, height:float) -> Gtk.PaperSize
        new_from_key_file(key_file:GLib.KeyFile, group_name:str=None) -> Gtk.PaperSize
        new_from_ppd(ppd_name:str, ppd_display_name:str, width:float, height:float) -> Gtk.PaperSize
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gtk.PaperSize """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> str """
        return ""

    def get_default_bottom_margin(self, unit): # real signature unknown; restored from __doc__
        """ get_default_bottom_margin(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_default_left_margin(self, unit): # real signature unknown; restored from __doc__
        """ get_default_left_margin(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_default_right_margin(self, unit): # real signature unknown; restored from __doc__
        """ get_default_right_margin(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_default_top_margin(self, unit): # real signature unknown; restored from __doc__
        """ get_default_top_margin(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_display_name(self): # real signature unknown; restored from __doc__
        """ get_display_name(self) -> str """
        return ""

    def get_height(self, unit): # real signature unknown; restored from __doc__
        """ get_height(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_paper_sizes(self, include_custom): # real signature unknown; restored from __doc__
        """ get_paper_sizes(include_custom:bool) -> list """
        return []

    def get_ppd_name(self): # real signature unknown; restored from __doc__
        """ get_ppd_name(self) -> str """
        return ""

    def get_width(self, unit): # real signature unknown; restored from __doc__
        """ get_width(self, unit:Gtk.Unit) -> float """
        return 0.0

    def is_custom(self): # real signature unknown; restored from __doc__
        """ is_custom(self) -> bool """
        return False

    def is_equal(self, size2): # real signature unknown; restored from __doc__
        """ is_equal(self, size2:Gtk.PaperSize) -> bool """
        return False

    def is_ipp(self): # real signature unknown; restored from __doc__
        """ is_ipp(self) -> bool """
        return False

    @classmethod
    def new(cls, name=None): # real signature unknown; restored from __doc__
        """ new(name:str=None) -> Gtk.PaperSize """
        pass

    @classmethod
    def new_custom(cls, name, display_name, width, height, unit): # real signature unknown; restored from __doc__
        """ new_custom(name:str, display_name:str, width:float, height:float, unit:Gtk.Unit) -> Gtk.PaperSize """
        pass

    @classmethod
    def new_from_gvariant(cls, variant): # real signature unknown; restored from __doc__
        """ new_from_gvariant(variant:GLib.Variant) -> Gtk.PaperSize """
        pass

    @classmethod
    def new_from_ipp(cls, ipp_name, width, height): # real signature unknown; restored from __doc__
        """ new_from_ipp(ipp_name:str, width:float, height:float) -> Gtk.PaperSize """
        pass

    @classmethod
    def new_from_key_file(cls, key_file, group_name=None): # real signature unknown; restored from __doc__
        """ new_from_key_file(key_file:GLib.KeyFile, group_name:str=None) -> Gtk.PaperSize """
        pass

    @classmethod
    def new_from_ppd(cls, ppd_name, ppd_display_name, width, height): # real signature unknown; restored from __doc__
        """ new_from_ppd(ppd_name:str, ppd_display_name:str, width:float, height:float) -> Gtk.PaperSize """
        pass

    def set_size(self, width, height, unit): # real signature unknown; restored from __doc__
        """ set_size(self, width:float, height:float, unit:Gtk.Unit) """
        pass

    def to_gvariant(self): # real signature unknown; restored from __doc__
        """ to_gvariant(self) -> GLib.Variant """
        pass

    def to_key_file(self, key_file, group_name): # real signature unknown; restored from __doc__
        """ to_key_file(self, key_file:GLib.KeyFile, group_name:str) """
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
        """ new(name:str=None) -> Gtk.PaperSize """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(PaperSize), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkPaperSize (3540063808)>, '__dict__': <attribute '__dict__' of 'PaperSize' objects>, '__weakref__': <attribute '__weakref__' of 'PaperSize' objects>, '__doc__': None, 'new': <classmethod(gi.FunctionInfo(new))>, 'new_custom': <classmethod(gi.FunctionInfo(new_custom))>, 'new_from_gvariant': <classmethod(gi.FunctionInfo(new_from_gvariant))>, 'new_from_ipp': <classmethod(gi.FunctionInfo(new_from_ipp))>, 'new_from_key_file': <classmethod(gi.FunctionInfo(new_from_key_file))>, 'new_from_ppd': <classmethod(gi.FunctionInfo(new_from_ppd))>, 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_default_bottom_margin': gi.FunctionInfo(get_default_bottom_margin), 'get_default_left_margin': gi.FunctionInfo(get_default_left_margin), 'get_default_right_margin': gi.FunctionInfo(get_default_right_margin), 'get_default_top_margin': gi.FunctionInfo(get_default_top_margin), 'get_display_name': gi.FunctionInfo(get_display_name), 'get_height': gi.FunctionInfo(get_height), 'get_name': gi.FunctionInfo(get_name), 'get_ppd_name': gi.FunctionInfo(get_ppd_name), 'get_width': gi.FunctionInfo(get_width), 'is_custom': gi.FunctionInfo(is_custom), 'is_equal': gi.FunctionInfo(is_equal), 'is_ipp': gi.FunctionInfo(is_ipp), 'set_size': gi.FunctionInfo(set_size), 'to_gvariant': gi.FunctionInfo(to_gvariant), 'to_key_file': gi.FunctionInfo(to_key_file), 'get_default': <staticmethod(gi.FunctionInfo(get_default))>, 'get_paper_sizes': <staticmethod(gi.FunctionInfo(get_paper_sizes))>, '__new__': <staticmethod(gi.FunctionInfo(new))>, '__init__': <function nothing at 0x000002bfce305010>})"
    __gtype__ = None # (!) real value is '<GType GtkPaperSize (3540063808)>'
    __info__ = StructInfo(PaperSize)


