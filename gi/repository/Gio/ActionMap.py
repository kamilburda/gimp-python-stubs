# encoding: utf-8
# module gi.repository.Gio
# by generator 1.147
# no doc

# imports
from gi.repository.GioWin32 import (NetworkMonitorClass, 
    NetworkMonitorPrivate, Win32InputStream, Win32InputStreamClass, 
    Win32InputStreamPrivate, Win32NetworkMonitor, Win32OutputStream, 
    Win32OutputStreamClass, Win32OutputStreamPrivate, 
    registry_settings_backend_new)

from _thread import _lock

import gi as __gi
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


from .ActionMap import ActionMap

class ActionMap(ActionMap):
    # no doc
    def add_action(self, action): # real signature unknown; restored from __doc__
        """ add_action(self, action:Gio.Action) """
        pass

    def add_action_entries(self, entries, user_data=None): # reliably restored by inspect
        """
        The ``add_action_entries()`` method is a convenience function for creating
                multiple :class:`~gi.repository.Gio.SimpleAction` instances and adding them
                to a :class:`~gi.repository.Gio.ActionMap`.
                Each action is constructed as per one entry.
        
                :param list entries:
                    List of entry tuples for :meth:`add_action` method. The entry tuple can
                    vary in size with the following information:
        
                    * The name of the action. Must be specified.
                    * The callback to connect to the "activate" signal of the
                      action. Since GLib 2.40, this can be ``None`` for stateful
                      actions, in which case the default handler is used. For
                      boolean-stated actions with no parameter, this is a toggle.
                      For other state types (and parameter type equal to the state
                      type) this will be a function that just calls change_state
                      (which you should provide).
                    * The type of the parameter that must be passed to the activate
                      function for this action, given as a single :class:`~gi.repository.GLib.Variant` type
                      string (or ``None`` for no parameter)
                    * The initial state for this action, given in GLib.Variant text
                      format. The state is parsed with no extra type information, so
                      type tags must be added to the string if they are necessary.
                      Stateless actions should give ``None`` here.
                    * The callback to connect to the "change-state" signal of the
                      action. All stateful actions should provide a handler here;
                      stateless actions should not.
        
                :param user_data:
                    The user data for signal connections, or ``None``
        """
        pass

    def lookup_action(self, action_name): # real signature unknown; restored from __doc__
        """ lookup_action(self, action_name:str) -> Gio.Action or None """
        pass

    def remove_action(self, action_name): # real signature unknown; restored from __doc__
        """ remove_action(self, action_name:str) """
        pass

    def remove_action_entries(self, entries): # real signature unknown; restored from __doc__
        """ remove_action_entries(self, entries:list) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gio', 'add_action_entries': <function ActionMap.add_action_entries at 0x000001ea7028af20>, '__doc__': None, '__gsignals__': {}})"
    __gdoc__ = 'Interface GActionMap\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GActionMap (1845786304)>'
    __info__ = InterfaceInfo(ActionMap)


