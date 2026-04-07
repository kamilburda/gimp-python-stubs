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


Property = property


