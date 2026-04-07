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


class ColorManaged(__gobject.GInterface):
    # no doc
    def get_color_profile(self): # real signature unknown; restored from __doc__
        """ get_color_profile(self) -> Gimp.ColorProfile """
        pass

    def get_icc_profile(self): # real signature unknown; restored from __doc__
        """ get_icc_profile(self) -> list """
        return []

    def get_simulation_bpc(self): # real signature unknown; restored from __doc__
        """ get_simulation_bpc(self) -> bool """
        return False

    def get_simulation_intent(self): # real signature unknown; restored from __doc__
        """ get_simulation_intent(self) -> Gimp.ColorRenderingIntent """
        pass

    def get_simulation_profile(self): # real signature unknown; restored from __doc__
        """ get_simulation_profile(self) -> Gimp.ColorProfile """
        pass

    def profile_changed(self): # real signature unknown; restored from __doc__
        """ profile_changed(self) """
        pass

    def simulation_bpc_changed(self): # real signature unknown; restored from __doc__
        """ simulation_bpc_changed(self) """
        pass

    def simulation_intent_changed(self): # real signature unknown; restored from __doc__
        """ simulation_intent_changed(self) """
        pass

    def simulation_profile_changed(self): # real signature unknown; restored from __doc__
        """ simulation_profile_changed(self) """
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(ColorManaged), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpColorManaged (2362305936)>, '__dict__': <attribute '__dict__' of 'ColorManaged' objects>, '__weakref__': <attribute '__weakref__' of 'ColorManaged' objects>, '__doc__': None, '__gsignals__': {}, 'get_color_profile': gi.FunctionInfo(get_color_profile), 'get_icc_profile': gi.FunctionInfo(get_icc_profile), 'get_simulation_bpc': gi.FunctionInfo(get_simulation_bpc), 'get_simulation_intent': gi.FunctionInfo(get_simulation_intent), 'get_simulation_profile': gi.FunctionInfo(get_simulation_profile), 'profile_changed': gi.FunctionInfo(profile_changed), 'simulation_bpc_changed': gi.FunctionInfo(simulation_bpc_changed), 'simulation_intent_changed': gi.FunctionInfo(simulation_intent_changed), 'simulation_profile_changed': gi.FunctionInfo(simulation_profile_changed)})"
    __gdoc__ = 'Interface GimpColorManaged\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GimpColorManaged (2362305936)>'
    __info__ = InterfaceInfo(ColorManaged)


