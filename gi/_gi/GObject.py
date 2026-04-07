# encoding: utf-8
# module gi._gi
# by generator 1.147
# no doc

# imports
from gobject import GBoxed, GInterface, GPointer, GType, Warning

import enum as __enum
import gi as __gi
import gobject as __gobject


from .object import object

class GObject(object):
    """
    Object GObject
    
    Signals from GObject:
      notify (GParam)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_constructed(self, *args, **kwargs): # real signature unknown
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001c5f54b2e30>'
    __dict__ = None # (!) real value is "mappingproxy({'__new__': <built-in method __new__ of type object at 0x00007ff9684a04e0>, '__repr__': <slot wrapper '__repr__' of 'gi._gi.GObject' objects>, '__hash__': <slot wrapper '__hash__' of 'gi._gi.GObject' objects>, '__lt__': <slot wrapper '__lt__' of 'gi._gi.GObject' objects>, '__le__': <slot wrapper '__le__' of 'gi._gi.GObject' objects>, '__eq__': <slot wrapper '__eq__' of 'gi._gi.GObject' objects>, '__ne__': <slot wrapper '__ne__' of 'gi._gi.GObject' objects>, '__gt__': <slot wrapper '__gt__' of 'gi._gi.GObject' objects>, '__ge__': <slot wrapper '__ge__' of 'gi._gi.GObject' objects>, '__init__': <slot wrapper '__init__' of 'gi._gi.GObject' objects>, 'get_property': <method 'get_property' of 'gi._gi.GObject' objects>, 'get_properties': <method 'get_properties' of 'gi._gi.GObject' objects>, 'set_property': <method 'set_property' of 'gi._gi.GObject' objects>, 'set_properties': <method 'set_properties' of 'gi._gi.GObject' objects>, 'bind_property': <method 'bind_property' of 'gi._gi.GObject' objects>, 'connect': <method 'connect' of 'gi._gi.GObject' objects>, 'connect_after': <method 'connect_after' of 'gi._gi.GObject' objects>, 'connect_object': <method 'connect_object' of 'gi._gi.GObject' objects>, 'connect_object_after': <method 'connect_object_after' of 'gi._gi.GObject' objects>, 'disconnect_by_func': <method 'disconnect_by_func' of 'gi._gi.GObject' objects>, 'handler_block_by_func': <method 'handler_block_by_func' of 'gi._gi.GObject' objects>, 'handler_unblock_by_func': <method 'handler_unblock_by_func' of 'gi._gi.GObject' objects>, 'emit': <method 'emit' of 'gi._gi.GObject' objects>, 'chain': <method 'chain' of 'gi._gi.GObject' objects>, 'weak_ref': <method 'weak_ref' of 'gi._gi.GObject' objects>, 'do_constructed': <method 'do_constructed' of 'gi._gi.GObject' objects>, 'do_dispose': <method 'do_dispose' of 'gi._gi.GObject' objects>, '__copy__': <method '__copy__' of 'gi._gi.GObject' objects>, '__deepcopy__': <method '__deepcopy__' of 'gi._gi.GObject' objects>, '__dict__': <attribute '__dict__' of 'gi._gi.GObject' objects>, '__grefcount__': <attribute '__grefcount__' of 'gi._gi.GObject' objects>, '__gpointer__': <attribute '__gpointer__' of 'gi._gi.GObject' objects>, '__doc__': <gobject.GObject.__doc__ object at 0x000001c5f4810c20>, '__module__': 'gi._gi', '__gtype__': <GType GObject (80)>, '__gdoc__': <gobject.GObject.__doc__ object at 0x000001c5f4810c20>, 'props': <gi._gi.GPropsDescr object at 0x000001c5f4810c10>})"
    __gdoc__ = 'Object GObject\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gtype__ = None # (!) real value is '<GType GObject (80)>'


