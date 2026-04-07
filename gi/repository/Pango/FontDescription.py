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


from .FontDescription import FontDescription

class FontDescription(FontDescription):
    """
    :Constructors:
    
    ::
    
        new() -> Pango.FontDescription
    """
    def better_match(self, old_match=None, new_match): # real signature unknown; restored from __doc__
        """ better_match(self, old_match:Pango.FontDescription=None, new_match:Pango.FontDescription) -> bool """
        return False

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Pango.FontDescription or None """
        pass

    def copy_static(self): # real signature unknown; restored from __doc__
        """ copy_static(self) -> Pango.FontDescription or None """
        pass

    def equal(self, desc2): # real signature unknown; restored from __doc__
        """ equal(self, desc2:Pango.FontDescription) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def from_string(self, p_str): # real signature unknown; restored from __doc__
        """ from_string(str:str) -> Pango.FontDescription """
        pass

    def get_family(self): # real signature unknown; restored from __doc__
        """ get_family(self) -> str or None """
        return ""

    def get_features(self): # real signature unknown; restored from __doc__
        """ get_features(self) -> str or None """
        return ""

    def get_gravity(self): # real signature unknown; restored from __doc__
        """ get_gravity(self) -> Pango.Gravity """
        pass

    def get_set_fields(self): # real signature unknown; restored from __doc__
        """ get_set_fields(self) -> Pango.FontMask """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_size_is_absolute(self): # real signature unknown; restored from __doc__
        """ get_size_is_absolute(self) -> bool """
        return False

    def get_stretch(self): # real signature unknown; restored from __doc__
        """ get_stretch(self) -> Pango.Stretch """
        pass

    def get_style(self): # real signature unknown; restored from __doc__
        """ get_style(self) -> Pango.Style """
        pass

    def get_variant(self): # real signature unknown; restored from __doc__
        """ get_variant(self) -> Pango.Variant """
        pass

    def get_variations(self): # real signature unknown; restored from __doc__
        """ get_variations(self) -> str or None """
        return ""

    def get_weight(self): # real signature unknown; restored from __doc__
        """ get_weight(self) -> Pango.Weight """
        pass

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def merge(self, desc_to_merge=None, replace_existing): # real signature unknown; restored from __doc__
        """ merge(self, desc_to_merge:Pango.FontDescription=None, replace_existing:bool) """
        pass

    def merge_static(self, desc_to_merge, replace_existing): # real signature unknown; restored from __doc__
        """ merge_static(self, desc_to_merge:Pango.FontDescription, replace_existing:bool) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Pango.FontDescription """
        pass

    def set_absolute_size(self, size): # real signature unknown; restored from __doc__
        """ set_absolute_size(self, size:float) """
        pass

    def set_family(self, family): # real signature unknown; restored from __doc__
        """ set_family(self, family:str) """
        pass

    def set_family_static(self, family): # real signature unknown; restored from __doc__
        """ set_family_static(self, family:str) """
        pass

    def set_features(self, features=None): # real signature unknown; restored from __doc__
        """ set_features(self, features:str=None) """
        pass

    def set_features_static(self, features): # real signature unknown; restored from __doc__
        """ set_features_static(self, features:str) """
        pass

    def set_gravity(self, gravity): # real signature unknown; restored from __doc__
        """ set_gravity(self, gravity:Pango.Gravity) """
        pass

    def set_size(self, size): # real signature unknown; restored from __doc__
        """ set_size(self, size:int) """
        pass

    def set_stretch(self, stretch): # real signature unknown; restored from __doc__
        """ set_stretch(self, stretch:Pango.Stretch) """
        pass

    def set_style(self, style): # real signature unknown; restored from __doc__
        """ set_style(self, style:Pango.Style) """
        pass

    def set_variant(self, variant): # real signature unknown; restored from __doc__
        """ set_variant(self, variant:Pango.Variant) """
        pass

    def set_variations(self, variations=None): # real signature unknown; restored from __doc__
        """ set_variations(self, variations:str=None) """
        pass

    def set_variations_static(self, variations): # real signature unknown; restored from __doc__
        """ set_variations_static(self, variations:str) """
        pass

    def set_weight(self, weight): # real signature unknown; restored from __doc__
        """ set_weight(self, weight:Pango.Weight) """
        pass

    def to_filename(self): # real signature unknown; restored from __doc__
        """ to_filename(self) -> str or None """
        return ""

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def unset_fields(self, to_unset): # real signature unknown; restored from __doc__
        """ unset_fields(self, to_unset:Pango.FontMask) """
        pass

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
    def __new__(cls, string=None): # reliably restored by inspect
        # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Pango', '__firstlineno__': 44, '__new__': <staticmethod(<function FontDescription.__new__ at 0x0000028035132980>)>, '__static_attributes__': (), '__doc__': None})"
    __firstlineno__ = 44
    __gtype__ = None # (!) real value is '<GType PangoFontDescription (842606336)>'
    __info__ = StructInfo(FontDescription)
    __static_attributes__ = ()


