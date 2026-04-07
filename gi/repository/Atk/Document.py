# encoding: utf-8
# module gi.repository.Atk
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gi._gi as __gi__gi
import gobject as __gobject


class Document(__gobject.GInterface):
    # no doc
    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> list """
        return []

    def get_attribute_value(self, attribute_name): # real signature unknown; restored from __doc__
        """ get_attribute_value(self, attribute_name:str) -> str or None """
        return ""

    def get_current_page_number(self): # real signature unknown; restored from __doc__
        """ get_current_page_number(self) -> int """
        return 0

    def get_document(self): # real signature unknown; restored from __doc__
        """ get_document(self) """
        pass

    def get_document_type(self): # real signature unknown; restored from __doc__
        """ get_document_type(self) -> str """
        return ""

    def get_locale(self): # real signature unknown; restored from __doc__
        """ get_locale(self) -> str """
        return ""

    def get_page_count(self): # real signature unknown; restored from __doc__
        """ get_page_count(self) -> int """
        return 0

    def get_text_selections(self): # real signature unknown; restored from __doc__
        """ get_text_selections(self) -> list """
        return []

    def set_attribute_value(self, attribute_name, attribute_value): # real signature unknown; restored from __doc__
        """ set_attribute_value(self, attribute_name:str, attribute_value:str) -> bool """
        return False

    def set_text_selections(self, selections): # real signature unknown; restored from __doc__
        """ set_text_selections(self, selections:list) -> bool """
        return False

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Document), '__module__': 'gi.repository.Atk', '__gtype__': <GType AtkDocument (1534560192)>, '__dict__': <attribute '__dict__' of 'Document' objects>, '__weakref__': <attribute '__weakref__' of 'Document' objects>, '__doc__': None, '__gsignals__': {}, 'get_attribute_value': gi.FunctionInfo(get_attribute_value), 'get_attributes': gi.FunctionInfo(get_attributes), 'get_current_page_number': gi.FunctionInfo(get_current_page_number), 'get_document': gi.FunctionInfo(get_document), 'get_document_type': gi.FunctionInfo(get_document_type), 'get_locale': gi.FunctionInfo(get_locale), 'get_page_count': gi.FunctionInfo(get_page_count), 'get_text_selections': gi.FunctionInfo(get_text_selections), 'set_attribute_value': gi.FunctionInfo(set_attribute_value), 'set_text_selections': gi.FunctionInfo(set_text_selections)})"
    __gdoc__ = 'Interface AtkDocument\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AtkDocument (1534560192)>'
    __info__ = InterfaceInfo(Document)


