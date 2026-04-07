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


class DBusError(__gi__gi.GEnum):
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


    ACCESS_DENIED = 9
    ADDRESS_IN_USE = 14
    ADT_AUDIT_DATA_UNKNOWN = 39
    AUTH_FAILED = 10
    BAD_ADDRESS = 6
    DISCONNECTED = 15
    FAILED = 0
    FILE_EXISTS = 18
    FILE_NOT_FOUND = 17
    INVALID_ARGS = 16
    INVALID_FILE_CONTENT = 37
    INVALID_SIGNATURE = 36
    IO_ERROR = 5
    LIMITS_EXCEEDED = 8
    MATCH_RULE_INVALID = 22
    MATCH_RULE_NOT_FOUND = 21
    NAME_HAS_NO_OWNER = 3
    NOT_SUPPORTED = 7
    NO_MEMORY = 1
    NO_NETWORK = 13
    NO_REPLY = 4
    NO_SERVER = 11
    OBJECT_PATH_IN_USE = 40
    PROPERTY_READ_ONLY = 44
    SELINUX_SECURITY_CONTEXT_UNKNOWN = 38
    SERVICE_UNKNOWN = 2
    SPAWN_CHILD_EXITED = 25
    SPAWN_CHILD_SIGNALED = 26
    SPAWN_CONFIG_INVALID = 29
    SPAWN_EXEC_FAILED = 23
    SPAWN_FAILED = 27
    SPAWN_FILE_INVALID = 33
    SPAWN_FORK_FAILED = 24
    SPAWN_NO_MEMORY = 34
    SPAWN_PERMISSIONS_INVALID = 32
    SPAWN_SERVICE_INVALID = 30
    SPAWN_SERVICE_NOT_FOUND = 31
    SPAWN_SETUP_FAILED = 28
    TIMED_OUT = 20
    TIMEOUT = 12
    UNIX_PROCESS_ID_UNKNOWN = 35
    UNKNOWN_INTERFACE = 42
    UNKNOWN_METHOD = 19
    UNKNOWN_OBJECT = 41
    UNKNOWN_PROPERTY = 43
    __class__ = None # (!) real value is "<class 'gi._enum.GEnumMeta'>"
    __members__ = None # (!) real value is "mappingproxy({'FAILED': <DBusError.FAILED: 0>, 'NO_MEMORY': <DBusError.NO_MEMORY: 1>, 'SERVICE_UNKNOWN': <DBusError.SERVICE_UNKNOWN: 2>, 'NAME_HAS_NO_OWNER': <DBusError.NAME_HAS_NO_OWNER: 3>, 'NO_REPLY': <DBusError.NO_REPLY: 4>, 'IO_ERROR': <DBusError.IO_ERROR: 5>, 'BAD_ADDRESS': <DBusError.BAD_ADDRESS: 6>, 'NOT_SUPPORTED': <DBusError.NOT_SUPPORTED: 7>, 'LIMITS_EXCEEDED': <DBusError.LIMITS_EXCEEDED: 8>, 'ACCESS_DENIED': <DBusError.ACCESS_DENIED: 9>, 'AUTH_FAILED': <DBusError.AUTH_FAILED: 10>, 'NO_SERVER': <DBusError.NO_SERVER: 11>, 'TIMEOUT': <DBusError.TIMEOUT: 12>, 'NO_NETWORK': <DBusError.NO_NETWORK: 13>, 'ADDRESS_IN_USE': <DBusError.ADDRESS_IN_USE: 14>, 'DISCONNECTED': <DBusError.DISCONNECTED: 15>, 'INVALID_ARGS': <DBusError.INVALID_ARGS: 16>, 'FILE_NOT_FOUND': <DBusError.FILE_NOT_FOUND: 17>, 'FILE_EXISTS': <DBusError.FILE_EXISTS: 18>, 'UNKNOWN_METHOD': <DBusError.UNKNOWN_METHOD: 19>, 'TIMED_OUT': <DBusError.TIMED_OUT: 20>, 'MATCH_RULE_NOT_FOUND': <DBusError.MATCH_RULE_NOT_FOUND: 21>, 'MATCH_RULE_INVALID': <DBusError.MATCH_RULE_INVALID: 22>, 'SPAWN_EXEC_FAILED': <DBusError.SPAWN_EXEC_FAILED: 23>, 'SPAWN_FORK_FAILED': <DBusError.SPAWN_FORK_FAILED: 24>, 'SPAWN_CHILD_EXITED': <DBusError.SPAWN_CHILD_EXITED: 25>, 'SPAWN_CHILD_SIGNALED': <DBusError.SPAWN_CHILD_SIGNALED: 26>, 'SPAWN_FAILED': <DBusError.SPAWN_FAILED: 27>, 'SPAWN_SETUP_FAILED': <DBusError.SPAWN_SETUP_FAILED: 28>, 'SPAWN_CONFIG_INVALID': <DBusError.SPAWN_CONFIG_INVALID: 29>, 'SPAWN_SERVICE_INVALID': <DBusError.SPAWN_SERVICE_INVALID: 30>, 'SPAWN_SERVICE_NOT_FOUND': <DBusError.SPAWN_SERVICE_NOT_FOUND: 31>, 'SPAWN_PERMISSIONS_INVALID': <DBusError.SPAWN_PERMISSIONS_INVALID: 32>, 'SPAWN_FILE_INVALID': <DBusError.SPAWN_FILE_INVALID: 33>, 'SPAWN_NO_MEMORY': <DBusError.SPAWN_NO_MEMORY: 34>, 'UNIX_PROCESS_ID_UNKNOWN': <DBusError.UNIX_PROCESS_ID_UNKNOWN: 35>, 'INVALID_SIGNATURE': <DBusError.INVALID_SIGNATURE: 36>, 'INVALID_FILE_CONTENT': <DBusError.INVALID_FILE_CONTENT: 37>, 'SELINUX_SECURITY_CONTEXT_UNKNOWN': <DBusError.SELINUX_SECURITY_CONTEXT_UNKNOWN: 38>, 'ADT_AUDIT_DATA_UNKNOWN': <DBusError.ADT_AUDIT_DATA_UNKNOWN: 39>, 'OBJECT_PATH_IN_USE': <DBusError.OBJECT_PATH_IN_USE: 40>, 'UNKNOWN_OBJECT': <DBusError.UNKNOWN_OBJECT: 41>, 'UNKNOWN_INTERFACE': <DBusError.UNKNOWN_INTERFACE: 42>, 'UNKNOWN_PROPERTY': <DBusError.UNKNOWN_PROPERTY: 43>, 'PROPERTY_READ_ONLY': <DBusError.PROPERTY_READ_ONLY: 44>})"
    __name__ = 'DBusError'
    __qualname__ = 'DBusError'


