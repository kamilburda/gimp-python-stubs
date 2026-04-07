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


class UnicodeScript(__gi__gi.GEnum):
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


    ADLAM = 132
    AHOM = 126
    ANATOLIAN_HIEROGLYPHS = 127
    ARABIC = 2
    ARMENIAN = 3
    AVESTAN = 78
    BALINESE = 62
    BAMUM = 79
    BASSA_VAH = 103
    BATAK = 93
    BENGALI = 4
    BHAIKSUKI = 133
    BOPOMOFO = 5
    BRAHMI = 94
    BRAILLE = 46
    BUGINESE = 55
    BUHID = 44
    CANADIAN_ABORIGINAL = 40
    CARIAN = 75
    CAUCASIAN_ALBANIAN = 104
    CHAKMA = 96
    CHAM = 72
    CHEROKEE = 6
    CHORASMIAN = 153
    COMMON = 0
    COPTIC = 7
    CUNEIFORM = 63
    CYPRIOT = 47
    CYPRO_MINOAN = 157
    CYRILLIC = 8
    DESERET = 9
    DEVANAGARI = 10
    DIVES_AKURU = 154
    DOGRA = 142
    DUPLOYAN = 105
    EGYPTIAN_HIEROGLYPHS = 80
    ELBASAN = 106
    ELYMAIC = 149
    ETHIOPIC = 11
    GARAY = 166
    GEORGIAN = 12
    GLAGOLITIC = 56
    GOTHIC = 13
    GRANTHA = 107
    GREEK = 14
    GUJARATI = 15
    GUNJALA_GONDI = 143
    GURMUKHI = 16
    GURUNG_KHEMA = 169
    HAN = 17
    HANGUL = 18
    HANIFI_ROHINGYA = 144
    HANUNOO = 43
    HATRAN = 128
    HEBREW = 19
    HIRAGANA = 20
    IMPERIAL_ARAMAIC = 81
    INHERITED = 1
    INSCRIPTIONAL_PAHLAVI = 82
    INSCRIPTIONAL_PARTHIAN = 83
    INVALID_CODE = -1
    JAVANESE = 84
    KAITHI = 85
    KANNADA = 21
    KATAKANA = 22
    KAWI = 163
    KAYAH_LI = 67
    KHAROSHTHI = 60
    KHITAN_SMALL_SCRIPT = 155
    KHMER = 23
    KHOJKI = 108
    KHUDAWADI = 109
    KIRAT_RAI = 170
    LAO = 24
    LATIN = 25
    LEPCHA = 68
    LIMBU = 48
    LINEAR_A = 110
    LINEAR_B = 51
    LISU = 86
    LYCIAN = 76
    LYDIAN = 77
    MAHAJANI = 111
    MAKASAR = 145
    MALAYALAM = 26
    MANDAIC = 95
    MANICHAEAN = 112
    MARCHEN = 134
    MASARAM_GONDI = 138
    MATH = 162
    MEDEFAIDRIN = 146
    MEETEI_MAYEK = 87
    MENDE_KIKAKUI = 113
    MEROITIC_CURSIVE = 97
    MEROITIC_HIEROGLYPHS = 98
    MIAO = 99
    MODI = 114
    MONGOLIAN = 27
    MRO = 115
    MULTANI = 129
    MYANMAR = 28
    NABATAEAN = 116
    NAG_MUNDARI = 164
    NANDINAGARI = 150
    NEWA = 135
    NEW_TAI_LUE = 54
    NKO = 66
    NUSHU = 139
    NYIAKENG_PUACHUE_HMONG = 151
    OGHAM = 29
    OLD_HUNGARIAN = 130
    OLD_ITALIC = 30
    OLD_NORTH_ARABIAN = 117
    OLD_PERMIC = 118
    OLD_PERSIAN = 59
    OLD_SOGDIAN = 147
    OLD_SOUTH_ARABIAN = 88
    OLD_TURKIC = 89
    OLD_UYGHUR = 158
    OL_CHIKI = 73
    OL_ONAL = 171
    ORIYA = 31
    OSAGE = 136
    OSMANYA = 49
    PAHAWH_HMONG = 119
    PALMYRENE = 120
    PAU_CIN_HAU = 121
    PHAGS_PA = 65
    PHOENICIAN = 64
    PSALTER_PAHLAVI = 122
    REJANG = 69
    RUNIC = 32
    SAMARITAN = 90
    SAURASHTRA = 71
    SHARADA = 100
    SHAVIAN = 50
    SIDDHAM = 123
    SIGNWRITING = 131
    SINHALA = 33
    SOGDIAN = 148
    SORA_SOMPENG = 101
    SOYOMBO = 140
    SUNDANESE = 70
    SUNUWAR = 168
    SYLOTI_NAGRI = 58
    SYRIAC = 34
    TAGALOG = 42
    TAGBANWA = 45
    TAI_LE = 52
    TAI_THAM = 91
    TAI_VIET = 92
    TAKRI = 102
    TAMIL = 35
    TANGSA = 159
    TANGUT = 137
    TELUGU = 36
    THAANA = 37
    THAI = 38
    TIBETAN = 39
    TIFINAGH = 57
    TIRHUTA = 124
    TODHRI = 165
    TOTO = 160
    TULU_TIGALARI = 167
    UGARITIC = 53
    UNKNOWN = 61
    VAI = 74
    VITHKUQI = 161
    WANCHO = 152
    WARANG_CITI = 125
    YEZIDI = 156
    YI = 41
    ZANABAZAR_SQUARE = 141
    __class__ = None # (!) real value is "<class 'gi._enum.GEnumMeta'>"
    __members__ = None # (!) real value is "mappingproxy({'INVALID_CODE': <UnicodeScript.INVALID_CODE: -1>, 'COMMON': <UnicodeScript.COMMON: 0>, 'INHERITED': <UnicodeScript.INHERITED: 1>, 'ARABIC': <UnicodeScript.ARABIC: 2>, 'ARMENIAN': <UnicodeScript.ARMENIAN: 3>, 'BENGALI': <UnicodeScript.BENGALI: 4>, 'BOPOMOFO': <UnicodeScript.BOPOMOFO: 5>, 'CHEROKEE': <UnicodeScript.CHEROKEE: 6>, 'COPTIC': <UnicodeScript.COPTIC: 7>, 'CYRILLIC': <UnicodeScript.CYRILLIC: 8>, 'DESERET': <UnicodeScript.DESERET: 9>, 'DEVANAGARI': <UnicodeScript.DEVANAGARI: 10>, 'ETHIOPIC': <UnicodeScript.ETHIOPIC: 11>, 'GEORGIAN': <UnicodeScript.GEORGIAN: 12>, 'GOTHIC': <UnicodeScript.GOTHIC: 13>, 'GREEK': <UnicodeScript.GREEK: 14>, 'GUJARATI': <UnicodeScript.GUJARATI: 15>, 'GURMUKHI': <UnicodeScript.GURMUKHI: 16>, 'HAN': <UnicodeScript.HAN: 17>, 'HANGUL': <UnicodeScript.HANGUL: 18>, 'HEBREW': <UnicodeScript.HEBREW: 19>, 'HIRAGANA': <UnicodeScript.HIRAGANA: 20>, 'KANNADA': <UnicodeScript.KANNADA: 21>, 'KATAKANA': <UnicodeScript.KATAKANA: 22>, 'KHMER': <UnicodeScript.KHMER: 23>, 'LAO': <UnicodeScript.LAO: 24>, 'LATIN': <UnicodeScript.LATIN: 25>, 'MALAYALAM': <UnicodeScript.MALAYALAM: 26>, 'MONGOLIAN': <UnicodeScript.MONGOLIAN: 27>, 'MYANMAR': <UnicodeScript.MYANMAR: 28>, 'OGHAM': <UnicodeScript.OGHAM: 29>, 'OLD_ITALIC': <UnicodeScript.OLD_ITALIC: 30>, 'ORIYA': <UnicodeScript.ORIYA: 31>, 'RUNIC': <UnicodeScript.RUNIC: 32>, 'SINHALA': <UnicodeScript.SINHALA: 33>, 'SYRIAC': <UnicodeScript.SYRIAC: 34>, 'TAMIL': <UnicodeScript.TAMIL: 35>, 'TELUGU': <UnicodeScript.TELUGU: 36>, 'THAANA': <UnicodeScript.THAANA: 37>, 'THAI': <UnicodeScript.THAI: 38>, 'TIBETAN': <UnicodeScript.TIBETAN: 39>, 'CANADIAN_ABORIGINAL': <UnicodeScript.CANADIAN_ABORIGINAL: 40>, 'YI': <UnicodeScript.YI: 41>, 'TAGALOG': <UnicodeScript.TAGALOG: 42>, 'HANUNOO': <UnicodeScript.HANUNOO: 43>, 'BUHID': <UnicodeScript.BUHID: 44>, 'TAGBANWA': <UnicodeScript.TAGBANWA: 45>, 'BRAILLE': <UnicodeScript.BRAILLE: 46>, 'CYPRIOT': <UnicodeScript.CYPRIOT: 47>, 'LIMBU': <UnicodeScript.LIMBU: 48>, 'OSMANYA': <UnicodeScript.OSMANYA: 49>, 'SHAVIAN': <UnicodeScript.SHAVIAN: 50>, 'LINEAR_B': <UnicodeScript.LINEAR_B: 51>, 'TAI_LE': <UnicodeScript.TAI_LE: 52>, 'UGARITIC': <UnicodeScript.UGARITIC: 53>, 'NEW_TAI_LUE': <UnicodeScript.NEW_TAI_LUE: 54>, 'BUGINESE': <UnicodeScript.BUGINESE: 55>, 'GLAGOLITIC': <UnicodeScript.GLAGOLITIC: 56>, 'TIFINAGH': <UnicodeScript.TIFINAGH: 57>, 'SYLOTI_NAGRI': <UnicodeScript.SYLOTI_NAGRI: 58>, 'OLD_PERSIAN': <UnicodeScript.OLD_PERSIAN: 59>, 'KHAROSHTHI': <UnicodeScript.KHAROSHTHI: 60>, 'UNKNOWN': <UnicodeScript.UNKNOWN: 61>, 'BALINESE': <UnicodeScript.BALINESE: 62>, 'CUNEIFORM': <UnicodeScript.CUNEIFORM: 63>, 'PHOENICIAN': <UnicodeScript.PHOENICIAN: 64>, 'PHAGS_PA': <UnicodeScript.PHAGS_PA: 65>, 'NKO': <UnicodeScript.NKO: 66>, 'KAYAH_LI': <UnicodeScript.KAYAH_LI: 67>, 'LEPCHA': <UnicodeScript.LEPCHA: 68>, 'REJANG': <UnicodeScript.REJANG: 69>, 'SUNDANESE': <UnicodeScript.SUNDANESE: 70>, 'SAURASHTRA': <UnicodeScript.SAURASHTRA: 71>, 'CHAM': <UnicodeScript.CHAM: 72>, 'OL_CHIKI': <UnicodeScript.OL_CHIKI: 73>, 'VAI': <UnicodeScript.VAI: 74>, 'CARIAN': <UnicodeScript.CARIAN: 75>, 'LYCIAN': <UnicodeScript.LYCIAN: 76>, 'LYDIAN': <UnicodeScript.LYDIAN: 77>, 'AVESTAN': <UnicodeScript.AVESTAN: 78>, 'BAMUM': <UnicodeScript.BAMUM: 79>, 'EGYPTIAN_HIEROGLYPHS': <UnicodeScript.EGYPTIAN_HIEROGLYPHS: 80>, 'IMPERIAL_ARAMAIC': <UnicodeScript.IMPERIAL_ARAMAIC: 81>, 'INSCRIPTIONAL_PAHLAVI': <UnicodeScript.INSCRIPTIONAL_PAHLAVI: 82>, 'INSCRIPTIONAL_PARTHIAN': <UnicodeScript.INSCRIPTIONAL_PARTHIAN: 83>, 'JAVANESE': <UnicodeScript.JAVANESE: 84>, 'KAITHI': <UnicodeScript.KAITHI: 85>, 'LISU': <UnicodeScript.LISU: 86>, 'MEETEI_MAYEK': <UnicodeScript.MEETEI_MAYEK: 87>, 'OLD_SOUTH_ARABIAN': <UnicodeScript.OLD_SOUTH_ARABIAN: 88>, 'OLD_TURKIC': <UnicodeScript.OLD_TURKIC: 89>, 'SAMARITAN': <UnicodeScript.SAMARITAN: 90>, 'TAI_THAM': <UnicodeScript.TAI_THAM: 91>, 'TAI_VIET': <UnicodeScript.TAI_VIET: 92>, 'BATAK': <UnicodeScript.BATAK: 93>, 'BRAHMI': <UnicodeScript.BRAHMI: 94>, 'MANDAIC': <UnicodeScript.MANDAIC: 95>, 'CHAKMA': <UnicodeScript.CHAKMA: 96>, 'MEROITIC_CURSIVE': <UnicodeScript.MEROITIC_CURSIVE: 97>, 'MEROITIC_HIEROGLYPHS': <UnicodeScript.MEROITIC_HIEROGLYPHS: 98>, 'MIAO': <UnicodeScript.MIAO: 99>, 'SHARADA': <UnicodeScript.SHARADA: 100>, 'SORA_SOMPENG': <UnicodeScript.SORA_SOMPENG: 101>, 'TAKRI': <UnicodeScript.TAKRI: 102>, 'BASSA_VAH': <UnicodeScript.BASSA_VAH: 103>, 'CAUCASIAN_ALBANIAN': <UnicodeScript.CAUCASIAN_ALBANIAN: 104>, 'DUPLOYAN': <UnicodeScript.DUPLOYAN: 105>, 'ELBASAN': <UnicodeScript.ELBASAN: 106>, 'GRANTHA': <UnicodeScript.GRANTHA: 107>, 'KHOJKI': <UnicodeScript.KHOJKI: 108>, 'KHUDAWADI': <UnicodeScript.KHUDAWADI: 109>, 'LINEAR_A': <UnicodeScript.LINEAR_A: 110>, 'MAHAJANI': <UnicodeScript.MAHAJANI: 111>, 'MANICHAEAN': <UnicodeScript.MANICHAEAN: 112>, 'MENDE_KIKAKUI': <UnicodeScript.MENDE_KIKAKUI: 113>, 'MODI': <UnicodeScript.MODI: 114>, 'MRO': <UnicodeScript.MRO: 115>, 'NABATAEAN': <UnicodeScript.NABATAEAN: 116>, 'OLD_NORTH_ARABIAN': <UnicodeScript.OLD_NORTH_ARABIAN: 117>, 'OLD_PERMIC': <UnicodeScript.OLD_PERMIC: 118>, 'PAHAWH_HMONG': <UnicodeScript.PAHAWH_HMONG: 119>, 'PALMYRENE': <UnicodeScript.PALMYRENE: 120>, 'PAU_CIN_HAU': <UnicodeScript.PAU_CIN_HAU: 121>, 'PSALTER_PAHLAVI': <UnicodeScript.PSALTER_PAHLAVI: 122>, 'SIDDHAM': <UnicodeScript.SIDDHAM: 123>, 'TIRHUTA': <UnicodeScript.TIRHUTA: 124>, 'WARANG_CITI': <UnicodeScript.WARANG_CITI: 125>, 'AHOM': <UnicodeScript.AHOM: 126>, 'ANATOLIAN_HIEROGLYPHS': <UnicodeScript.ANATOLIAN_HIEROGLYPHS: 127>, 'HATRAN': <UnicodeScript.HATRAN: 128>, 'MULTANI': <UnicodeScript.MULTANI: 129>, 'OLD_HUNGARIAN': <UnicodeScript.OLD_HUNGARIAN: 130>, 'SIGNWRITING': <UnicodeScript.SIGNWRITING: 131>, 'ADLAM': <UnicodeScript.ADLAM: 132>, 'BHAIKSUKI': <UnicodeScript.BHAIKSUKI: 133>, 'MARCHEN': <UnicodeScript.MARCHEN: 134>, 'NEWA': <UnicodeScript.NEWA: 135>, 'OSAGE': <UnicodeScript.OSAGE: 136>, 'TANGUT': <UnicodeScript.TANGUT: 137>, 'MASARAM_GONDI': <UnicodeScript.MASARAM_GONDI: 138>, 'NUSHU': <UnicodeScript.NUSHU: 139>, 'SOYOMBO': <UnicodeScript.SOYOMBO: 140>, 'ZANABAZAR_SQUARE': <UnicodeScript.ZANABAZAR_SQUARE: 141>, 'DOGRA': <UnicodeScript.DOGRA: 142>, 'GUNJALA_GONDI': <UnicodeScript.GUNJALA_GONDI: 143>, 'HANIFI_ROHINGYA': <UnicodeScript.HANIFI_ROHINGYA: 144>, 'MAKASAR': <UnicodeScript.MAKASAR: 145>, 'MEDEFAIDRIN': <UnicodeScript.MEDEFAIDRIN: 146>, 'OLD_SOGDIAN': <UnicodeScript.OLD_SOGDIAN: 147>, 'SOGDIAN': <UnicodeScript.SOGDIAN: 148>, 'ELYMAIC': <UnicodeScript.ELYMAIC: 149>, 'NANDINAGARI': <UnicodeScript.NANDINAGARI: 150>, 'NYIAKENG_PUACHUE_HMONG': <UnicodeScript.NYIAKENG_PUACHUE_HMONG: 151>, 'WANCHO': <UnicodeScript.WANCHO: 152>, 'CHORASMIAN': <UnicodeScript.CHORASMIAN: 153>, 'DIVES_AKURU': <UnicodeScript.DIVES_AKURU: 154>, 'KHITAN_SMALL_SCRIPT': <UnicodeScript.KHITAN_SMALL_SCRIPT: 155>, 'YEZIDI': <UnicodeScript.YEZIDI: 156>, 'CYPRO_MINOAN': <UnicodeScript.CYPRO_MINOAN: 157>, 'OLD_UYGHUR': <UnicodeScript.OLD_UYGHUR: 158>, 'TANGSA': <UnicodeScript.TANGSA: 159>, 'TOTO': <UnicodeScript.TOTO: 160>, 'VITHKUQI': <UnicodeScript.VITHKUQI: 161>, 'MATH': <UnicodeScript.MATH: 162>, 'KAWI': <UnicodeScript.KAWI: 163>, 'NAG_MUNDARI': <UnicodeScript.NAG_MUNDARI: 164>, 'TODHRI': <UnicodeScript.TODHRI: 165>, 'GARAY': <UnicodeScript.GARAY: 166>, 'TULU_TIGALARI': <UnicodeScript.TULU_TIGALARI: 167>, 'SUNUWAR': <UnicodeScript.SUNUWAR: 168>, 'GURUNG_KHEMA': <UnicodeScript.GURUNG_KHEMA: 169>, 'KIRAT_RAI': <UnicodeScript.KIRAT_RAI: 170>, 'OL_ONAL': <UnicodeScript.OL_ONAL: 171>})"
    __name__ = 'UnicodeScript'
    __qualname__ = 'UnicodeScript'


