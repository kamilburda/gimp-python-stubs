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


class Range(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(lower_limit:float, upper_limit:float, description:str) -> Atk.Range
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Atk.Range """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_lower_limit(self): # real signature unknown; restored from __doc__
        """ get_lower_limit(self) -> float """
        return 0.0

    def get_upper_limit(self): # real signature unknown; restored from __doc__
        """ get_upper_limit(self) -> float """
        return 0.0

    @classmethod
    def new(cls, lower_limit, upper_limit, description): # real signature unknown; restored from __doc__
        """ new(lower_limit:float, upper_limit:float, description:str) -> Atk.Range """
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
        """ new(lower_limit:float, upper_limit:float, description:str) -> Atk.Range """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Range), '__module__': 'gi.repository.Atk', '__gtype__': <GType AtkRange (1534562784)>, '__dict__': <attribute '__dict__' of 'Range' objects>, '__weakref__': <attribute '__weakref__' of 'Range' objects>, '__doc__': None, 'new': <classmethod(gi.FunctionInfo(new))>, 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_description': gi.FunctionInfo(get_description), 'get_lower_limit': gi.FunctionInfo(get_lower_limit), 'get_upper_limit': gi.FunctionInfo(get_upper_limit), '__new__': <staticmethod(gi.FunctionInfo(new))>, '__init__': <function nothing at 0x000001c85c381010>})"
    __gtype__ = None # (!) real value is '<GType AtkRange (1534562784)>'
    __info__ = StructInfo(Range)


