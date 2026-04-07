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


class Text(__gobject.GInterface):
    # no doc
    def add_selection(self, start_offset, end_offset): # real signature unknown; restored from __doc__
        """ add_selection(self, start_offset:int, end_offset:int) -> bool """
        return False

    def free_ranges(self, ranges): # real signature unknown; restored from __doc__
        """ free_ranges(ranges:list) """
        pass

    def get_bounded_ranges(self, rect, coord_type, x_clip_type, y_clip_type): # real signature unknown; restored from __doc__
        """ get_bounded_ranges(self, rect:Atk.TextRectangle, coord_type:Atk.CoordType, x_clip_type:Atk.TextClipType, y_clip_type:Atk.TextClipType) -> list """
        return []

    def get_caret_offset(self): # real signature unknown; restored from __doc__
        """ get_caret_offset(self) -> int """
        return 0

    def get_character_at_offset(self, offset): # real signature unknown; restored from __doc__
        """ get_character_at_offset(self, offset:int) -> str """
        return ""

    def get_character_count(self): # real signature unknown; restored from __doc__
        """ get_character_count(self) -> int """
        return 0

    def get_character_extents(self, offset, coords): # real signature unknown; restored from __doc__
        """ get_character_extents(self, offset:int, coords:Atk.CoordType) -> x:int, y:int, width:int, height:int """
        pass

    def get_default_attributes(self): # real signature unknown; restored from __doc__
        """ get_default_attributes(self) -> list """
        return []

    def get_n_selections(self): # real signature unknown; restored from __doc__
        """ get_n_selections(self) -> int """
        return 0

    def get_offset_at_point(self, x, y, coords): # real signature unknown; restored from __doc__
        """ get_offset_at_point(self, x:int, y:int, coords:Atk.CoordType) -> int """
        return 0

    def get_range_extents(self, start_offset, end_offset, coord_type): # real signature unknown; restored from __doc__
        """ get_range_extents(self, start_offset:int, end_offset:int, coord_type:Atk.CoordType) -> rect:Atk.TextRectangle """
        pass

    def get_run_attributes(self, offset): # real signature unknown; restored from __doc__
        """ get_run_attributes(self, offset:int) -> list, start_offset:int, end_offset:int """
        return []

    def get_selection(self, selection_num): # real signature unknown; restored from __doc__
        """ get_selection(self, selection_num:int) -> str, start_offset:int, end_offset:int """
        return ""

    def get_string_at_offset(self, offset, granularity): # real signature unknown; restored from __doc__
        """ get_string_at_offset(self, offset:int, granularity:Atk.TextGranularity) -> str or None, start_offset:int, end_offset:int """
        return ""

    def get_text(self, start_offset, end_offset): # real signature unknown; restored from __doc__
        """ get_text(self, start_offset:int, end_offset:int) -> str """
        return ""

    def get_text_after_offset(self, offset, boundary_type): # real signature unknown; restored from __doc__
        """ get_text_after_offset(self, offset:int, boundary_type:Atk.TextBoundary) -> str, start_offset:int, end_offset:int """
        return ""

    def get_text_at_offset(self, offset, boundary_type): # real signature unknown; restored from __doc__
        """ get_text_at_offset(self, offset:int, boundary_type:Atk.TextBoundary) -> str, start_offset:int, end_offset:int """
        return ""

    def get_text_before_offset(self, offset, boundary_type): # real signature unknown; restored from __doc__
        """ get_text_before_offset(self, offset:int, boundary_type:Atk.TextBoundary) -> str, start_offset:int, end_offset:int """
        return ""

    def remove_selection(self, selection_num): # real signature unknown; restored from __doc__
        """ remove_selection(self, selection_num:int) -> bool """
        return False

    def scroll_substring_to(self, start_offset, end_offset, type): # real signature unknown; restored from __doc__
        """ scroll_substring_to(self, start_offset:int, end_offset:int, type:Atk.ScrollType) -> bool """
        return False

    def scroll_substring_to_point(self, start_offset, end_offset, coords, x, y): # real signature unknown; restored from __doc__
        """ scroll_substring_to_point(self, start_offset:int, end_offset:int, coords:Atk.CoordType, x:int, y:int) -> bool """
        return False

    def set_caret_offset(self, offset): # real signature unknown; restored from __doc__
        """ set_caret_offset(self, offset:int) -> bool """
        return False

    def set_selection(self, selection_num, start_offset, end_offset): # real signature unknown; restored from __doc__
        """ set_selection(self, selection_num:int, start_offset:int, end_offset:int) -> bool """
        return False

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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Text), '__module__': 'gi.repository.Atk', '__gtype__': <GType AtkText (1534561440)>, '__dict__': <attribute '__dict__' of 'Text' objects>, '__weakref__': <attribute '__weakref__' of 'Text' objects>, '__doc__': None, '__gsignals__': {}, 'free_ranges': <staticmethod(gi.FunctionInfo(free_ranges))>, 'add_selection': gi.FunctionInfo(add_selection), 'get_bounded_ranges': gi.FunctionInfo(get_bounded_ranges), 'get_caret_offset': gi.FunctionInfo(get_caret_offset), 'get_character_at_offset': gi.FunctionInfo(get_character_at_offset), 'get_character_count': gi.FunctionInfo(get_character_count), 'get_character_extents': gi.FunctionInfo(get_character_extents), 'get_default_attributes': gi.FunctionInfo(get_default_attributes), 'get_n_selections': gi.FunctionInfo(get_n_selections), 'get_offset_at_point': gi.FunctionInfo(get_offset_at_point), 'get_range_extents': gi.FunctionInfo(get_range_extents), 'get_run_attributes': gi.FunctionInfo(get_run_attributes), 'get_selection': gi.FunctionInfo(get_selection), 'get_string_at_offset': gi.FunctionInfo(get_string_at_offset), 'get_text': gi.FunctionInfo(get_text), 'get_text_after_offset': gi.FunctionInfo(get_text_after_offset), 'get_text_at_offset': gi.FunctionInfo(get_text_at_offset), 'get_text_before_offset': gi.FunctionInfo(get_text_before_offset), 'remove_selection': gi.FunctionInfo(remove_selection), 'scroll_substring_to': gi.FunctionInfo(scroll_substring_to), 'scroll_substring_to_point': gi.FunctionInfo(scroll_substring_to_point), 'set_caret_offset': gi.FunctionInfo(set_caret_offset), 'set_selection': gi.FunctionInfo(set_selection)})"
    __gdoc__ = 'Interface AtkText\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AtkText (1534561440)>'
    __info__ = InterfaceInfo(Text)


