# encoding: utf-8
# module gi.repository.Gtk
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


from .TextIter import TextIter

class TextIter(TextIter):
    """
    :Constructors:
    
    ::
    
        TextIter()
    """
    def assign(self, other): # real signature unknown; restored from __doc__
        """ assign(self, other:Gtk.TextIter) """
        pass

    def backward_char(self): # real signature unknown; restored from __doc__
        """ backward_char(self) -> bool """
        return False

    def backward_chars(self, count): # real signature unknown; restored from __doc__
        """ backward_chars(self, count:int) -> bool """
        return False

    def backward_cursor_position(self): # real signature unknown; restored from __doc__
        """ backward_cursor_position(self) -> bool """
        return False

    def backward_cursor_positions(self, count): # real signature unknown; restored from __doc__
        """ backward_cursor_positions(self, count:int) -> bool """
        return False

    def backward_find_char(self, pred, user_data=None, limit=None): # real signature unknown; restored from __doc__
        """ backward_find_char(self, pred:Gtk.TextCharPredicate, user_data=None, limit:Gtk.TextIter=None) -> bool """
        return False

    def backward_line(self): # real signature unknown; restored from __doc__
        """ backward_line(self) -> bool """
        return False

    def backward_lines(self, count): # real signature unknown; restored from __doc__
        """ backward_lines(self, count:int) -> bool """
        return False

    def backward_search(*args, **kwargs): # reliably restored by inspect
        """ backward_search(self, str:str, flags:Gtk.TextSearchFlags, limit:Gtk.TextIter=None) -> bool, match_start:Gtk.TextIter, match_end:Gtk.TextIter """
        pass

    def backward_sentence_start(self): # real signature unknown; restored from __doc__
        """ backward_sentence_start(self) -> bool """
        return False

    def backward_sentence_starts(self, count): # real signature unknown; restored from __doc__
        """ backward_sentence_starts(self, count:int) -> bool """
        return False

    def backward_to_tag_toggle(self, tag=None): # real signature unknown; restored from __doc__
        """ backward_to_tag_toggle(self, tag:Gtk.TextTag=None) -> bool """
        return False

    def backward_visible_cursor_position(self): # real signature unknown; restored from __doc__
        """ backward_visible_cursor_position(self) -> bool """
        return False

    def backward_visible_cursor_positions(self, count): # real signature unknown; restored from __doc__
        """ backward_visible_cursor_positions(self, count:int) -> bool """
        return False

    def backward_visible_line(self): # real signature unknown; restored from __doc__
        """ backward_visible_line(self) -> bool """
        return False

    def backward_visible_lines(self, count): # real signature unknown; restored from __doc__
        """ backward_visible_lines(self, count:int) -> bool """
        return False

    def backward_visible_word_start(self): # real signature unknown; restored from __doc__
        """ backward_visible_word_start(self) -> bool """
        return False

    def backward_visible_word_starts(self, count): # real signature unknown; restored from __doc__
        """ backward_visible_word_starts(self, count:int) -> bool """
        return False

    def backward_word_start(self): # real signature unknown; restored from __doc__
        """ backward_word_start(self) -> bool """
        return False

    def backward_word_starts(self, count): # real signature unknown; restored from __doc__
        """ backward_word_starts(self, count:int) -> bool """
        return False

    def begins_tag(self, tag=None): # real signature unknown; restored from __doc__
        """ begins_tag(self, tag:Gtk.TextTag=None) -> bool """
        return False

    def can_insert(self, default_editability): # real signature unknown; restored from __doc__
        """ can_insert(self, default_editability:bool) -> bool """
        return False

    def compare(self, rhs): # real signature unknown; restored from __doc__
        """ compare(self, rhs:Gtk.TextIter) -> int """
        return 0

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gtk.TextIter """
        pass

    def editable(self, default_setting): # real signature unknown; restored from __doc__
        """ editable(self, default_setting:bool) -> bool """
        return False

    def ends_line(self): # real signature unknown; restored from __doc__
        """ ends_line(self) -> bool """
        return False

    def ends_sentence(self): # real signature unknown; restored from __doc__
        """ ends_sentence(self) -> bool """
        return False

    def ends_tag(self, tag=None): # real signature unknown; restored from __doc__
        """ ends_tag(self, tag:Gtk.TextTag=None) -> bool """
        return False

    def ends_word(self): # real signature unknown; restored from __doc__
        """ ends_word(self) -> bool """
        return False

    def equal(self, rhs): # real signature unknown; restored from __doc__
        """ equal(self, rhs:Gtk.TextIter) -> bool """
        return False

    def forward_char(self): # real signature unknown; restored from __doc__
        """ forward_char(self) -> bool """
        return False

    def forward_chars(self, count): # real signature unknown; restored from __doc__
        """ forward_chars(self, count:int) -> bool """
        return False

    def forward_cursor_position(self): # real signature unknown; restored from __doc__
        """ forward_cursor_position(self) -> bool """
        return False

    def forward_cursor_positions(self, count): # real signature unknown; restored from __doc__
        """ forward_cursor_positions(self, count:int) -> bool """
        return False

    def forward_find_char(self, pred, user_data=None, limit=None): # real signature unknown; restored from __doc__
        """ forward_find_char(self, pred:Gtk.TextCharPredicate, user_data=None, limit:Gtk.TextIter=None) -> bool """
        return False

    def forward_line(self): # real signature unknown; restored from __doc__
        """ forward_line(self) -> bool """
        return False

    def forward_lines(self, count): # real signature unknown; restored from __doc__
        """ forward_lines(self, count:int) -> bool """
        return False

    def forward_search(*args, **kwargs): # reliably restored by inspect
        """ forward_search(self, str:str, flags:Gtk.TextSearchFlags, limit:Gtk.TextIter=None) -> bool, match_start:Gtk.TextIter, match_end:Gtk.TextIter """
        pass

    def forward_sentence_end(self): # real signature unknown; restored from __doc__
        """ forward_sentence_end(self) -> bool """
        return False

    def forward_sentence_ends(self, count): # real signature unknown; restored from __doc__
        """ forward_sentence_ends(self, count:int) -> bool """
        return False

    def forward_to_end(self): # real signature unknown; restored from __doc__
        """ forward_to_end(self) """
        pass

    def forward_to_line_end(self): # real signature unknown; restored from __doc__
        """ forward_to_line_end(self) -> bool """
        return False

    def forward_to_tag_toggle(self, tag=None): # real signature unknown; restored from __doc__
        """ forward_to_tag_toggle(self, tag:Gtk.TextTag=None) -> bool """
        return False

    def forward_visible_cursor_position(self): # real signature unknown; restored from __doc__
        """ forward_visible_cursor_position(self) -> bool """
        return False

    def forward_visible_cursor_positions(self, count): # real signature unknown; restored from __doc__
        """ forward_visible_cursor_positions(self, count:int) -> bool """
        return False

    def forward_visible_line(self): # real signature unknown; restored from __doc__
        """ forward_visible_line(self) -> bool """
        return False

    def forward_visible_lines(self, count): # real signature unknown; restored from __doc__
        """ forward_visible_lines(self, count:int) -> bool """
        return False

    def forward_visible_word_end(self): # real signature unknown; restored from __doc__
        """ forward_visible_word_end(self) -> bool """
        return False

    def forward_visible_word_ends(self, count): # real signature unknown; restored from __doc__
        """ forward_visible_word_ends(self, count:int) -> bool """
        return False

    def forward_word_end(self): # real signature unknown; restored from __doc__
        """ forward_word_end(self) -> bool """
        return False

    def forward_word_ends(self, count): # real signature unknown; restored from __doc__
        """ forward_word_ends(self, count:int) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> bool, values:Gtk.TextAttributes """
        return False

    def get_buffer(self): # real signature unknown; restored from __doc__
        """ get_buffer(self) -> Gtk.TextBuffer """
        pass

    def get_bytes_in_line(self): # real signature unknown; restored from __doc__
        """ get_bytes_in_line(self) -> int """
        return 0

    def get_char(self): # real signature unknown; restored from __doc__
        """ get_char(self) -> str """
        return ""

    def get_chars_in_line(self): # real signature unknown; restored from __doc__
        """ get_chars_in_line(self) -> int """
        return 0

    def get_child_anchor(self): # real signature unknown; restored from __doc__
        """ get_child_anchor(self) -> Gtk.TextChildAnchor """
        pass

    def get_language(self): # real signature unknown; restored from __doc__
        """ get_language(self) -> Pango.Language """
        pass

    def get_line(self): # real signature unknown; restored from __doc__
        """ get_line(self) -> int """
        return 0

    def get_line_index(self): # real signature unknown; restored from __doc__
        """ get_line_index(self) -> int """
        return 0

    def get_line_offset(self): # real signature unknown; restored from __doc__
        """ get_line_offset(self) -> int """
        return 0

    def get_marks(self): # real signature unknown; restored from __doc__
        """ get_marks(self) -> list """
        return []

    def get_offset(self): # real signature unknown; restored from __doc__
        """ get_offset(self) -> int """
        return 0

    def get_pixbuf(self): # real signature unknown; restored from __doc__
        """ get_pixbuf(self) -> GdkPixbuf.Pixbuf """
        pass

    def get_slice(self, end): # real signature unknown; restored from __doc__
        """ get_slice(self, end:Gtk.TextIter) -> str """
        return ""

    def get_tags(self): # real signature unknown; restored from __doc__
        """ get_tags(self) -> list """
        return []

    def get_text(self, end): # real signature unknown; restored from __doc__
        """ get_text(self, end:Gtk.TextIter) -> str """
        return ""

    def get_toggled_tags(self, toggled_on): # real signature unknown; restored from __doc__
        """ get_toggled_tags(self, toggled_on:bool) -> list """
        return []

    def get_visible_line_index(self): # real signature unknown; restored from __doc__
        """ get_visible_line_index(self) -> int """
        return 0

    def get_visible_line_offset(self): # real signature unknown; restored from __doc__
        """ get_visible_line_offset(self) -> int """
        return 0

    def get_visible_slice(self, end): # real signature unknown; restored from __doc__
        """ get_visible_slice(self, end:Gtk.TextIter) -> str """
        return ""

    def get_visible_text(self, end): # real signature unknown; restored from __doc__
        """ get_visible_text(self, end:Gtk.TextIter) -> str """
        return ""

    def has_tag(self, tag): # real signature unknown; restored from __doc__
        """ has_tag(self, tag:Gtk.TextTag) -> bool """
        return False

    def inside_sentence(self): # real signature unknown; restored from __doc__
        """ inside_sentence(self) -> bool """
        return False

    def inside_word(self): # real signature unknown; restored from __doc__
        """ inside_word(self) -> bool """
        return False

    def in_range(self, start, end): # real signature unknown; restored from __doc__
        """ in_range(self, start:Gtk.TextIter, end:Gtk.TextIter) -> bool """
        return False

    def is_cursor_position(self): # real signature unknown; restored from __doc__
        """ is_cursor_position(self) -> bool """
        return False

    def is_end(self): # real signature unknown; restored from __doc__
        """ is_end(self) -> bool """
        return False

    def is_start(self): # real signature unknown; restored from __doc__
        """ is_start(self) -> bool """
        return False

    def order(self, second): # real signature unknown; restored from __doc__
        """ order(self, second:Gtk.TextIter) """
        pass

    def set_line(self, line_number): # real signature unknown; restored from __doc__
        """ set_line(self, line_number:int) """
        pass

    def set_line_index(self, byte_on_line): # real signature unknown; restored from __doc__
        """ set_line_index(self, byte_on_line:int) """
        pass

    def set_line_offset(self, char_on_line): # real signature unknown; restored from __doc__
        """ set_line_offset(self, char_on_line:int) """
        pass

    def set_offset(self, char_offset): # real signature unknown; restored from __doc__
        """ set_offset(self, char_offset:int) """
        pass

    def set_visible_line_index(self, byte_on_line): # real signature unknown; restored from __doc__
        """ set_visible_line_index(self, byte_on_line:int) """
        pass

    def set_visible_line_offset(self, char_on_line): # real signature unknown; restored from __doc__
        """ set_visible_line_offset(self, char_on_line:int) """
        pass

    def starts_line(self): # real signature unknown; restored from __doc__
        """ starts_line(self) -> bool """
        return False

    def starts_sentence(self): # real signature unknown; restored from __doc__
        """ starts_sentence(self) -> bool """
        return False

    def starts_tag(self, tag=None): # real signature unknown; restored from __doc__
        """ starts_tag(self, tag:Gtk.TextTag=None) -> bool """
        return False

    def starts_word(self): # real signature unknown; restored from __doc__
        """ starts_word(self) -> bool """
        return False

    def toggles_tag(self, tag=None): # real signature unknown; restored from __doc__
        """ toggles_tag(self, tag:Gtk.TextTag=None) -> bool """
        return False

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """
        Default object formatter.
        
        Return str(self) if format_spec is empty. Raise TypeError otherwise.
        """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    dummy1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy11 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy12 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy13 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy14 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy9 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gtk', '__firstlineno__': 882, 'forward_search': <function strip_boolean_result.<locals>.wrapped at 0x000002bfcebd03b0>, 'backward_search': <function strip_boolean_result.<locals>.wrapped at 0x000002bfcebd0460>, '__static_attributes__': (), '__doc__': None})"
    __firstlineno__ = 882
    __gtype__ = None # (!) real value is '<GType GtkTextIter (3416383536)>'
    __info__ = StructInfo(TextIter)
    __static_attributes__ = ()


