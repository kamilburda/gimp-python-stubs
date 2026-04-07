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


class Action(__gobject.GInterface):
    # no doc
    def do_action(self, i): # real signature unknown; restored from __doc__
        """ do_action(self, i:int) -> bool """
        return False

    def get_description(self, i): # real signature unknown; restored from __doc__
        """ get_description(self, i:int) -> str or None """
        return ""

    def get_keybinding(self, i): # real signature unknown; restored from __doc__
        """ get_keybinding(self, i:int) -> str or None """
        return ""

    def get_localized_name(self, i): # real signature unknown; restored from __doc__
        """ get_localized_name(self, i:int) -> str or None """
        return ""

    def get_name(self, i): # real signature unknown; restored from __doc__
        """ get_name(self, i:int) -> str or None """
        return ""

    def get_n_actions(self): # real signature unknown; restored from __doc__
        """ get_n_actions(self) -> int """
        return 0

    def set_description(self, i, desc): # real signature unknown; restored from __doc__
        """ set_description(self, i:int, desc:str) -> bool """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Action), '__module__': 'gi.repository.Atk', '__gtype__': <GType AtkAction (1534560096)>, '__dict__': <attribute '__dict__' of 'Action' objects>, '__weakref__': <attribute '__weakref__' of 'Action' objects>, '__doc__': None, '__gsignals__': {}, 'do_action': gi.FunctionInfo(do_action), 'get_description': gi.FunctionInfo(get_description), 'get_keybinding': gi.FunctionInfo(get_keybinding), 'get_localized_name': gi.FunctionInfo(get_localized_name), 'get_n_actions': gi.FunctionInfo(get_n_actions), 'get_name': gi.FunctionInfo(get_name), 'set_description': gi.FunctionInfo(set_description)})"
    __gdoc__ = 'Interface AtkAction\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AtkAction (1534560096)>'
    __info__ = InterfaceInfo(Action)


