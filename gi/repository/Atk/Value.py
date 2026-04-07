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


class Value(__gobject.GInterface):
    # no doc
    def get_current_value(self): # real signature unknown; restored from __doc__
        """ get_current_value(self) -> value:GObject.Value """
        pass

    def get_increment(self): # real signature unknown; restored from __doc__
        """ get_increment(self) -> float """
        return 0.0

    def get_maximum_value(self): # real signature unknown; restored from __doc__
        """ get_maximum_value(self) -> value:GObject.Value """
        pass

    def get_minimum_increment(self): # real signature unknown; restored from __doc__
        """ get_minimum_increment(self) -> value:GObject.Value """
        pass

    def get_minimum_value(self): # real signature unknown; restored from __doc__
        """ get_minimum_value(self) -> value:GObject.Value """
        pass

    def get_range(self): # real signature unknown; restored from __doc__
        """ get_range(self) -> Atk.Range or None """
        pass

    def get_sub_ranges(self): # real signature unknown; restored from __doc__
        """ get_sub_ranges(self) -> list """
        return []

    def get_value_and_text(self): # real signature unknown; restored from __doc__
        """ get_value_and_text(self) -> value:float, text:str """
        pass

    def set_current_value(self, value): # real signature unknown; restored from __doc__
        """ set_current_value(self, value:GObject.Value) -> bool """
        return False

    def set_value(self, new_value): # real signature unknown; restored from __doc__
        """ set_value(self, new_value:float) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Value), '__module__': 'gi.repository.Atk', '__gtype__': <GType AtkValue (1534561248)>, '__dict__': <attribute '__dict__' of 'Value' objects>, '__weakref__': <attribute '__weakref__' of 'Value' objects>, '__doc__': None, '__gsignals__': {}, 'get_current_value': gi.FunctionInfo(get_current_value), 'get_increment': gi.FunctionInfo(get_increment), 'get_maximum_value': gi.FunctionInfo(get_maximum_value), 'get_minimum_increment': gi.FunctionInfo(get_minimum_increment), 'get_minimum_value': gi.FunctionInfo(get_minimum_value), 'get_range': gi.FunctionInfo(get_range), 'get_sub_ranges': gi.FunctionInfo(get_sub_ranges), 'get_value_and_text': gi.FunctionInfo(get_value_and_text), 'set_current_value': gi.FunctionInfo(set_current_value), 'set_value': gi.FunctionInfo(set_value)})"
    __gdoc__ = 'Interface AtkValue\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AtkValue (1534561248)>'
    __info__ = InterfaceInfo(Value)


