# encoding: utf-8
# module gi.repository.HarfBuzz
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi


class ot_metrics_tag_t(__enum.IntFlag):
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

    def __and__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __contains__(self, other): # reliably restored by inspect
        """ Returns True if self has at least the same flags set as other. """
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

    def __invert__(self): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        """ Returns flags in definition order. """
        pass

    def __len__(self): # reliably restored by inspect
        # no doc
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

    def __or__(self, other): # reliably restored by inspect
        # no doc
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

    def __rand__(self, other): # reliably restored by inspect
        # no doc
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

    def __ror__(self, other): # reliably restored by inspect
        # no doc
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

    def __rxor__(self, other): # reliably restored by inspect
        # no doc
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

    def __xor__(self, other): # reliably restored by inspect
        # no doc
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""


    __class__ = None # (!) real value is "<class 'enum.EnumType'>"
    __members__ = None # (!) real value is "mappingproxy({'B_OT_METRICS_TAG_HORIZONTAL_ASCENDER': <ot_metrics_tag_t.B_OT_METRICS_TAG_HORIZONTAL_ASCENDER: 1751216995>, 'B_OT_METRICS_TAG_HORIZONTAL_DESCENDER': <ot_metrics_tag_t.B_OT_METRICS_TAG_HORIZONTAL_DESCENDER: 1751413603>, 'B_OT_METRICS_TAG_HORIZONTAL_LINE_GAP': <ot_metrics_tag_t.B_OT_METRICS_TAG_HORIZONTAL_LINE_GAP: 1751934832>, 'B_OT_METRICS_TAG_HORIZONTAL_CLIPPING_ASCENT': <ot_metrics_tag_t.B_OT_METRICS_TAG_HORIZONTAL_CLIPPING_ASCENT: 1751346273>, 'B_OT_METRICS_TAG_HORIZONTAL_CLIPPING_DESCENT': <ot_metrics_tag_t.B_OT_METRICS_TAG_HORIZONTAL_CLIPPING_DESCENT: 1751346276>, 'B_OT_METRICS_TAG_VERTICAL_ASCENDER': <ot_metrics_tag_t.B_OT_METRICS_TAG_VERTICAL_ASCENDER: 1986098019>, 'B_OT_METRICS_TAG_VERTICAL_DESCENDER': <ot_metrics_tag_t.B_OT_METRICS_TAG_VERTICAL_DESCENDER: 1986294627>, 'B_OT_METRICS_TAG_VERTICAL_LINE_GAP': <ot_metrics_tag_t.B_OT_METRICS_TAG_VERTICAL_LINE_GAP: 1986815856>, 'B_OT_METRICS_TAG_HORIZONTAL_CARET_RISE': <ot_metrics_tag_t.B_OT_METRICS_TAG_HORIZONTAL_CARET_RISE: 1751347827>, 'B_OT_METRICS_TAG_HORIZONTAL_CARET_RUN': <ot_metrics_tag_t.B_OT_METRICS_TAG_HORIZONTAL_CARET_RUN: 1751347822>, 'B_OT_METRICS_TAG_HORIZONTAL_CARET_OFFSET': <ot_metrics_tag_t.B_OT_METRICS_TAG_HORIZONTAL_CARET_OFFSET: 1751347046>, 'B_OT_METRICS_TAG_VERTICAL_CARET_RISE': <ot_metrics_tag_t.B_OT_METRICS_TAG_VERTICAL_CARET_RISE: 1986228851>, 'B_OT_METRICS_TAG_VERTICAL_CARET_RUN': <ot_metrics_tag_t.B_OT_METRICS_TAG_VERTICAL_CARET_RUN: 1986228846>, 'B_OT_METRICS_TAG_VERTICAL_CARET_OFFSET': <ot_metrics_tag_t.B_OT_METRICS_TAG_VERTICAL_CARET_OFFSET: 1986228070>, 'B_OT_METRICS_TAG_X_HEIGHT': <ot_metrics_tag_t.B_OT_METRICS_TAG_X_HEIGHT: 2020108148>, 'B_OT_METRICS_TAG_CAP_HEIGHT': <ot_metrics_tag_t.B_OT_METRICS_TAG_CAP_HEIGHT: 1668311156>, 'B_OT_METRICS_TAG_SUBSCRIPT_EM_X_SIZE': <ot_metrics_tag_t.B_OT_METRICS_TAG_SUBSCRIPT_EM_X_SIZE: 1935833203>, 'B_OT_METRICS_TAG_SUBSCRIPT_EM_Y_SIZE': <ot_metrics_tag_t.B_OT_METRICS_TAG_SUBSCRIPT_EM_Y_SIZE: 1935833459>, 'B_OT_METRICS_TAG_SUBSCRIPT_EM_X_OFFSET': <ot_metrics_tag_t.B_OT_METRICS_TAG_SUBSCRIPT_EM_X_OFFSET: 1935833199>, 'B_OT_METRICS_TAG_SUBSCRIPT_EM_Y_OFFSET': <ot_metrics_tag_t.B_OT_METRICS_TAG_SUBSCRIPT_EM_Y_OFFSET: 1935833455>, 'B_OT_METRICS_TAG_SUPERSCRIPT_EM_X_SIZE': <ot_metrics_tag_t.B_OT_METRICS_TAG_SUPERSCRIPT_EM_X_SIZE: 1936750707>, 'B_OT_METRICS_TAG_SUPERSCRIPT_EM_Y_SIZE': <ot_metrics_tag_t.B_OT_METRICS_TAG_SUPERSCRIPT_EM_Y_SIZE: 1936750963>, 'B_OT_METRICS_TAG_SUPERSCRIPT_EM_X_OFFSET': <ot_metrics_tag_t.B_OT_METRICS_TAG_SUPERSCRIPT_EM_X_OFFSET: 1936750703>, 'B_OT_METRICS_TAG_SUPERSCRIPT_EM_Y_OFFSET': <ot_metrics_tag_t.B_OT_METRICS_TAG_SUPERSCRIPT_EM_Y_OFFSET: 1936750959>, 'B_OT_METRICS_TAG_STRIKEOUT_SIZE': <ot_metrics_tag_t.B_OT_METRICS_TAG_STRIKEOUT_SIZE: 1937011315>, 'B_OT_METRICS_TAG_STRIKEOUT_OFFSET': <ot_metrics_tag_t.B_OT_METRICS_TAG_STRIKEOUT_OFFSET: 1937011311>, 'B_OT_METRICS_TAG_UNDERLINE_SIZE': <ot_metrics_tag_t.B_OT_METRICS_TAG_UNDERLINE_SIZE: 1970168947>, 'B_OT_METRICS_TAG_UNDERLINE_OFFSET': <ot_metrics_tag_t.B_OT_METRICS_TAG_UNDERLINE_OFFSET: 1970168943>})"
    __name__ = 'ot_metrics_tag_t'
    __qualname__ = 'ot_metrics_tag_t'


