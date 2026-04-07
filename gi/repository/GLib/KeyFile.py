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


class KeyFile(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> GLib.KeyFile
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def get_boolean(self, group_name, key): # real signature unknown; restored from __doc__
        """ get_boolean(self, group_name:str, key:str) -> bool """
        return False

    def get_boolean_list(self, group_name, key): # real signature unknown; restored from __doc__
        """ get_boolean_list(self, group_name:str, key:str) -> list """
        return []

    def get_comment(self, group_name=None, key=None): # real signature unknown; restored from __doc__
        """ get_comment(self, group_name:str=None, key:str=None) -> str """
        return ""

    def get_double(self, group_name, key): # real signature unknown; restored from __doc__
        """ get_double(self, group_name:str, key:str) -> float """
        return 0.0

    def get_double_list(self, group_name, key): # real signature unknown; restored from __doc__
        """ get_double_list(self, group_name:str, key:str) -> list """
        return []

    def get_groups(self): # real signature unknown; restored from __doc__
        """ get_groups(self) -> list, length:int """
        return []

    def get_int64(self, group_name, key): # real signature unknown; restored from __doc__
        """ get_int64(self, group_name:str, key:str) -> int """
        return 0

    def get_integer(self, group_name, key): # real signature unknown; restored from __doc__
        """ get_integer(self, group_name:str, key:str) -> int """
        return 0

    def get_integer_list(self, group_name, key): # real signature unknown; restored from __doc__
        """ get_integer_list(self, group_name:str, key:str) -> list """
        return []

    def get_keys(self, group_name): # real signature unknown; restored from __doc__
        """ get_keys(self, group_name:str) -> list, length:int """
        return []

    def get_locale_for_key(self, group_name, key, locale=None): # real signature unknown; restored from __doc__
        """ get_locale_for_key(self, group_name:str, key:str, locale:str=None) -> str or None """
        return ""

    def get_locale_string(self, group_name, key, locale=None): # real signature unknown; restored from __doc__
        """ get_locale_string(self, group_name:str, key:str, locale:str=None) -> str """
        return ""

    def get_locale_string_list(self, group_name, key, locale=None): # real signature unknown; restored from __doc__
        """ get_locale_string_list(self, group_name:str, key:str, locale:str=None) -> list """
        return []

    def get_start_group(self): # real signature unknown; restored from __doc__
        """ get_start_group(self) -> str or None """
        return ""

    def get_string(self, group_name, key): # real signature unknown; restored from __doc__
        """ get_string(self, group_name:str, key:str) -> str """
        return ""

    def get_string_list(self, group_name, key): # real signature unknown; restored from __doc__
        """ get_string_list(self, group_name:str, key:str) -> list """
        return []

    def get_uint64(self, group_name, key): # real signature unknown; restored from __doc__
        """ get_uint64(self, group_name:str, key:str) -> int """
        return 0

    def get_value(self, group_name, key): # real signature unknown; restored from __doc__
        """ get_value(self, group_name:str, key:str) -> str """
        return ""

    def has_group(self, group_name): # real signature unknown; restored from __doc__
        """ has_group(self, group_name:str) -> bool """
        return False

    def load_from_bytes(self, bytes, flags): # real signature unknown; restored from __doc__
        """ load_from_bytes(self, bytes:GLib.Bytes, flags:GLib.KeyFileFlags) -> bool """
        return False

    def load_from_data(self, data, length, flags): # real signature unknown; restored from __doc__
        """ load_from_data(self, data:str, length:int, flags:GLib.KeyFileFlags) -> bool """
        return False

    def load_from_data_dirs(self, file, flags): # real signature unknown; restored from __doc__
        """ load_from_data_dirs(self, file:str, flags:GLib.KeyFileFlags) -> bool, full_path:str """
        return False

    def load_from_dirs(self, file, search_dirs, flags): # real signature unknown; restored from __doc__
        """ load_from_dirs(self, file:str, search_dirs:list, flags:GLib.KeyFileFlags) -> bool, full_path:str """
        return False

    def load_from_file(self, file, flags): # real signature unknown; restored from __doc__
        """ load_from_file(self, file:str, flags:GLib.KeyFileFlags) -> bool """
        return False

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> GLib.KeyFile """
        pass

    def remove_comment(self, group_name=None, key=None): # real signature unknown; restored from __doc__
        """ remove_comment(self, group_name:str=None, key:str=None) -> bool """
        return False

    def remove_group(self, group_name): # real signature unknown; restored from __doc__
        """ remove_group(self, group_name:str) -> bool """
        return False

    def remove_key(self, group_name, key): # real signature unknown; restored from __doc__
        """ remove_key(self, group_name:str, key:str) -> bool """
        return False

    def save_to_file(self, filename): # real signature unknown; restored from __doc__
        """ save_to_file(self, filename:str) -> bool """
        return False

    def set_boolean(self, group_name, key, value): # real signature unknown; restored from __doc__
        """ set_boolean(self, group_name:str, key:str, value:bool) """
        pass

    def set_boolean_list(self, group_name, key, p_list): # real signature unknown; restored from __doc__
        """ set_boolean_list(self, group_name:str, key:str, list:list) """
        pass

    def set_comment(self, group_name=None, key=None, comment): # real signature unknown; restored from __doc__
        """ set_comment(self, group_name:str=None, key:str=None, comment:str) -> bool """
        return False

    def set_double(self, group_name, key, value): # real signature unknown; restored from __doc__
        """ set_double(self, group_name:str, key:str, value:float) """
        pass

    def set_double_list(self, group_name, key, p_list): # real signature unknown; restored from __doc__
        """ set_double_list(self, group_name:str, key:str, list:list) """
        pass

    def set_int64(self, group_name, key, value): # real signature unknown; restored from __doc__
        """ set_int64(self, group_name:str, key:str, value:int) """
        pass

    def set_integer(self, group_name, key, value): # real signature unknown; restored from __doc__
        """ set_integer(self, group_name:str, key:str, value:int) """
        pass

    def set_integer_list(self, group_name, key, p_list): # real signature unknown; restored from __doc__
        """ set_integer_list(self, group_name:str, key:str, list:list) """
        pass

    def set_list_separator(self, separator): # real signature unknown; restored from __doc__
        """ set_list_separator(self, separator:int) """
        pass

    def set_locale_string(self, group_name, key, locale, string): # real signature unknown; restored from __doc__
        """ set_locale_string(self, group_name:str, key:str, locale:str, string:str) """
        pass

    def set_locale_string_list(self, group_name, key, locale, p_list): # real signature unknown; restored from __doc__
        """ set_locale_string_list(self, group_name:str, key:str, locale:str, list:list) """
        pass

    def set_string(self, group_name, key, string): # real signature unknown; restored from __doc__
        """ set_string(self, group_name:str, key:str, string:str) """
        pass

    def set_string_list(self, group_name, key, p_list): # real signature unknown; restored from __doc__
        """ set_string_list(self, group_name:str, key:str, list:list) """
        pass

    def set_uint64(self, group_name, key, value): # real signature unknown; restored from __doc__
        """ set_uint64(self, group_name:str, key:str, value:int) """
        pass

    def set_value(self, group_name, key, value): # real signature unknown; restored from __doc__
        """ set_value(self, group_name:str, key:str, value:str) """
        pass

    def to_data(self): # real signature unknown; restored from __doc__
        """ to_data(self) -> str, length:int """
        return ""

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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
    def __new__(*args, **kwargs): # real signature unknown
        """ new() -> GLib.KeyFile """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(KeyFile), '__module__': 'gi.repository.GLib', '__gtype__': <GType GKeyFile (2640521760)>, '__dict__': <attribute '__dict__' of 'KeyFile' objects>, '__weakref__': <attribute '__weakref__' of 'KeyFile' objects>, '__doc__': None, 'new': <classmethod(gi.FunctionInfo(new))>, 'get_boolean': gi.FunctionInfo(get_boolean), 'get_boolean_list': gi.FunctionInfo(get_boolean_list), 'get_comment': gi.FunctionInfo(get_comment), 'get_double': gi.FunctionInfo(get_double), 'get_double_list': gi.FunctionInfo(get_double_list), 'get_groups': gi.FunctionInfo(get_groups), 'get_int64': gi.FunctionInfo(get_int64), 'get_integer': gi.FunctionInfo(get_integer), 'get_integer_list': gi.FunctionInfo(get_integer_list), 'get_keys': gi.FunctionInfo(get_keys), 'get_locale_for_key': gi.FunctionInfo(get_locale_for_key), 'get_locale_string': gi.FunctionInfo(get_locale_string), 'get_locale_string_list': gi.FunctionInfo(get_locale_string_list), 'get_start_group': gi.FunctionInfo(get_start_group), 'get_string': gi.FunctionInfo(get_string), 'get_string_list': gi.FunctionInfo(get_string_list), 'get_uint64': gi.FunctionInfo(get_uint64), 'get_value': gi.FunctionInfo(get_value), 'has_group': gi.FunctionInfo(has_group), 'load_from_bytes': gi.FunctionInfo(load_from_bytes), 'load_from_data': gi.FunctionInfo(load_from_data), 'load_from_data_dirs': gi.FunctionInfo(load_from_data_dirs), 'load_from_dirs': gi.FunctionInfo(load_from_dirs), 'load_from_file': gi.FunctionInfo(load_from_file), 'remove_comment': gi.FunctionInfo(remove_comment), 'remove_group': gi.FunctionInfo(remove_group), 'remove_key': gi.FunctionInfo(remove_key), 'save_to_file': gi.FunctionInfo(save_to_file), 'set_boolean': gi.FunctionInfo(set_boolean), 'set_boolean_list': gi.FunctionInfo(set_boolean_list), 'set_comment': gi.FunctionInfo(set_comment), 'set_double': gi.FunctionInfo(set_double), 'set_double_list': gi.FunctionInfo(set_double_list), 'set_int64': gi.FunctionInfo(set_int64), 'set_integer': gi.FunctionInfo(set_integer), 'set_integer_list': gi.FunctionInfo(set_integer_list), 'set_list_separator': gi.FunctionInfo(set_list_separator), 'set_locale_string': gi.FunctionInfo(set_locale_string), 'set_locale_string_list': gi.FunctionInfo(set_locale_string_list), 'set_string': gi.FunctionInfo(set_string), 'set_string_list': gi.FunctionInfo(set_string_list), 'set_uint64': gi.FunctionInfo(set_uint64), 'set_value': gi.FunctionInfo(set_value), 'to_data': gi.FunctionInfo(to_data), 'unref': gi.FunctionInfo(unref), 'error_quark': <staticmethod(gi.FunctionInfo(error_quark))>, '__new__': <staticmethod(gi.FunctionInfo(new))>, '__init__': <function nothing at 0x0000018e9fdc1010>})"
    __gtype__ = None # (!) real value is '<GType GKeyFile (2640521760)>'
    __info__ = StructInfo(KeyFile)


