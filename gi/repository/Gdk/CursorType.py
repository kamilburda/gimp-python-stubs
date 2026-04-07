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


class CursorType(__gi__gi.GEnum):
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


    ARROW = 2
    BASED_ARROW_DOWN = 4
    BASED_ARROW_UP = 6
    BLANK_CURSOR = -2
    BOAT = 8
    BOGOSITY = 10
    BOTTOM_LEFT_CORNER = 12
    BOTTOM_RIGHT_CORNER = 14
    BOTTOM_SIDE = 16
    BOTTOM_TEE = 18
    BOX_SPIRAL = 20
    CENTER_PTR = 22
    CIRCLE = 24
    CLOCK = 26
    COFFEE_MUG = 28
    CROSS = 30
    CROSSHAIR = 34
    CROSS_REVERSE = 32
    CURSOR_IS_PIXMAP = -1
    DIAMOND_CROSS = 36
    DOT = 38
    DOTBOX = 40
    DOUBLE_ARROW = 42
    DRAFT_LARGE = 44
    DRAFT_SMALL = 46
    DRAPED_BOX = 48
    EXCHANGE = 50
    FLEUR = 52
    GOBBLER = 54
    GUMBY = 56
    HAND1 = 58
    HAND2 = 60
    HEART = 62
    ICON = 64
    IRON_CROSS = 66
    LAST_CURSOR = 153
    LEFTBUTTON = 74
    LEFT_PTR = 68
    LEFT_SIDE = 70
    LEFT_TEE = 72
    LL_ANGLE = 76
    LR_ANGLE = 78
    MAN = 80
    MIDDLEBUTTON = 82
    MOUSE = 84
    PENCIL = 86
    PIRATE = 88
    PLUS = 90
    QUESTION_ARROW = 92
    RIGHTBUTTON = 100
    RIGHT_PTR = 94
    RIGHT_SIDE = 96
    RIGHT_TEE = 98
    RTL_LOGO = 102
    SAILBOAT = 104
    SB_DOWN_ARROW = 106
    SB_H_DOUBLE_ARROW = 108
    SB_LEFT_ARROW = 110
    SB_RIGHT_ARROW = 112
    SB_UP_ARROW = 114
    SB_V_DOUBLE_ARROW = 116
    SHUTTLE = 118
    SIZING = 120
    SPIDER = 122
    SPRAYCAN = 124
    STAR = 126
    TARGET = 128
    TCROSS = 130
    TOP_LEFT_ARROW = 132
    TOP_LEFT_CORNER = 134
    TOP_RIGHT_CORNER = 136
    TOP_SIDE = 138
    TOP_TEE = 140
    TREK = 142
    UL_ANGLE = 144
    UMBRELLA = 146
    UR_ANGLE = 148
    WATCH = 150
    XTERM = 152
    X_CURSOR = 0
    __class__ = None # (!) real value is "<class 'gi._enum.GEnumMeta'>"
    __members__ = None # (!) real value is "mappingproxy({'X_CURSOR': <CursorType.X_CURSOR: 0>, 'ARROW': <CursorType.ARROW: 2>, 'BASED_ARROW_DOWN': <CursorType.BASED_ARROW_DOWN: 4>, 'BASED_ARROW_UP': <CursorType.BASED_ARROW_UP: 6>, 'BOAT': <CursorType.BOAT: 8>, 'BOGOSITY': <CursorType.BOGOSITY: 10>, 'BOTTOM_LEFT_CORNER': <CursorType.BOTTOM_LEFT_CORNER: 12>, 'BOTTOM_RIGHT_CORNER': <CursorType.BOTTOM_RIGHT_CORNER: 14>, 'BOTTOM_SIDE': <CursorType.BOTTOM_SIDE: 16>, 'BOTTOM_TEE': <CursorType.BOTTOM_TEE: 18>, 'BOX_SPIRAL': <CursorType.BOX_SPIRAL: 20>, 'CENTER_PTR': <CursorType.CENTER_PTR: 22>, 'CIRCLE': <CursorType.CIRCLE: 24>, 'CLOCK': <CursorType.CLOCK: 26>, 'COFFEE_MUG': <CursorType.COFFEE_MUG: 28>, 'CROSS': <CursorType.CROSS: 30>, 'CROSS_REVERSE': <CursorType.CROSS_REVERSE: 32>, 'CROSSHAIR': <CursorType.CROSSHAIR: 34>, 'DIAMOND_CROSS': <CursorType.DIAMOND_CROSS: 36>, 'DOT': <CursorType.DOT: 38>, 'DOTBOX': <CursorType.DOTBOX: 40>, 'DOUBLE_ARROW': <CursorType.DOUBLE_ARROW: 42>, 'DRAFT_LARGE': <CursorType.DRAFT_LARGE: 44>, 'DRAFT_SMALL': <CursorType.DRAFT_SMALL: 46>, 'DRAPED_BOX': <CursorType.DRAPED_BOX: 48>, 'EXCHANGE': <CursorType.EXCHANGE: 50>, 'FLEUR': <CursorType.FLEUR: 52>, 'GOBBLER': <CursorType.GOBBLER: 54>, 'GUMBY': <CursorType.GUMBY: 56>, 'HAND1': <CursorType.HAND1: 58>, 'HAND2': <CursorType.HAND2: 60>, 'HEART': <CursorType.HEART: 62>, 'ICON': <CursorType.ICON: 64>, 'IRON_CROSS': <CursorType.IRON_CROSS: 66>, 'LEFT_PTR': <CursorType.LEFT_PTR: 68>, 'LEFT_SIDE': <CursorType.LEFT_SIDE: 70>, 'LEFT_TEE': <CursorType.LEFT_TEE: 72>, 'LEFTBUTTON': <CursorType.LEFTBUTTON: 74>, 'LL_ANGLE': <CursorType.LL_ANGLE: 76>, 'LR_ANGLE': <CursorType.LR_ANGLE: 78>, 'MAN': <CursorType.MAN: 80>, 'MIDDLEBUTTON': <CursorType.MIDDLEBUTTON: 82>, 'MOUSE': <CursorType.MOUSE: 84>, 'PENCIL': <CursorType.PENCIL: 86>, 'PIRATE': <CursorType.PIRATE: 88>, 'PLUS': <CursorType.PLUS: 90>, 'QUESTION_ARROW': <CursorType.QUESTION_ARROW: 92>, 'RIGHT_PTR': <CursorType.RIGHT_PTR: 94>, 'RIGHT_SIDE': <CursorType.RIGHT_SIDE: 96>, 'RIGHT_TEE': <CursorType.RIGHT_TEE: 98>, 'RIGHTBUTTON': <CursorType.RIGHTBUTTON: 100>, 'RTL_LOGO': <CursorType.RTL_LOGO: 102>, 'SAILBOAT': <CursorType.SAILBOAT: 104>, 'SB_DOWN_ARROW': <CursorType.SB_DOWN_ARROW: 106>, 'SB_H_DOUBLE_ARROW': <CursorType.SB_H_DOUBLE_ARROW: 108>, 'SB_LEFT_ARROW': <CursorType.SB_LEFT_ARROW: 110>, 'SB_RIGHT_ARROW': <CursorType.SB_RIGHT_ARROW: 112>, 'SB_UP_ARROW': <CursorType.SB_UP_ARROW: 114>, 'SB_V_DOUBLE_ARROW': <CursorType.SB_V_DOUBLE_ARROW: 116>, 'SHUTTLE': <CursorType.SHUTTLE: 118>, 'SIZING': <CursorType.SIZING: 120>, 'SPIDER': <CursorType.SPIDER: 122>, 'SPRAYCAN': <CursorType.SPRAYCAN: 124>, 'STAR': <CursorType.STAR: 126>, 'TARGET': <CursorType.TARGET: 128>, 'TCROSS': <CursorType.TCROSS: 130>, 'TOP_LEFT_ARROW': <CursorType.TOP_LEFT_ARROW: 132>, 'TOP_LEFT_CORNER': <CursorType.TOP_LEFT_CORNER: 134>, 'TOP_RIGHT_CORNER': <CursorType.TOP_RIGHT_CORNER: 136>, 'TOP_SIDE': <CursorType.TOP_SIDE: 138>, 'TOP_TEE': <CursorType.TOP_TEE: 140>, 'TREK': <CursorType.TREK: 142>, 'UL_ANGLE': <CursorType.UL_ANGLE: 144>, 'UMBRELLA': <CursorType.UMBRELLA: 146>, 'UR_ANGLE': <CursorType.UR_ANGLE: 148>, 'WATCH': <CursorType.WATCH: 150>, 'XTERM': <CursorType.XTERM: 152>, 'LAST_CURSOR': <CursorType.LAST_CURSOR: 153>, 'BLANK_CURSOR': <CursorType.BLANK_CURSOR: -2>, 'CURSOR_IS_PIXMAP': <CursorType.CURSOR_IS_PIXMAP: -1>})"
    __name__ = 'CursorType'
    __qualname__ = 'CursorType'


