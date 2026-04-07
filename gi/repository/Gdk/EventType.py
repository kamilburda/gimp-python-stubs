# encoding: utf-8
# module gi.repository.Gdk
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gi._gi as __gi__gi
import gobject as __gobject


class EventType(__gi__gi.GEnum):
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


    2BUTTON_PRESS = 5
    3BUTTON_PRESS = 6
    BUTTON_PRESS = 4
    BUTTON_RELEASE = 7
    CLIENT_EVENT = 28
    CONFIGURE = 13
    DAMAGE = 36
    DELETE = 0
    DESTROY = 1
    DRAG_ENTER = 22
    DRAG_LEAVE = 23
    DRAG_MOTION = 24
    DRAG_STATUS = 25
    DROP_FINISHED = 27
    DROP_START = 26
    ENTER_NOTIFY = 10
    EVENT_LAST = 48
    EXPOSE = 2
    FOCUS_CHANGE = 12
    GRAB_BROKEN = 35
    KEY_PRESS = 8
    KEY_RELEASE = 9
    LEAVE_NOTIFY = 11
    MAP = 14
    MOTION_NOTIFY = 3
    NOTHING = -1
    OWNER_CHANGE = 34
    PAD_BUTTON_PRESS = 43
    PAD_BUTTON_RELEASE = 44
    PAD_GROUP_MODE = 47
    PAD_RING = 45
    PAD_STRIP = 46
    PROPERTY_NOTIFY = 16
    PROXIMITY_IN = 20
    PROXIMITY_OUT = 21
    SCROLL = 31
    SELECTION_CLEAR = 17
    SELECTION_NOTIFY = 19
    SELECTION_REQUEST = 18
    SETTING = 33
    TOUCHPAD_PINCH = 42
    TOUCHPAD_SWIPE = 41
    TOUCH_BEGIN = 37
    TOUCH_CANCEL = 40
    TOUCH_END = 39
    TOUCH_UPDATE = 38
    UNMAP = 15
    VISIBILITY_NOTIFY = 29
    WINDOW_STATE = 32
    __class__ = None # (!) real value is "<class 'gi._enum.GEnumMeta'>"
    __members__ = None # (!) real value is "mappingproxy({'NOTHING': <EventType.NOTHING: -1>, 'DELETE': <EventType.DELETE: 0>, 'DESTROY': <EventType.DESTROY: 1>, 'EXPOSE': <EventType.EXPOSE: 2>, 'MOTION_NOTIFY': <EventType.MOTION_NOTIFY: 3>, 'BUTTON_PRESS': <EventType.BUTTON_PRESS: 4>, '2BUTTON_PRESS': <EventType.2BUTTON_PRESS: 5>, 'DOUBLE_BUTTON_PRESS': <EventType.2BUTTON_PRESS: 5>, '3BUTTON_PRESS': <EventType.3BUTTON_PRESS: 6>, 'TRIPLE_BUTTON_PRESS': <EventType.3BUTTON_PRESS: 6>, 'BUTTON_RELEASE': <EventType.BUTTON_RELEASE: 7>, 'KEY_PRESS': <EventType.KEY_PRESS: 8>, 'KEY_RELEASE': <EventType.KEY_RELEASE: 9>, 'ENTER_NOTIFY': <EventType.ENTER_NOTIFY: 10>, 'LEAVE_NOTIFY': <EventType.LEAVE_NOTIFY: 11>, 'FOCUS_CHANGE': <EventType.FOCUS_CHANGE: 12>, 'CONFIGURE': <EventType.CONFIGURE: 13>, 'MAP': <EventType.MAP: 14>, 'UNMAP': <EventType.UNMAP: 15>, 'PROPERTY_NOTIFY': <EventType.PROPERTY_NOTIFY: 16>, 'SELECTION_CLEAR': <EventType.SELECTION_CLEAR: 17>, 'SELECTION_REQUEST': <EventType.SELECTION_REQUEST: 18>, 'SELECTION_NOTIFY': <EventType.SELECTION_NOTIFY: 19>, 'PROXIMITY_IN': <EventType.PROXIMITY_IN: 20>, 'PROXIMITY_OUT': <EventType.PROXIMITY_OUT: 21>, 'DRAG_ENTER': <EventType.DRAG_ENTER: 22>, 'DRAG_LEAVE': <EventType.DRAG_LEAVE: 23>, 'DRAG_MOTION': <EventType.DRAG_MOTION: 24>, 'DRAG_STATUS': <EventType.DRAG_STATUS: 25>, 'DROP_START': <EventType.DROP_START: 26>, 'DROP_FINISHED': <EventType.DROP_FINISHED: 27>, 'CLIENT_EVENT': <EventType.CLIENT_EVENT: 28>, 'VISIBILITY_NOTIFY': <EventType.VISIBILITY_NOTIFY: 29>, 'SCROLL': <EventType.SCROLL: 31>, 'WINDOW_STATE': <EventType.WINDOW_STATE: 32>, 'SETTING': <EventType.SETTING: 33>, 'OWNER_CHANGE': <EventType.OWNER_CHANGE: 34>, 'GRAB_BROKEN': <EventType.GRAB_BROKEN: 35>, 'DAMAGE': <EventType.DAMAGE: 36>, 'TOUCH_BEGIN': <EventType.TOUCH_BEGIN: 37>, 'TOUCH_UPDATE': <EventType.TOUCH_UPDATE: 38>, 'TOUCH_END': <EventType.TOUCH_END: 39>, 'TOUCH_CANCEL': <EventType.TOUCH_CANCEL: 40>, 'TOUCHPAD_SWIPE': <EventType.TOUCHPAD_SWIPE: 41>, 'TOUCHPAD_PINCH': <EventType.TOUCHPAD_PINCH: 42>, 'PAD_BUTTON_PRESS': <EventType.PAD_BUTTON_PRESS: 43>, 'PAD_BUTTON_RELEASE': <EventType.PAD_BUTTON_RELEASE: 44>, 'PAD_RING': <EventType.PAD_RING: 45>, 'PAD_STRIP': <EventType.PAD_STRIP: 46>, 'PAD_GROUP_MODE': <EventType.PAD_GROUP_MODE: 47>, 'EVENT_LAST': <EventType.EVENT_LAST: 48>})"
    __name__ = 'EventType'
    __qualname__ = 'EventType'


