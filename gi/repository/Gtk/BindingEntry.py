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


class BindingEntry(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        BindingEntry()
    """
    def add_signall(self, binding_set, keyval, modifiers, signal_name, binding_args): # real signature unknown; restored from __doc__
        """ add_signall(binding_set:Gtk.BindingSet, keyval:int, modifiers:Gdk.ModifierType, signal_name:str, binding_args:list) """
        pass

    def add_signal_from_string(self, binding_set, signal_desc): # real signature unknown; restored from __doc__
        """ add_signal_from_string(binding_set:Gtk.BindingSet, signal_desc:str) -> GLib.TokenType """
        pass

    def remove(self, binding_set, keyval, modifiers): # real signature unknown; restored from __doc__
        """ remove(binding_set:Gtk.BindingSet, keyval:int, modifiers:Gdk.ModifierType) """
        pass

    def skip(self, binding_set, keyval, modifiers): # real signature unknown; restored from __doc__
        """ skip(binding_set:Gtk.BindingSet, keyval:int, modifiers:Gdk.ModifierType) """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    binding_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    destroyed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hash_next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    in_emission = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keyval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    marks_unbound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    modifiers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    signals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BindingEntry), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BindingEntry' objects>, '__weakref__': <attribute '__weakref__' of 'BindingEntry' objects>, '__doc__': None, 'keyval': <property object at 0x000002bfd17b22f0>, 'modifiers': <property object at 0x000002bfd17b23e0>, 'binding_set': <property object at 0x000002bfd17b24d0>, 'destroyed': <property object at 0x000002bfd17b25c0>, 'in_emission': <property object at 0x000002bfd17b26b0>, 'marks_unbound': <property object at 0x000002bfd17b27a0>, 'set_next': <property object at 0x000002bfd17b2890>, 'hash_next': <property object at 0x000002bfd17b2980>, 'signals': <property object at 0x000002bfd17b2a70>, 'add_signal_from_string': <staticmethod(gi.FunctionInfo(add_signal_from_string))>, 'add_signall': <staticmethod(gi.FunctionInfo(add_signall))>, 'remove': <staticmethod(gi.FunctionInfo(remove))>, 'skip': <staticmethod(gi.FunctionInfo(skip))>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BindingEntry)


