# encoding: utf-8
# module gi.repository.Atk
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gi._gi as __gi__gi
import gobject as __gobject


class Role(__gi__gi.GEnum):
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


    ACCELERATOR_LABEL = 1
    ALERT = 2
    ANIMATION = 3
    APPLICATION = 73
    ARROW = 4
    ARTICLE = 107
    AUDIO = 104
    AUTOCOMPLETE = 74
    BLOCK_QUOTE = 103
    BUTTON = 42
    CALENDAR = 5
    CANVAS = 6
    CAPTION = 79
    CHART = 78
    CHECK_BOX = 7
    CHECK_MENU_ITEM = 8
    COLOR_CHOOSER = 9
    COLUMN_HEADER = 10
    COMBO_BOX = 11
    COMMENT = 95
    CONTENT_DELETION = 123
    CONTENT_INSERTION = 124
    DATE_EDITOR = 12
    DEFINITION = 106
    DESCRIPTION_LIST = 114
    DESCRIPTION_TERM = 115
    DESCRIPTION_VALUE = 116
    DESKTOP_FRAME = 14
    DESKTOP_ICON = 13
    DIAL = 15
    DIALOG = 16
    DIRECTORY_PANE = 17
    DOCUMENT_EMAIL = 94
    DOCUMENT_FRAME = 80
    DOCUMENT_PRESENTATION = 91
    DOCUMENT_SPREADSHEET = 90
    DOCUMENT_TEXT = 92
    DOCUMENT_WEB = 93
    DRAWING_AREA = 18
    EDIT_BAR = 75
    EMBEDDED = 76
    ENTRY = 77
    FILE_CHOOSER = 19
    FILLER = 20
    FONT_CHOOSER = 21
    FOOTER = 70
    FOOTNOTE = 122
    FORM = 85
    FRAME = 22
    GLASS_PANE = 23
    GROUPING = 97
    HEADER = 69
    HEADING = 81
    HTML_CONTAINER = 24
    ICON = 25
    IMAGE = 26
    IMAGE_MAP = 98
    INFO_BAR = 100
    INPUT_METHOD_WINDOW = 87
    INTERNAL_FRAME = 27
    INVALID = 0
    LABEL = 28
    LANDMARK = 108
    LAST_DEFINED = 129
    LAYERED_PANE = 29
    LEVEL_BAR = 101
    LINK = 86
    LIST = 30
    LIST_BOX = 96
    LIST_ITEM = 31
    LOG = 109
    MARK = 125
    MARQUEE = 110
    MATH = 111
    MATH_FRACTION = 118
    MATH_ROOT = 119
    MENU = 32
    MENU_BAR = 33
    MENU_ITEM = 34
    NOTIFICATION = 99
    OPTION_PANE = 35
    PAGE = 82
    PAGE_TAB = 36
    PAGE_TAB_LIST = 37
    PANEL = 38
    PARAGRAPH = 71
    PASSWORD_TEXT = 39
    POPUP_MENU = 40
    PROGRESS_BAR = 41
    PUSH_BUTTON_MENU = 127
    RADIO_BUTTON = 43
    RADIO_MENU_ITEM = 44
    RATING = 112
    REDUNDANT_OBJECT = 84
    ROOT_PANE = 45
    ROW_HEADER = 46
    RULER = 72
    SCROLL_BAR = 47
    SCROLL_PANE = 48
    SECTION = 83
    SEPARATOR = 49
    SLIDER = 50
    SPIN_BUTTON = 52
    SPLIT_PANE = 51
    STATIC = 117
    STATUSBAR = 53
    SUBSCRIPT = 120
    SUGGESTION = 126
    SUPERSCRIPT = 121
    SWITCH = 128
    TABLE = 54
    TABLE_CELL = 55
    TABLE_COLUMN_HEADER = 56
    TABLE_ROW = 88
    TABLE_ROW_HEADER = 57
    TEAR_OFF_MENU_ITEM = 58
    TERMINAL = 59
    TEXT = 60
    TIMER = 113
    TITLE_BAR = 102
    TOGGLE_BUTTON = 61
    TOOL_BAR = 62
    TOOL_TIP = 63
    TREE = 64
    TREE_ITEM = 89
    TREE_TABLE = 65
    UNKNOWN = 66
    VIDEO = 105
    VIEWPORT = 67
    WINDOW = 68
    __class__ = None # (!) real value is "<class 'gi._enum.GEnumMeta'>"
    __members__ = None # (!) real value is "mappingproxy({'INVALID': <Role.INVALID: 0>, 'ACCELERATOR_LABEL': <Role.ACCELERATOR_LABEL: 1>, 'ALERT': <Role.ALERT: 2>, 'ANIMATION': <Role.ANIMATION: 3>, 'ARROW': <Role.ARROW: 4>, 'CALENDAR': <Role.CALENDAR: 5>, 'CANVAS': <Role.CANVAS: 6>, 'CHECK_BOX': <Role.CHECK_BOX: 7>, 'CHECK_MENU_ITEM': <Role.CHECK_MENU_ITEM: 8>, 'COLOR_CHOOSER': <Role.COLOR_CHOOSER: 9>, 'COLUMN_HEADER': <Role.COLUMN_HEADER: 10>, 'COMBO_BOX': <Role.COMBO_BOX: 11>, 'DATE_EDITOR': <Role.DATE_EDITOR: 12>, 'DESKTOP_ICON': <Role.DESKTOP_ICON: 13>, 'DESKTOP_FRAME': <Role.DESKTOP_FRAME: 14>, 'DIAL': <Role.DIAL: 15>, 'DIALOG': <Role.DIALOG: 16>, 'DIRECTORY_PANE': <Role.DIRECTORY_PANE: 17>, 'DRAWING_AREA': <Role.DRAWING_AREA: 18>, 'FILE_CHOOSER': <Role.FILE_CHOOSER: 19>, 'FILLER': <Role.FILLER: 20>, 'FONT_CHOOSER': <Role.FONT_CHOOSER: 21>, 'FRAME': <Role.FRAME: 22>, 'GLASS_PANE': <Role.GLASS_PANE: 23>, 'HTML_CONTAINER': <Role.HTML_CONTAINER: 24>, 'ICON': <Role.ICON: 25>, 'IMAGE': <Role.IMAGE: 26>, 'INTERNAL_FRAME': <Role.INTERNAL_FRAME: 27>, 'LABEL': <Role.LABEL: 28>, 'LAYERED_PANE': <Role.LAYERED_PANE: 29>, 'LIST': <Role.LIST: 30>, 'LIST_ITEM': <Role.LIST_ITEM: 31>, 'MENU': <Role.MENU: 32>, 'MENU_BAR': <Role.MENU_BAR: 33>, 'MENU_ITEM': <Role.MENU_ITEM: 34>, 'OPTION_PANE': <Role.OPTION_PANE: 35>, 'PAGE_TAB': <Role.PAGE_TAB: 36>, 'PAGE_TAB_LIST': <Role.PAGE_TAB_LIST: 37>, 'PANEL': <Role.PANEL: 38>, 'PASSWORD_TEXT': <Role.PASSWORD_TEXT: 39>, 'POPUP_MENU': <Role.POPUP_MENU: 40>, 'PROGRESS_BAR': <Role.PROGRESS_BAR: 41>, 'BUTTON': <Role.BUTTON: 42>, 'RADIO_BUTTON': <Role.RADIO_BUTTON: 43>, 'RADIO_MENU_ITEM': <Role.RADIO_MENU_ITEM: 44>, 'ROOT_PANE': <Role.ROOT_PANE: 45>, 'ROW_HEADER': <Role.ROW_HEADER: 46>, 'SCROLL_BAR': <Role.SCROLL_BAR: 47>, 'SCROLL_PANE': <Role.SCROLL_PANE: 48>, 'SEPARATOR': <Role.SEPARATOR: 49>, 'SLIDER': <Role.SLIDER: 50>, 'SPLIT_PANE': <Role.SPLIT_PANE: 51>, 'SPIN_BUTTON': <Role.SPIN_BUTTON: 52>, 'STATUSBAR': <Role.STATUSBAR: 53>, 'TABLE': <Role.TABLE: 54>, 'TABLE_CELL': <Role.TABLE_CELL: 55>, 'TABLE_COLUMN_HEADER': <Role.TABLE_COLUMN_HEADER: 56>, 'TABLE_ROW_HEADER': <Role.TABLE_ROW_HEADER: 57>, 'TEAR_OFF_MENU_ITEM': <Role.TEAR_OFF_MENU_ITEM: 58>, 'TERMINAL': <Role.TERMINAL: 59>, 'TEXT': <Role.TEXT: 60>, 'TOGGLE_BUTTON': <Role.TOGGLE_BUTTON: 61>, 'TOOL_BAR': <Role.TOOL_BAR: 62>, 'TOOL_TIP': <Role.TOOL_TIP: 63>, 'TREE': <Role.TREE: 64>, 'TREE_TABLE': <Role.TREE_TABLE: 65>, 'UNKNOWN': <Role.UNKNOWN: 66>, 'VIEWPORT': <Role.VIEWPORT: 67>, 'WINDOW': <Role.WINDOW: 68>, 'HEADER': <Role.HEADER: 69>, 'FOOTER': <Role.FOOTER: 70>, 'PARAGRAPH': <Role.PARAGRAPH: 71>, 'RULER': <Role.RULER: 72>, 'APPLICATION': <Role.APPLICATION: 73>, 'AUTOCOMPLETE': <Role.AUTOCOMPLETE: 74>, 'EDIT_BAR': <Role.EDIT_BAR: 75>, 'EMBEDDED': <Role.EMBEDDED: 76>, 'ENTRY': <Role.ENTRY: 77>, 'CHART': <Role.CHART: 78>, 'CAPTION': <Role.CAPTION: 79>, 'DOCUMENT_FRAME': <Role.DOCUMENT_FRAME: 80>, 'HEADING': <Role.HEADING: 81>, 'PAGE': <Role.PAGE: 82>, 'SECTION': <Role.SECTION: 83>, 'REDUNDANT_OBJECT': <Role.REDUNDANT_OBJECT: 84>, 'FORM': <Role.FORM: 85>, 'LINK': <Role.LINK: 86>, 'INPUT_METHOD_WINDOW': <Role.INPUT_METHOD_WINDOW: 87>, 'TABLE_ROW': <Role.TABLE_ROW: 88>, 'TREE_ITEM': <Role.TREE_ITEM: 89>, 'DOCUMENT_SPREADSHEET': <Role.DOCUMENT_SPREADSHEET: 90>, 'DOCUMENT_PRESENTATION': <Role.DOCUMENT_PRESENTATION: 91>, 'DOCUMENT_TEXT': <Role.DOCUMENT_TEXT: 92>, 'DOCUMENT_WEB': <Role.DOCUMENT_WEB: 93>, 'DOCUMENT_EMAIL': <Role.DOCUMENT_EMAIL: 94>, 'COMMENT': <Role.COMMENT: 95>, 'LIST_BOX': <Role.LIST_BOX: 96>, 'GROUPING': <Role.GROUPING: 97>, 'IMAGE_MAP': <Role.IMAGE_MAP: 98>, 'NOTIFICATION': <Role.NOTIFICATION: 99>, 'INFO_BAR': <Role.INFO_BAR: 100>, 'LEVEL_BAR': <Role.LEVEL_BAR: 101>, 'TITLE_BAR': <Role.TITLE_BAR: 102>, 'BLOCK_QUOTE': <Role.BLOCK_QUOTE: 103>, 'AUDIO': <Role.AUDIO: 104>, 'VIDEO': <Role.VIDEO: 105>, 'DEFINITION': <Role.DEFINITION: 106>, 'ARTICLE': <Role.ARTICLE: 107>, 'LANDMARK': <Role.LANDMARK: 108>, 'LOG': <Role.LOG: 109>, 'MARQUEE': <Role.MARQUEE: 110>, 'MATH': <Role.MATH: 111>, 'RATING': <Role.RATING: 112>, 'TIMER': <Role.TIMER: 113>, 'DESCRIPTION_LIST': <Role.DESCRIPTION_LIST: 114>, 'DESCRIPTION_TERM': <Role.DESCRIPTION_TERM: 115>, 'DESCRIPTION_VALUE': <Role.DESCRIPTION_VALUE: 116>, 'STATIC': <Role.STATIC: 117>, 'MATH_FRACTION': <Role.MATH_FRACTION: 118>, 'MATH_ROOT': <Role.MATH_ROOT: 119>, 'SUBSCRIPT': <Role.SUBSCRIPT: 120>, 'SUPERSCRIPT': <Role.SUPERSCRIPT: 121>, 'FOOTNOTE': <Role.FOOTNOTE: 122>, 'CONTENT_DELETION': <Role.CONTENT_DELETION: 123>, 'CONTENT_INSERTION': <Role.CONTENT_INSERTION: 124>, 'MARK': <Role.MARK: 125>, 'SUGGESTION': <Role.SUGGESTION: 126>, 'PUSH_BUTTON_MENU': <Role.PUSH_BUTTON_MENU: 127>, 'SWITCH': <Role.SWITCH: 128>, 'LAST_DEFINED': <Role.LAST_DEFINED: 129>, 'PUSH_BUTTON': <Role.BUTTON: 42>})"
    __name__ = 'Role'
    __qualname__ = 'Role'


