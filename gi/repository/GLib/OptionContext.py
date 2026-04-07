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


class OptionContext(__gi.Struct):
    # no doc
    def add_group(self, group): # real signature unknown; restored from __doc__
        """ add_group(self, group:GLib.OptionGroup) """
        pass

    def add_main_entries(self, entries, translation_domain=None): # real signature unknown; restored from __doc__
        """ add_main_entries(self, entries:list, translation_domain:str=None) """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_help(self, main_help, group=None): # real signature unknown; restored from __doc__
        """ get_help(self, main_help:bool, group:GLib.OptionGroup=None) -> str """
        return ""

    def get_help_enabled(self): # real signature unknown; restored from __doc__
        """ get_help_enabled(self) -> bool """
        return False

    def get_ignore_unknown_options(self): # real signature unknown; restored from __doc__
        """ get_ignore_unknown_options(self) -> bool """
        return False

    def get_main_group(self): # real signature unknown; restored from __doc__
        """ get_main_group(self) -> GLib.OptionGroup """
        pass

    def get_strict_posix(self): # real signature unknown; restored from __doc__
        """ get_strict_posix(self) -> bool """
        return False

    def get_summary(self): # real signature unknown; restored from __doc__
        """ get_summary(self) -> str """
        return ""

    def parse(self, argv, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ parse(self, argv:list=<optional>) -> bool, argv:list """
        pass

    def parse_strv(self, arguments, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ parse_strv(self, arguments:list=<optional>) -> bool, arguments:list """
        pass

    def set_description(self, description=None): # real signature unknown; restored from __doc__
        """ set_description(self, description:str=None) """
        pass

    def set_help_enabled(self, help_enabled): # real signature unknown; restored from __doc__
        """ set_help_enabled(self, help_enabled:bool) """
        pass

    def set_ignore_unknown_options(self, ignore_unknown): # real signature unknown; restored from __doc__
        """ set_ignore_unknown_options(self, ignore_unknown:bool) """
        pass

    def set_main_group(self, group): # real signature unknown; restored from __doc__
        """ set_main_group(self, group:GLib.OptionGroup) """
        pass

    def set_strict_posix(self, strict_posix): # real signature unknown; restored from __doc__
        """ set_strict_posix(self, strict_posix:bool) """
        pass

    def set_summary(self, summary=None): # real signature unknown; restored from __doc__
        """ set_summary(self, summary:str=None) """
        pass

    def set_translate_func(self, func=None, data=None): # real signature unknown; restored from __doc__
        """ set_translate_func(self, func:GLib.TranslateFunc=None, data=None) """
        pass

    def set_translation_domain(self, domain): # real signature unknown; restored from __doc__
        """ set_translation_domain(self, domain:str) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(OptionContext), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'OptionContext' objects>, '__weakref__': <attribute '__weakref__' of 'OptionContext' objects>, '__doc__': None, 'add_group': gi.FunctionInfo(add_group), 'add_main_entries': gi.FunctionInfo(add_main_entries), 'free': gi.FunctionInfo(free), 'get_description': gi.FunctionInfo(get_description), 'get_help': gi.FunctionInfo(get_help), 'get_help_enabled': gi.FunctionInfo(get_help_enabled), 'get_ignore_unknown_options': gi.FunctionInfo(get_ignore_unknown_options), 'get_main_group': gi.FunctionInfo(get_main_group), 'get_strict_posix': gi.FunctionInfo(get_strict_posix), 'get_summary': gi.FunctionInfo(get_summary), 'parse': gi.FunctionInfo(parse), 'parse_strv': gi.FunctionInfo(parse_strv), 'set_description': gi.FunctionInfo(set_description), 'set_help_enabled': gi.FunctionInfo(set_help_enabled), 'set_ignore_unknown_options': gi.FunctionInfo(set_ignore_unknown_options), 'set_main_group': gi.FunctionInfo(set_main_group), 'set_strict_posix': gi.FunctionInfo(set_strict_posix), 'set_summary': gi.FunctionInfo(set_summary), 'set_translate_func': gi.FunctionInfo(set_translate_func), 'set_translation_domain': gi.FunctionInfo(set_translation_domain)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(OptionContext)


