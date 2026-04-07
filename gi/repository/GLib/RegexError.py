# encoding: utf-8
# module gi.repository.GLib
# by generator 1.147
# no doc

# imports
from gi._gi import Pid, spawn_async

from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GLib as __gi_overrides_GLib
import gi._gi as __gi__gi


class RegexError(__enum.IntEnum):
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


    ASSERTION_EXPECTED = 128
    BACKTRACKING_CONTROL_VERB_ARGUMENT_FORBIDDEN = 159
    BACKTRACKING_CONTROL_VERB_ARGUMENT_REQUIRED = 166
    CHARACTER_VALUE_TOO_LARGE = 176
    COMPILE = 0
    DEFINE_REPETION = 155
    DUPLICATE_SUBPATTERN_NAME = 143
    EXPRESSION_TOO_LARGE = 120
    EXTRA_SUBPATTERN_NAME = 165
    HEX_CODE_TOO_LARGE = 134
    INCONSISTENT_NEWLINE_OPTIONS = 156
    INEXISTENT_SUBPATTERN_REFERENCE = 115
    INFINITE_LOOP = 140
    INTERNAL = 4
    INVALID_CONDITION = 135
    INVALID_CONTROL_CHAR = 168
    INVALID_DATA_CHARACTER = 164
    INVALID_ESCAPE_IN_CHARACTER_CLASS = 107
    INVALID_OCTAL_VALUE = 151
    INVALID_RELATIVE_REFERENCE = 158
    MALFORMED_CONDITION = 126
    MALFORMED_PROPERTY = 146
    MATCH = 3
    MEMORY_ERROR = 121
    MISSING_BACK_REFERENCE = 157
    MISSING_CONTROL_CHAR = 102
    MISSING_DIGIT = 163
    MISSING_NAME = 169
    MISSING_SUBPATTERN_NAME = 162
    MISSING_SUBPATTERN_NAME_TERMINATOR = 142
    NAME_TOO_LONG = 175
    NOTHING_TO_REPEAT = 109
    NOT_SUPPORTED_IN_CLASS = 171
    NUMBER_TOO_BIG = 161
    OPTIMIZE = 1
    POSIX_COLLATING_ELEMENTS_NOT_SUPPORTED = 131
    POSIX_NAMED_CLASS_OUTSIDE_CLASS = 113
    QUANTIFIERS_OUT_OF_ORDER = 104
    QUANTIFIER_TOO_BIG = 105
    RANGE_OUT_OF_ORDER = 108
    REPLACE = 2
    SINGLE_BYTE_MATCH_IN_LOOKBEHIND = 136
    STRAY_BACKSLASH = 101
    SUBPATTERN_NAME_TOO_LONG = 148
    TOO_MANY_BRANCHES_IN_DEFINE = 154
    TOO_MANY_CONDITIONAL_BRANCHES = 127
    TOO_MANY_FORWARD_REFERENCES = 172
    TOO_MANY_SUBPATTERNS = 149
    UNKNOWN_BACKTRACKING_CONTROL_VERB = 160
    UNKNOWN_POSIX_CLASS_NAME = 130
    UNKNOWN_PROPERTY = 147
    UNMATCHED_PARENTHESIS = 114
    UNRECOGNIZED_CHARACTER = 112
    UNRECOGNIZED_ESCAPE = 103
    UNTERMINATED_CHARACTER_CLASS = 106
    UNTERMINATED_COMMENT = 118
    VARIABLE_LENGTH_LOOKBEHIND = 125
    __class__ = None # (!) real value is "<class 'enum.EnumType'>"
    __members__ = None # (!) real value is "mappingproxy({'COMPILE': <RegexError.COMPILE: 0>, 'OPTIMIZE': <RegexError.OPTIMIZE: 1>, 'REPLACE': <RegexError.REPLACE: 2>, 'MATCH': <RegexError.MATCH: 3>, 'INTERNAL': <RegexError.INTERNAL: 4>, 'STRAY_BACKSLASH': <RegexError.STRAY_BACKSLASH: 101>, 'MISSING_CONTROL_CHAR': <RegexError.MISSING_CONTROL_CHAR: 102>, 'UNRECOGNIZED_ESCAPE': <RegexError.UNRECOGNIZED_ESCAPE: 103>, 'QUANTIFIERS_OUT_OF_ORDER': <RegexError.QUANTIFIERS_OUT_OF_ORDER: 104>, 'QUANTIFIER_TOO_BIG': <RegexError.QUANTIFIER_TOO_BIG: 105>, 'UNTERMINATED_CHARACTER_CLASS': <RegexError.UNTERMINATED_CHARACTER_CLASS: 106>, 'INVALID_ESCAPE_IN_CHARACTER_CLASS': <RegexError.INVALID_ESCAPE_IN_CHARACTER_CLASS: 107>, 'RANGE_OUT_OF_ORDER': <RegexError.RANGE_OUT_OF_ORDER: 108>, 'NOTHING_TO_REPEAT': <RegexError.NOTHING_TO_REPEAT: 109>, 'UNRECOGNIZED_CHARACTER': <RegexError.UNRECOGNIZED_CHARACTER: 112>, 'POSIX_NAMED_CLASS_OUTSIDE_CLASS': <RegexError.POSIX_NAMED_CLASS_OUTSIDE_CLASS: 113>, 'UNMATCHED_PARENTHESIS': <RegexError.UNMATCHED_PARENTHESIS: 114>, 'INEXISTENT_SUBPATTERN_REFERENCE': <RegexError.INEXISTENT_SUBPATTERN_REFERENCE: 115>, 'UNTERMINATED_COMMENT': <RegexError.UNTERMINATED_COMMENT: 118>, 'EXPRESSION_TOO_LARGE': <RegexError.EXPRESSION_TOO_LARGE: 120>, 'MEMORY_ERROR': <RegexError.MEMORY_ERROR: 121>, 'VARIABLE_LENGTH_LOOKBEHIND': <RegexError.VARIABLE_LENGTH_LOOKBEHIND: 125>, 'MALFORMED_CONDITION': <RegexError.MALFORMED_CONDITION: 126>, 'TOO_MANY_CONDITIONAL_BRANCHES': <RegexError.TOO_MANY_CONDITIONAL_BRANCHES: 127>, 'ASSERTION_EXPECTED': <RegexError.ASSERTION_EXPECTED: 128>, 'UNKNOWN_POSIX_CLASS_NAME': <RegexError.UNKNOWN_POSIX_CLASS_NAME: 130>, 'POSIX_COLLATING_ELEMENTS_NOT_SUPPORTED': <RegexError.POSIX_COLLATING_ELEMENTS_NOT_SUPPORTED: 131>, 'HEX_CODE_TOO_LARGE': <RegexError.HEX_CODE_TOO_LARGE: 134>, 'INVALID_CONDITION': <RegexError.INVALID_CONDITION: 135>, 'SINGLE_BYTE_MATCH_IN_LOOKBEHIND': <RegexError.SINGLE_BYTE_MATCH_IN_LOOKBEHIND: 136>, 'INFINITE_LOOP': <RegexError.INFINITE_LOOP: 140>, 'MISSING_SUBPATTERN_NAME_TERMINATOR': <RegexError.MISSING_SUBPATTERN_NAME_TERMINATOR: 142>, 'DUPLICATE_SUBPATTERN_NAME': <RegexError.DUPLICATE_SUBPATTERN_NAME: 143>, 'MALFORMED_PROPERTY': <RegexError.MALFORMED_PROPERTY: 146>, 'UNKNOWN_PROPERTY': <RegexError.UNKNOWN_PROPERTY: 147>, 'SUBPATTERN_NAME_TOO_LONG': <RegexError.SUBPATTERN_NAME_TOO_LONG: 148>, 'TOO_MANY_SUBPATTERNS': <RegexError.TOO_MANY_SUBPATTERNS: 149>, 'INVALID_OCTAL_VALUE': <RegexError.INVALID_OCTAL_VALUE: 151>, 'TOO_MANY_BRANCHES_IN_DEFINE': <RegexError.TOO_MANY_BRANCHES_IN_DEFINE: 154>, 'DEFINE_REPETION': <RegexError.DEFINE_REPETION: 155>, 'INCONSISTENT_NEWLINE_OPTIONS': <RegexError.INCONSISTENT_NEWLINE_OPTIONS: 156>, 'MISSING_BACK_REFERENCE': <RegexError.MISSING_BACK_REFERENCE: 157>, 'INVALID_RELATIVE_REFERENCE': <RegexError.INVALID_RELATIVE_REFERENCE: 158>, 'BACKTRACKING_CONTROL_VERB_ARGUMENT_FORBIDDEN': <RegexError.BACKTRACKING_CONTROL_VERB_ARGUMENT_FORBIDDEN: 159>, 'UNKNOWN_BACKTRACKING_CONTROL_VERB': <RegexError.UNKNOWN_BACKTRACKING_CONTROL_VERB: 160>, 'NUMBER_TOO_BIG': <RegexError.NUMBER_TOO_BIG: 161>, 'MISSING_SUBPATTERN_NAME': <RegexError.MISSING_SUBPATTERN_NAME: 162>, 'MISSING_DIGIT': <RegexError.MISSING_DIGIT: 163>, 'INVALID_DATA_CHARACTER': <RegexError.INVALID_DATA_CHARACTER: 164>, 'EXTRA_SUBPATTERN_NAME': <RegexError.EXTRA_SUBPATTERN_NAME: 165>, 'BACKTRACKING_CONTROL_VERB_ARGUMENT_REQUIRED': <RegexError.BACKTRACKING_CONTROL_VERB_ARGUMENT_REQUIRED: 166>, 'INVALID_CONTROL_CHAR': <RegexError.INVALID_CONTROL_CHAR: 168>, 'MISSING_NAME': <RegexError.MISSING_NAME: 169>, 'NOT_SUPPORTED_IN_CLASS': <RegexError.NOT_SUPPORTED_IN_CLASS: 171>, 'TOO_MANY_FORWARD_REFERENCES': <RegexError.TOO_MANY_FORWARD_REFERENCES: 172>, 'NAME_TOO_LONG': <RegexError.NAME_TOO_LONG: 175>, 'CHARACTER_VALUE_TOO_LARGE': <RegexError.CHARACTER_VALUE_TOO_LARGE: 176>})"
    __name__ = 'RegexError'
    __qualname__ = 'RegexError'


