# encoding: utf-8
# module gi.repository.cairo
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi._gi as __gi__gi


class Status(__gi__gi.GEnum):
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


    CLIP_NOT_REPRESENTABLE = 22
    DEVICE_ERROR = 35
    DEVICE_FINISHED = 37
    DEVICE_TYPE_MISMATCH = 34
    FILE_NOT_FOUND = 18
    FONT_TYPE_MISMATCH = 25
    FREETYPE_ERROR = 40
    INVALID_CLUSTERS = 29
    INVALID_CONTENT = 15
    INVALID_DASH = 19
    INVALID_DSC_COMMENT = 20
    INVALID_FORMAT = 16
    INVALID_INDEX = 21
    INVALID_MATRIX = 5
    INVALID_MESH_CONSTRUCTION = 36
    INVALID_PATH_DATA = 9
    INVALID_POP_GROUP = 3
    INVALID_RESTORE = 2
    INVALID_SIZE = 32
    INVALID_SLANT = 30
    INVALID_STATUS = 6
    INVALID_STRIDE = 24
    INVALID_STRING = 8
    INVALID_VISUAL = 17
    INVALID_WEIGHT = 31
    JBIG2_GLOBAL_MISSING = 38
    LAST_STATUS = 45
    NEGATIVE_COUNT = 28
    NO_CURRENT_POINT = 4
    NO_MEMORY = 1
    NULL_POINTER = 7
    PATTERN_TYPE_MISMATCH = 14
    PNG_ERROR = 39
    READ_ERROR = 10
    SUCCESS = 0
    SURFACE_FINISHED = 12
    SURFACE_TYPE_MISMATCH = 13
    TEMP_FILE_ERROR = 23
    USER_FONT_ERROR = 27
    USER_FONT_IMMUTABLE = 26
    USER_FONT_NOT_IMPLEMENTED = 33
    WIN32_GDI_ERROR = 41
    WRITE_ERROR = 11
    __class__ = None # (!) real value is "<class 'gi._enum.GEnumMeta'>"
    __members__ = None # (!) real value is "mappingproxy({'SUCCESS': <Status.SUCCESS: 0>, 'NO_MEMORY': <Status.NO_MEMORY: 1>, 'INVALID_RESTORE': <Status.INVALID_RESTORE: 2>, 'INVALID_POP_GROUP': <Status.INVALID_POP_GROUP: 3>, 'NO_CURRENT_POINT': <Status.NO_CURRENT_POINT: 4>, 'INVALID_MATRIX': <Status.INVALID_MATRIX: 5>, 'INVALID_STATUS': <Status.INVALID_STATUS: 6>, 'NULL_POINTER': <Status.NULL_POINTER: 7>, 'INVALID_STRING': <Status.INVALID_STRING: 8>, 'INVALID_PATH_DATA': <Status.INVALID_PATH_DATA: 9>, 'READ_ERROR': <Status.READ_ERROR: 10>, 'WRITE_ERROR': <Status.WRITE_ERROR: 11>, 'SURFACE_FINISHED': <Status.SURFACE_FINISHED: 12>, 'SURFACE_TYPE_MISMATCH': <Status.SURFACE_TYPE_MISMATCH: 13>, 'PATTERN_TYPE_MISMATCH': <Status.PATTERN_TYPE_MISMATCH: 14>, 'INVALID_CONTENT': <Status.INVALID_CONTENT: 15>, 'INVALID_FORMAT': <Status.INVALID_FORMAT: 16>, 'INVALID_VISUAL': <Status.INVALID_VISUAL: 17>, 'FILE_NOT_FOUND': <Status.FILE_NOT_FOUND: 18>, 'INVALID_DASH': <Status.INVALID_DASH: 19>, 'INVALID_DSC_COMMENT': <Status.INVALID_DSC_COMMENT: 20>, 'INVALID_INDEX': <Status.INVALID_INDEX: 21>, 'CLIP_NOT_REPRESENTABLE': <Status.CLIP_NOT_REPRESENTABLE: 22>, 'TEMP_FILE_ERROR': <Status.TEMP_FILE_ERROR: 23>, 'INVALID_STRIDE': <Status.INVALID_STRIDE: 24>, 'FONT_TYPE_MISMATCH': <Status.FONT_TYPE_MISMATCH: 25>, 'USER_FONT_IMMUTABLE': <Status.USER_FONT_IMMUTABLE: 26>, 'USER_FONT_ERROR': <Status.USER_FONT_ERROR: 27>, 'NEGATIVE_COUNT': <Status.NEGATIVE_COUNT: 28>, 'INVALID_CLUSTERS': <Status.INVALID_CLUSTERS: 29>, 'INVALID_SLANT': <Status.INVALID_SLANT: 30>, 'INVALID_WEIGHT': <Status.INVALID_WEIGHT: 31>, 'INVALID_SIZE': <Status.INVALID_SIZE: 32>, 'USER_FONT_NOT_IMPLEMENTED': <Status.USER_FONT_NOT_IMPLEMENTED: 33>, 'DEVICE_TYPE_MISMATCH': <Status.DEVICE_TYPE_MISMATCH: 34>, 'DEVICE_ERROR': <Status.DEVICE_ERROR: 35>, 'INVALID_MESH_CONSTRUCTION': <Status.INVALID_MESH_CONSTRUCTION: 36>, 'DEVICE_FINISHED': <Status.DEVICE_FINISHED: 37>, 'JBIG2_GLOBAL_MISSING': <Status.JBIG2_GLOBAL_MISSING: 38>, 'PNG_ERROR': <Status.PNG_ERROR: 39>, 'FREETYPE_ERROR': <Status.FREETYPE_ERROR: 40>, 'LAST_STATUS': <Status.LAST_STATUS: 45>, 'WIN32_GDI_ERROR': <Status.WIN32_GDI_ERROR: 41>})"
    __name__ = 'Status'
    __qualname__ = 'Status'


