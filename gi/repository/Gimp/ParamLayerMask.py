# encoding: utf-8
# module gi.repository.Gimp
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GExiv2 as __gi_overrides_GExiv2
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


from .ParamChannel import ParamChannel

class ParamLayerMask(ParamChannel):
    """
    :Constructors:
    
    ::
    
        ParamLayerMask(**properties)
    """
    def blurb(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def do_finalize(self, *args, **kwargs): # real signature unknown
        """ finalize(self) """
        pass

    def do_get_property(self, pspec): # reliably restored by inspect
        # no doc
        pass

    def do_set_property(self, pspec, value): # reliably restored by inspect
        # no doc
        pass

    def do_values_cmp(self, *args, **kwargs): # real signature unknown
        """ values_cmp(self, value1:GObject.Value, value2:GObject.Value) -> int """
        pass

    def do_value_is_valid(self, *args, **kwargs): # real signature unknown
        """ value_is_valid(self, value:GObject.Value) -> bool """
        pass

    def do_value_set_default(self, *args, **kwargs): # real signature unknown
        """ value_set_default(self, value:GObject.Value) """
        pass

    def do_value_validate(self, *args, **kwargs): # real signature unknown
        """ value_validate(self, value:GObject.Value) -> bool """
        pass

    def get_blurb(self): # real signature unknown; restored from __doc__
        """ get_blurb(self) -> str or None """
        return ""

    def get_default_value(self): # real signature unknown; restored from __doc__
        """ get_default_value(self) -> GObject.Value """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_name_quark(self): # real signature unknown; restored from __doc__
        """ get_name_quark(self) -> int """
        return 0

    def get_nick(self): # real signature unknown; restored from __doc__
        """ get_nick(self) -> str """
        return ""

    def get_qdata(self, quark): # real signature unknown; restored from __doc__
        """ get_qdata(self, quark:int) """
        pass

    def get_redirect_target(self): # real signature unknown; restored from __doc__
        """ get_redirect_target(self) -> GObject.ParamSpec or None """
        pass

    def is_valid_name(self, name): # real signature unknown; restored from __doc__
        """ is_valid_name(name:str) -> bool """
        return False

    def nick(self, *args, **kwargs): # real signature unknown
        """  """
        pass

    def set_qdata(self, quark, data=None): # real signature unknown; restored from __doc__
        """ set_qdata(self, quark:int, data=None) """
        pass

    def sink(self): # real signature unknown; restored from __doc__
        """ sink(self) """
        pass

    def steal_qdata(self, quark): # real signature unknown; restored from __doc__
        """ steal_qdata(self, quark:int) """
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    owner_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    param_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _blurb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ParamLayerMask), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpParamLayerMask (2359068384)>, '__doc__': None, '__gsignals__': {}})"
    __firstlineno__ = 843
    __gproperties__ = {
        'blurb': (
            None, # (!) real value is '<GType PyObject (2352384080)>'
            '',
            '',
            3,
        ),
        'nick': '<value is a self-reference, replaced by this string>',
    }
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GimpParamLayerMask (2359068384)>'
    __info__ = ObjectInfo(ParamLayerMask)
    __static_attributes__ = (
        '_blurb',
        '_nick',
    )


