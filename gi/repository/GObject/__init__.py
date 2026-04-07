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


# Variables with simple values

G_MAXDOUBLE = 1.7976931348623157e+308
G_MAXFLOAT = 3.4028234663852886e+38
G_MAXINT = 2147483647
G_MAXINT16 = 32767
G_MAXINT32 = 2147483647
G_MAXINT64 = 9223372036854775807
G_MAXINT8 = 127
G_MAXLONG = 2147483647
G_MAXOFFSET = 9223372036854775807
G_MAXSHORT = 32767
G_MAXSIZE = 18446744073709551615
G_MAXSSIZE = 9223372036854775807
G_MAXUINT = 4294967295
G_MAXUINT16 = 65535
G_MAXUINT32 = 4294967295
G_MAXUINT64 = 18446744073709551615
G_MAXUINT8 = 255
G_MAXULONG = 4294967295
G_MAXUSHORT = 65535
G_MINDOUBLE = 2.2250738585072014e-308
G_MINFLOAT = 1.1754943508222875e-38
G_MININT = -2147483648
G_MININT16 = -32768
G_MININT32 = -2147483648
G_MININT64 = -9223372036854775808
G_MININT8 = -128
G_MINLONG = -2147483648
G_MINOFFSET = -9223372036854775808
G_MINSHORT = -32768
G_MINSSIZE = -9223372036854775808

OPTION_REMAINING = ''

PARAM_CONSTRUCT = 4

PARAM_CONSTRUCT_ONLY = 8

PARAM_LAX_VALIDATION = 16

PARAM_MASK = 255
PARAM_READABLE = 1
PARAM_READWRITE = 3

PARAM_STATIC_STRINGS = 224

PARAM_USER_SHIFT = 8

PARAM_WRITABLE = 2

PRIORITY_DEFAULT = 0

PRIORITY_DEFAULT_IDLE = 200

PRIORITY_HIGH = -100

PRIORITY_HIGH_IDLE = 100

PRIORITY_LOW = 300

SIGNAL_ACTION = 32
SIGNAL_DETAILED = 16

SIGNAL_FLAGS_MASK = 511

SIGNAL_MATCH_MASK = 63

SIGNAL_NO_HOOKS = 64
SIGNAL_NO_RECURSE = 8

SIGNAL_RUN_CLEANUP = 4
SIGNAL_RUN_FIRST = 1
SIGNAL_RUN_LAST = 2

TYPE_FLAG_RESERVED_ID_BIT = 1

TYPE_FUNDAMENTAL_MAX = 1020
TYPE_FUNDAMENTAL_SHIFT = 2

TYPE_RESERVED_BSE_FIRST = 32
TYPE_RESERVED_BSE_LAST = 48

TYPE_RESERVED_GLIB_FIRST = 22
TYPE_RESERVED_GLIB_LAST = 31

TYPE_RESERVED_USER_FIRST = 49

VALUE_COLLECT_FORMAT_MAX_LENGTH = 8

VALUE_INTERNED_STRING = 268435456

VALUE_NOCOPY_CONTENTS = 134217728

_namespace = 'GObject'

_version = '2.0'

# functions

def boxed_copy(boxed_type, src_boxed): # real signature unknown; restored from __doc__
    """ boxed_copy(boxed_type:GType, src_boxed) """
    pass

def boxed_free(boxed_type, boxed): # real signature unknown; restored from __doc__
    """ boxed_free(boxed_type:GType, boxed) """
    pass

def boxed_type_register_static(name, boxed_copy, boxed_free): # real signature unknown; restored from __doc__
    """ boxed_type_register_static(name:str, boxed_copy:GObject.BoxedCopyFunc, boxed_free:GObject.BoxedFreeFunc) -> GType """
    return GType

