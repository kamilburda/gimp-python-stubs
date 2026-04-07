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


class LayerMode(__gi__gi.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return a pair of integers, whose ratio is equal to the original int.
        
        The ratio is in lowest terms and has a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_count(self): # real signature unknown; restored from __doc__
        """
        Number of ones in the binary representation of the absolute value of self.
        
        Also known as the population count.
        
        >>> bin(13)
        '0b1101'
        >>> (13).bit_count()
        3
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            sys.byteorder as the byte order value.  Default is to use 'big'.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def is_integer(self, *args, **kwargs): # real signature unknown
        """ Returns True. Exists for duck type compatibility with float.is_integer. """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.  Default
            is length 1.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            sys.byteorder as the byte order value.  Default is to use 'big'.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """
        Return True if `value` is in `cls`.
        
        `value` is in `cls` if:
        1) `value` is a member of `cls`, or
        2) `value` is the value of one of the `cls`'s members.
        3) `value` is a pseudo-member (flags)
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # reliably restored by inspect
        """ Returns public methods and other interesting attributes. """
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
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Convert to a string according to format_spec. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return the member matching `name`. """
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Return members in definition order. """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return the number of members (no aliases) """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
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
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
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

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, proto): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
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
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""


    ADDITION = 33
    ADDITION_LEGACY = 7
    BEHIND = 29
    BEHIND_LEGACY = 2
    BURN = 43
    BURN_LEGACY = 17
    COLOR_ERASE = 57
    COLOR_ERASE_LEGACY = 22
    DARKEN_ONLY = 35
    DARKEN_ONLY_LEGACY = 9
    DIFFERENCE = 32
    DIFFERENCE_LEGACY = 6
    DISSOLVE = 1
    DIVIDE = 41
    DIVIDE_LEGACY = 15
    DODGE = 42
    DODGE_LEGACY = 16
    ERASE = 58
    EXCLUSION = 52
    GRAIN_EXTRACT = 46
    GRAIN_EXTRACT_LEGACY = 20
    GRAIN_MERGE = 47
    GRAIN_MERGE_LEGACY = 21
    HARDLIGHT = 44
    HARDLIGHT_LEGACY = 18
    HARD_MIX = 51
    HSL_COLOR = 39
    HSL_COLOR_LEGACY = 13
    HSV_HUE = 37
    HSV_HUE_LEGACY = 11
    HSV_SATURATION = 38
    HSV_SATURATION_LEGACY = 12
    HSV_VALUE = 40
    HSV_VALUE_LEGACY = 14
    LCH_CHROMA = 25
    LCH_COLOR = 26
    LCH_HUE = 24
    LCH_LIGHTNESS = 27
    LIGHTEN_ONLY = 36
    LIGHTEN_ONLY_LEGACY = 10
    LINEAR_BURN = 53
    LINEAR_LIGHT = 50
    LUMA_DARKEN_ONLY = 54
    LUMA_LIGHTEN_ONLY = 55
    LUMINANCE = 56
    MERGE = 59
    MULTIPLY = 30
    MULTIPLY_LEGACY = 3
    NORMAL = 28
    NORMAL_LEGACY = 0
    OVERLAY = 23
    OVERLAY_LEGACY = 5
    OVERWRITE = 63
    PASS_THROUGH = 61
    PIN_LIGHT = 49
    REPLACE = 62
    SCREEN = 31
    SCREEN_LEGACY = 4
    SOFTLIGHT = 45
    SOFTLIGHT_LEGACY = 19
    SPLIT = 60
    SUBTRACT = 34
    SUBTRACT_LEGACY = 8
    VIVID_LIGHT = 48
    __class__ = None # (!) real value is "<class 'gi._enum.GEnumMeta'>"
    __members__ = None # (!) real value is "mappingproxy({'NORMAL_LEGACY': <LayerMode.NORMAL_LEGACY: 0>, 'DISSOLVE': <LayerMode.DISSOLVE: 1>, 'BEHIND_LEGACY': <LayerMode.BEHIND_LEGACY: 2>, 'MULTIPLY_LEGACY': <LayerMode.MULTIPLY_LEGACY: 3>, 'SCREEN_LEGACY': <LayerMode.SCREEN_LEGACY: 4>, 'OVERLAY_LEGACY': <LayerMode.OVERLAY_LEGACY: 5>, 'DIFFERENCE_LEGACY': <LayerMode.DIFFERENCE_LEGACY: 6>, 'ADDITION_LEGACY': <LayerMode.ADDITION_LEGACY: 7>, 'SUBTRACT_LEGACY': <LayerMode.SUBTRACT_LEGACY: 8>, 'DARKEN_ONLY_LEGACY': <LayerMode.DARKEN_ONLY_LEGACY: 9>, 'LIGHTEN_ONLY_LEGACY': <LayerMode.LIGHTEN_ONLY_LEGACY: 10>, 'HSV_HUE_LEGACY': <LayerMode.HSV_HUE_LEGACY: 11>, 'HSV_SATURATION_LEGACY': <LayerMode.HSV_SATURATION_LEGACY: 12>, 'HSL_COLOR_LEGACY': <LayerMode.HSL_COLOR_LEGACY: 13>, 'HSV_VALUE_LEGACY': <LayerMode.HSV_VALUE_LEGACY: 14>, 'DIVIDE_LEGACY': <LayerMode.DIVIDE_LEGACY: 15>, 'DODGE_LEGACY': <LayerMode.DODGE_LEGACY: 16>, 'BURN_LEGACY': <LayerMode.BURN_LEGACY: 17>, 'HARDLIGHT_LEGACY': <LayerMode.HARDLIGHT_LEGACY: 18>, 'SOFTLIGHT_LEGACY': <LayerMode.SOFTLIGHT_LEGACY: 19>, 'GRAIN_EXTRACT_LEGACY': <LayerMode.GRAIN_EXTRACT_LEGACY: 20>, 'GRAIN_MERGE_LEGACY': <LayerMode.GRAIN_MERGE_LEGACY: 21>, 'COLOR_ERASE_LEGACY': <LayerMode.COLOR_ERASE_LEGACY: 22>, 'OVERLAY': <LayerMode.OVERLAY: 23>, 'LCH_HUE': <LayerMode.LCH_HUE: 24>, 'LCH_CHROMA': <LayerMode.LCH_CHROMA: 25>, 'LCH_COLOR': <LayerMode.LCH_COLOR: 26>, 'LCH_LIGHTNESS': <LayerMode.LCH_LIGHTNESS: 27>, 'NORMAL': <LayerMode.NORMAL: 28>, 'BEHIND': <LayerMode.BEHIND: 29>, 'MULTIPLY': <LayerMode.MULTIPLY: 30>, 'SCREEN': <LayerMode.SCREEN: 31>, 'DIFFERENCE': <LayerMode.DIFFERENCE: 32>, 'ADDITION': <LayerMode.ADDITION: 33>, 'SUBTRACT': <LayerMode.SUBTRACT: 34>, 'DARKEN_ONLY': <LayerMode.DARKEN_ONLY: 35>, 'LIGHTEN_ONLY': <LayerMode.LIGHTEN_ONLY: 36>, 'HSV_HUE': <LayerMode.HSV_HUE: 37>, 'HSV_SATURATION': <LayerMode.HSV_SATURATION: 38>, 'HSL_COLOR': <LayerMode.HSL_COLOR: 39>, 'HSV_VALUE': <LayerMode.HSV_VALUE: 40>, 'DIVIDE': <LayerMode.DIVIDE: 41>, 'DODGE': <LayerMode.DODGE: 42>, 'BURN': <LayerMode.BURN: 43>, 'HARDLIGHT': <LayerMode.HARDLIGHT: 44>, 'SOFTLIGHT': <LayerMode.SOFTLIGHT: 45>, 'GRAIN_EXTRACT': <LayerMode.GRAIN_EXTRACT: 46>, 'GRAIN_MERGE': <LayerMode.GRAIN_MERGE: 47>, 'VIVID_LIGHT': <LayerMode.VIVID_LIGHT: 48>, 'PIN_LIGHT': <LayerMode.PIN_LIGHT: 49>, 'LINEAR_LIGHT': <LayerMode.LINEAR_LIGHT: 50>, 'HARD_MIX': <LayerMode.HARD_MIX: 51>, 'EXCLUSION': <LayerMode.EXCLUSION: 52>, 'LINEAR_BURN': <LayerMode.LINEAR_BURN: 53>, 'LUMA_DARKEN_ONLY': <LayerMode.LUMA_DARKEN_ONLY: 54>, 'LUMA_LIGHTEN_ONLY': <LayerMode.LUMA_LIGHTEN_ONLY: 55>, 'LUMINANCE': <LayerMode.LUMINANCE: 56>, 'COLOR_ERASE': <LayerMode.COLOR_ERASE: 57>, 'ERASE': <LayerMode.ERASE: 58>, 'MERGE': <LayerMode.MERGE: 59>, 'SPLIT': <LayerMode.SPLIT: 60>, 'PASS_THROUGH': <LayerMode.PASS_THROUGH: 61>, 'REPLACE': <LayerMode.REPLACE: 62>, 'OVERWRITE': <LayerMode.OVERWRITE: 63>})"
    __name__ = 'LayerMode'
    __qualname__ = 'LayerMode'


