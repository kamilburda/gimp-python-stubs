# encoding: utf-8
# module gi.repository.GObject
# by generator 1.147
# no doc

# imports
from gi.repository.GLib import (Error, GError, IOCondition, IO_ERR, 
    IO_FLAG_APPEND, IO_FLAG_GET_MASK, IO_FLAG_IS_READABLE, 
    IO_FLAG_IS_SEEKABLE, IO_FLAG_IS_WRITEABLE, IO_FLAG_MASK, IO_FLAG_NONBLOCK, 
    IO_FLAG_SET_MASK, IO_HUP, IO_IN, IO_NVAL, IO_OUT, IO_PRI, IO_STATUS_AGAIN, 
    IO_STATUS_EOF, IO_STATUS_ERROR, IO_STATUS_NORMAL, OPTION_ERROR_BAD_VALUE, 
    OPTION_ERROR_FAILED, OPTION_ERROR_UNKNOWN_OPTION, OPTION_FLAG_FILENAME, 
    OPTION_FLAG_HIDDEN, OPTION_FLAG_IN_MAIN, OPTION_FLAG_NOALIAS, 
    OPTION_FLAG_NO_ARG, OPTION_FLAG_OPTIONAL_ARG, OPTION_FLAG_REVERSE, 
    SPAWN_CHILD_INHERITS_STDIN, SPAWN_DO_NOT_REAP_CHILD, 
    SPAWN_FILE_AND_ARGV_ZERO, SPAWN_LEAVE_DESCRIPTORS_OPEN, SPAWN_SEARCH_PATH, 
    SPAWN_STDERR_TO_DEV_NULL, SPAWN_STDOUT_TO_DEV_NULL, 
    filename_display_basename, filename_display_name, get_application_name, 
    get_prgname, main_context_default, main_depth, set_application_name, 
    set_prgname, source_remove, uri_list_extract_uris)

from gi._gi import (GEnum, GFlags, GObjectWeakRef, OptionContext, OptionGroup, 
    Pid, add_emission_hook, list_properties, new, signal_new, spawn_async, 
    type_register)

from gobject import GBoxed, GInterface, GPointer, GType, Warning

from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GLib as __gi_overrides_GLib
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GLib as __gi_repository_GLib
import gi._gi as __gi__gi
import gi._signalhelper as __gi__signalhelper
import gobject as __gobject


class MainContext(__gi_repository_GLib.MainContext):
    """
    :Constructors:
    
    ::
    
        new() -> GLib.MainContext
        new_with_flags(flags:GLib.MainContextFlags) -> GLib.MainContext
    """
    def acquire(self): # real signature unknown; restored from __doc__
        """ acquire(self) -> bool """
        return False

    def add_poll(self, fd, priority): # real signature unknown; restored from __doc__
        """ add_poll(self, fd:GLib.PollFD, priority:int) """
        pass

    def check(self, max_priority, fds): # real signature unknown; restored from __doc__
        """ check(self, max_priority:int, fds:list) -> bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def default(self): # real signature unknown; restored from __doc__
        """ default() -> GLib.MainContext """
        pass

    def dispatch(self): # real signature unknown; restored from __doc__
        """ dispatch(self) """
        pass

    def find_source_by_funcs_user_data(self, funcs, user_data=None): # real signature unknown; restored from __doc__
        """ find_source_by_funcs_user_data(self, funcs:GLib.SourceFuncs, user_data=None) -> GLib.Source or None """
        pass

    def find_source_by_id(self, source_id): # real signature unknown; restored from __doc__
        """ find_source_by_id(self, source_id:int) -> GLib.Source """
        pass

    def find_source_by_user_data(self, user_data=None): # real signature unknown; restored from __doc__
        """ find_source_by_user_data(self, user_data=None) -> GLib.Source or None """
        pass

    def get_thread_default(self): # real signature unknown; restored from __doc__
        """ get_thread_default() -> GLib.MainContext or None """
        pass

    def invoke_full(self, priority, function, data=None): # real signature unknown; restored from __doc__
        """ invoke_full(self, priority:int, function:GLib.SourceFunc, data=None) """
        pass

    def is_owner(self): # real signature unknown; restored from __doc__
        """ is_owner(self) -> bool """
        return False

    def iteration(self, may_block=True): # reliably restored by inspect
        # no doc
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> GLib.MainContext """
        pass

    def new_with_flags(self, flags): # real signature unknown; restored from __doc__
        """ new_with_flags(flags:GLib.MainContextFlags) -> GLib.MainContext """
        pass

    def pending(self): # real signature unknown; restored from __doc__
        """ pending(self) -> bool """
        return False

    def pop_thread_default(self): # real signature unknown; restored from __doc__
        """ pop_thread_default(self) """
        pass

    def prepare(self): # real signature unknown; restored from __doc__
        """ prepare(self) -> bool, priority:int """
        return False

    def pusher_new(self): # real signature unknown; restored from __doc__
        """ pusher_new(self) """
        pass

    def push_thread_default(self): # real signature unknown; restored from __doc__
        """ push_thread_default(self) """
        pass

    def query(self, max_priority): # reliably restored by inspect
        """
        Determines information necessary to poll this main loop.
        
                :param max_priority: maximum priority source to check
                :returns:
                  The timeout (msec) used for polling,
                  and the list of poll fd's.
        
                Please also check the usage notes in the
                `C documention <https://docs.gtk.org/glib/method.MainContext.query.html>`__.
        """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.MainContext """
        pass

    def ref_thread_default(self): # real signature unknown; restored from __doc__
        """ ref_thread_default() -> GLib.MainContext """
        pass

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) """
        pass

    def remove_poll(self, fd): # real signature unknown; restored from __doc__
        """ remove_poll(self, fd:GLib.PollFD) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def wait(self, cond, mutex): # real signature unknown; restored from __doc__
        """ wait(self, cond:GLib.Cond, mutex:GLib.Mutex) -> bool """
        return False

    def wakeup(self): # real signature unknown; restored from __doc__
        """ wakeup(self) """
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
        """ new() -> GLib.MainContext """
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.GLib', 'iteration': <function MainContext.iteration at 0x000001dd11de6160>, 'query': <function MainContext.query at 0x000001dd11de6200>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType GMainContext (257692144)>'
    __info__ = StructInfo(MainContext)


