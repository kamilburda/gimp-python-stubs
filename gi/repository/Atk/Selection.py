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


class Selection(__gobject.GInterface):
    # no doc
    def add_selection(self, i): # real signature unknown; restored from __doc__
        """ add_selection(self, i:int) -> bool """
        return False

    def clear_selection(self): # real signature unknown; restored from __doc__
        """ clear_selection(self) -> bool """
        return False

    def get_selection_count(self): # real signature unknown; restored from __doc__
        """ get_selection_count(self) -> int """
        return 0

    def is_child_selected(self, i): # real signature unknown; restored from __doc__
        """ is_child_selected(self, i:int) -> bool """
        return False

    def ref_selection(self, i): # real signature unknown; restored from __doc__
        """ ref_selection(self, i:int) -> Atk.Object or None """
        pass

    def remove_selection(self, i): # real signature unknown; restored from __doc__
        """ remove_selection(self, i:int) -> bool """
        return False

    def select_all_selection(self): # real signature unknown; restored from __doc__
        """ select_all_selection(self) -> bool """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Selection), '__module__': 'gi.repository.Atk', '__gtype__': <GType AtkSelection (1534563456)>, '__dict__': <attribute '__dict__' of 'Selection' objects>, '__weakref__': <attribute '__weakref__' of 'Selection' objects>, '__doc__': None, '__gsignals__': {}, 'add_selection': gi.FunctionInfo(add_selection), 'clear_selection': gi.FunctionInfo(clear_selection), 'get_selection_count': gi.FunctionInfo(get_selection_count), 'is_child_selected': gi.FunctionInfo(is_child_selected), 'ref_selection': gi.FunctionInfo(ref_selection), 'remove_selection': gi.FunctionInfo(remove_selection), 'select_all_selection': gi.FunctionInfo(select_all_selection)})"
    __gdoc__ = 'Interface AtkSelection\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AtkSelection (1534563456)>'
    __info__ = InterfaceInfo(Selection)


