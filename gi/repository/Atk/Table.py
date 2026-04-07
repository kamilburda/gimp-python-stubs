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


class Table(__gobject.GInterface):
    # no doc
    def add_column_selection(self, column): # real signature unknown; restored from __doc__
        """ add_column_selection(self, column:int) -> bool """
        return False

    def add_row_selection(self, row): # real signature unknown; restored from __doc__
        """ add_row_selection(self, row:int) -> bool """
        return False

    def get_caption(self): # real signature unknown; restored from __doc__
        """ get_caption(self) -> Atk.Object or None """
        pass

    def get_column_at_index(self, index_): # real signature unknown; restored from __doc__
        """ get_column_at_index(self, index_:int) -> int """
        return 0

    def get_column_description(self, column): # real signature unknown; restored from __doc__
        """ get_column_description(self, column:int) -> str """
        return ""

    def get_column_extent_at(self, row, column): # real signature unknown; restored from __doc__
        """ get_column_extent_at(self, row:int, column:int) -> int """
        return 0

    def get_column_header(self, column): # real signature unknown; restored from __doc__
        """ get_column_header(self, column:int) -> Atk.Object or None """
        pass

    def get_index_at(self, row, column): # real signature unknown; restored from __doc__
        """ get_index_at(self, row:int, column:int) -> int """
        return 0

    def get_n_columns(self): # real signature unknown; restored from __doc__
        """ get_n_columns(self) -> int """
        return 0

    def get_n_rows(self): # real signature unknown; restored from __doc__
        """ get_n_rows(self) -> int """
        return 0

    def get_row_at_index(self, index_): # real signature unknown; restored from __doc__
        """ get_row_at_index(self, index_:int) -> int """
        return 0

    def get_row_description(self, row): # real signature unknown; restored from __doc__
        """ get_row_description(self, row:int) -> str or None """
        return ""

    def get_row_extent_at(self, row, column): # real signature unknown; restored from __doc__
        """ get_row_extent_at(self, row:int, column:int) -> int """
        return 0

    def get_row_header(self, row): # real signature unknown; restored from __doc__
        """ get_row_header(self, row:int) -> Atk.Object or None """
        pass

    def get_selected_columns(self, selected): # real signature unknown; restored from __doc__
        """ get_selected_columns(self, selected:int) -> int """
        return 0

    def get_selected_rows(self, selected): # real signature unknown; restored from __doc__
        """ get_selected_rows(self, selected:int) -> int """
        return 0

    def get_summary(self): # real signature unknown; restored from __doc__
        """ get_summary(self) -> Atk.Object """
        pass

    def is_column_selected(self, column): # real signature unknown; restored from __doc__
        """ is_column_selected(self, column:int) -> bool """
        return False

    def is_row_selected(self, row): # real signature unknown; restored from __doc__
        """ is_row_selected(self, row:int) -> bool """
        return False

    def is_selected(self, row, column): # real signature unknown; restored from __doc__
        """ is_selected(self, row:int, column:int) -> bool """
        return False

    def ref_at(self, row, column): # real signature unknown; restored from __doc__
        """ ref_at(self, row:int, column:int) -> Atk.Object """
        pass

    def remove_column_selection(self, column): # real signature unknown; restored from __doc__
        """ remove_column_selection(self, column:int) -> bool """
        return False

    def remove_row_selection(self, row): # real signature unknown; restored from __doc__
        """ remove_row_selection(self, row:int) -> bool """
        return False

    def set_caption(self, caption): # real signature unknown; restored from __doc__
        """ set_caption(self, caption:Atk.Object) """
        pass

    def set_column_description(self, column, description): # real signature unknown; restored from __doc__
        """ set_column_description(self, column:int, description:str) """
        pass

    def set_column_header(self, column, header): # real signature unknown; restored from __doc__
        """ set_column_header(self, column:int, header:Atk.Object) """
        pass

    def set_row_description(self, row, description): # real signature unknown; restored from __doc__
        """ set_row_description(self, row:int, description:str) """
        pass

    def set_row_header(self, row, header): # real signature unknown; restored from __doc__
        """ set_row_header(self, row:int, header:Atk.Object) """
        pass

    def set_summary(self, accessible): # real signature unknown; restored from __doc__
        """ set_summary(self, accessible:Atk.Object) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Table), '__module__': 'gi.repository.Atk', '__gtype__': <GType AtkTable (1534561824)>, '__dict__': <attribute '__dict__' of 'Table' objects>, '__weakref__': <attribute '__weakref__' of 'Table' objects>, '__doc__': None, '__gsignals__': {}, 'add_column_selection': gi.FunctionInfo(add_column_selection), 'add_row_selection': gi.FunctionInfo(add_row_selection), 'get_caption': gi.FunctionInfo(get_caption), 'get_column_at_index': gi.FunctionInfo(get_column_at_index), 'get_column_description': gi.FunctionInfo(get_column_description), 'get_column_extent_at': gi.FunctionInfo(get_column_extent_at), 'get_column_header': gi.FunctionInfo(get_column_header), 'get_index_at': gi.FunctionInfo(get_index_at), 'get_n_columns': gi.FunctionInfo(get_n_columns), 'get_n_rows': gi.FunctionInfo(get_n_rows), 'get_row_at_index': gi.FunctionInfo(get_row_at_index), 'get_row_description': gi.FunctionInfo(get_row_description), 'get_row_extent_at': gi.FunctionInfo(get_row_extent_at), 'get_row_header': gi.FunctionInfo(get_row_header), 'get_selected_columns': gi.FunctionInfo(get_selected_columns), 'get_selected_rows': gi.FunctionInfo(get_selected_rows), 'get_summary': gi.FunctionInfo(get_summary), 'is_column_selected': gi.FunctionInfo(is_column_selected), 'is_row_selected': gi.FunctionInfo(is_row_selected), 'is_selected': gi.FunctionInfo(is_selected), 'ref_at': gi.FunctionInfo(ref_at), 'remove_column_selection': gi.FunctionInfo(remove_column_selection), 'remove_row_selection': gi.FunctionInfo(remove_row_selection), 'set_caption': gi.FunctionInfo(set_caption), 'set_column_description': gi.FunctionInfo(set_column_description), 'set_column_header': gi.FunctionInfo(set_column_header), 'set_row_description': gi.FunctionInfo(set_row_description), 'set_row_header': gi.FunctionInfo(set_row_header), 'set_summary': gi.FunctionInfo(set_summary)})"
    __gdoc__ = 'Interface AtkTable\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AtkTable (1534561824)>'
    __info__ = InterfaceInfo(Table)


