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


class CellAccessibleParent(__gobject.GInterface):
    # no doc
    def activate(self, cell): # real signature unknown; restored from __doc__
        """ activate(self, cell:Gtk.CellAccessible) """
        pass

    def edit(self, cell): # real signature unknown; restored from __doc__
        """ edit(self, cell:Gtk.CellAccessible) """
        pass

    def expand_collapse(self, cell): # real signature unknown; restored from __doc__
        """ expand_collapse(self, cell:Gtk.CellAccessible) """
        pass

    def get_cell_area(self, cell): # real signature unknown; restored from __doc__
        """ get_cell_area(self, cell:Gtk.CellAccessible) -> cell_rect:Gdk.Rectangle """
        pass

    def get_cell_extents(self, cell, coord_type): # real signature unknown; restored from __doc__
        """ get_cell_extents(self, cell:Gtk.CellAccessible, coord_type:Atk.CoordType) -> x:int, y:int, width:int, height:int """
        pass

    def get_cell_position(self, cell): # real signature unknown; restored from __doc__
        """ get_cell_position(self, cell:Gtk.CellAccessible) -> row:int, column:int """
        pass

    def get_child_index(self, cell): # real signature unknown; restored from __doc__
        """ get_child_index(self, cell:Gtk.CellAccessible) -> int """
        return 0

    def get_column_header_cells(self, cell): # real signature unknown; restored from __doc__
        """ get_column_header_cells(self, cell:Gtk.CellAccessible) -> list """
        return []

    def get_renderer_state(self, cell): # real signature unknown; restored from __doc__
        """ get_renderer_state(self, cell:Gtk.CellAccessible) -> Gtk.CellRendererState """
        pass

    def get_row_header_cells(self, cell): # real signature unknown; restored from __doc__
        """ get_row_header_cells(self, cell:Gtk.CellAccessible) -> list """
        return []

    def grab_focus(self, cell): # real signature unknown; restored from __doc__
        """ grab_focus(self, cell:Gtk.CellAccessible) -> bool """
        return False

    def update_relationset(self, cell, relationset): # real signature unknown; restored from __doc__
        """ update_relationset(self, cell:Gtk.CellAccessible, relationset:Atk.RelationSet) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(CellAccessibleParent), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkCellAccessibleParent (3418538144)>, '__dict__': <attribute '__dict__' of 'CellAccessibleParent' objects>, '__weakref__': <attribute '__weakref__' of 'CellAccessibleParent' objects>, '__doc__': None, '__gsignals__': {}, 'activate': gi.FunctionInfo(activate), 'edit': gi.FunctionInfo(edit), 'expand_collapse': gi.FunctionInfo(expand_collapse), 'get_cell_area': gi.FunctionInfo(get_cell_area), 'get_cell_extents': gi.FunctionInfo(get_cell_extents), 'get_cell_position': gi.FunctionInfo(get_cell_position), 'get_child_index': gi.FunctionInfo(get_child_index), 'get_column_header_cells': gi.FunctionInfo(get_column_header_cells), 'get_renderer_state': gi.FunctionInfo(get_renderer_state), 'get_row_header_cells': gi.FunctionInfo(get_row_header_cells), 'grab_focus': gi.FunctionInfo(grab_focus), 'update_relationset': gi.FunctionInfo(update_relationset)})"
    __gdoc__ = 'Interface GtkCellAccessibleParent\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkCellAccessibleParent (3418538144)>'
    __info__ = InterfaceInfo(CellAccessibleParent)


