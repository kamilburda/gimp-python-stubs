# encoding: utf-8
# module gi.repository.HarfBuzz
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi


class unicode_combining_class_t(__enum.IntEnum):
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


    ABOVE = 230
    ABOVE_LEFT = 228
    ABOVE_RIGHT = 232
    ATTACHED_ABOVE = 214
    ATTACHED_ABOVE_RIGHT = 216
    ATTACHED_BELOW = 202
    ATTACHED_BELOW_LEFT = 200
    BELOW = 220
    BELOW_LEFT = 218
    BELOW_RIGHT = 222
    CCC10 = 10
    CCC103 = 103
    CCC107 = 107
    CCC11 = 11
    CCC118 = 118
    CCC12 = 12
    CCC122 = 122
    CCC129 = 129
    CCC13 = 13
    CCC130 = 130
    CCC132 = 132
    CCC14 = 14
    CCC15 = 15
    CCC16 = 16
    CCC17 = 17
    CCC18 = 18
    CCC19 = 19
    CCC20 = 20
    CCC21 = 21
    CCC22 = 22
    CCC23 = 23
    CCC24 = 24
    CCC25 = 25
    CCC26 = 26
    CCC27 = 27
    CCC28 = 28
    CCC29 = 29
    CCC30 = 30
    CCC31 = 31
    CCC32 = 32
    CCC33 = 33
    CCC34 = 34
    CCC35 = 35
    CCC36 = 36
    CCC84 = 84
    CCC91 = 91
    DOUBLE_ABOVE = 234
    DOUBLE_BELOW = 233
    INVALID = 255
    IOTA_SUBSCRIPT = 240
    KANA_VOICING = 8
    LEFT = 224
    NOT_REORDERED = 0
    NUKTA = 7
    OVERLAY = 1
    RIGHT = 226
    VIRAMA = 9
    __class__ = None # (!) real value is "<class 'enum.EnumType'>"
    __members__ = None # (!) real value is "mappingproxy({'NOT_REORDERED': <unicode_combining_class_t.NOT_REORDERED: 0>, 'OVERLAY': <unicode_combining_class_t.OVERLAY: 1>, 'NUKTA': <unicode_combining_class_t.NUKTA: 7>, 'KANA_VOICING': <unicode_combining_class_t.KANA_VOICING: 8>, 'VIRAMA': <unicode_combining_class_t.VIRAMA: 9>, 'CCC10': <unicode_combining_class_t.CCC10: 10>, 'CCC11': <unicode_combining_class_t.CCC11: 11>, 'CCC12': <unicode_combining_class_t.CCC12: 12>, 'CCC13': <unicode_combining_class_t.CCC13: 13>, 'CCC14': <unicode_combining_class_t.CCC14: 14>, 'CCC15': <unicode_combining_class_t.CCC15: 15>, 'CCC16': <unicode_combining_class_t.CCC16: 16>, 'CCC17': <unicode_combining_class_t.CCC17: 17>, 'CCC18': <unicode_combining_class_t.CCC18: 18>, 'CCC19': <unicode_combining_class_t.CCC19: 19>, 'CCC20': <unicode_combining_class_t.CCC20: 20>, 'CCC21': <unicode_combining_class_t.CCC21: 21>, 'CCC22': <unicode_combining_class_t.CCC22: 22>, 'CCC23': <unicode_combining_class_t.CCC23: 23>, 'CCC24': <unicode_combining_class_t.CCC24: 24>, 'CCC25': <unicode_combining_class_t.CCC25: 25>, 'CCC26': <unicode_combining_class_t.CCC26: 26>, 'CCC27': <unicode_combining_class_t.CCC27: 27>, 'CCC28': <unicode_combining_class_t.CCC28: 28>, 'CCC29': <unicode_combining_class_t.CCC29: 29>, 'CCC30': <unicode_combining_class_t.CCC30: 30>, 'CCC31': <unicode_combining_class_t.CCC31: 31>, 'CCC32': <unicode_combining_class_t.CCC32: 32>, 'CCC33': <unicode_combining_class_t.CCC33: 33>, 'CCC34': <unicode_combining_class_t.CCC34: 34>, 'CCC35': <unicode_combining_class_t.CCC35: 35>, 'CCC36': <unicode_combining_class_t.CCC36: 36>, 'CCC84': <unicode_combining_class_t.CCC84: 84>, 'CCC91': <unicode_combining_class_t.CCC91: 91>, 'CCC103': <unicode_combining_class_t.CCC103: 103>, 'CCC107': <unicode_combining_class_t.CCC107: 107>, 'CCC118': <unicode_combining_class_t.CCC118: 118>, 'CCC122': <unicode_combining_class_t.CCC122: 122>, 'CCC129': <unicode_combining_class_t.CCC129: 129>, 'CCC130': <unicode_combining_class_t.CCC130: 130>, 'CCC132': <unicode_combining_class_t.CCC132: 132>, 'ATTACHED_BELOW_LEFT': <unicode_combining_class_t.ATTACHED_BELOW_LEFT: 200>, 'ATTACHED_BELOW': <unicode_combining_class_t.ATTACHED_BELOW: 202>, 'ATTACHED_ABOVE': <unicode_combining_class_t.ATTACHED_ABOVE: 214>, 'ATTACHED_ABOVE_RIGHT': <unicode_combining_class_t.ATTACHED_ABOVE_RIGHT: 216>, 'BELOW_LEFT': <unicode_combining_class_t.BELOW_LEFT: 218>, 'BELOW': <unicode_combining_class_t.BELOW: 220>, 'BELOW_RIGHT': <unicode_combining_class_t.BELOW_RIGHT: 222>, 'LEFT': <unicode_combining_class_t.LEFT: 224>, 'RIGHT': <unicode_combining_class_t.RIGHT: 226>, 'ABOVE_LEFT': <unicode_combining_class_t.ABOVE_LEFT: 228>, 'ABOVE': <unicode_combining_class_t.ABOVE: 230>, 'ABOVE_RIGHT': <unicode_combining_class_t.ABOVE_RIGHT: 232>, 'DOUBLE_BELOW': <unicode_combining_class_t.DOUBLE_BELOW: 233>, 'DOUBLE_ABOVE': <unicode_combining_class_t.DOUBLE_ABOVE: 234>, 'IOTA_SUBSCRIPT': <unicode_combining_class_t.IOTA_SUBSCRIPT: 240>, 'INVALID': <unicode_combining_class_t.INVALID: 255>})"
    __name__ = 'unicode_combining_class_t'
    __qualname__ = 'unicode_combining_class_t'


