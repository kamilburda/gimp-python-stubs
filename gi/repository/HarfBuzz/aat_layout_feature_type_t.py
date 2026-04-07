# encoding: utf-8
# module gi.repository.HarfBuzz
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi


class aat_layout_feature_type_t(__enum.IntFlag):
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


    B_AAT_LAYOUT_FEATURE_TYPE_CURSIVE_CONNECTION = 2
    B_AAT_LAYOUT_FEATURE_TYPE_ITALIC_CJK_ROMAN = 32
    B_AAT_LAYOUT_FEATURE_TYPE_LIGATURES = 1
    B_AAT_LAYOUT_FEATURE_TYPE_ORNAMENT_SETS_TYPE = 16
    B_AAT_LAYOUT_FEATURE_TYPE_SMART_SWASH_TYPE = 8
    B_AAT_LAYOUT_FEATURE_TYPE_VERTICAL_SUBSTITUTION = 4
    __class__ = None # (!) real value is "<class 'enum.EnumType'>"
    __members__ = None # (!) real value is "mappingproxy({'B_AAT_LAYOUT_FEATURE_TYPE_INVALID': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_INVALID: 65535>, 'B_AAT_LAYOUT_FEATURE_TYPE_ALL_TYPOGRAPHIC': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_ALL_TYPOGRAPHIC: 0>, 'B_AAT_LAYOUT_FEATURE_TYPE_LIGATURES': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_LIGATURES: 1>, 'B_AAT_LAYOUT_FEATURE_TYPE_CURSIVE_CONNECTION': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_CURSIVE_CONNECTION: 2>, 'B_AAT_LAYOUT_FEATURE_TYPE_LETTER_CASE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_LETTER_CASE: 3>, 'B_AAT_LAYOUT_FEATURE_TYPE_VERTICAL_SUBSTITUTION': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_VERTICAL_SUBSTITUTION: 4>, 'B_AAT_LAYOUT_FEATURE_TYPE_LINGUISTIC_REARRANGEMENT': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_LINGUISTIC_REARRANGEMENT: 5>, 'B_AAT_LAYOUT_FEATURE_TYPE_NUMBER_SPACING': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_NUMBER_SPACING: 6>, 'B_AAT_LAYOUT_FEATURE_TYPE_SMART_SWASH_TYPE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_SMART_SWASH_TYPE: 8>, 'B_AAT_LAYOUT_FEATURE_TYPE_DIACRITICS_TYPE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_DIACRITICS_TYPE: 9>, 'B_AAT_LAYOUT_FEATURE_TYPE_VERTICAL_POSITION': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_VERTICAL_POSITION: 10>, 'B_AAT_LAYOUT_FEATURE_TYPE_FRACTIONS': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_FRACTIONS: 11>, 'B_AAT_LAYOUT_FEATURE_TYPE_OVERLAPPING_CHARACTERS_TYPE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_OVERLAPPING_CHARACTERS_TYPE: 13>, 'B_AAT_LAYOUT_FEATURE_TYPE_TYPOGRAPHIC_EXTRAS': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_TYPOGRAPHIC_EXTRAS: 14>, 'B_AAT_LAYOUT_FEATURE_TYPE_MATHEMATICAL_EXTRAS': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_MATHEMATICAL_EXTRAS: 15>, 'B_AAT_LAYOUT_FEATURE_TYPE_ORNAMENT_SETS_TYPE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_ORNAMENT_SETS_TYPE: 16>, 'B_AAT_LAYOUT_FEATURE_TYPE_CHARACTER_ALTERNATIVES': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_CHARACTER_ALTERNATIVES: 17>, 'B_AAT_LAYOUT_FEATURE_TYPE_DESIGN_COMPLEXITY_TYPE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_DESIGN_COMPLEXITY_TYPE: 18>, 'B_AAT_LAYOUT_FEATURE_TYPE_STYLE_OPTIONS': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_STYLE_OPTIONS: 19>, 'B_AAT_LAYOUT_FEATURE_TYPE_CHARACTER_SHAPE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_CHARACTER_SHAPE: 20>, 'B_AAT_LAYOUT_FEATURE_TYPE_NUMBER_CASE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_NUMBER_CASE: 21>, 'B_AAT_LAYOUT_FEATURE_TYPE_TEXT_SPACING': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_TEXT_SPACING: 22>, 'B_AAT_LAYOUT_FEATURE_TYPE_TRANSLITERATION': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_TRANSLITERATION: 23>, 'B_AAT_LAYOUT_FEATURE_TYPE_ANNOTATION_TYPE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_ANNOTATION_TYPE: 24>, 'B_AAT_LAYOUT_FEATURE_TYPE_KANA_SPACING_TYPE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_KANA_SPACING_TYPE: 25>, 'B_AAT_LAYOUT_FEATURE_TYPE_IDEOGRAPHIC_SPACING_TYPE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_IDEOGRAPHIC_SPACING_TYPE: 26>, 'B_AAT_LAYOUT_FEATURE_TYPE_UNICODE_DECOMPOSITION_TYPE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_UNICODE_DECOMPOSITION_TYPE: 27>, 'B_AAT_LAYOUT_FEATURE_TYPE_RUBY_KANA': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_RUBY_KANA: 28>, 'B_AAT_LAYOUT_FEATURE_TYPE_CJK_SYMBOL_ALTERNATIVES_TYPE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_CJK_SYMBOL_ALTERNATIVES_TYPE: 29>, 'B_AAT_LAYOUT_FEATURE_TYPE_IDEOGRAPHIC_ALTERNATIVES_TYPE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_IDEOGRAPHIC_ALTERNATIVES_TYPE: 30>, 'B_AAT_LAYOUT_FEATURE_TYPE_CJK_VERTICAL_ROMAN_PLACEMENT_TYPE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_CJK_VERTICAL_ROMAN_PLACEMENT_TYPE: 31>, 'B_AAT_LAYOUT_FEATURE_TYPE_ITALIC_CJK_ROMAN': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_ITALIC_CJK_ROMAN: 32>, 'B_AAT_LAYOUT_FEATURE_TYPE_CASE_SENSITIVE_LAYOUT': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_CASE_SENSITIVE_LAYOUT: 33>, 'B_AAT_LAYOUT_FEATURE_TYPE_ALTERNATE_KANA': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_ALTERNATE_KANA: 34>, 'B_AAT_LAYOUT_FEATURE_TYPE_STYLISTIC_ALTERNATIVES': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_STYLISTIC_ALTERNATIVES: 35>, 'B_AAT_LAYOUT_FEATURE_TYPE_CONTEXTUAL_ALTERNATIVES': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_CONTEXTUAL_ALTERNATIVES: 36>, 'B_AAT_LAYOUT_FEATURE_TYPE_LOWER_CASE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_LOWER_CASE: 37>, 'B_AAT_LAYOUT_FEATURE_TYPE_UPPER_CASE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_UPPER_CASE: 38>, 'B_AAT_LAYOUT_FEATURE_TYPE_LANGUAGE_TAG_TYPE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_LANGUAGE_TAG_TYPE: 39>, 'B_AAT_LAYOUT_FEATURE_TYPE_CJK_ROMAN_SPACING_TYPE': <aat_layout_feature_type_t.B_AAT_LAYOUT_FEATURE_TYPE_CJK_ROMAN_SPACING_TYPE: 103>})"
    __name__ = 'aat_layout_feature_type_t'
    __qualname__ = 'aat_layout_feature_type_t'


