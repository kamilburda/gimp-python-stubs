# encoding: utf-8
# module gi.repository.Atk
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gi._gi as __gi__gi
import gobject as __gobject


class Component(__gobject.GInterface):
    # no doc
    def contains(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ contains(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def get_alpha(self): # real signature unknown; restored from __doc__
        """ get_alpha(self) -> float """
        return 0.0

    def get_extents(self, coord_type): # real signature unknown; restored from __doc__
        """ get_extents(self, coord_type:Atk.CoordType) -> x:int, y:int, width:int, height:int """
        pass

    def get_layer(self): # real signature unknown; restored from __doc__
        """ get_layer(self) -> Atk.Layer """
        pass

    def get_mdi_zorder(self): # real signature unknown; restored from __doc__
        """ get_mdi_zorder(self) -> int """
        return 0

    def get_position(self, coord_type): # real signature unknown; restored from __doc__
        """ get_position(self, coord_type:Atk.CoordType) -> x:int, y:int """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> width:int, height:int """
        pass

    def grab_focus(self): # real signature unknown; restored from __doc__
        """ grab_focus(self) -> bool """
        return False

    def ref_accessible_at_point(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ ref_accessible_at_point(self, x:int, y:int, coord_type:Atk.CoordType) -> Atk.Object or None """
        pass

    def remove_focus_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_focus_handler(self, handler_id:int) """
        pass

    def scroll_to(self, type): # real signature unknown; restored from __doc__
        """ scroll_to(self, type:Atk.ScrollType) -> bool """
        return False

    def scroll_to_point(self, coords, x, y): # real signature unknown; restored from __doc__
        """ scroll_to_point(self, coords:Atk.CoordType, x:int, y:int) -> bool """
        return False

    def set_extents(self, x, y, width, height, coord_type): # real signature unknown; restored from __doc__
        """ set_extents(self, x:int, y:int, width:int, height:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_position(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ set_position(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_size(self, width, height): # real signature unknown; restored from __doc__
        """ set_size(self, width:int, height:int) -> bool """
        return False

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Component), '__module__': 'gi.repository.Atk', '__gtype__': <GType AtkComponent (1534561920)>, '__dict__': <attribute '__dict__' of 'Component' objects>, '__weakref__': <attribute '__weakref__' of 'Component' objects>, '__doc__': None, '__gsignals__': {}, 'contains': gi.FunctionInfo(contains), 'get_alpha': gi.FunctionInfo(get_alpha), 'get_extents': gi.FunctionInfo(get_extents), 'get_layer': gi.FunctionInfo(get_layer), 'get_mdi_zorder': gi.FunctionInfo(get_mdi_zorder), 'get_position': gi.FunctionInfo(get_position), 'get_size': gi.FunctionInfo(get_size), 'grab_focus': gi.FunctionInfo(grab_focus), 'ref_accessible_at_point': gi.FunctionInfo(ref_accessible_at_point), 'remove_focus_handler': gi.FunctionInfo(remove_focus_handler), 'scroll_to': gi.FunctionInfo(scroll_to), 'scroll_to_point': gi.FunctionInfo(scroll_to_point), 'set_extents': gi.FunctionInfo(set_extents), 'set_position': gi.FunctionInfo(set_position), 'set_size': gi.FunctionInfo(set_size)})"
    __gdoc__ = 'Interface AtkComponent\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AtkComponent (1534561920)>'
    __info__ = InterfaceInfo(Component)


