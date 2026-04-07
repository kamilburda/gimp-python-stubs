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


class ScannerConfig(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ScannerConfig()
    """
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

    case_sensitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    char_2_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cpair_comment_single = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cset_identifier_first = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cset_identifier_nth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cset_skip_characters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    identifier_2_string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    int_2_float = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numbers_2_int = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding_dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_binary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_comment_multi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_float = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_hex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_hex_dollar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_identifier_1char = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_identifier_NULL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_octal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_string_dq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_string_sq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan_symbols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scope_0_fallback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skip_comment_multi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skip_comment_single = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    store_int64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    symbol_2_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ScannerConfig), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ScannerConfig' objects>, '__weakref__': <attribute '__weakref__' of 'ScannerConfig' objects>, '__doc__': None, 'cset_skip_characters': <property object at 0x0000018ea0065080>, 'cset_identifier_first': <property object at 0x0000018ea0065170>, 'cset_identifier_nth': <property object at 0x0000018ea0065260>, 'cpair_comment_single': <property object at 0x0000018ea0065350>, 'case_sensitive': <property object at 0x0000018ea0065440>, 'skip_comment_multi': <property object at 0x0000018ea0065530>, 'skip_comment_single': <property object at 0x0000018ea0065620>, 'scan_comment_multi': <property object at 0x0000018ea0065710>, 'scan_identifier': <property object at 0x0000018ea0065800>, 'scan_identifier_1char': <property object at 0x0000018ea00658f0>, 'scan_identifier_NULL': <property object at 0x0000018ea00659e0>, 'scan_symbols': <property object at 0x0000018ea0065ad0>, 'scan_binary': <property object at 0x0000018ea0065bc0>, 'scan_octal': <property object at 0x0000018ea0065cb0>, 'scan_float': <property object at 0x0000018ea0065da0>, 'scan_hex': <property object at 0x0000018ea0065e90>, 'scan_hex_dollar': <property object at 0x0000018ea0065f80>, 'scan_string_sq': <property object at 0x0000018ea0066070>, 'scan_string_dq': <property object at 0x0000018ea0066160>, 'numbers_2_int': <property object at 0x0000018ea0066250>, 'int_2_float': <property object at 0x0000018ea0066340>, 'identifier_2_string': <property object at 0x0000018ea0066430>, 'char_2_token': <property object at 0x0000018ea0066520>, 'symbol_2_token': <property object at 0x0000018ea0066610>, 'scope_0_fallback': <property object at 0x0000018ea0066700>, 'store_int64': <property object at 0x0000018ea00667f0>, 'padding_dummy': <property object at 0x0000018ea00668e0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ScannerConfig)


