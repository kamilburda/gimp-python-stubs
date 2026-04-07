# encoding: utf-8
# module gi.repository.Pango
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi._gi as __gi__gi


class Script(__gi__gi.GEnum):
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


    AHOM = 111
    ANATOLIAN_HIEROGLYPHS = 112
    ARABIC = 2
    ARMENIAN = 3
    BALINESE = 62
    BASSA_VAH = 88
    BATAK = 78
    BENGALI = 4
    BOPOMOFO = 5
    BRAHMI = 79
    BRAILLE = 46
    BUGINESE = 55
    BUHID = 44
    CANADIAN_ABORIGINAL = 40
    CARIAN = 75
    CAUCASIAN_ALBANIAN = 89
    CHAKMA = 81
    CHAM = 72
    CHEROKEE = 6
    COMMON = 0
    COPTIC = 7
    CUNEIFORM = 63
    CYPRIOT = 47
    CYRILLIC = 8
    DESERET = 9
    DEVANAGARI = 10
    DUPLOYAN = 90
    ELBASAN = 91
    ETHIOPIC = 11
    GEORGIAN = 12
    GLAGOLITIC = 56
    GOTHIC = 13
    GRANTHA = 92
    GREEK = 14
    GUJARATI = 15
    GURMUKHI = 16
    HAN = 17
    HANGUL = 18
    HANUNOO = 43
    HATRAN = 113
    HEBREW = 19
    HIRAGANA = 20
    INHERITED = 1
    INVALID_CODE = -1
    KANNADA = 21
    KATAKANA = 22
    KAYAH_LI = 67
    KHAROSHTHI = 60
    KHMER = 23
    KHOJKI = 93
    KHUDAWADI = 94
    LAO = 24
    LATIN = 25
    LEPCHA = 68
    LIMBU = 48
    LINEAR_A = 95
    LINEAR_B = 51
    LYCIAN = 76
    LYDIAN = 77
    MAHAJANI = 96
    MALAYALAM = 26
    MANDAIC = 80
    MANICHAEAN = 97
    MENDE_KIKAKUI = 98
    MEROITIC_CURSIVE = 82
    MEROITIC_HIEROGLYPHS = 83
    MIAO = 84
    MODI = 99
    MONGOLIAN = 27
    MRO = 100
    MULTANI = 114
    MYANMAR = 28
    NABATAEAN = 101
    NEW_TAI_LUE = 54
    NKO = 66
    OGHAM = 29
    OLD_HUNGARIAN = 115
    OLD_ITALIC = 30
    OLD_NORTH_ARABIAN = 102
    OLD_PERMIC = 103
    OLD_PERSIAN = 59
    OL_CHIKI = 73
    ORIYA = 31
    OSMANYA = 49
    PAHAWH_HMONG = 104
    PALMYRENE = 105
    PAU_CIN_HAU = 106
    PHAGS_PA = 65
    PHOENICIAN = 64
    PSALTER_PAHLAVI = 107
    REJANG = 69
    RUNIC = 32
    SAURASHTRA = 71
    SHARADA = 85
    SHAVIAN = 50
    SIDDHAM = 108
    SIGNWRITING = 116
    SINHALA = 33
    SORA_SOMPENG = 86
    SUNDANESE = 70
    SYLOTI_NAGRI = 58
    SYRIAC = 34
    TAGALOG = 42
    TAGBANWA = 45
    TAI_LE = 52
    TAKRI = 87
    TAMIL = 35
    TELUGU = 36
    THAANA = 37
    THAI = 38
    TIBETAN = 39
    TIFINAGH = 57
    TIRHUTA = 109
    UGARITIC = 53
    UNKNOWN = 61
    VAI = 74
    WARANG_CITI = 110
    YI = 41
    __class__ = None # (!) real value is "<class 'gi._enum.GEnumMeta'>"
    __members__ = None # (!) real value is "mappingproxy({'INVALID_CODE': <Script.INVALID_CODE: -1>, 'COMMON': <Script.COMMON: 0>, 'INHERITED': <Script.INHERITED: 1>, 'ARABIC': <Script.ARABIC: 2>, 'ARMENIAN': <Script.ARMENIAN: 3>, 'BENGALI': <Script.BENGALI: 4>, 'BOPOMOFO': <Script.BOPOMOFO: 5>, 'CHEROKEE': <Script.CHEROKEE: 6>, 'COPTIC': <Script.COPTIC: 7>, 'CYRILLIC': <Script.CYRILLIC: 8>, 'DESERET': <Script.DESERET: 9>, 'DEVANAGARI': <Script.DEVANAGARI: 10>, 'ETHIOPIC': <Script.ETHIOPIC: 11>, 'GEORGIAN': <Script.GEORGIAN: 12>, 'GOTHIC': <Script.GOTHIC: 13>, 'GREEK': <Script.GREEK: 14>, 'GUJARATI': <Script.GUJARATI: 15>, 'GURMUKHI': <Script.GURMUKHI: 16>, 'HAN': <Script.HAN: 17>, 'HANGUL': <Script.HANGUL: 18>, 'HEBREW': <Script.HEBREW: 19>, 'HIRAGANA': <Script.HIRAGANA: 20>, 'KANNADA': <Script.KANNADA: 21>, 'KATAKANA': <Script.KATAKANA: 22>, 'KHMER': <Script.KHMER: 23>, 'LAO': <Script.LAO: 24>, 'LATIN': <Script.LATIN: 25>, 'MALAYALAM': <Script.MALAYALAM: 26>, 'MONGOLIAN': <Script.MONGOLIAN: 27>, 'MYANMAR': <Script.MYANMAR: 28>, 'OGHAM': <Script.OGHAM: 29>, 'OLD_ITALIC': <Script.OLD_ITALIC: 30>, 'ORIYA': <Script.ORIYA: 31>, 'RUNIC': <Script.RUNIC: 32>, 'SINHALA': <Script.SINHALA: 33>, 'SYRIAC': <Script.SYRIAC: 34>, 'TAMIL': <Script.TAMIL: 35>, 'TELUGU': <Script.TELUGU: 36>, 'THAANA': <Script.THAANA: 37>, 'THAI': <Script.THAI: 38>, 'TIBETAN': <Script.TIBETAN: 39>, 'CANADIAN_ABORIGINAL': <Script.CANADIAN_ABORIGINAL: 40>, 'YI': <Script.YI: 41>, 'TAGALOG': <Script.TAGALOG: 42>, 'HANUNOO': <Script.HANUNOO: 43>, 'BUHID': <Script.BUHID: 44>, 'TAGBANWA': <Script.TAGBANWA: 45>, 'BRAILLE': <Script.BRAILLE: 46>, 'CYPRIOT': <Script.CYPRIOT: 47>, 'LIMBU': <Script.LIMBU: 48>, 'OSMANYA': <Script.OSMANYA: 49>, 'SHAVIAN': <Script.SHAVIAN: 50>, 'LINEAR_B': <Script.LINEAR_B: 51>, 'TAI_LE': <Script.TAI_LE: 52>, 'UGARITIC': <Script.UGARITIC: 53>, 'NEW_TAI_LUE': <Script.NEW_TAI_LUE: 54>, 'BUGINESE': <Script.BUGINESE: 55>, 'GLAGOLITIC': <Script.GLAGOLITIC: 56>, 'TIFINAGH': <Script.TIFINAGH: 57>, 'SYLOTI_NAGRI': <Script.SYLOTI_NAGRI: 58>, 'OLD_PERSIAN': <Script.OLD_PERSIAN: 59>, 'KHAROSHTHI': <Script.KHAROSHTHI: 60>, 'UNKNOWN': <Script.UNKNOWN: 61>, 'BALINESE': <Script.BALINESE: 62>, 'CUNEIFORM': <Script.CUNEIFORM: 63>, 'PHOENICIAN': <Script.PHOENICIAN: 64>, 'PHAGS_PA': <Script.PHAGS_PA: 65>, 'NKO': <Script.NKO: 66>, 'KAYAH_LI': <Script.KAYAH_LI: 67>, 'LEPCHA': <Script.LEPCHA: 68>, 'REJANG': <Script.REJANG: 69>, 'SUNDANESE': <Script.SUNDANESE: 70>, 'SAURASHTRA': <Script.SAURASHTRA: 71>, 'CHAM': <Script.CHAM: 72>, 'OL_CHIKI': <Script.OL_CHIKI: 73>, 'VAI': <Script.VAI: 74>, 'CARIAN': <Script.CARIAN: 75>, 'LYCIAN': <Script.LYCIAN: 76>, 'LYDIAN': <Script.LYDIAN: 77>, 'BATAK': <Script.BATAK: 78>, 'BRAHMI': <Script.BRAHMI: 79>, 'MANDAIC': <Script.MANDAIC: 80>, 'CHAKMA': <Script.CHAKMA: 81>, 'MEROITIC_CURSIVE': <Script.MEROITIC_CURSIVE: 82>, 'MEROITIC_HIEROGLYPHS': <Script.MEROITIC_HIEROGLYPHS: 83>, 'MIAO': <Script.MIAO: 84>, 'SHARADA': <Script.SHARADA: 85>, 'SORA_SOMPENG': <Script.SORA_SOMPENG: 86>, 'TAKRI': <Script.TAKRI: 87>, 'BASSA_VAH': <Script.BASSA_VAH: 88>, 'CAUCASIAN_ALBANIAN': <Script.CAUCASIAN_ALBANIAN: 89>, 'DUPLOYAN': <Script.DUPLOYAN: 90>, 'ELBASAN': <Script.ELBASAN: 91>, 'GRANTHA': <Script.GRANTHA: 92>, 'KHOJKI': <Script.KHOJKI: 93>, 'KHUDAWADI': <Script.KHUDAWADI: 94>, 'LINEAR_A': <Script.LINEAR_A: 95>, 'MAHAJANI': <Script.MAHAJANI: 96>, 'MANICHAEAN': <Script.MANICHAEAN: 97>, 'MENDE_KIKAKUI': <Script.MENDE_KIKAKUI: 98>, 'MODI': <Script.MODI: 99>, 'MRO': <Script.MRO: 100>, 'NABATAEAN': <Script.NABATAEAN: 101>, 'OLD_NORTH_ARABIAN': <Script.OLD_NORTH_ARABIAN: 102>, 'OLD_PERMIC': <Script.OLD_PERMIC: 103>, 'PAHAWH_HMONG': <Script.PAHAWH_HMONG: 104>, 'PALMYRENE': <Script.PALMYRENE: 105>, 'PAU_CIN_HAU': <Script.PAU_CIN_HAU: 106>, 'PSALTER_PAHLAVI': <Script.PSALTER_PAHLAVI: 107>, 'SIDDHAM': <Script.SIDDHAM: 108>, 'TIRHUTA': <Script.TIRHUTA: 109>, 'WARANG_CITI': <Script.WARANG_CITI: 110>, 'AHOM': <Script.AHOM: 111>, 'ANATOLIAN_HIEROGLYPHS': <Script.ANATOLIAN_HIEROGLYPHS: 112>, 'HATRAN': <Script.HATRAN: 113>, 'MULTANI': <Script.MULTANI: 114>, 'OLD_HUNGARIAN': <Script.OLD_HUNGARIAN: 115>, 'SIGNWRITING': <Script.SIGNWRITING: 116>})"
    __name__ = 'Script'
    __qualname__ = 'Script'


