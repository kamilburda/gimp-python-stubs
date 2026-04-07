# encoding: utf-8
# module gi.repository.HarfBuzz
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi


class aat_layout_feature_selector_t(__enum.IntFlag):
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


    B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF = 1
    B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON = 2
    B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON = 4
    B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON = 8
    B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SIXTEEN_ON = 32
    B_AAT_LAYOUT_FEATURE_SELECTOR_SYMBOL_LIGATURES_ON = 16
    __class__ = None # (!) real value is "<class 'enum.EnumType'>"
    __members__ = None # (!) real value is "mappingproxy({'B_AAT_LAYOUT_FEATURE_SELECTOR_INVALID': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_INVALID: 65535>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_REQUIRED_LIGATURES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_REQUIRED_LIGATURES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF: 5>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON: 6>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF: 7>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON: 8>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF: 9>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_ON: 10>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_OFF: 11>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SQUARED_LIGATURES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_SQUARED_LIGATURES_ON: 12>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SQUARED_LIGATURES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_SQUARED_LIGATURES_OFF: 13>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ABBREV_SQUARED_LIGATURES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ABBREV_SQUARED_LIGATURES_ON: 14>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ABBREV_SQUARED_LIGATURES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ABBREV_SQUARED_LIGATURES_OFF: 15>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SYMBOL_LIGATURES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_SYMBOL_LIGATURES_ON: 16>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SYMBOL_LIGATURES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_SYMBOL_LIGATURES_OFF: 17>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CONTEXTUAL_LIGATURES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_CONTEXTUAL_LIGATURES_ON: 18>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CONTEXTUAL_LIGATURES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_CONTEXTUAL_LIGATURES_OFF: 19>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HISTORICAL_LIGATURES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_HISTORICAL_LIGATURES_ON: 20>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HISTORICAL_LIGATURES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_HISTORICAL_LIGATURES_OFF: 21>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_UNCONNECTED': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_PARTIALLY_CONNECTED': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CURSIVE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_UPPER_AND_LOWER_CASE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_CAPS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_LOWER_CASE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SMALL_CAPS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_INITIAL_CAPS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_INITIAL_CAPS_AND_SMALL_CAPS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF: 5>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SUBSTITUTE_VERTICAL_FORMS_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SUBSTITUTE_VERTICAL_FORMS_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_LINGUISTIC_REARRANGEMENT_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_LINGUISTIC_REARRANGEMENT_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_MONOSPACED_NUMBERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_PROPORTIONAL_NUMBERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_THIRD_WIDTH_NUMBERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_QUARTER_WIDTH_NUMBERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_WORD_INITIAL_SWASHES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_WORD_INITIAL_SWASHES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_WORD_FINAL_SWASHES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_WORD_FINAL_SWASHES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_LINE_INITIAL_SWASHES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_LINE_INITIAL_SWASHES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF: 5>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_LINE_FINAL_SWASHES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON: 6>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_LINE_FINAL_SWASHES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF: 7>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_NON_FINAL_SWASHES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON: 8>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_NON_FINAL_SWASHES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF: 9>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SHOW_DIACRITICS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HIDE_DIACRITICS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_DECOMPOSE_DIACRITICS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_NORMAL_POSITION': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SUPERIORS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_INFERIORS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ORDINALS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SCIENTIFIC_INFERIORS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_NO_FRACTIONS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_VERTICAL_FRACTIONS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_DIAGONAL_FRACTIONS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_PREVENT_OVERLAP_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_PREVENT_OVERLAP_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HYPHENS_TO_EM_DASH_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HYPHENS_TO_EM_DASH_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HYPHEN_TO_EN_DASH_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HYPHEN_TO_EN_DASH_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SLASHED_ZERO_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SLASHED_ZERO_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF: 5>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_FORM_INTERROBANG_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON: 6>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_FORM_INTERROBANG_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF: 7>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SMART_QUOTES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON: 8>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SMART_QUOTES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF: 9>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_PERIODS_TO_ELLIPSIS_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_ON: 10>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_PERIODS_TO_ELLIPSIS_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_OFF: 11>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HYPHEN_TO_MINUS_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HYPHEN_TO_MINUS_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ASTERISK_TO_MULTIPLY_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ASTERISK_TO_MULTIPLY_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SLASH_TO_DIVIDE_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SLASH_TO_DIVIDE_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF: 5>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_INEQUALITY_LIGATURES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON: 6>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_INEQUALITY_LIGATURES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF: 7>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_EXPONENTS_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON: 8>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_EXPONENTS_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF: 9>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_MATHEMATICAL_GREEK_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_ON: 10>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_MATHEMATICAL_GREEK_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_OFF: 11>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_NO_ORNAMENTS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_DINGBATS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_PI_CHARACTERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_FLEURONS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_DECORATIVE_BORDERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_INTERNATIONAL_SYMBOLS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF: 5>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_MATH_SYMBOLS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON: 6>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_NO_ALTERNATES': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_DESIGN_LEVEL1': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_DESIGN_LEVEL2': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_DESIGN_LEVEL3': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_DESIGN_LEVEL4': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_DESIGN_LEVEL5': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_NO_STYLE_OPTIONS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_DISPLAY_TEXT': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ENGRAVED_TEXT': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ILLUMINATED_CAPS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_TITLING_CAPS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_TALL_CAPS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF: 5>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_TRADITIONAL_CHARACTERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SIMPLIFIED_CHARACTERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_JIS1978_CHARACTERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_JIS1983_CHARACTERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_JIS1990_CHARACTERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_TRADITIONAL_ALT_ONE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF: 5>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_TRADITIONAL_ALT_TWO': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON: 6>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_TRADITIONAL_ALT_THREE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF: 7>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_TRADITIONAL_ALT_FOUR': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON: 8>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_TRADITIONAL_ALT_FIVE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF: 9>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_EXPERT_CHARACTERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_ON: 10>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_JIS2004_CHARACTERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_OFF: 11>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HOJO_CHARACTERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_SQUARED_LIGATURES_ON: 12>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_NLCCHARACTERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_SQUARED_LIGATURES_OFF: 13>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_TRADITIONAL_NAMES_CHARACTERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ABBREV_SQUARED_LIGATURES_ON: 14>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_LOWER_CASE_NUMBERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_UPPER_CASE_NUMBERS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_PROPORTIONAL_TEXT': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_MONOSPACED_TEXT': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HALF_WIDTH_TEXT': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_THIRD_WIDTH_TEXT': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_QUARTER_WIDTH_TEXT': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ALT_PROPORTIONAL_TEXT': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF: 5>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ALT_HALF_WIDTH_TEXT': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON: 6>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_NO_TRANSLITERATION': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HANJA_TO_HANGUL': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HIRAGANA_TO_KATAKANA': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_KATAKANA_TO_HIRAGANA': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_KANA_TO_ROMANIZATION': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ROMANIZATION_TO_HIRAGANA': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF: 5>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ROMANIZATION_TO_KATAKANA': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON: 6>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HANJA_TO_HANGUL_ALT_ONE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF: 7>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HANJA_TO_HANGUL_ALT_TWO': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON: 8>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HANJA_TO_HANGUL_ALT_THREE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF: 9>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_NO_ANNOTATION': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_BOX_ANNOTATION': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ROUNDED_BOX_ANNOTATION': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CIRCLE_ANNOTATION': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_INVERTED_CIRCLE_ANNOTATION': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_PARENTHESIS_ANNOTATION': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF: 5>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_PERIOD_ANNOTATION': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON: 6>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ROMAN_NUMERAL_ANNOTATION': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF: 7>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_DIAMOND_ANNOTATION': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON: 8>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_INVERTED_BOX_ANNOTATION': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF: 9>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_INVERTED_ROUNDED_BOX_ANNOTATION': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_ON: 10>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_FULL_WIDTH_KANA': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_PROPORTIONAL_KANA': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_FULL_WIDTH_IDEOGRAPHS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_PROPORTIONAL_IDEOGRAPHS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HALF_WIDTH_IDEOGRAPHS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CANONICAL_COMPOSITION_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CANONICAL_COMPOSITION_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_COMPATIBILITY_COMPOSITION_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_COMPATIBILITY_COMPOSITION_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_TRANSCODING_COMPOSITION_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_TRANSCODING_COMPOSITION_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF: 5>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_NO_RUBY_KANA': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_RUBY_KANA': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_RUBY_KANA_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_RUBY_KANA_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_NO_CJK_SYMBOL_ALTERNATIVES': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CJK_SYMBOL_ALT_ONE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CJK_SYMBOL_ALT_TWO': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CJK_SYMBOL_ALT_THREE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CJK_SYMBOL_ALT_FOUR': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CJK_SYMBOL_ALT_FIVE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF: 5>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_NO_IDEOGRAPHIC_ALTERNATIVES': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_IDEOGRAPHIC_ALT_ONE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_IDEOGRAPHIC_ALT_TWO': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_IDEOGRAPHIC_ALT_THREE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_IDEOGRAPHIC_ALT_FOUR': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_IDEOGRAPHIC_ALT_FIVE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF: 5>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CJK_VERTICAL_ROMAN_CENTERED': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CJK_VERTICAL_ROMAN_HBASELINE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_NO_CJK_ITALIC_ROMAN': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CJK_ITALIC_ROMAN': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CJK_ITALIC_ROMAN_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CJK_ITALIC_ROMAN_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CASE_SENSITIVE_LAYOUT_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CASE_SENSITIVE_LAYOUT_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CASE_SENSITIVE_SPACING_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CASE_SENSITIVE_SPACING_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ALTERNATE_HORIZ_KANA_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ALTERNATE_HORIZ_KANA_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ALTERNATE_VERT_KANA_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_ALTERNATE_VERT_KANA_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_NO_STYLISTIC_ALTERNATES': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_ONE_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_ONE_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWO_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWO_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF: 5>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_THREE_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_ON: 6>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_THREE_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_LOGOS_OFF: 7>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FOUR_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_ON: 8>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FOUR_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_REBUS_PICTURES_OFF: 9>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FIVE_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_ON: 10>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FIVE_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_DIPHTHONG_LIGATURES_OFF: 11>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SIX_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_SQUARED_LIGATURES_ON: 12>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SIX_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_SQUARED_LIGATURES_OFF: 13>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SEVEN_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ABBREV_SQUARED_LIGATURES_ON: 14>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SEVEN_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ABBREV_SQUARED_LIGATURES_OFF: 15>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_EIGHT_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_SYMBOL_LIGATURES_ON: 16>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_EIGHT_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_SYMBOL_LIGATURES_OFF: 17>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_NINE_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_CONTEXTUAL_LIGATURES_ON: 18>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_NINE_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_CONTEXTUAL_LIGATURES_OFF: 19>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TEN_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_HISTORICAL_LIGATURES_ON: 20>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TEN_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_HISTORICAL_LIGATURES_OFF: 21>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_ELEVEN_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_ELEVEN_ON: 22>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_ELEVEN_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_ELEVEN_OFF: 23>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWELVE_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWELVE_ON: 24>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWELVE_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWELVE_OFF: 25>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_THIRTEEN_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_THIRTEEN_ON: 26>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_THIRTEEN_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_THIRTEEN_OFF: 27>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FOURTEEN_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FOURTEEN_ON: 28>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FOURTEEN_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FOURTEEN_OFF: 29>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FIFTEEN_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FIFTEEN_ON: 30>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FIFTEEN_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_FIFTEEN_OFF: 31>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SIXTEEN_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SIXTEEN_ON: 32>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SIXTEEN_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SIXTEEN_OFF: 33>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SEVENTEEN_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SEVENTEEN_ON: 34>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SEVENTEEN_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_SEVENTEEN_OFF: 35>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_EIGHTEEN_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_EIGHTEEN_ON: 36>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_EIGHTEEN_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_EIGHTEEN_OFF: 37>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_NINETEEN_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_NINETEEN_ON: 38>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_NINETEEN_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_NINETEEN_OFF: 39>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWENTY_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWENTY_ON: 40>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWENTY_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_STYLISTIC_ALT_TWENTY_OFF: 41>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CONTEXTUAL_ALTERNATES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CONTEXTUAL_ALTERNATES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SWASH_ALTERNATES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_SWASH_ALTERNATES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CONTEXTUAL_SWASH_ALTERNATES_ON': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_ON: 4>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_CONTEXTUAL_SWASH_ALTERNATES_OFF': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_RARE_LIGATURES_OFF: 5>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_DEFAULT_LOWER_CASE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_LOWER_CASE_SMALL_CAPS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_LOWER_CASE_PETITE_CAPS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_DEFAULT_UPPER_CASE': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_UPPER_CASE_SMALL_CAPS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_UPPER_CASE_PETITE_CAPS': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_HALF_WIDTH_CJK_ROMAN': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_ON: 0>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_PROPORTIONAL_CJK_ROMAN': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_ALL_TYPE_FEATURES_OFF: 1>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_DEFAULT_CJK_ROMAN': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_ON: 2>, 'B_AAT_LAYOUT_FEATURE_SELECTOR_FULL_WIDTH_CJK_ROMAN': <aat_layout_feature_selector_t.B_AAT_LAYOUT_FEATURE_SELECTOR_COMMON_LIGATURES_OFF: 3>})"
    __name__ = 'aat_layout_feature_selector_t'
    __qualname__ = 'aat_layout_feature_selector_t'


