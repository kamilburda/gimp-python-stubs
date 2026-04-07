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


class TabArray(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(initial_size:int, positions_in_pixels:bool) -> Pango.TabArray
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Pango.TabArray """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def from_string(self, text): # real signature unknown; restored from __doc__
        """ from_string(text:str) -> Pango.TabArray or None """
        pass

    def get_decimal_point(self, tab_index): # real signature unknown; restored from __doc__
        """ get_decimal_point(self, tab_index:int) -> str """
        return ""

    def get_positions_in_pixels(self): # real signature unknown; restored from __doc__
        """ get_positions_in_pixels(self) -> bool """
        return False

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_tab(self, tab_index): # real signature unknown; restored from __doc__
        """ get_tab(self, tab_index:int) -> alignment:Pango.TabAlign, location:int """
        pass

    def get_tabs(self): # real signature unknown; restored from __doc__
        """ get_tabs(self) -> alignments:Pango.TabAlign, locations:list """
        pass

    @classmethod
    def new(cls, initial_size, positions_in_pixels): # real signature unknown; restored from __doc__
        """ new(initial_size:int, positions_in_pixels:bool) -> Pango.TabArray """
        pass

    def resize(self, new_size): # real signature unknown; restored from __doc__
        """ resize(self, new_size:int) """
        pass

    def set_decimal_point(self, tab_index, decimal_point): # real signature unknown; restored from __doc__
        """ set_decimal_point(self, tab_index:int, decimal_point:str) """
        pass

    def set_positions_in_pixels(self, positions_in_pixels): # real signature unknown; restored from __doc__
        """ set_positions_in_pixels(self, positions_in_pixels:bool) """
        pass

    def set_tab(self, tab_index, alignment, location): # real signature unknown; restored from __doc__
        """ set_tab(self, tab_index:int, alignment:Pango.TabAlign, location:int) """
        pass

    def sort(self): # real signature unknown; restored from __doc__
        """ sort(self) """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new(initial_size:int, positions_in_pixels:bool) -> Pango.TabArray """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TabArray), '__module__': 'gi.repository.Pango', '__gtype__': <GType PangoTabArray (843936672)>, '__dict__': <attribute '__dict__' of 'TabArray' objects>, '__weakref__': <attribute '__weakref__' of 'TabArray' objects>, '__doc__': None, 'new': <classmethod(gi.FunctionInfo(new))>, 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_decimal_point': gi.FunctionInfo(get_decimal_point), 'get_positions_in_pixels': gi.FunctionInfo(get_positions_in_pixels), 'get_size': gi.FunctionInfo(get_size), 'get_tab': gi.FunctionInfo(get_tab), 'get_tabs': gi.FunctionInfo(get_tabs), 'resize': gi.FunctionInfo(resize), 'set_decimal_point': gi.FunctionInfo(set_decimal_point), 'set_positions_in_pixels': gi.FunctionInfo(set_positions_in_pixels), 'set_tab': gi.FunctionInfo(set_tab), 'sort': gi.FunctionInfo(sort), 'to_string': gi.FunctionInfo(to_string), 'from_string': <staticmethod(gi.FunctionInfo(from_string))>, '__new__': <staticmethod(gi.FunctionInfo(new))>, '__init__': <function nothing at 0x0000028034ff1010>})"
    __gtype__ = None # (!) real value is '<GType PangoTabArray (843936672)>'
    __info__ = StructInfo(TabArray)


