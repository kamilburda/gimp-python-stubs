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


class ContainerClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ContainerClass()
    """
    def find_child_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_child_property(self, property_name:str) -> GObject.ParamSpec or None """
        pass

    def handle_border_width(self): # real signature unknown; restored from __doc__
        """ handle_border_width(self) """
        pass

    def install_child_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_child_properties(self, pspecs:list) """
        pass

    def install_child_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_child_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def list_child_properties(self): # real signature unknown; restored from __doc__
        """ list_child_properties(self) -> list """
        return []

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

    add = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    check_resize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    child_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    composite_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forall = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_child_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_path_for_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_child_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_focus_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _handle_border_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ContainerClass), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ContainerClass' objects>, '__weakref__': <attribute '__weakref__' of 'ContainerClass' objects>, '__doc__': None, 'parent_class': <property object at 0x000002bfd1776200>, 'add': <property object at 0x000002bfd17762f0>, 'remove': <property object at 0x000002bfd17763e0>, 'check_resize': <property object at 0x000002bfd17764d0>, 'forall': <property object at 0x000002bfd17765c0>, 'set_focus_child': <property object at 0x000002bfd17766b0>, 'child_type': <property object at 0x000002bfd17767a0>, 'composite_name': <property object at 0x000002bfd1776890>, 'set_child_property': <property object at 0x000002bfd1776980>, 'get_child_property': <property object at 0x000002bfd1776a70>, 'get_path_for_child': <property object at 0x000002bfd1776b60>, '_handle_border_width': <property object at 0x000002bfd1776c50>, '_gtk_reserved1': <property object at 0x000002bfd1776d40>, '_gtk_reserved2': <property object at 0x000002bfd1776e30>, '_gtk_reserved3': <property object at 0x000002bfd1776f20>, '_gtk_reserved4': <property object at 0x000002bfd1777010>, '_gtk_reserved5': <property object at 0x000002bfd1777100>, '_gtk_reserved6': <property object at 0x000002bfd17771f0>, '_gtk_reserved7': <property object at 0x000002bfd17772e0>, '_gtk_reserved8': <property object at 0x000002bfd17773d0>, 'find_child_property': gi.FunctionInfo(find_child_property), 'handle_border_width': gi.FunctionInfo(handle_border_width), 'install_child_properties': gi.FunctionInfo(install_child_properties), 'install_child_property': gi.FunctionInfo(install_child_property), 'list_child_properties': gi.FunctionInfo(list_child_properties)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ContainerClass)


