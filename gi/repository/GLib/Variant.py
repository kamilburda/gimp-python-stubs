# encoding: utf-8
# module gi.repository.GLib
# by generator 1.147
# no doc

# imports
from gi._gi import Pid, spawn_async

from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GLib as __gi_overrides_GLib
import gi._gi as __gi__gi


from .Variant import Variant

class Variant(Variant):
    """
    :Constructors:
    
    ::
    
        new_array(child_type:GLib.VariantType=None, children:list=None) -> GLib.Variant
        new_boolean(value:bool) -> GLib.Variant
        new_byte(value:int) -> GLib.Variant
        new_bytestring(string:list) -> GLib.Variant
        new_bytestring_array(strv:list) -> GLib.Variant
        new_dict_entry(key:GLib.Variant, value:GLib.Variant) -> GLib.Variant
        new_double(value:float) -> GLib.Variant
        new_fixed_array(element_type:GLib.VariantType, elements=None, n_elements:int, element_size:int) -> GLib.Variant
        new_from_bytes(type:GLib.VariantType, bytes:GLib.Bytes, trusted:bool) -> GLib.Variant
        new_from_data(type:GLib.VariantType, data:list, trusted:bool, notify:GLib.DestroyNotify, user_data=None) -> GLib.Variant
        new_handle(value:int) -> GLib.Variant
        new_int16(value:int) -> GLib.Variant
        new_int32(value:int) -> GLib.Variant
        new_int64(value:int) -> GLib.Variant
        new_maybe(child_type:GLib.VariantType=None, child:GLib.Variant=None) -> GLib.Variant
        new_object_path(object_path:str) -> GLib.Variant
        new_objv(strv:list) -> GLib.Variant
        new_signature(signature:str) -> GLib.Variant
        new_string(string:str) -> GLib.Variant
        new_strv(strv:list) -> GLib.Variant
        new_tuple(children:list) -> GLib.Variant
        new_uint16(value:int) -> GLib.Variant
        new_uint32(value:int) -> GLib.Variant
        new_uint64(value:int) -> GLib.Variant
        new_variant(value:GLib.Variant) -> GLib.Variant
    """
    def byteswap(self): # real signature unknown; restored from __doc__
        """ byteswap(self) -> GLib.Variant """
        pass

    def check_format_string(self, format_string, copy_only): # real signature unknown; restored from __doc__
        """ check_format_string(self, format_string:str, copy_only:bool) -> bool """
        return False

    def classify(self): # real signature unknown; restored from __doc__
        """ classify(self) -> GLib.VariantClass """
        pass

    def compare(self, two): # real signature unknown; restored from __doc__
        """ compare(self, two:GLib.Variant) -> int """
        return 0

    def dup_bytestring(self): # real signature unknown; restored from __doc__
        """ dup_bytestring(self) -> list """
        return []

    def dup_bytestring_array(self): # real signature unknown; restored from __doc__
        """ dup_bytestring_array(self) -> list """
        return []

    def dup_objv(self): # real signature unknown; restored from __doc__
        """ dup_objv(self) -> list """
        return []

    def dup_string(self): # real signature unknown; restored from __doc__
        """ dup_string(self) -> str, length:int """
        return ""

    def dup_strv(self): # real signature unknown; restored from __doc__
        """ dup_strv(self) -> list """
        return []

    def equal(self, two): # real signature unknown; restored from __doc__
        """ equal(self, two:GLib.Variant) -> bool """
        return False

    def get_boolean(self): # real signature unknown; restored from __doc__
        """ get_boolean(self) -> bool """
        return False

    def get_byte(self): # real signature unknown; restored from __doc__
        """ get_byte(self) -> int """
        return 0

    def get_bytestring(self): # real signature unknown; restored from __doc__
        """ get_bytestring(self) -> list """
        return []

    def get_bytestring_array(self): # real signature unknown; restored from __doc__
        """ get_bytestring_array(self) -> list """
        return []

    def get_child_value(self, index_): # real signature unknown; restored from __doc__
        """ get_child_value(self, index_:int) -> GLib.Variant """
        pass

    def get_data(self): # real signature unknown; restored from __doc__
        """ get_data(self) """
        pass

    def get_data_as_bytes(self): # real signature unknown; restored from __doc__
        """ get_data_as_bytes(self) -> GLib.Bytes """
        pass

    def get_double(self): # real signature unknown; restored from __doc__
        """ get_double(self) -> float """
        return 0.0

    def get_handle(self): # real signature unknown; restored from __doc__
        """ get_handle(self) -> int """
        return 0

    def get_int16(self): # real signature unknown; restored from __doc__
        """ get_int16(self) -> int """
        return 0

    def get_int32(self): # real signature unknown; restored from __doc__
        """ get_int32(self) -> int """
        return 0

    def get_int64(self): # real signature unknown; restored from __doc__
        """ get_int64(self) -> int """
        return 0

    def get_maybe(self): # real signature unknown; restored from __doc__
        """ get_maybe(self) -> GLib.Variant or None """
        pass

    def get_normal_form(self): # real signature unknown; restored from __doc__
        """ get_normal_form(self) -> GLib.Variant """
        pass

    def get_objv(self): # real signature unknown; restored from __doc__
        """ get_objv(self) -> list """
        return []

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_string(self): # reliably restored by inspect
        # no doc
        pass

    def get_strv(self): # real signature unknown; restored from __doc__
        """ get_strv(self) -> list """
        return []

    def get_type(self): # real signature unknown; restored from __doc__
        """ get_type(self) -> GLib.VariantType """
        pass

    def get_type_string(self): # real signature unknown; restored from __doc__
        """ get_type_string(self) -> str """
        return ""

    def get_uint16(self): # real signature unknown; restored from __doc__
        """ get_uint16(self) -> int """
        return 0

    def get_uint32(self): # real signature unknown; restored from __doc__
        """ get_uint32(self) -> int """
        return 0

    def get_uint64(self): # real signature unknown; restored from __doc__
        """ get_uint64(self) -> int """
        return 0

    def get_variant(self): # real signature unknown; restored from __doc__
        """ get_variant(self) -> GLib.Variant """
        pass

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def is_container(self): # real signature unknown; restored from __doc__
        """ is_container(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_normal_form(self): # real signature unknown; restored from __doc__
        """ is_normal_form(self) -> bool """
        return False

    def is_object_path(self, string): # real signature unknown; restored from __doc__
        """ is_object_path(string:str) -> bool """
        return False

    def is_of_type(self, type): # real signature unknown; restored from __doc__
        """ is_of_type(self, type:GLib.VariantType) -> bool """
        return False

    def is_signature(self, string): # real signature unknown; restored from __doc__
        """ is_signature(string:str) -> bool """
        return False

    def keys(self): # reliably restored by inspect
        # no doc
        pass

    def lookup_value(self, key, expected_type=None): # real signature unknown; restored from __doc__
        """ lookup_value(self, key:str, expected_type:GLib.VariantType=None) -> GLib.Variant """
        pass

    def new_array(self, child_type=None, children=None): # real signature unknown; restored from __doc__
        """ new_array(child_type:GLib.VariantType=None, children:list=None) -> GLib.Variant """
        pass

    def new_boolean(self, value): # real signature unknown; restored from __doc__
        """ new_boolean(value:bool) -> GLib.Variant """
        pass

    def new_byte(self, value): # real signature unknown; restored from __doc__
        """ new_byte(value:int) -> GLib.Variant """
        pass

    def new_bytestring(self, string): # real signature unknown; restored from __doc__
        """ new_bytestring(string:list) -> GLib.Variant """
        pass

    def new_bytestring_array(self, strv): # real signature unknown; restored from __doc__
        """ new_bytestring_array(strv:list) -> GLib.Variant """
        pass

    def new_dict_entry(self, key, value): # real signature unknown; restored from __doc__
        """ new_dict_entry(key:GLib.Variant, value:GLib.Variant) -> GLib.Variant """
        pass

    def new_double(self, value): # real signature unknown; restored from __doc__
        """ new_double(value:float) -> GLib.Variant """
        pass

    def new_fixed_array(self, element_type, elements=None, n_elements, element_size): # real signature unknown; restored from __doc__
        """ new_fixed_array(element_type:GLib.VariantType, elements=None, n_elements:int, element_size:int) -> GLib.Variant """
        pass

    def new_from_bytes(self, type, bytes, trusted): # real signature unknown; restored from __doc__
        """ new_from_bytes(type:GLib.VariantType, bytes:GLib.Bytes, trusted:bool) -> GLib.Variant """
        pass

    def new_from_data(self, type, data, trusted, notify, user_data=None): # real signature unknown; restored from __doc__
        """ new_from_data(type:GLib.VariantType, data:list, trusted:bool, notify:GLib.DestroyNotify, user_data=None) -> GLib.Variant """
        pass

    def new_handle(self, value): # real signature unknown; restored from __doc__
        """ new_handle(value:int) -> GLib.Variant """
        pass

    def new_int16(self, value): # real signature unknown; restored from __doc__
        """ new_int16(value:int) -> GLib.Variant """
        pass

    def new_int32(self, value): # real signature unknown; restored from __doc__
        """ new_int32(value:int) -> GLib.Variant """
        pass

    def new_int64(self, value): # real signature unknown; restored from __doc__
        """ new_int64(value:int) -> GLib.Variant """
        pass

    def new_maybe(self, child_type=None, child=None): # real signature unknown; restored from __doc__
        """ new_maybe(child_type:GLib.VariantType=None, child:GLib.Variant=None) -> GLib.Variant """
        pass

    def new_object_path(self, object_path): # real signature unknown; restored from __doc__
        """ new_object_path(object_path:str) -> GLib.Variant """
        pass

    def new_objv(self, strv): # real signature unknown; restored from __doc__
        """ new_objv(strv:list) -> GLib.Variant """
        pass

    def new_signature(self, signature): # real signature unknown; restored from __doc__
        """ new_signature(signature:str) -> GLib.Variant """
        pass

    def new_string(self, string): # real signature unknown; restored from __doc__
        """ new_string(string:str) -> GLib.Variant """
        pass

    def new_strv(self, strv): # real signature unknown; restored from __doc__
        """ new_strv(strv:list) -> GLib.Variant """
        pass

    def new_tuple(*elements): # reliably restored by inspect
        # no doc
        pass

    def new_uint16(self, value): # real signature unknown; restored from __doc__
        """ new_uint16(value:int) -> GLib.Variant """
        pass

    def new_uint32(self, value): # real signature unknown; restored from __doc__
        """ new_uint32(value:int) -> GLib.Variant """
        pass

    def new_uint64(self, value): # real signature unknown; restored from __doc__
        """ new_uint64(value:int) -> GLib.Variant """
        pass

    def new_variant(self, value): # real signature unknown; restored from __doc__
        """ new_variant(value:GLib.Variant) -> GLib.Variant """
        pass

    def n_children(self): # real signature unknown; restored from __doc__
        """ n_children(self) -> int """
        return 0

    def parse(self, type=None, text, limit=None, endptr=None): # real signature unknown; restored from __doc__
        """ parse(type:GLib.VariantType=None, text:str, limit:str=None, endptr:str=None) -> GLib.Variant """
        pass

    def parser_get_error_quark(self): # real signature unknown; restored from __doc__
        """ parser_get_error_quark() -> int """
        return 0

    def parse_error_print_context(self, error, source_str): # real signature unknown; restored from __doc__
        """ parse_error_print_context(error:error, source_str:str) -> str """
        return ""

    def parse_error_quark(self): # real signature unknown; restored from __doc__
        """ parse_error_quark() -> int """
        return 0

    def print_(self, type_annotate): # real signature unknown; restored from __doc__
        """ print_(self, type_annotate:bool) -> str """
        return ""

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.Variant """
        pass

    def ref_sink(self): # real signature unknown; restored from __doc__
        """ ref_sink(self) -> GLib.Variant """
        pass

    @classmethod
    def split_signature(cls, *args, **kwargs): # real signature unknown
        """
        Return a list of the element signatures of the topmost signature tuple.
        
        If the signature is not a tuple, it returns one element with the entire
        signature. If the signature is an empty tuple, the result is [].
        
        This is useful for e. g. iterating over method parameters which are
        passed as a single Variant.
        """
        pass

    def store(self, data): # real signature unknown; restored from __doc__
        """ store(self, data) """
        pass

    def take_ref(self): # real signature unknown; restored from __doc__
        """ take_ref(self) -> GLib.Variant """
        pass

    def unpack(self): # reliably restored by inspect
        """ Decompose a GVariant into a native Python object. """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def __bool__(self): # reliably restored by inspect
        # no doc
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __del__(self): # reliably restored by inspect
        # no doc
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
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

    def __getitem__(self, key): # reliably restored by inspect
        # no doc
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

    def __hash__(self): # reliably restored by inspect
        # no doc
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

    def __len__(self): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(cls, format_string, value): # reliably restored by inspect
        """
        Create a GVariant from a native Python object.
        
        format_string is a standard GVariant type signature, value is a Python
        object whose structure has to match the signature.
        
        Examples:
          GLib.Variant('i', 1)
          GLib.Variant('(is)', (1, 'hello'))
          GLib.Variant('(asa{sv})', ([], {'foo': GLib.Variant('b', True),
                                          'bar': GLib.Variant('i', 2)}))
        """
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __nonzero__(self): # reliably restored by inspect
        # no doc
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.GLib', '__firstlineno__': 187, '__new__': <staticmethod(<function Variant.__new__ at 0x0000018e9fdc35e0>)>, 'new_tuple': <staticmethod(<function Variant.new_tuple at 0x0000018e9fdc3740>)>, '__del__': <function Variant.__del__ at 0x0000018e9fdc37f0>, '__str__': <function Variant.__str__ at 0x0000018e9fdc3950>, '__repr__': <function Variant.__repr__ at 0x0000018e9fdc3ab0>, '__eq__': <function Variant.__eq__ at 0x0000018e9fdc3c10>, '__ne__': <function Variant.__ne__ at 0x0000018e9fdc3d70>, '__hash__': <function Variant.__hash__ at 0x0000018e9fdc3ed0>, 'unpack': <function Variant.unpack at 0x0000018e9fee80f0>, 'split_signature': <classmethod(<function Variant.split_signature at 0x0000018e9fee81a0>)>, '__len__': <function Variant.__len__ at 0x0000018e9fee8300>, '__getitem__': <function Variant.__getitem__ at 0x0000018e9fee8460>, '__nonzero__': <function Variant.__nonzero__ at 0x0000018e9fee8510>, '__bool__': <function Variant.__bool__ at 0x0000018e9fee8670>, 'keys': <function Variant.keys at 0x0000018e9fee87d0>, 'get_string': <function Variant.get_string at 0x0000018e9fee8930>, '__static_attributes__': (), '__doc__': None})"
    __firstlineno__ = 187
    __gtype__ = None # (!) real value is '<GType GVariant (84)>'
    __info__ = StructInfo(Variant)
    __static_attributes__ = ()


