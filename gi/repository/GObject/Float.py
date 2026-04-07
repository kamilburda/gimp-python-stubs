# encoding: utf-8
# module gi.repository.GObject
# by generator 1.147
# no doc

# imports
from gi.repository.GLib import (Error, GError, IOCondition, IO_ERR, 
    IO_FLAG_APPEND, IO_FLAG_GET_MASK, IO_FLAG_IS_READABLE, 
    IO_FLAG_IS_SEEKABLE, IO_FLAG_IS_WRITEABLE, IO_FLAG_MASK, IO_FLAG_NONBLOCK, 
    IO_FLAG_SET_MASK, IO_HUP, IO_IN, IO_NVAL, IO_OUT, IO_PRI, IO_STATUS_AGAIN, 
    IO_STATUS_EOF, IO_STATUS_ERROR, IO_STATUS_NORMAL, OPTION_ERROR_BAD_VALUE, 
    OPTION_ERROR_FAILED, OPTION_ERROR_UNKNOWN_OPTION, OPTION_FLAG_FILENAME, 
    OPTION_FLAG_HIDDEN, OPTION_FLAG_IN_MAIN, OPTION_FLAG_NOALIAS, 
    OPTION_FLAG_NO_ARG, OPTION_FLAG_OPTIONAL_ARG, OPTION_FLAG_REVERSE, 
    SPAWN_CHILD_INHERITS_STDIN, SPAWN_DO_NOT_REAP_CHILD, 
    SPAWN_FILE_AND_ARGV_ZERO, SPAWN_LEAVE_DESCRIPTORS_OPEN, SPAWN_SEARCH_PATH, 
    SPAWN_STDERR_TO_DEV_NULL, SPAWN_STDOUT_TO_DEV_NULL, 
    filename_display_basename, filename_display_name, get_application_name, 
    get_prgname, main_context_default, main_depth, set_application_name, 
    set_prgname, source_remove, uri_list_extract_uris)

from gi._gi import (GEnum, GFlags, GObjectWeakRef, OptionContext, OptionGroup, 
    Pid, add_emission_hook, list_properties, new, signal_new, spawn_async, 
    type_register)

from gobject import GBoxed, GInterface, GPointer, GType, Warning

from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GLib as __gi_overrides_GLib
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GLib as __gi_repository_GLib
import gi._gi as __gi__gi
import gi._signalhelper as __gi__signalhelper
import gobject as __gobject


from .float import float

class Float(float):
    """
    A wrapper to force conversion to G_TYPE_FLOAT instead of G_TYPE_DOUBLE when
        used in GValue APIs.
    """
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return a pair of integers, whose ratio is exactly equal to the original float.
        
        The ratio is in lowest terms and has a positive denominator.  Raise
        OverflowError on infinities and a ValueError on NaNs.
        
        >>> (10.0).as_integer_ratio()
        (10, 1)
        >>> (0.0).as_integer_ratio()
        (0, 1)
        >>> (-.25).as_integer_ratio()
        (-1, 4)
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Return self, the complex conjugate of any float. """
        pass

    def fromhex(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Create a floating-point number from a hexadecimal string.
        
        >>> float.fromhex('0x1.ffffp10')
        2047.984375
        >>> float.fromhex('-0x1p-1074')
        -5e-324
        """
        pass

    def hex(self): # real signature unknown; restored from __doc__
        """
        Return a hexadecimal representation of a floating-point number.
        
        >>> (-0.1).hex()
        '-0x1.999999999999ap-4'
        >>> 3.14159.hex()
        '0x1.921f9f01b866ep+1'
        """
        pass

    def is_integer(self, *args, **kwargs): # real signature unknown
        """ Return True if the float is an integer. """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Return the ceiling as an Integral. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Return the floor as an Integral. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Formats the float according to format_spec. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getformat__(self, *args, **kwargs): # real signature unknown
        """
        You probably don't want to use this function.
        
          typestr
            Must be 'double' or 'float'.
        
        It exists mainly to be used in Python's test suite.
        
        This function returns whichever of 'unknown', 'IEEE, big-endian' or 'IEEE,
        little-endian' best describes the format of floating-point numbers used by the
        C type named by typestr.
        """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
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

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Return the Integral closest to x, rounding half toward even.
        
        When an argument is passed, work like built-in round(x, ndigits).
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Return the Integral closest to x between 0 and x. """
        pass

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.GObject', '__doc__': 'A wrapper to force conversion to G_TYPE_FLOAT instead of G_TYPE_DOUBLE when\\n    used in GValue APIs.\\n    ', '__gtype__': <GType gfloat (56)>, '__dict__': <attribute '__dict__' of 'Float' objects>, '__weakref__': <attribute '__weakref__' of 'Float' objects>})"
    __gtype__ = None # (!) forward: TYPE_FLOAT, real value is '<GType gfloat (56)>'


