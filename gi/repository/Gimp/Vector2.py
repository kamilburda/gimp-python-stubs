# encoding: utf-8
# module gi.repository.Gimp
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GExiv2 as __gi_overrides_GExiv2
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


class Vector2(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Vector2()
        new(x:float, y:float) -> Gimp.Vector2
    """
    def add(self, vector1, vector2): # real signature unknown; restored from __doc__
        """ add(vector1:Gimp.Vector2, vector2:Gimp.Vector2) -> result:Gimp.Vector2 """
        pass

    def add_val(self, vector2): # real signature unknown; restored from __doc__
        """ add_val(self, vector2:Gimp.Vector2) -> Gimp.Vector2 """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def cross_product(self, vector2): # real signature unknown; restored from __doc__
        """ cross_product(self, vector2:Gimp.Vector2) -> Gimp.Vector2 """
        pass

    def cross_product_val(self, vector2): # real signature unknown; restored from __doc__
        """ cross_product_val(self, vector2:Gimp.Vector2) -> Gimp.Vector2 """
        pass

    def inner_product(self, vector2): # real signature unknown; restored from __doc__
        """ inner_product(self, vector2:Gimp.Vector2) -> float """
        return 0.0

    def inner_product_val(self, vector2): # real signature unknown; restored from __doc__
        """ inner_product_val(self, vector2:Gimp.Vector2) -> float """
        return 0.0

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def length_val(self): # real signature unknown; restored from __doc__
        """ length_val(self) -> float """
        return 0.0

    def mul(self, factor): # real signature unknown; restored from __doc__
        """ mul(self, factor:float) """
        pass

    def mul_val(self, factor): # real signature unknown; restored from __doc__
        """ mul_val(self, factor:float) -> Gimp.Vector2 """
        pass

    def neg(self): # real signature unknown; restored from __doc__
        """ neg(self) """
        pass

    def neg_val(self): # real signature unknown; restored from __doc__
        """ neg_val(self) -> Gimp.Vector2 """
        pass

    @classmethod
    def new(cls, x, y): # real signature unknown; restored from __doc__
        """ new(x:float, y:float) -> Gimp.Vector2 """
        pass

    def normal(self): # real signature unknown; restored from __doc__
        """ normal(self) -> Gimp.Vector2 """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) """
        pass

    def normalize_val(self): # real signature unknown; restored from __doc__
        """ normalize_val(self) -> Gimp.Vector2 """
        pass

    def normal_val(self): # real signature unknown; restored from __doc__
        """ normal_val(self) -> Gimp.Vector2 """
        pass

    def rotate(self, alpha): # real signature unknown; restored from __doc__
        """ rotate(self, alpha:float) """
        pass

    def rotate_val(self, alpha): # real signature unknown; restored from __doc__
        """ rotate_val(self, alpha:float) -> Gimp.Vector2 """
        pass

    def set(self, x, y): # real signature unknown; restored from __doc__
        """ set(self, x:float, y:float) """
        pass

    def sub(self, vector1, vector2): # real signature unknown; restored from __doc__
        """ sub(vector1:Gimp.Vector2, vector2:Gimp.Vector2) -> result:Gimp.Vector2 """
        pass

    def sub_val(self, vector2): # real signature unknown; restored from __doc__
        """ sub_val(self, vector2:Gimp.Vector2) -> Gimp.Vector2 """
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

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Vector2), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpVector2 (2360887776)>, '__dict__': <attribute '__dict__' of 'Vector2' objects>, '__weakref__': <attribute '__weakref__' of 'Vector2' objects>, '__doc__': None, 'x': <property object at 0x000001268f548540>, 'y': <property object at 0x000001268f548450>, 'new': <classmethod(gi.FunctionInfo(new))>, 'add_val': gi.FunctionInfo(add_val), 'cross_product': gi.FunctionInfo(cross_product), 'cross_product_val': gi.FunctionInfo(cross_product_val), 'inner_product': gi.FunctionInfo(inner_product), 'inner_product_val': gi.FunctionInfo(inner_product_val), 'length': gi.FunctionInfo(length), 'length_val': gi.FunctionInfo(length_val), 'mul': gi.FunctionInfo(mul), 'mul_val': gi.FunctionInfo(mul_val), 'neg': gi.FunctionInfo(neg), 'neg_val': gi.FunctionInfo(neg_val), 'normal': gi.FunctionInfo(normal), 'normal_val': gi.FunctionInfo(normal_val), 'normalize': gi.FunctionInfo(normalize), 'normalize_val': gi.FunctionInfo(normalize_val), 'rotate': gi.FunctionInfo(rotate), 'rotate_val': gi.FunctionInfo(rotate_val), 'set': gi.FunctionInfo(set), 'sub_val': gi.FunctionInfo(sub_val), 'add': <staticmethod(gi.FunctionInfo(add))>, 'sub': <staticmethod(gi.FunctionInfo(sub))>})"
    __gtype__ = None # (!) real value is '<GType GimpVector2 (2360887776)>'
    __info__ = StructInfo(Vector2)