def cclosure_marshal_BOOLEAN__BOXED_BOXED(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_BOOLEAN__BOXED_BOXED(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_BOOLEAN__FLAGS(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_BOOLEAN__FLAGS(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_generic(closure, return_gvalue, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_generic(closure:GObject.Closure, return_gvalue:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_STRING__OBJECT_POINTER(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_STRING__OBJECT_POINTER(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__BOOLEAN(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__BOOLEAN(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__BOXED(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__BOXED(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__CHAR(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__CHAR(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__DOUBLE(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__DOUBLE(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__ENUM(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__ENUM(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__FLAGS(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__FLAGS(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__FLOAT(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__FLOAT(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__INT(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__INT(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__LONG(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__LONG(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__OBJECT(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__OBJECT(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__PARAM(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__PARAM(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__POINTER(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__POINTER(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__STRING(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__STRING(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__UCHAR(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__UCHAR(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__UINT(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__UINT(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__UINT_POINTER(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__UINT_POINTER(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__ULONG(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__ULONG(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__VARIANT(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__VARIANT(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def cclosure_marshal_VOID__VOID(closure, return_value, n_param_values, param_values, invocation_hint=None, marshal_data=None): # real signature unknown; restored from __doc__
    """ cclosure_marshal_VOID__VOID(closure:GObject.Closure, return_value:GObject.Value, n_param_values:int, param_values:GObject.Value, invocation_hint=None, marshal_data=None) """
    pass

def child_watch_add(*args, **kwargs): # reliably restored by inspect
    """ child_watch_add(priority, pid, function, *data). """
    pass

def clear_signal_handler(handler_id_ptr, instance): # real signature unknown; restored from __doc__
    """ clear_signal_handler(handler_id_ptr:int, instance:GObject.Object) """
    pass

def enum_complete_type_info(g_enum_type, const_values): # real signature unknown; restored from __doc__
    """ enum_complete_type_info(g_enum_type:GType, const_values:list) -> info:GObject.TypeInfo """
    pass

def enum_get_value(enum_class, value): # real signature unknown; restored from __doc__
    """ enum_get_value(enum_class:GObject.EnumClass, value:int) -> GObject.EnumValue or None """
    pass

def enum_get_value_by_name(enum_class, name): # real signature unknown; restored from __doc__
    """ enum_get_value_by_name(enum_class:GObject.EnumClass, name:str) -> GObject.EnumValue or None """
    pass

def enum_get_value_by_nick(enum_class, nick): # real signature unknown; restored from __doc__
    """ enum_get_value_by_nick(enum_class:GObject.EnumClass, nick:str) -> GObject.EnumValue or None """
    pass

def enum_register_static(name, const_static_values): # real signature unknown; restored from __doc__
    """ enum_register_static(name:str, const_static_values:list) -> GType """
    return GType

def enum_to_string(g_enum_type, value): # real signature unknown; restored from __doc__
    """ enum_to_string(g_enum_type:GType, value:int) -> str """
    return ""

def filename_from_utf8(utf8string, len=-1): # reliably restored by inspect
    # no doc
    pass

def flags_complete_type_info(g_flags_type, const_values): # real signature unknown; restored from __doc__
    """ flags_complete_type_info(g_flags_type:GType, const_values:list) -> info:GObject.TypeInfo """
    pass

def flags_get_first_value(flags_class, value): # real signature unknown; restored from __doc__
    """ flags_get_first_value(flags_class:GObject.FlagsClass, value:int) -> GObject.FlagsValue or None """
    pass

def flags_get_value_by_name(flags_class, name): # real signature unknown; restored from __doc__
    """ flags_get_value_by_name(flags_class:GObject.FlagsClass, name:str) -> GObject.FlagsValue or None """
    pass

def flags_get_value_by_nick(flags_class, nick): # real signature unknown; restored from __doc__
    """ flags_get_value_by_nick(flags_class:GObject.FlagsClass, nick:str) -> GObject.FlagsValue or None """
    pass

def flags_register_static(name, const_static_values): # real signature unknown; restored from __doc__
    """ flags_register_static(name:str, const_static_values:list) -> GType """
    return GType

def flags_to_string(flags_type, value): # real signature unknown; restored from __doc__
    """ flags_to_string(flags_type:GType, value:int) -> str """
    return ""

def get_current_time(*args, **kwargs): # reliably restored by inspect
    # no doc
    pass

def gtype_get_type(): # real signature unknown; restored from __doc__
    """ gtype_get_type() -> GType """
    return GType

def idle_add(function, *user_data, priority=200): # reliably restored by inspect
    # no doc
    pass

def io_add_watch(*args, **kwargs): # reliably restored by inspect
    """ io_add_watch(channel, priority, condition, func, *user_data) -> event_source_id. """
    pass

def markup_escape_text(text, length=-1): # reliably restored by inspect
    # no doc
    pass

def param_spec_boolean(name, nick=None, blurb=None, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_boolean(name:str, nick:str=None, blurb:str=None, default_value:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_boxed(name, nick=None, blurb=None, boxed_type, flags): # real signature unknown; restored from __doc__
    """ param_spec_boxed(name:str, nick:str=None, blurb:str=None, boxed_type:GType, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_char(name, nick=None, blurb=None, minimum, maximum, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_char(name:str, nick:str=None, blurb:str=None, minimum:int, maximum:int, default_value:int, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_double(name, nick=None, blurb=None, minimum, maximum, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_double(name:str, nick:str=None, blurb:str=None, minimum:float, maximum:float, default_value:float, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_enum(name, nick=None, blurb=None, enum_type, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_enum(name:str, nick:str=None, blurb:str=None, enum_type:GType, default_value:int, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_flags(name, nick=None, blurb=None, flags_type, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_flags(name:str, nick:str=None, blurb:str=None, flags_type:GType, default_value:int, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_float(name, nick=None, blurb=None, minimum, maximum, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_float(name:str, nick:str=None, blurb:str=None, minimum:float, maximum:float, default_value:float, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_gtype(name, nick=None, blurb=None, is_a_type, flags): # real signature unknown; restored from __doc__
    """ param_spec_gtype(name:str, nick:str=None, blurb:str=None, is_a_type:GType, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_int(name, nick=None, blurb=None, minimum, maximum, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_int(name:str, nick:str=None, blurb:str=None, minimum:int, maximum:int, default_value:int, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_int64(name, nick=None, blurb=None, minimum, maximum, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_int64(name:str, nick:str=None, blurb:str=None, minimum:int, maximum:int, default_value:int, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_long(name, nick=None, blurb=None, minimum, maximum, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_long(name:str, nick:str=None, blurb:str=None, minimum:int, maximum:int, default_value:int, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_object(name, nick=None, blurb=None, object_type, flags): # real signature unknown; restored from __doc__
    """ param_spec_object(name:str, nick:str=None, blurb:str=None, object_type:GType, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_param(name, nick=None, blurb=None, param_type, flags): # real signature unknown; restored from __doc__
    """ param_spec_param(name:str, nick:str=None, blurb:str=None, param_type:GType, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_pointer(name, nick=None, blurb=None, flags): # real signature unknown; restored from __doc__
    """ param_spec_pointer(name:str, nick:str=None, blurb:str=None, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_string(name, nick=None, blurb=None, default_value=None, flags): # real signature unknown; restored from __doc__
    """ param_spec_string(name:str, nick:str=None, blurb:str=None, default_value:str=None, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_uchar(name, nick=None, blurb=None, minimum, maximum, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_uchar(name:str, nick:str=None, blurb:str=None, minimum:int, maximum:int, default_value:int, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_uint(name, nick=None, blurb=None, minimum, maximum, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_uint(name:str, nick:str=None, blurb:str=None, minimum:int, maximum:int, default_value:int, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_uint64(name, nick=None, blurb=None, minimum, maximum, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_uint64(name:str, nick:str=None, blurb:str=None, minimum:int, maximum:int, default_value:int, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_ulong(name, nick=None, blurb=None, minimum, maximum, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_ulong(name:str, nick:str=None, blurb:str=None, minimum:int, maximum:int, default_value:int, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_unichar(name, nick=None, blurb=None, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_unichar(name:str, nick:str=None, blurb:str=None, default_value:str, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_variant(name, nick=None, blurb=None, type, default_value=None, flags): # real signature unknown; restored from __doc__
    """ param_spec_variant(name:str, nick:str=None, blurb:str=None, type:GLib.VariantType, default_value:GLib.Variant=None, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_type_register_static(name, pspec_info): # real signature unknown; restored from __doc__
    """ param_type_register_static(name:str, pspec_info:GObject.ParamSpecTypeInfo) -> GType """
    return GType

def param_values_cmp(pspec, value1, value2): # real signature unknown; restored from __doc__
    """ param_values_cmp(pspec:GObject.ParamSpec, value1:GObject.Value, value2:GObject.Value) -> int """
    return 0

def param_value_convert(pspec, src_value, dest_value, strict_validation): # real signature unknown; restored from __doc__
    """ param_value_convert(pspec:GObject.ParamSpec, src_value:GObject.Value, dest_value:GObject.Value, strict_validation:bool) -> bool """
    return False

def param_value_defaults(pspec, value): # real signature unknown; restored from __doc__
    """ param_value_defaults(pspec:GObject.ParamSpec, value:GObject.Value) -> bool """
    return False

def param_value_is_valid(pspec, value): # real signature unknown; restored from __doc__
    """ param_value_is_valid(pspec:GObject.ParamSpec, value:GObject.Value) -> bool """
    return False

def param_value_set_default(pspec, value): # real signature unknown; restored from __doc__
    """ param_value_set_default(pspec:GObject.ParamSpec, value:GObject.Value) """
    pass

def param_value_validate(pspec, value): # real signature unknown; restored from __doc__
    """ param_value_validate(pspec:GObject.ParamSpec, value:GObject.Value) -> bool """
    return False

def pointer_type_register_static(name): # real signature unknown; restored from __doc__
    """ pointer_type_register_static(name:str) -> GType """
    return GType

def remove_emission_hook(obj, detailed_signal, hook_id): # reliably restored by inspect
    # no doc
    pass

def signal_accumulator_first_wins(ihint, return_accu, handler_return, user_data=None): # reliably restored by inspect
    # no doc
    pass

def signal_accumulator_true_handled(ihint, return_accu, handler_return, user_data=None): # reliably restored by inspect
    # no doc
    pass

def signal_add_emission_hook(signal_id, detail, hook_func): # real signature unknown; restored from __doc__
    """ signal_add_emission_hook(signal_id:int, detail:int, hook_func:GObject.SignalEmissionHook) -> int """
    return 0

def signal_chain_from_overridden(instance_and_params, return_value): # real signature unknown; restored from __doc__
    """ signal_chain_from_overridden(instance_and_params:list, return_value:GObject.Value) """
    pass

def signal_connect_closure(instance, detailed_signal, closure, after): # real signature unknown; restored from __doc__
    """ signal_connect_closure(instance:GObject.Object, detailed_signal:str, closure:GObject.Closure, after:bool) -> int """
    return 0

def signal_connect_closure_by_id(instance, signal_id, detail, closure, after): # real signature unknown; restored from __doc__
    """ signal_connect_closure_by_id(instance:GObject.Object, signal_id:int, detail:int, closure:GObject.Closure, after:bool) -> int """
    return 0

def signal_emitv(instance_and_params, signal_id, detail, return_value, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ signal_emitv(instance_and_params:list, signal_id:int, detail:int, return_value:GObject.Value=<optional>) -> return_value:GObject.Value """
    pass

def signal_get_invocation_hint(instance): # real signature unknown; restored from __doc__
    """ signal_get_invocation_hint(instance:GObject.Object) -> GObject.SignalInvocationHint or None """
    pass

def signal_handlers_block_matched(instance, mask, signal_id, detail, closure=None, func=None, data=None): # real signature unknown; restored from __doc__
    """ signal_handlers_block_matched(instance:GObject.Object, mask:GObject.SignalMatchType, signal_id:int, detail:int, closure:GObject.Closure=None, func=None, data=None) -> int """
    return 0

def signal_handlers_destroy(instance): # real signature unknown; restored from __doc__
    """ signal_handlers_destroy(instance:GObject.Object) """
    pass

def signal_handlers_disconnect_matched(instance, mask, signal_id, detail, closure=None, func=None, data=None): # real signature unknown; restored from __doc__
    """ signal_handlers_disconnect_matched(instance:GObject.Object, mask:GObject.SignalMatchType, signal_id:int, detail:int, closure:GObject.Closure=None, func=None, data=None) -> int """
    return 0

def signal_handlers_unblock_matched(instance, mask, signal_id, detail, closure=None, func=None, data=None): # real signature unknown; restored from __doc__
    """ signal_handlers_unblock_matched(instance:GObject.Object, mask:GObject.SignalMatchType, signal_id:int, detail:int, closure:GObject.Closure=None, func=None, data=None) -> int """
    return 0

def signal_handler_block(obj, handler_id): # reliably restored by inspect
    """
    Blocks the signal handler from being invoked until
        handler_unblock() is called.
    
        :param GObject.Object obj:
            Object instance to block handlers for.
        :param int handler_id:
            Id of signal to block.
        :returns:
            A context manager which optionally can be used to
            automatically unblock the handler:
    
        .. code-block:: python
    
            with GObject.signal_handler_block(obj, id):
                pass
    """
    pass

def signal_handler_disconnect(instance, handler_id): # real signature unknown; restored from __doc__
    """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
    pass

def signal_handler_find(instance, mask, signal_id, detail, closure=None, func=None, data=None): # real signature unknown; restored from __doc__
    """ signal_handler_find(instance:GObject.Object, mask:GObject.SignalMatchType, signal_id:int, detail:int, closure:GObject.Closure=None, func=None, data=None) -> int """
    return 0

def signal_handler_is_connected(instance, handler_id): # real signature unknown; restored from __doc__
    """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
    return False

def signal_handler_unblock(instance, handler_id): # real signature unknown; restored from __doc__
    """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
    pass

def signal_has_handler_pending(instance, signal_id, detail, may_be_blocked): # real signature unknown; restored from __doc__
    """ signal_has_handler_pending(instance:GObject.Object, signal_id:int, detail:int, may_be_blocked:bool) -> bool """
    return False

def signal_is_valid_name(name): # real signature unknown; restored from __doc__
    """ signal_is_valid_name(name:str) -> bool """
    return False

def signal_list_ids(type_): # reliably restored by inspect
    # no doc
    pass

def signal_list_names(type_): # reliably restored by inspect
    # no doc
    pass

def signal_lookup(name, type_): # reliably restored by inspect
    # no doc
    pass

def signal_name(signal_id): # real signature unknown; restored from __doc__
    """ signal_name(signal_id:int) -> str or None """
    return ""

def signal_override_class_closure(signal_id, instance_type, class_closure): # real signature unknown; restored from __doc__
    """ signal_override_class_closure(signal_id:int, instance_type:GType, class_closure:GObject.Closure) """
    pass

def signal_override_class_handler(signal_name, instance_type, class_handler): # real signature unknown; restored from __doc__
    """ signal_override_class_handler(signal_name:str, instance_type:GType, class_handler:GObject.Callback) """
    pass

def signal_parse_name(detailed_signal, itype, force_detail_quark): # reliably restored by inspect
    """
    Parse a detailed signal name into (signal_id, detail).
    
        :param str detailed_signal:
            Signal name which can include detail.
            For example: "notify:prop_name"
        :returns:
            Tuple of (signal_id, detail)
        :raises ValueError:
            If the given signal is unknown.
    """
    pass

def signal_query(id_or_name, type_=None): # reliably restored by inspect
    # no doc
    pass

def signal_remove_emission_hook(signal_id, hook_id): # real signature unknown; restored from __doc__
    """ signal_remove_emission_hook(signal_id:int, hook_id:int) """
    pass

def signal_stop_emission(instance, signal_id, detail): # real signature unknown; restored from __doc__
    """ signal_stop_emission(instance:GObject.Object, signal_id:int, detail:int) """
    pass

def signal_stop_emission_by_name(instance, detailed_signal): # real signature unknown; restored from __doc__
    """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
    pass

def signal_type_cclosure_new(itype, struct_offset): # real signature unknown; restored from __doc__
    """ signal_type_cclosure_new(itype:GType, struct_offset:int) -> GObject.Closure """
    pass

def source_set_closure(source, closure): # real signature unknown; restored from __doc__
    """ source_set_closure(source:GLib.Source, closure:GObject.Closure) """
    pass

def source_set_dummy_callback(source): # real signature unknown; restored from __doc__
    """ source_set_dummy_callback(source:GLib.Source) """
    pass

def strdup_value_contents(value): # real signature unknown; restored from __doc__
    """ strdup_value_contents(value:GObject.Value) -> str """
    return ""

def threads_init(): # reliably restored by inspect
    # no doc
    pass

def timeout_add(interval, function, *user_data, priority=0): # reliably restored by inspect
    # no doc
    pass

def timeout_add_seconds(interval, function, *user_data, priority=0): # reliably restored by inspect
    # no doc
    pass

def type_add_class_private(class_type, private_size): # real signature unknown; restored from __doc__
    """ type_add_class_private(class_type:GType, private_size:int) """
    pass

def type_add_instance_private(class_type, private_size): # real signature unknown; restored from __doc__
    """ type_add_instance_private(class_type:GType, private_size:int) -> int """
    return 0

def type_add_interface_dynamic(instance_type, interface_type, plugin): # real signature unknown; restored from __doc__
    """ type_add_interface_dynamic(instance_type:GType, interface_type:GType, plugin:GObject.TypePlugin) """
    pass

def type_add_interface_static(instance_type, interface_type, info): # real signature unknown; restored from __doc__
    """ type_add_interface_static(instance_type:GType, interface_type:GType, info:GObject.InterfaceInfo) """
    pass

def type_check_class_is_a(g_class, is_a_type): # real signature unknown; restored from __doc__
    """ type_check_class_is_a(g_class:GObject.TypeClass, is_a_type:GType) -> bool """
    return False

def type_check_instance(instance): # real signature unknown; restored from __doc__
    """ type_check_instance(instance:GObject.TypeInstance) -> bool """
    return False

def type_check_instance_is_a(instance, iface_type): # real signature unknown; restored from __doc__
    """ type_check_instance_is_a(instance:GObject.TypeInstance, iface_type:GType) -> bool """
    return False

def type_check_instance_is_fundamentally_a(instance, fundamental_type): # real signature unknown; restored from __doc__
    """ type_check_instance_is_fundamentally_a(instance:GObject.TypeInstance, fundamental_type:GType) -> bool """
    return False

def type_check_is_value_type(type): # real signature unknown; restored from __doc__
    """ type_check_is_value_type(type:GType) -> bool """
    return False

def type_check_value(value): # real signature unknown; restored from __doc__
    """ type_check_value(value:GObject.Value) -> bool """
    return False

def type_check_value_holds(value, type): # real signature unknown; restored from __doc__
    """ type_check_value_holds(value:GObject.Value, type:GType) -> bool """
    return False

def type_children(type): # real signature unknown; restored from __doc__
    """ type_children(type:GType) -> list """
    return []

def type_class_adjust_private_offset(g_class=None, private_size_or_offset): # real signature unknown; restored from __doc__
    """ type_class_adjust_private_offset(g_class=None, private_size_or_offset:int) """
    pass

def type_class_get(type): # real signature unknown; restored from __doc__
    """ type_class_get(type:GType) -> GObject.TypeClass """
    pass

def type_class_peek(type): # real signature unknown; restored from __doc__
    """ type_class_peek(type:GType) -> GObject.TypeClass or None """
    pass

def type_class_peek_static(type): # real signature unknown; restored from __doc__
    """ type_class_peek_static(type:GType) -> GObject.TypeClass or None """
    pass

def type_class_ref(type): # real signature unknown; restored from __doc__
    """ type_class_ref(type:GType) -> GObject.TypeClass """
    pass

def type_default_interface_get(g_type): # real signature unknown; restored from __doc__
    """ type_default_interface_get(g_type:GType) -> GObject.TypeInterface """
    pass

def type_default_interface_peek(g_type): # real signature unknown; restored from __doc__
    """ type_default_interface_peek(g_type:GType) -> GObject.TypeInterface """
    pass

def type_default_interface_ref(g_type): # real signature unknown; restored from __doc__
    """ type_default_interface_ref(g_type:GType) -> GObject.TypeInterface """
    pass

def type_default_interface_unref(g_iface): # real signature unknown; restored from __doc__
    """ type_default_interface_unref(g_iface:GObject.TypeInterface) """
    pass

def type_depth(type): # real signature unknown; restored from __doc__
    """ type_depth(type:GType) -> int """
    return 0

def type_ensure(type): # real signature unknown; restored from __doc__
    """ type_ensure(type:GType) """
    pass

def type_free_instance(instance): # real signature unknown; restored from __doc__
    """ type_free_instance(instance:GObject.TypeInstance) """
    pass

def type_from_name(name): # reliably restored by inspect
    # no doc
    pass

def type_fundamental(type_id): # real signature unknown; restored from __doc__
    """ type_fundamental(type_id:GType) -> GType """
    return GType

def type_fundamental_next(): # real signature unknown; restored from __doc__
    """ type_fundamental_next() -> GType """
    return GType

def type_get_instance_count(type): # real signature unknown; restored from __doc__
    """ type_get_instance_count(type:GType) -> int """
    return 0

def type_get_plugin(type): # real signature unknown; restored from __doc__
    """ type_get_plugin(type:GType) -> GObject.TypePlugin """
    pass

def type_get_qdata(type, quark): # real signature unknown; restored from __doc__
    """ type_get_qdata(type:GType, quark:int) """
    pass

def type_get_type_registration_serial(): # real signature unknown; restored from __doc__
    """ type_get_type_registration_serial() -> int """
    return 0

def type_init(): # real signature unknown; restored from __doc__
    """ type_init() """
    pass

def type_init_with_debug_flags(debug_flags): # real signature unknown; restored from __doc__
    """ type_init_with_debug_flags(debug_flags:GObject.TypeDebugFlags) """
    pass

def type_interfaces(type): # real signature unknown; restored from __doc__
    """ type_interfaces(type:GType) -> list """
    return []

def type_interface_add_prerequisite(interface_type, prerequisite_type): # real signature unknown; restored from __doc__
    """ type_interface_add_prerequisite(interface_type:GType, prerequisite_type:GType) """
    pass

def type_interface_get_plugin(instance_type, interface_type): # real signature unknown; restored from __doc__
    """ type_interface_get_plugin(instance_type:GType, interface_type:GType) -> GObject.TypePlugin """
    pass

def type_interface_instantiatable_prerequisite(interface_type): # real signature unknown; restored from __doc__
    """ type_interface_instantiatable_prerequisite(interface_type:GType) -> GType """
    return GType

def type_interface_peek(instance_class, iface_type): # real signature unknown; restored from __doc__
    """ type_interface_peek(instance_class:GObject.TypeClass, iface_type:GType) -> GObject.TypeInterface or None """
    pass

def type_interface_prerequisites(interface_type): # real signature unknown; restored from __doc__
    """ type_interface_prerequisites(interface_type:GType) -> list """
    return []

def type_is_a(type, is_a_type): # real signature unknown; restored from __doc__
    """ type_is_a(type:GType, is_a_type:GType) -> bool """
    return False

def type_name(type): # real signature unknown; restored from __doc__
    """ type_name(type:GType) -> str or None """
    return ""

def type_name_from_class(g_class): # real signature unknown; restored from __doc__
    """ type_name_from_class(g_class:GObject.TypeClass) -> str """
    return ""

def type_name_from_instance(instance): # real signature unknown; restored from __doc__
    """ type_name_from_instance(instance:GObject.TypeInstance) -> str """
    return ""

def type_next_base(leaf_type, root_type): # real signature unknown; restored from __doc__
    """ type_next_base(leaf_type:GType, root_type:GType) -> GType """
    return GType

def type_parent(type_): # reliably restored by inspect
    # no doc
    pass

def type_qname(type): # real signature unknown; restored from __doc__
    """ type_qname(type:GType) -> int """
    return 0

def type_query(type): # real signature unknown; restored from __doc__
    """ type_query(type:GType) -> query:GObject.TypeQuery """
    pass

def type_register_dynamic(parent_type, type_name, plugin, flags): # real signature unknown; restored from __doc__
    """ type_register_dynamic(parent_type:GType, type_name:str, plugin:GObject.TypePlugin, flags:GObject.TypeFlags) -> GType """
    return GType

def type_register_fundamental(type_id, type_name, info, finfo, flags): # real signature unknown; restored from __doc__
    """ type_register_fundamental(type_id:GType, type_name:str, info:GObject.TypeInfo, finfo:GObject.TypeFundamentalInfo, flags:GObject.TypeFlags) -> GType """
    return GType

def type_register_static(parent_type, type_name, info, flags): # real signature unknown; restored from __doc__
    """ type_register_static(parent_type:GType, type_name:str, info:GObject.TypeInfo, flags:GObject.TypeFlags) -> GType """
    return GType

def type_set_qdata(type, quark, data=None): # real signature unknown; restored from __doc__
    """ type_set_qdata(type:GType, quark:int, data=None) """
    pass

def type_test_flags(type, flags): # real signature unknown; restored from __doc__
    """ type_test_flags(type:GType, flags:int) -> bool """
    return False

def value_type_compatible(src_type, dest_type): # real signature unknown; restored from __doc__
    """ value_type_compatible(src_type:GType, dest_type:GType) -> bool """
    return False

def value_type_transformable(src_type, dest_type): # real signature unknown; restored from __doc__
    """ value_type_transformable(src_type:GType, dest_type:GType) -> bool """
    return False

def variant_get_gtype(): # real signature unknown; restored from __doc__
    """ variant_get_gtype() -> GType """
    return GType

# classes

from .Array import Array
from .Object import Object
from .GObject import GObject
from .Binding import Binding
from .BindingFlags import BindingFlags
from .BindingGroup import BindingGroup
from .BookmarkFile import BookmarkFile
from .ByteArray import ByteArray
from .Bytes import Bytes
from .CClosure import CClosure
from .Checksum import Checksum
from .Closure import Closure
from .ClosureNotifyData import ClosureNotifyData
from .ConnectFlags import ConnectFlags
from .Date import Date
from .DateTime import DateTime
from .Dir import Dir
from .EnumClass import EnumClass
from .EnumValue import EnumValue
from .FlagsClass import FlagsClass
from .FlagsValue import FlagsValue
from .Float import Float
from .ParamSpec import ParamSpec
from .GParamSpec import GParamSpec
from .HashTable import HashTable
from .Hmac import Hmac
from .Source import Source
from .Idle import Idle
from .InitiallyUnowned import InitiallyUnowned
from .InitiallyUnownedClass import InitiallyUnownedClass
from .InterfaceInfo import InterfaceInfo
from .IOChannel import IOChannel
from .KeyFile import KeyFile
from .MainContext import MainContext
from .MainLoop import MainLoop
from .MappedFile import MappedFile
from .MarkupParseContext import MarkupParseContext
from .MatchInfo import MatchInfo
from .ObjectClass import ObjectClass
from .ObjectConstructParam import ObjectConstructParam
from .Parameter import Parameter
from .ParamFlags import ParamFlags
from .ParamSpecBoolean import ParamSpecBoolean
from .ParamSpecBoxed import ParamSpecBoxed
from .ParamSpecChar import ParamSpecChar
from .ParamSpecClass import ParamSpecClass
from .ParamSpecDouble import ParamSpecDouble
from .ParamSpecEnum import ParamSpecEnum
from .ParamSpecFlags import ParamSpecFlags
from .ParamSpecFloat import ParamSpecFloat
from .ParamSpecGType import ParamSpecGType
from .ParamSpecInt import ParamSpecInt
from .ParamSpecInt64 import ParamSpecInt64
from .ParamSpecLong import ParamSpecLong
from .ParamSpecObject import ParamSpecObject
from .ParamSpecOverride import ParamSpecOverride
from .ParamSpecParam import ParamSpecParam
from .ParamSpecPointer import ParamSpecPointer
from .ParamSpecPool import ParamSpecPool
from .ParamSpecString import ParamSpecString
from .ParamSpecTypeInfo import ParamSpecTypeInfo
from .ParamSpecUChar import ParamSpecUChar
from .ParamSpecUInt import ParamSpecUInt
from .ParamSpecUInt64 import ParamSpecUInt64
from .ParamSpecULong import ParamSpecULong
from .ParamSpecUnichar import ParamSpecUnichar
from .ParamSpecValueArray import ParamSpecValueArray
from .ParamSpecVariant import ParamSpecVariant
from .PatternSpec import PatternSpec
from .PollFD import PollFD
from .property import property
from .Property import Property
from .PtrArray import PtrArray
from .Rand import Rand
from .Regex import Regex
from .Signal import Signal
from .SignalFlags import SignalFlags
from .SignalGroup import SignalGroup
from .SignalInvocationHint import SignalInvocationHint
from .SignalMatchType import SignalMatchType
from .SignalOverride import SignalOverride
from .SignalQuery import SignalQuery
from .String import String
from .Strv import Strv
from .StrvBuilder import StrvBuilder
from .Thread import Thread
from .Timeout import Timeout
from .TimeZone import TimeZone
from .Tree import Tree
from .TypeClass import TypeClass
from .TypeCValue import TypeCValue
from .TypeDebugFlags import TypeDebugFlags
from .TypeFlags import TypeFlags
from .TypeFundamentalFlags import TypeFundamentalFlags
from .TypeFundamentalInfo import TypeFundamentalInfo
from .TypeInfo import TypeInfo
from .TypeInstance import TypeInstance
from .TypeInterface import TypeInterface
from .TypePlugin import TypePlugin
from .TypeModule import TypeModule
from .TypeModuleClass import TypeModuleClass
from .TypePluginClass import TypePluginClass
from .TypeQuery import TypeQuery
from .TypeValueTable import TypeValueTable
from .Uri import Uri
from .Value import Value
from .ValueArray import ValueArray
from .VariantBuilder import VariantBuilder
from .VariantDict import VariantDict
from .VariantType import VariantType
from .WeakRef import WeakRef
from ._Value__data__union import _Value__data__union
# variables with complex values

features = {
    'generic-c-marshaller': True,
}

glib_version = (
    2,
    86,
    3,
)

pygobject_version = (
    3,
    54,
    5,
)

TYPE_BOOLEAN = None # (!) real value is '<GType gboolean (20)>'

TYPE_BOXED = None # (!) real value is '<GType GBoxed (72)>'

TYPE_CHAR = None # (!) real value is '<GType gchar (12)>'

TYPE_DOUBLE = None # (!) real value is '<GType gdouble (60)>'

TYPE_ENUM = None # (!) real value is '<GType GEnum (48)>'

TYPE_FLAGS = None # (!) real value is '<GType GFlags (52)>'

TYPE_FLOAT = None # (!) real value is '<GType gfloat (56)>'

TYPE_GSTRING = None # (!) real value is '<GType GString (255840976)>'

TYPE_GTYPE = None # (!) real value is '<GType GType (252362848)>'

TYPE_INT = None # (!) real value is '<GType gint (24)>'

TYPE_INT64 = None # (!) real value is '<GType gint64 (40)>'

TYPE_INTERFACE = None # (!) real value is '<GType GInterface (8)>'

TYPE_INVALID = None # (!) real value is '<GType invalid (0)>'

TYPE_LONG = None # (!) real value is '<GType glong (32)>'

TYPE_NONE = None # (!) real value is '<GType void (4)>'

TYPE_OBJECT = None # (!) real value is '<GType GObject (80)>'

TYPE_PARAM = None # (!) real value is '<GType GParam (76)>'

TYPE_POINTER = None # (!) real value is '<GType gpointer (68)>'

TYPE_PYOBJECT = None # (!) real value is '<GType PyObject (255842896)>'

TYPE_STRING = None # (!) real value is '<GType gchararray (64)>'

TYPE_STRV = None # (!) real value is '<GType GStrv (255842032)>'

TYPE_UCHAR = None # (!) real value is '<GType guchar (16)>'

TYPE_UINT = None # (!) real value is '<GType guint (28)>'

TYPE_UINT64 = None # (!) real value is '<GType guint64 (44)>'

TYPE_ULONG = None # (!) real value is '<GType gulong (36)>'

TYPE_UNICHAR = TYPE_UINT

TYPE_VALUE = None # (!) real value is '<GType GValue (265149856)>'

TYPE_VARIANT = None # (!) real value is '<GType GVariant (84)>'

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x000001dd0f966fc0>'

__path__ = []

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GObject', loader=<gi.importer.DynamicImporter object at 0x000001dd0f966fc0>)"

