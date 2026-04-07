# encoding: utf-8
# module gi.repository.HarfBuzz
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi


class script_t(__enum.IntFlag):
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


    __class__ = None # (!) real value is "<class 'enum.EnumType'>"
    __members__ = None # (!) real value is "mappingproxy({'B_SCRIPT_COMMON': <script_t.B_SCRIPT_COMMON: 1517910393>, 'B_SCRIPT_INHERITED': <script_t.B_SCRIPT_INHERITED: 1516858984>, 'B_SCRIPT_UNKNOWN': <script_t.B_SCRIPT_UNKNOWN: 1517976186>, 'B_SCRIPT_ARABIC': <script_t.B_SCRIPT_ARABIC: 1098015074>, 'B_SCRIPT_ARMENIAN': <script_t.B_SCRIPT_ARMENIAN: 1098018158>, 'B_SCRIPT_BENGALI': <script_t.B_SCRIPT_BENGALI: 1113943655>, 'B_SCRIPT_CYRILLIC': <script_t.B_SCRIPT_CYRILLIC: 1132032620>, 'B_SCRIPT_DEVANAGARI': <script_t.B_SCRIPT_DEVANAGARI: 1147500129>, 'B_SCRIPT_GEORGIAN': <script_t.B_SCRIPT_GEORGIAN: 1197830002>, 'B_SCRIPT_GREEK': <script_t.B_SCRIPT_GREEK: 1198679403>, 'B_SCRIPT_GUJARATI': <script_t.B_SCRIPT_GUJARATI: 1198877298>, 'B_SCRIPT_GURMUKHI': <script_t.B_SCRIPT_GURMUKHI: 1198879349>, 'B_SCRIPT_HANGUL': <script_t.B_SCRIPT_HANGUL: 1214344807>, 'B_SCRIPT_HAN': <script_t.B_SCRIPT_HAN: 1214344809>, 'B_SCRIPT_HEBREW': <script_t.B_SCRIPT_HEBREW: 1214603890>, 'B_SCRIPT_HIRAGANA': <script_t.B_SCRIPT_HIRAGANA: 1214870113>, 'B_SCRIPT_KANNADA': <script_t.B_SCRIPT_KANNADA: 1265525857>, 'B_SCRIPT_KATAKANA': <script_t.B_SCRIPT_KATAKANA: 1264676449>, 'B_SCRIPT_LAO': <script_t.B_SCRIPT_LAO: 1281453935>, 'B_SCRIPT_LATIN': <script_t.B_SCRIPT_LATIN: 1281455214>, 'B_SCRIPT_MALAYALAM': <script_t.B_SCRIPT_MALAYALAM: 1298954605>, 'B_SCRIPT_ORIYA': <script_t.B_SCRIPT_ORIYA: 1332902241>, 'B_SCRIPT_TAMIL': <script_t.B_SCRIPT_TAMIL: 1415671148>, 'B_SCRIPT_TELUGU': <script_t.B_SCRIPT_TELUGU: 1415933045>, 'B_SCRIPT_THAI': <script_t.B_SCRIPT_THAI: 1416126825>, 'B_SCRIPT_TIBETAN': <script_t.B_SCRIPT_TIBETAN: 1416192628>, 'B_SCRIPT_BOPOMOFO': <script_t.B_SCRIPT_BOPOMOFO: 1114599535>, 'B_SCRIPT_BRAILLE': <script_t.B_SCRIPT_BRAILLE: 1114792297>, 'B_SCRIPT_CANADIAN_SYLLABICS': <script_t.B_SCRIPT_CANADIAN_SYLLABICS: 1130458739>, 'B_SCRIPT_CHEROKEE': <script_t.B_SCRIPT_CHEROKEE: 1130915186>, 'B_SCRIPT_ETHIOPIC': <script_t.B_SCRIPT_ETHIOPIC: 1165256809>, 'B_SCRIPT_KHMER': <script_t.B_SCRIPT_KHMER: 1265134962>, 'B_SCRIPT_MONGOLIAN': <script_t.B_SCRIPT_MONGOLIAN: 1299148391>, 'B_SCRIPT_MYANMAR': <script_t.B_SCRIPT_MYANMAR: 1299803506>, 'B_SCRIPT_OGHAM': <script_t.B_SCRIPT_OGHAM: 1332175213>, 'B_SCRIPT_RUNIC': <script_t.B_SCRIPT_RUNIC: 1383427698>, 'B_SCRIPT_SINHALA': <script_t.B_SCRIPT_SINHALA: 1399418472>, 'B_SCRIPT_SYRIAC': <script_t.B_SCRIPT_SYRIAC: 1400468067>, 'B_SCRIPT_THAANA': <script_t.B_SCRIPT_THAANA: 1416126817>, 'B_SCRIPT_YI': <script_t.B_SCRIPT_YI: 1500080489>, 'B_SCRIPT_DESERET': <script_t.B_SCRIPT_DESERET: 1148416628>, 'B_SCRIPT_GOTHIC': <script_t.B_SCRIPT_GOTHIC: 1198486632>, 'B_SCRIPT_OLD_ITALIC': <script_t.B_SCRIPT_OLD_ITALIC: 1232363884>, 'B_SCRIPT_BUHID': <script_t.B_SCRIPT_BUHID: 1114990692>, 'B_SCRIPT_HANUNOO': <script_t.B_SCRIPT_HANUNOO: 1214344815>, 'B_SCRIPT_TAGALOG': <script_t.B_SCRIPT_TAGALOG: 1416064103>, 'B_SCRIPT_TAGBANWA': <script_t.B_SCRIPT_TAGBANWA: 1415669602>, 'B_SCRIPT_CYPRIOT': <script_t.B_SCRIPT_CYPRIOT: 1131442804>, 'B_SCRIPT_LIMBU': <script_t.B_SCRIPT_LIMBU: 1281977698>, 'B_SCRIPT_LINEAR_B': <script_t.B_SCRIPT_LINEAR_B: 1281977954>, 'B_SCRIPT_OSMANYA': <script_t.B_SCRIPT_OSMANYA: 1332964705>, 'B_SCRIPT_SHAVIAN': <script_t.B_SCRIPT_SHAVIAN: 1399349623>, 'B_SCRIPT_TAI_LE': <script_t.B_SCRIPT_TAI_LE: 1415670885>, 'B_SCRIPT_UGARITIC': <script_t.B_SCRIPT_UGARITIC: 1432838514>, 'B_SCRIPT_BUGINESE': <script_t.B_SCRIPT_BUGINESE: 1114990441>, 'B_SCRIPT_COPTIC': <script_t.B_SCRIPT_COPTIC: 1131376756>, 'B_SCRIPT_GLAGOLITIC': <script_t.B_SCRIPT_GLAGOLITIC: 1198285159>, 'B_SCRIPT_KHAROSHTHI': <script_t.B_SCRIPT_KHAROSHTHI: 1265131890>, 'B_SCRIPT_NEW_TAI_LUE': <script_t.B_SCRIPT_NEW_TAI_LUE: 1415670901>, 'B_SCRIPT_OLD_PERSIAN': <script_t.B_SCRIPT_OLD_PERSIAN: 1483761007>, 'B_SCRIPT_SYLOTI_NAGRI': <script_t.B_SCRIPT_SYLOTI_NAGRI: 1400466543>, 'B_SCRIPT_TIFINAGH': <script_t.B_SCRIPT_TIFINAGH: 1415999079>, 'B_SCRIPT_BALINESE': <script_t.B_SCRIPT_BALINESE: 1113681001>, 'B_SCRIPT_CUNEIFORM': <script_t.B_SCRIPT_CUNEIFORM: 1483961720>, 'B_SCRIPT_NKO': <script_t.B_SCRIPT_NKO: 1315663727>, 'B_SCRIPT_PHAGS_PA': <script_t.B_SCRIPT_PHAGS_PA: 1349017959>, 'B_SCRIPT_PHOENICIAN': <script_t.B_SCRIPT_PHOENICIAN: 1349021304>, 'B_SCRIPT_CARIAN': <script_t.B_SCRIPT_CARIAN: 1130459753>, 'B_SCRIPT_CHAM': <script_t.B_SCRIPT_CHAM: 1130914157>, 'B_SCRIPT_KAYAH_LI': <script_t.B_SCRIPT_KAYAH_LI: 1264675945>, 'B_SCRIPT_LEPCHA': <script_t.B_SCRIPT_LEPCHA: 1281716323>, 'B_SCRIPT_LYCIAN': <script_t.B_SCRIPT_LYCIAN: 1283023721>, 'B_SCRIPT_LYDIAN': <script_t.B_SCRIPT_LYDIAN: 1283023977>, 'B_SCRIPT_OL_CHIKI': <script_t.B_SCRIPT_OL_CHIKI: 1332503403>, 'B_SCRIPT_REJANG': <script_t.B_SCRIPT_REJANG: 1382706791>, 'B_SCRIPT_SAURASHTRA': <script_t.B_SCRIPT_SAURASHTRA: 1398895986>, 'B_SCRIPT_SUNDANESE': <script_t.B_SCRIPT_SUNDANESE: 1400204900>, 'B_SCRIPT_VAI': <script_t.B_SCRIPT_VAI: 1449224553>, 'B_SCRIPT_AVESTAN': <script_t.B_SCRIPT_AVESTAN: 1098281844>, 'B_SCRIPT_BAMUM': <script_t.B_SCRIPT_BAMUM: 1113681269>, 'B_SCRIPT_EGYPTIAN_HIEROGLYPHS': <script_t.B_SCRIPT_EGYPTIAN_HIEROGLYPHS: 1164409200>, 'B_SCRIPT_IMPERIAL_ARAMAIC': <script_t.B_SCRIPT_IMPERIAL_ARAMAIC: 1098018153>, 'B_SCRIPT_INSCRIPTIONAL_PAHLAVI': <script_t.B_SCRIPT_INSCRIPTIONAL_PAHLAVI: 1349020777>, 'B_SCRIPT_INSCRIPTIONAL_PARTHIAN': <script_t.B_SCRIPT_INSCRIPTIONAL_PARTHIAN: 1349678185>, 'B_SCRIPT_JAVANESE': <script_t.B_SCRIPT_JAVANESE: 1247901281>, 'B_SCRIPT_KAITHI': <script_t.B_SCRIPT_KAITHI: 1265920105>, 'B_SCRIPT_LISU': <script_t.B_SCRIPT_LISU: 1281979253>, 'B_SCRIPT_MEETEI_MAYEK': <script_t.B_SCRIPT_MEETEI_MAYEK: 1299473769>, 'B_SCRIPT_OLD_SOUTH_ARABIAN': <script_t.B_SCRIPT_OLD_SOUTH_ARABIAN: 1398895202>, 'B_SCRIPT_OLD_TURKIC': <script_t.B_SCRIPT_OLD_TURKIC: 1332898664>, 'B_SCRIPT_SAMARITAN': <script_t.B_SCRIPT_SAMARITAN: 1398893938>, 'B_SCRIPT_TAI_THAM': <script_t.B_SCRIPT_TAI_THAM: 1281453665>, 'B_SCRIPT_TAI_VIET': <script_t.B_SCRIPT_TAI_VIET: 1415673460>, 'B_SCRIPT_BATAK': <script_t.B_SCRIPT_BATAK: 1113683051>, 'B_SCRIPT_BRAHMI': <script_t.B_SCRIPT_BRAHMI: 1114792296>, 'B_SCRIPT_MANDAIC': <script_t.B_SCRIPT_MANDAIC: 1298230884>, 'B_SCRIPT_CHAKMA': <script_t.B_SCRIPT_CHAKMA: 1130457965>, 'B_SCRIPT_MEROITIC_CURSIVE': <script_t.B_SCRIPT_MEROITIC_CURSIVE: 1298494051>, 'B_SCRIPT_MEROITIC_HIEROGLYPHS': <script_t.B_SCRIPT_MEROITIC_HIEROGLYPHS: 1298494063>, 'B_SCRIPT_MIAO': <script_t.B_SCRIPT_MIAO: 1349284452>, 'B_SCRIPT_SHARADA': <script_t.B_SCRIPT_SHARADA: 1399353956>, 'B_SCRIPT_SORA_SOMPENG': <script_t.B_SCRIPT_SORA_SOMPENG: 1399812705>, 'B_SCRIPT_TAKRI': <script_t.B_SCRIPT_TAKRI: 1415670642>, 'B_SCRIPT_BASSA_VAH': <script_t.B_SCRIPT_BASSA_VAH: 1113682803>, 'B_SCRIPT_CAUCASIAN_ALBANIAN': <script_t.B_SCRIPT_CAUCASIAN_ALBANIAN: 1097295970>, 'B_SCRIPT_DUPLOYAN': <script_t.B_SCRIPT_DUPLOYAN: 1148547180>, 'B_SCRIPT_ELBASAN': <script_t.B_SCRIPT_ELBASAN: 1164730977>, 'B_SCRIPT_GRANTHA': <script_t.B_SCRIPT_GRANTHA: 1198678382>, 'B_SCRIPT_KHOJKI': <script_t.B_SCRIPT_KHOJKI: 1265135466>, 'B_SCRIPT_KHUDAWADI': <script_t.B_SCRIPT_KHUDAWADI: 1399418468>, 'B_SCRIPT_LINEAR_A': <script_t.B_SCRIPT_LINEAR_A: 1281977953>, 'B_SCRIPT_MAHAJANI': <script_t.B_SCRIPT_MAHAJANI: 1298229354>, 'B_SCRIPT_MANICHAEAN': <script_t.B_SCRIPT_MANICHAEAN: 1298230889>, 'B_SCRIPT_MENDE_KIKAKUI': <script_t.B_SCRIPT_MENDE_KIKAKUI: 1298493028>, 'B_SCRIPT_MODI': <script_t.B_SCRIPT_MODI: 1299145833>, 'B_SCRIPT_MRO': <script_t.B_SCRIPT_MRO: 1299345263>, 'B_SCRIPT_NABATAEAN': <script_t.B_SCRIPT_NABATAEAN: 1315070324>, 'B_SCRIPT_OLD_NORTH_ARABIAN': <script_t.B_SCRIPT_OLD_NORTH_ARABIAN: 1315009122>, 'B_SCRIPT_OLD_PERMIC': <script_t.B_SCRIPT_OLD_PERMIC: 1348825709>, 'B_SCRIPT_PAHAWH_HMONG': <script_t.B_SCRIPT_PAHAWH_HMONG: 1215131239>, 'B_SCRIPT_PALMYRENE': <script_t.B_SCRIPT_PALMYRENE: 1348562029>, 'B_SCRIPT_PAU_CIN_HAU': <script_t.B_SCRIPT_PAU_CIN_HAU: 1348564323>, 'B_SCRIPT_PSALTER_PAHLAVI': <script_t.B_SCRIPT_PSALTER_PAHLAVI: 1349020784>, 'B_SCRIPT_SIDDHAM': <script_t.B_SCRIPT_SIDDHAM: 1399415908>, 'B_SCRIPT_TIRHUTA': <script_t.B_SCRIPT_TIRHUTA: 1416196712>, 'B_SCRIPT_WARANG_CITI': <script_t.B_SCRIPT_WARANG_CITI: 1466004065>, 'B_SCRIPT_AHOM': <script_t.B_SCRIPT_AHOM: 1097363309>, 'B_SCRIPT_ANATOLIAN_HIEROGLYPHS': <script_t.B_SCRIPT_ANATOLIAN_HIEROGLYPHS: 1215067511>, 'B_SCRIPT_HATRAN': <script_t.B_SCRIPT_HATRAN: 1214346354>, 'B_SCRIPT_MULTANI': <script_t.B_SCRIPT_MULTANI: 1299541108>, 'B_SCRIPT_OLD_HUNGARIAN': <script_t.B_SCRIPT_OLD_HUNGARIAN: 1215655527>, 'B_SCRIPT_SIGNWRITING': <script_t.B_SCRIPT_SIGNWRITING: 1399287415>, 'B_SCRIPT_ADLAM': <script_t.B_SCRIPT_ADLAM: 1097100397>, 'B_SCRIPT_BHAIKSUKI': <script_t.B_SCRIPT_BHAIKSUKI: 1114139507>, 'B_SCRIPT_MARCHEN': <script_t.B_SCRIPT_MARCHEN: 1298231907>, 'B_SCRIPT_OSAGE': <script_t.B_SCRIPT_OSAGE: 1332963173>, 'B_SCRIPT_TANGUT': <script_t.B_SCRIPT_TANGUT: 1415671399>, 'B_SCRIPT_NEWA': <script_t.B_SCRIPT_NEWA: 1315272545>, 'B_SCRIPT_MASARAM_GONDI': <script_t.B_SCRIPT_MASARAM_GONDI: 1198485101>, 'B_SCRIPT_NUSHU': <script_t.B_SCRIPT_NUSHU: 1316186229>, 'B_SCRIPT_SOYOMBO': <script_t.B_SCRIPT_SOYOMBO: 1399814511>, 'B_SCRIPT_ZANABAZAR_SQUARE': <script_t.B_SCRIPT_ZANABAZAR_SQUARE: 1516334690>, 'B_SCRIPT_DOGRA': <script_t.B_SCRIPT_DOGRA: 1148151666>, 'B_SCRIPT_GUNJALA_GONDI': <script_t.B_SCRIPT_GUNJALA_GONDI: 1198485095>, 'B_SCRIPT_HANIFI_ROHINGYA': <script_t.B_SCRIPT_HANIFI_ROHINGYA: 1383032935>, 'B_SCRIPT_MAKASAR': <script_t.B_SCRIPT_MAKASAR: 1298230113>, 'B_SCRIPT_MEDEFAIDRIN': <script_t.B_SCRIPT_MEDEFAIDRIN: 1298490470>, 'B_SCRIPT_OLD_SOGDIAN': <script_t.B_SCRIPT_OLD_SOGDIAN: 1399809903>, 'B_SCRIPT_SOGDIAN': <script_t.B_SCRIPT_SOGDIAN: 1399809892>, 'B_SCRIPT_ELYMAIC': <script_t.B_SCRIPT_ELYMAIC: 1164736877>, 'B_SCRIPT_NANDINAGARI': <script_t.B_SCRIPT_NANDINAGARI: 1315008100>, 'B_SCRIPT_NYIAKENG_PUACHUE_HMONG': <script_t.B_SCRIPT_NYIAKENG_PUACHUE_HMONG: 1215131248>, 'B_SCRIPT_WANCHO': <script_t.B_SCRIPT_WANCHO: 1466132591>, 'B_SCRIPT_CHORASMIAN': <script_t.B_SCRIPT_CHORASMIAN: 1130918515>, 'B_SCRIPT_DIVES_AKURU': <script_t.B_SCRIPT_DIVES_AKURU: 1147756907>, 'B_SCRIPT_KHITAN_SMALL_SCRIPT': <script_t.B_SCRIPT_KHITAN_SMALL_SCRIPT: 1265202291>, 'B_SCRIPT_YEZIDI': <script_t.B_SCRIPT_YEZIDI: 1499822697>, 'B_SCRIPT_CYPRO_MINOAN': <script_t.B_SCRIPT_CYPRO_MINOAN: 1131441518>, 'B_SCRIPT_OLD_UYGHUR': <script_t.B_SCRIPT_OLD_UYGHUR: 1333094258>, 'B_SCRIPT_TANGSA': <script_t.B_SCRIPT_TANGSA: 1416524641>, 'B_SCRIPT_TOTO': <script_t.B_SCRIPT_TOTO: 1416590447>, 'B_SCRIPT_VITHKUQI': <script_t.B_SCRIPT_VITHKUQI: 1449751656>, 'B_SCRIPT_MATH': <script_t.B_SCRIPT_MATH: 1517122664>, 'B_SCRIPT_KAWI': <script_t.B_SCRIPT_KAWI: 1264678761>, 'B_SCRIPT_NAG_MUNDARI': <script_t.B_SCRIPT_NAG_MUNDARI: 1315006317>, 'B_SCRIPT_GARAY': <script_t.B_SCRIPT_GARAY: 1197568609>, 'B_SCRIPT_GURUNG_KHEMA': <script_t.B_SCRIPT_GURUNG_KHEMA: 1198877544>, 'B_SCRIPT_KIRAT_RAI': <script_t.B_SCRIPT_KIRAT_RAI: 1265787241>, 'B_SCRIPT_OL_ONAL': <script_t.B_SCRIPT_OL_ONAL: 1332633967>, 'B_SCRIPT_SUNUWAR': <script_t.B_SCRIPT_SUNUWAR: 1400204917>, 'B_SCRIPT_TODHRI': <script_t.B_SCRIPT_TODHRI: 1416586354>, 'B_SCRIPT_TULU_TIGALARI': <script_t.B_SCRIPT_TULU_TIGALARI: 1416983655>, 'B_SCRIPT_BERIA_ERFE': <script_t.B_SCRIPT_BERIA_ERFE: 1113944678>, 'B_SCRIPT_SIDETIC': <script_t.B_SCRIPT_SIDETIC: 1399415924>, 'B_SCRIPT_TAI_YO': <script_t.B_SCRIPT_TAI_YO: 1415674223>, 'B_SCRIPT_TOLONG_SIKI': <script_t.B_SCRIPT_TOLONG_SIKI: 1416588403>, 'B_SCRIPT_INVALID': <script_t.B_SCRIPT_INVALID: 0>})"
    __name__ = 'script_t'
    __qualname__ = 'script_t'


