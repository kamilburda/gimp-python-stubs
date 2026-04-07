# encoding: utf-8
# module gi.repository.Gio
# by generator 1.147
# no doc

# imports
from gi.repository.GioWin32 import (NetworkMonitorClass, 
    NetworkMonitorPrivate, Win32InputStream, Win32InputStreamClass, 
    Win32InputStreamPrivate, Win32NetworkMonitor, Win32OutputStream, 
    Win32OutputStreamClass, Win32OutputStreamPrivate, 
    registry_settings_backend_new)

from _thread import _lock

import gi as __gi
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


class IOErrorEnum(__gi__gi.GEnum):
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
            `sys.byteorder' as the byte order value.  Default is to use 'big'.
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
            `sys.byteorder' as the byte order value.  Default is to use 'big'.
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

    def __init__(self, *args, **kwds): # reliably restored by inspect
        # no doc
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


    ADDRESS_IN_USE = 33
    ALREADY_MOUNTED = 17
    BROKEN_PIPE = 44
    BUSY = 26
    CANCELLED = 19
    CANT_CREATE_BACKUP = 22
    CLOSED = 18
    CONNECTION_REFUSED = 39
    DBUS_ERROR = 36
    DESTINATION_UNSET = 48
    EXISTS = 2
    FAILED = 0
    FAILED_HANDLED = 30
    FILENAME_TOO_LONG = 9
    HOST_NOT_FOUND = 28
    HOST_UNREACHABLE = 37
    INVALID_ARGUMENT = 13
    INVALID_DATA = 35
    INVALID_FILENAME = 10
    IS_DIRECTORY = 3
    MESSAGE_TOO_LARGE = 46
    NETWORK_UNREACHABLE = 38
    NOT_CONNECTED = 45
    NOT_DIRECTORY = 4
    NOT_EMPTY = 5
    NOT_FOUND = 1
    NOT_INITIALIZED = 32
    NOT_MOUNTABLE_FILE = 8
    NOT_MOUNTED = 16
    NOT_REGULAR_FILE = 6
    NOT_SUPPORTED = 15
    NOT_SYMBOLIC_LINK = 7
    NO_SPACE = 12
    NO_SUCH_DEVICE = 47
    PARTIAL_INPUT = 34
    PENDING = 20
    PERMISSION_DENIED = 14
    PROXY_AUTH_FAILED = 41
    PROXY_FAILED = 40
    PROXY_NEED_AUTH = 42
    PROXY_NOT_ALLOWED = 43
    READ_ONLY = 21
    TIMED_OUT = 24
    TOO_MANY_LINKS = 11
    TOO_MANY_OPEN_FILES = 31
    WOULD_BLOCK = 27
    WOULD_MERGE = 29
    WOULD_RECURSE = 25
    WRONG_ETAG = 23
    __class__ = None # (!) real value is "<class 'gi._enum.GEnumMeta'>"
    __members__ = None # (!) real value is "mappingproxy({'FAILED': <IOErrorEnum.FAILED: 0>, 'NOT_FOUND': <IOErrorEnum.NOT_FOUND: 1>, 'EXISTS': <IOErrorEnum.EXISTS: 2>, 'IS_DIRECTORY': <IOErrorEnum.IS_DIRECTORY: 3>, 'NOT_DIRECTORY': <IOErrorEnum.NOT_DIRECTORY: 4>, 'NOT_EMPTY': <IOErrorEnum.NOT_EMPTY: 5>, 'NOT_REGULAR_FILE': <IOErrorEnum.NOT_REGULAR_FILE: 6>, 'NOT_SYMBOLIC_LINK': <IOErrorEnum.NOT_SYMBOLIC_LINK: 7>, 'NOT_MOUNTABLE_FILE': <IOErrorEnum.NOT_MOUNTABLE_FILE: 8>, 'FILENAME_TOO_LONG': <IOErrorEnum.FILENAME_TOO_LONG: 9>, 'INVALID_FILENAME': <IOErrorEnum.INVALID_FILENAME: 10>, 'TOO_MANY_LINKS': <IOErrorEnum.TOO_MANY_LINKS: 11>, 'NO_SPACE': <IOErrorEnum.NO_SPACE: 12>, 'INVALID_ARGUMENT': <IOErrorEnum.INVALID_ARGUMENT: 13>, 'PERMISSION_DENIED': <IOErrorEnum.PERMISSION_DENIED: 14>, 'NOT_SUPPORTED': <IOErrorEnum.NOT_SUPPORTED: 15>, 'NOT_MOUNTED': <IOErrorEnum.NOT_MOUNTED: 16>, 'ALREADY_MOUNTED': <IOErrorEnum.ALREADY_MOUNTED: 17>, 'CLOSED': <IOErrorEnum.CLOSED: 18>, 'CANCELLED': <IOErrorEnum.CANCELLED: 19>, 'PENDING': <IOErrorEnum.PENDING: 20>, 'READ_ONLY': <IOErrorEnum.READ_ONLY: 21>, 'CANT_CREATE_BACKUP': <IOErrorEnum.CANT_CREATE_BACKUP: 22>, 'WRONG_ETAG': <IOErrorEnum.WRONG_ETAG: 23>, 'TIMED_OUT': <IOErrorEnum.TIMED_OUT: 24>, 'WOULD_RECURSE': <IOErrorEnum.WOULD_RECURSE: 25>, 'BUSY': <IOErrorEnum.BUSY: 26>, 'WOULD_BLOCK': <IOErrorEnum.WOULD_BLOCK: 27>, 'HOST_NOT_FOUND': <IOErrorEnum.HOST_NOT_FOUND: 28>, 'WOULD_MERGE': <IOErrorEnum.WOULD_MERGE: 29>, 'FAILED_HANDLED': <IOErrorEnum.FAILED_HANDLED: 30>, 'TOO_MANY_OPEN_FILES': <IOErrorEnum.TOO_MANY_OPEN_FILES: 31>, 'NOT_INITIALIZED': <IOErrorEnum.NOT_INITIALIZED: 32>, 'ADDRESS_IN_USE': <IOErrorEnum.ADDRESS_IN_USE: 33>, 'PARTIAL_INPUT': <IOErrorEnum.PARTIAL_INPUT: 34>, 'INVALID_DATA': <IOErrorEnum.INVALID_DATA: 35>, 'DBUS_ERROR': <IOErrorEnum.DBUS_ERROR: 36>, 'HOST_UNREACHABLE': <IOErrorEnum.HOST_UNREACHABLE: 37>, 'NETWORK_UNREACHABLE': <IOErrorEnum.NETWORK_UNREACHABLE: 38>, 'CONNECTION_REFUSED': <IOErrorEnum.CONNECTION_REFUSED: 39>, 'PROXY_FAILED': <IOErrorEnum.PROXY_FAILED: 40>, 'PROXY_AUTH_FAILED': <IOErrorEnum.PROXY_AUTH_FAILED: 41>, 'PROXY_NEED_AUTH': <IOErrorEnum.PROXY_NEED_AUTH: 42>, 'PROXY_NOT_ALLOWED': <IOErrorEnum.PROXY_NOT_ALLOWED: 43>, 'BROKEN_PIPE': <IOErrorEnum.BROKEN_PIPE: 44>, 'CONNECTION_CLOSED': <IOErrorEnum.BROKEN_PIPE: 44>, 'NOT_CONNECTED': <IOErrorEnum.NOT_CONNECTED: 45>, 'MESSAGE_TOO_LARGE': <IOErrorEnum.MESSAGE_TOO_LARGE: 46>, 'NO_SUCH_DEVICE': <IOErrorEnum.NO_SUCH_DEVICE: 47>, 'DESTINATION_UNSET': <IOErrorEnum.DESTINATION_UNSET: 48>})"
    __name__ = 'IOErrorEnum'
    __qualname__ = 'IOErrorEnum'


