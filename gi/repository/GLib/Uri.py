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


class Uri(__gi.Boxed):
    # no doc
    def build(self, flags, scheme, userinfo=None, host=None, port, path, query=None, fragment=None): # real signature unknown; restored from __doc__
        """ build(flags:GLib.UriFlags, scheme:str, userinfo:str=None, host:str=None, port:int, path:str, query:str=None, fragment:str=None) -> GLib.Uri """
        pass

    def build_with_user(self, flags, scheme, user=None, password=None, auth_params=None, host=None, port, path, query=None, fragment=None): # real signature unknown; restored from __doc__
        """ build_with_user(flags:GLib.UriFlags, scheme:str, user:str=None, password:str=None, auth_params:str=None, host:str=None, port:int, path:str, query:str=None, fragment:str=None) -> GLib.Uri """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def escape_bytes(self, unescaped, reserved_chars_allowed=None): # real signature unknown; restored from __doc__
        """ escape_bytes(unescaped:list, reserved_chars_allowed:str=None) -> str """
        return ""

    def escape_string(self, unescaped, reserved_chars_allowed=None, allow_utf8): # real signature unknown; restored from __doc__
        """ escape_string(unescaped:str, reserved_chars_allowed:str=None, allow_utf8:bool) -> str """
        return ""

    def get_auth_params(self): # real signature unknown; restored from __doc__
        """ get_auth_params(self) -> str or None """
        return ""

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> GLib.UriFlags """
        pass

    def get_fragment(self): # real signature unknown; restored from __doc__
        """ get_fragment(self) -> str or None """
        return ""

    def get_host(self): # real signature unknown; restored from __doc__
        """ get_host(self) -> str or None """
        return ""

    def get_password(self): # real signature unknown; restored from __doc__
        """ get_password(self) -> str or None """
        return ""

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> str """
        return ""

    def get_port(self): # real signature unknown; restored from __doc__
        """ get_port(self) -> int """
        return 0

    def get_query(self): # real signature unknown; restored from __doc__
        """ get_query(self) -> str or None """
        return ""

    def get_scheme(self): # real signature unknown; restored from __doc__
        """ get_scheme(self) -> str """
        return ""

    def get_user(self): # real signature unknown; restored from __doc__
        """ get_user(self) -> str or None """
        return ""

    def get_userinfo(self): # real signature unknown; restored from __doc__
        """ get_userinfo(self) -> str or None """
        return ""

    def is_valid(self, uri_string, flags): # real signature unknown; restored from __doc__
        """ is_valid(uri_string:str, flags:GLib.UriFlags) -> bool """
        return False

    def join(self, flags, scheme=None, userinfo=None, host=None, port, path, query=None, fragment=None): # real signature unknown; restored from __doc__
        """ join(flags:GLib.UriFlags, scheme:str=None, userinfo:str=None, host:str=None, port:int, path:str, query:str=None, fragment:str=None) -> str """
        return ""

    def join_with_user(self, flags, scheme=None, user=None, password=None, auth_params=None, host=None, port, path, query=None, fragment=None): # real signature unknown; restored from __doc__
        """ join_with_user(flags:GLib.UriFlags, scheme:str=None, user:str=None, password:str=None, auth_params:str=None, host:str=None, port:int, path:str, query:str=None, fragment:str=None) -> str """
        return ""

    def list_extract_uris(self, uri_list): # real signature unknown; restored from __doc__
        """ list_extract_uris(uri_list:str) -> list """
        return []

    def parse(self, uri_string, flags): # real signature unknown; restored from __doc__
        """ parse(uri_string:str, flags:GLib.UriFlags) -> GLib.Uri """
        pass

    def parse_params(self, params, length, separators, flags): # real signature unknown; restored from __doc__
        """ parse_params(params:str, length:int, separators:str, flags:GLib.UriParamsFlags) -> dict """
        return {}

    def parse_relative(self, uri_ref, flags): # real signature unknown; restored from __doc__
        """ parse_relative(self, uri_ref:str, flags:GLib.UriFlags) -> GLib.Uri """
        pass

    def parse_scheme(self, uri): # real signature unknown; restored from __doc__
        """ parse_scheme(uri:str) -> str or None """
        return ""

    def peek_scheme(self, uri): # real signature unknown; restored from __doc__
        """ peek_scheme(uri:str) -> str or None """
        return ""

    def resolve_relative(self, base_uri_string=None, uri_ref, flags): # real signature unknown; restored from __doc__
        """ resolve_relative(base_uri_string:str=None, uri_ref:str, flags:GLib.UriFlags) -> str """
        return ""

    def split(self, uri_ref, flags): # real signature unknown; restored from __doc__
        """ split(uri_ref:str, flags:GLib.UriFlags) -> scheme:str, userinfo:str, host:str, port:int, path:str, query:str, fragment:str """
        pass

    def split_network(self, uri_string, flags): # real signature unknown; restored from __doc__
        """ split_network(uri_string:str, flags:GLib.UriFlags) -> scheme:str, host:str, port:int """
        pass

    def split_with_user(self, uri_ref, flags): # real signature unknown; restored from __doc__
        """ split_with_user(uri_ref:str, flags:GLib.UriFlags) -> scheme:str, user:str, password:str, auth_params:str, host:str, port:int, path:str, query:str, fragment:str """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def to_string_partial(self, flags): # real signature unknown; restored from __doc__
        """ to_string_partial(self, flags:GLib.UriHideFlags) -> str """
        return ""

    def unescape_bytes(self, escaped_string, length, illegal_characters=None): # real signature unknown; restored from __doc__
        """ unescape_bytes(escaped_string:str, length:int, illegal_characters:str=None) -> GLib.Bytes """
        pass

    def unescape_segment(self, escaped_string=None, escaped_string_end=None, illegal_characters=None): # real signature unknown; restored from __doc__
        """ unescape_segment(escaped_string:str=None, escaped_string_end:str=None, illegal_characters:str=None) -> str or None """
        return ""

    def unescape_string(self, escaped_string, illegal_characters=None): # real signature unknown; restored from __doc__
        """ unescape_string(escaped_string:str, illegal_characters:str=None) -> str or None """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Uri), '__module__': 'gi.repository.GLib', '__gtype__': <GType GUri (2640519744)>, '__dict__': <attribute '__dict__' of 'Uri' objects>, '__weakref__': <attribute '__weakref__' of 'Uri' objects>, '__doc__': None, 'get_auth_params': gi.FunctionInfo(get_auth_params), 'get_flags': gi.FunctionInfo(get_flags), 'get_fragment': gi.FunctionInfo(get_fragment), 'get_host': gi.FunctionInfo(get_host), 'get_password': gi.FunctionInfo(get_password), 'get_path': gi.FunctionInfo(get_path), 'get_port': gi.FunctionInfo(get_port), 'get_query': gi.FunctionInfo(get_query), 'get_scheme': gi.FunctionInfo(get_scheme), 'get_user': gi.FunctionInfo(get_user), 'get_userinfo': gi.FunctionInfo(get_userinfo), 'parse_relative': gi.FunctionInfo(parse_relative), 'to_string': gi.FunctionInfo(to_string), 'to_string_partial': gi.FunctionInfo(to_string_partial), 'build': <staticmethod(gi.FunctionInfo(build))>, 'build_with_user': <staticmethod(gi.FunctionInfo(build_with_user))>, 'error_quark': <staticmethod(gi.FunctionInfo(error_quark))>, 'escape_bytes': <staticmethod(gi.FunctionInfo(escape_bytes))>, 'escape_string': <staticmethod(gi.FunctionInfo(escape_string))>, 'is_valid': <staticmethod(gi.FunctionInfo(is_valid))>, 'join': <staticmethod(gi.FunctionInfo(join))>, 'join_with_user': <staticmethod(gi.FunctionInfo(join_with_user))>, 'list_extract_uris': <staticmethod(gi.FunctionInfo(list_extract_uris))>, 'parse': <staticmethod(gi.FunctionInfo(parse))>, 'parse_params': <staticmethod(gi.FunctionInfo(parse_params))>, 'parse_scheme': <staticmethod(gi.FunctionInfo(parse_scheme))>, 'peek_scheme': <staticmethod(gi.FunctionInfo(peek_scheme))>, 'resolve_relative': <staticmethod(gi.FunctionInfo(resolve_relative))>, 'split': <staticmethod(gi.FunctionInfo(split))>, 'split_network': <staticmethod(gi.FunctionInfo(split_network))>, 'split_with_user': <staticmethod(gi.FunctionInfo(split_with_user))>, 'unescape_bytes': <staticmethod(gi.FunctionInfo(unescape_bytes))>, 'unescape_segment': <staticmethod(gi.FunctionInfo(unescape_segment))>, 'unescape_string': <staticmethod(gi.FunctionInfo(unescape_string))>})"
    __gtype__ = None # (!) real value is '<GType GUri (2640519744)>'
    __info__ = StructInfo(Uri)


