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


class FontChooser(__gobject.GInterface):
    # no doc
    def get_font(self): # real signature unknown; restored from __doc__
        """ get_font(self) -> str or None """
        return ""

    def get_font_desc(self): # real signature unknown; restored from __doc__
        """ get_font_desc(self) -> Pango.FontDescription or None """
        pass

    def get_font_face(self): # real signature unknown; restored from __doc__
        """ get_font_face(self) -> Pango.FontFace or None """
        pass

    def get_font_family(self): # real signature unknown; restored from __doc__
        """ get_font_family(self) -> Pango.FontFamily or None """
        pass

    def get_font_features(self): # real signature unknown; restored from __doc__
        """ get_font_features(self) -> str """
        return ""

    def get_font_map(self): # real signature unknown; restored from __doc__
        """ get_font_map(self) -> Pango.FontMap or None """
        pass

    def get_font_size(self): # real signature unknown; restored from __doc__
        """ get_font_size(self) -> int """
        return 0

    def get_language(self): # real signature unknown; restored from __doc__
        """ get_language(self) -> str """
        return ""

    def get_level(self): # real signature unknown; restored from __doc__
        """ get_level(self) -> Gtk.FontChooserLevel """
        pass

    def get_preview_text(self): # real signature unknown; restored from __doc__
        """ get_preview_text(self) -> str """
        return ""

    def get_show_preview_entry(self): # real signature unknown; restored from __doc__
        """ get_show_preview_entry(self) -> bool """
        return False

    def set_filter_func(self, filter=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_filter_func(self, filter:Gtk.FontFilterFunc=None, user_data=None) """
        pass

    def set_font(self, fontname): # real signature unknown; restored from __doc__
        """ set_font(self, fontname:str) """
        pass

    def set_font_desc(self, font_desc): # real signature unknown; restored from __doc__
        """ set_font_desc(self, font_desc:Pango.FontDescription) """
        pass

    def set_font_map(self, fontmap=None): # real signature unknown; restored from __doc__
        """ set_font_map(self, fontmap:Pango.FontMap=None) """
        pass

    def set_language(self, language): # real signature unknown; restored from __doc__
        """ set_language(self, language:str) """
        pass

    def set_level(self, level): # real signature unknown; restored from __doc__
        """ set_level(self, level:Gtk.FontChooserLevel) """
        pass

    def set_preview_text(self, text): # real signature unknown; restored from __doc__
        """ set_preview_text(self, text:str) """
        pass

    def set_show_preview_entry(self, show_preview_entry): # real signature unknown; restored from __doc__
        """ set_show_preview_entry(self, show_preview_entry:bool) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(FontChooser), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkFontChooser (3537895856)>, '__dict__': <attribute '__dict__' of 'FontChooser' objects>, '__weakref__': <attribute '__weakref__' of 'FontChooser' objects>, '__doc__': None, '__gsignals__': {}, 'get_font': gi.FunctionInfo(get_font), 'get_font_desc': gi.FunctionInfo(get_font_desc), 'get_font_face': gi.FunctionInfo(get_font_face), 'get_font_family': gi.FunctionInfo(get_font_family), 'get_font_features': gi.FunctionInfo(get_font_features), 'get_font_map': gi.FunctionInfo(get_font_map), 'get_font_size': gi.FunctionInfo(get_font_size), 'get_language': gi.FunctionInfo(get_language), 'get_level': gi.FunctionInfo(get_level), 'get_preview_text': gi.FunctionInfo(get_preview_text), 'get_show_preview_entry': gi.FunctionInfo(get_show_preview_entry), 'set_filter_func': gi.FunctionInfo(set_filter_func), 'set_font': gi.FunctionInfo(set_font), 'set_font_desc': gi.FunctionInfo(set_font_desc), 'set_font_map': gi.FunctionInfo(set_font_map), 'set_language': gi.FunctionInfo(set_language), 'set_level': gi.FunctionInfo(set_level), 'set_preview_text': gi.FunctionInfo(set_preview_text), 'set_show_preview_entry': gi.FunctionInfo(set_show_preview_entry)})"
    __gdoc__ = 'Interface GtkFontChooser\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkFontChooser (3537895856)>'
    __info__ = InterfaceInfo(FontChooser)


