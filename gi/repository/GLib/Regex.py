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


class Regex(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(pattern:str, compile_options:GLib.RegexCompileFlags, match_options:GLib.RegexMatchFlags) -> GLib.Regex or None
    """
    def check_replacement(self, replacement): # real signature unknown; restored from __doc__
        """ check_replacement(replacement:str) -> bool, has_references:bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def escape_nul(self, string, length): # real signature unknown; restored from __doc__
        """ escape_nul(string:str, length:int) -> str """
        return ""

    def escape_string(self, string, length): # real signature unknown; restored from __doc__
        """ escape_string(string:str, length:int) -> str """
        return ""

    def get_capture_count(self): # real signature unknown; restored from __doc__
        """ get_capture_count(self) -> int """
        return 0

    def get_compile_flags(self): # real signature unknown; restored from __doc__
        """ get_compile_flags(self) -> GLib.RegexCompileFlags """
        pass

    def get_has_cr_or_lf(self): # real signature unknown; restored from __doc__
        """ get_has_cr_or_lf(self) -> bool """
        return False

    def get_match_flags(self): # real signature unknown; restored from __doc__
        """ get_match_flags(self) -> GLib.RegexMatchFlags """
        pass

    def get_max_backref(self): # real signature unknown; restored from __doc__
        """ get_max_backref(self) -> int """
        return 0

    def get_max_lookbehind(self): # real signature unknown; restored from __doc__
        """ get_max_lookbehind(self) -> int """
        return 0

    def get_pattern(self): # real signature unknown; restored from __doc__
        """ get_pattern(self) -> str """
        return ""

    def get_string_number(self, name): # real signature unknown; restored from __doc__
        """ get_string_number(self, name:str) -> int """
        return 0

    def match(self, string, match_options): # real signature unknown; restored from __doc__
        """ match(self, string:str, match_options:GLib.RegexMatchFlags) -> bool, match_info:GLib.MatchInfo """
        return False

    def match_all(self, string, match_options): # real signature unknown; restored from __doc__
        """ match_all(self, string:str, match_options:GLib.RegexMatchFlags) -> bool, match_info:GLib.MatchInfo """
        return False

    def match_all_full(self, string, start_position, match_options): # real signature unknown; restored from __doc__
        """ match_all_full(self, string:list, start_position:int, match_options:GLib.RegexMatchFlags) -> bool, match_info:GLib.MatchInfo """
        return False

    def match_full(self, string, start_position, match_options): # real signature unknown; restored from __doc__
        """ match_full(self, string:list, start_position:int, match_options:GLib.RegexMatchFlags) -> bool, match_info:GLib.MatchInfo """
        return False

    def match_simple(self, pattern, string, compile_options, match_options): # real signature unknown; restored from __doc__
        """ match_simple(pattern:str, string:str, compile_options:GLib.RegexCompileFlags, match_options:GLib.RegexMatchFlags) -> bool """
        return False

    @classmethod
    def new(cls, pattern, compile_options, match_options): # real signature unknown; restored from __doc__
        """ new(pattern:str, compile_options:GLib.RegexCompileFlags, match_options:GLib.RegexMatchFlags) -> GLib.Regex or None """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.Regex """
        pass

    def replace(self, string, start_position, replacement, match_options): # real signature unknown; restored from __doc__
        """ replace(self, string:list, start_position:int, replacement:str, match_options:GLib.RegexMatchFlags) -> str """
        return ""

    def replace_eval(self, string, start_position, match_options, eval, user_data=None): # real signature unknown; restored from __doc__
        """ replace_eval(self, string:list, start_position:int, match_options:GLib.RegexMatchFlags, eval:GLib.RegexEvalCallback, user_data=None) -> str """
        return ""

    def replace_literal(self, string, start_position, replacement, match_options): # real signature unknown; restored from __doc__
        """ replace_literal(self, string:list, start_position:int, replacement:str, match_options:GLib.RegexMatchFlags) -> str """
        return ""

    def split(self, string, match_options): # real signature unknown; restored from __doc__
        """ split(self, string:str, match_options:GLib.RegexMatchFlags) -> list """
        return []

    def split_full(self, string, start_position, match_options, max_tokens): # real signature unknown; restored from __doc__
        """ split_full(self, string:list, start_position:int, match_options:GLib.RegexMatchFlags, max_tokens:int) -> list """
        return []

    def split_simple(self, pattern, string, compile_options, match_options): # real signature unknown; restored from __doc__
        """ split_simple(pattern:str, string:str, compile_options:GLib.RegexCompileFlags, match_options:GLib.RegexMatchFlags) -> list """
        return []

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
        """ new(pattern:str, compile_options:GLib.RegexCompileFlags, match_options:GLib.RegexMatchFlags) -> GLib.Regex or None """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Regex), '__module__': 'gi.repository.GLib', '__gtype__': <GType GRegex (2640521952)>, '__dict__': <attribute '__dict__' of 'Regex' objects>, '__weakref__': <attribute '__weakref__' of 'Regex' objects>, '__doc__': None, 'new': <classmethod(gi.FunctionInfo(new))>, 'get_capture_count': gi.FunctionInfo(get_capture_count), 'get_compile_flags': gi.FunctionInfo(get_compile_flags), 'get_has_cr_or_lf': gi.FunctionInfo(get_has_cr_or_lf), 'get_match_flags': gi.FunctionInfo(get_match_flags), 'get_max_backref': gi.FunctionInfo(get_max_backref), 'get_max_lookbehind': gi.FunctionInfo(get_max_lookbehind), 'get_pattern': gi.FunctionInfo(get_pattern), 'get_string_number': gi.FunctionInfo(get_string_number), 'match': gi.FunctionInfo(match), 'match_all': gi.FunctionInfo(match_all), 'match_all_full': gi.FunctionInfo(match_all_full), 'match_full': gi.FunctionInfo(match_full), 'ref': gi.FunctionInfo(ref), 'replace': gi.FunctionInfo(replace), 'replace_eval': gi.FunctionInfo(replace_eval), 'replace_literal': gi.FunctionInfo(replace_literal), 'split': gi.FunctionInfo(split), 'split_full': gi.FunctionInfo(split_full), 'unref': gi.FunctionInfo(unref), 'check_replacement': <staticmethod(gi.FunctionInfo(check_replacement))>, 'error_quark': <staticmethod(gi.FunctionInfo(error_quark))>, 'escape_nul': <staticmethod(gi.FunctionInfo(escape_nul))>, 'escape_string': <staticmethod(gi.FunctionInfo(escape_string))>, 'match_simple': <staticmethod(gi.FunctionInfo(match_simple))>, 'split_simple': <staticmethod(gi.FunctionInfo(split_simple))>, '__new__': <staticmethod(gi.FunctionInfo(new))>, '__init__': <function nothing at 0x0000018e9fdc1010>})"
    __gtype__ = None # (!) real value is '<GType GRegex (2640521952)>'
    __info__ = StructInfo(Regex)


