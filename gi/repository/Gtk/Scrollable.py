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


class Scrollable(__gobject.GInterface):
    # no doc
    def get_border(self): # real signature unknown; restored from __doc__
        """ get_border(self) -> bool, border:Gtk.Border """
        return False

    def get_hadjustment(self): # real signature unknown; restored from __doc__
        """ get_hadjustment(self) -> Gtk.Adjustment """
        pass

    def get_hscroll_policy(self): # real signature unknown; restored from __doc__
        """ get_hscroll_policy(self) -> Gtk.ScrollablePolicy """
        pass

    def get_vadjustment(self): # real signature unknown; restored from __doc__
        """ get_vadjustment(self) -> Gtk.Adjustment """
        pass

    def get_vscroll_policy(self): # real signature unknown; restored from __doc__
        """ get_vscroll_policy(self) -> Gtk.ScrollablePolicy """
        pass

    def set_hadjustment(self, hadjustment=None): # real signature unknown; restored from __doc__
        """ set_hadjustment(self, hadjustment:Gtk.Adjustment=None) """
        pass

    def set_hscroll_policy(self, policy): # real signature unknown; restored from __doc__
        """ set_hscroll_policy(self, policy:Gtk.ScrollablePolicy) """
        pass

    def set_vadjustment(self, vadjustment=None): # real signature unknown; restored from __doc__
        """ set_vadjustment(self, vadjustment:Gtk.Adjustment=None) """
        pass

    def set_vscroll_policy(self, policy): # real signature unknown; restored from __doc__
        """ set_vscroll_policy(self, policy:Gtk.ScrollablePolicy) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Scrollable), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkScrollable (3416384496)>, '__dict__': <attribute '__dict__' of 'Scrollable' objects>, '__weakref__': <attribute '__weakref__' of 'Scrollable' objects>, '__doc__': None, '__gsignals__': {}, 'get_border': gi.FunctionInfo(get_border), 'get_hadjustment': gi.FunctionInfo(get_hadjustment), 'get_hscroll_policy': gi.FunctionInfo(get_hscroll_policy), 'get_vadjustment': gi.FunctionInfo(get_vadjustment), 'get_vscroll_policy': gi.FunctionInfo(get_vscroll_policy), 'set_hadjustment': gi.FunctionInfo(set_hadjustment), 'set_hscroll_policy': gi.FunctionInfo(set_hscroll_policy), 'set_vadjustment': gi.FunctionInfo(set_vadjustment), 'set_vscroll_policy': gi.FunctionInfo(set_vscroll_policy)})"
    __gdoc__ = 'Interface GtkScrollable\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkScrollable (3416384496)>'
    __info__ = InterfaceInfo(Scrollable)


