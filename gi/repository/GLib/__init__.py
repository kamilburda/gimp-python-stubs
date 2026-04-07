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


# Variables with simple values

ALLOCATOR_LIST = 1
ALLOCATOR_NODE = 3
ALLOCATOR_SLIST = 2

ALLOC_AND_FREE = 2

ALLOC_ONLY = 1

ANALYZER_ANALYZING = 1

ASCII_DTOSTR_BUF_SIZE = 39

ATOMIC_REF_COUNT_INIT = 1

BIG_ENDIAN = 4321

CSET_A_2_Z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

CSET_a_2_z = 'abcdefghijklmnopqrstuvwxyz'

CSET_DIGITS = '0123456789'

C_STD_VERSION = 199000

DATALIST_FLAGS_MASK = 3

DATE_BAD_DAY = 0
DATE_BAD_JULIAN = 0
DATE_BAD_YEAR = 0

DIR_SEPARATOR = 92

DIR_SEPARATOR_S = '\\'
E = 2.718282

GINT16_FORMAT = 'hi'
GINT16_MODIFIER = 'h'

GINT32_FORMAT = 'i'
GINT32_MODIFIER = ''

GINT64_FORMAT = 'lli'
GINT64_MODIFIER = 'll'

GINTPTR_FORMAT = 'lli'
GINTPTR_MODIFIER = 'll'

GNUC_FUNCTION = ''

GNUC_PRETTY_FUNCTION = ''

GSIZE_FORMAT = 'llu'
GSIZE_MODIFIER = 'll'

GSSIZE_FORMAT = 'lli'
GSSIZE_MODIFIER = 'll'

GUINT16_FORMAT = 'hu'

GUINT32_FORMAT = 'u'

GUINT64_FORMAT = 'llu'

GUINTPTR_FORMAT = 'llu'

HAVE_GINT64 = 1

HAVE_GNUC_VARARGS = 1
HAVE_GNUC_VISIBILITY = 1

HAVE_GROWING_STACK = 0

HAVE_ISO_VARARGS = 1

HOOK_FLAG_USER_SHIFT = 4

IEEE754_DOUBLE_BIAS = 1023

IEEE754_FLOAT_BIAS = 127

IO_ERR = 8

IO_FLAG_APPEND = 1

IO_FLAG_GET_MASK = 31

IO_FLAG_IS_READABLE = 4
IO_FLAG_IS_SEEKABLE = 16
IO_FLAG_IS_WRITEABLE = 8

IO_FLAG_MASK = 31
IO_FLAG_NONBLOCK = 2

IO_FLAG_SET_MASK = 3

IO_HUP = 16
IO_IN = 1
IO_NVAL = 32
IO_OUT = 4
IO_PRI = 2

IO_STATUS_AGAIN = 3
IO_STATUS_EOF = 2
IO_STATUS_ERROR = 0
IO_STATUS_NORMAL = 1

KEY_FILE_DESKTOP_GROUP = 'Desktop Entry'

KEY_FILE_DESKTOP_KEY_ACTIONS = 'Actions'
KEY_FILE_DESKTOP_KEY_CATEGORIES = 'Categories'
KEY_FILE_DESKTOP_KEY_COMMENT = 'Comment'

KEY_FILE_DESKTOP_KEY_DBUS_ACTIVATABLE = 'DBusActivatable'

KEY_FILE_DESKTOP_KEY_EXEC = 'Exec'

KEY_FILE_DESKTOP_KEY_GENERIC_NAME = 'GenericName'

KEY_FILE_DESKTOP_KEY_HIDDEN = 'Hidden'
KEY_FILE_DESKTOP_KEY_ICON = 'Icon'

KEY_FILE_DESKTOP_KEY_MIME_TYPE = 'MimeType'

KEY_FILE_DESKTOP_KEY_NAME = 'Name'

KEY_FILE_DESKTOP_KEY_NOT_SHOW_IN = 'NotShowIn'

KEY_FILE_DESKTOP_KEY_NO_DISPLAY = 'NoDisplay'

KEY_FILE_DESKTOP_KEY_ONLY_SHOW_IN = 'OnlyShowIn'

KEY_FILE_DESKTOP_KEY_PATH = 'Path'

KEY_FILE_DESKTOP_KEY_STARTUP_NOTIFY = 'StartupNotify'

KEY_FILE_DESKTOP_KEY_STARTUP_WM_CLASS = 'StartupWMClass'

KEY_FILE_DESKTOP_KEY_TERMINAL = 'Terminal'

KEY_FILE_DESKTOP_KEY_TRY_EXEC = 'TryExec'

KEY_FILE_DESKTOP_KEY_TYPE = 'Type'
KEY_FILE_DESKTOP_KEY_URL = 'URL'
KEY_FILE_DESKTOP_KEY_VERSION = 'Version'

KEY_FILE_DESKTOP_TYPE_APPLICATION = 'Application'
KEY_FILE_DESKTOP_TYPE_DIRECTORY = 'Directory'
KEY_FILE_DESKTOP_TYPE_LINK = 'Link'

LITTLE_ENDIAN = 1234

LN10 = 2.302585
LN2 = 0.693147

LOG_2_BASE_10 = 0.30103

LOG_DOMAIN = 0

LOG_FATAL_MASK = 5

LOG_LEVEL_USER_SHIFT = 8

macro__has_attribute_ifunc = 0

macro__has_attribute_no_sanitize_address = 0

macro__has_attribute___noreturn__ = 0

MAJOR_VERSION = 2

MAXDOUBLE = 1.7976931348623157e+308
MAXFLOAT = 3.4028234663852886e+38
MAXINT = 2147483647
MAXINT16 = 32767
MAXINT32 = 2147483647
MAXINT64 = 9223372036854775807
MAXINT8 = 127
MAXLONG = 2147483647
MAXOFFSET = 9223372036854775807
MAXSHORT = 32767
MAXSIZE = 18446744073709551615
MAXSSIZE = 9223372036854775807
MAXUINT = 4294967295
MAXUINT16 = 65535
MAXUINT32 = 4294967295
MAXUINT64 = 18446744073709551615
MAXUINT8 = 255
MAXULONG = 4294967295
MAXUSHORT = 65535

MICRO_VERSION = 4

MINDOUBLE = 2.2250738585072014e-308
MINFLOAT = 1.1754943508222875e-38
MININT = -2147483648
MININT16 = -32768
MININT32 = -2147483648
MININT64 = -9223372036854775808
MININT8 = -128
MINLONG = -2147483648
MINOFFSET = -9223372036854775808

MINOR_VERSION = 86

MINSHORT = -32768
MINSSIZE = -9223372036854775808

MODULE_SUFFIX = 'dll'

OPTION_ERROR_BAD_VALUE = 1

OPTION_ERROR_FAILED = 2

OPTION_ERROR_UNKNOWN_OPTION = 0

OPTION_FLAG_FILENAME = 16
OPTION_FLAG_HIDDEN = 1

OPTION_FLAG_IN_MAIN = 2

OPTION_FLAG_NOALIAS = 64

OPTION_FLAG_NO_ARG = 8

OPTION_FLAG_OPTIONAL_ARG = 32

OPTION_FLAG_REVERSE = 4

OPTION_REMAINING = ''

PDP_ENDIAN = 3412

PI = 3.141593

PID_FORMAT = 'p'

PI_2 = 1.570796
PI_4 = 0.785398

POLLFD_FORMAT = '%#llx'

PRIORITY_DEFAULT = 0

PRIORITY_DEFAULT_IDLE = 200

PRIORITY_HIGH = -100

PRIORITY_HIGH_IDLE = 100

PRIORITY_LOW = 300

REF_COUNT_INIT = -1

SEARCHPATH_SEPARATOR = 59

SEARCHPATH_SEPARATOR_S = ';'

SIZEOF_LONG = 4

SIZEOF_SIZE_T = 8

SIZEOF_SSIZE_T = 8

SIZEOF_VOID_P = 8

SOURCE_CONTINUE = True
SOURCE_REMOVE = False

SPAWN_CHILD_INHERITS_STDIN = 32

SPAWN_DO_NOT_REAP_CHILD = 2

SPAWN_FILE_AND_ARGV_ZERO = 64

SPAWN_LEAVE_DESCRIPTORS_OPEN = 1

SPAWN_SEARCH_PATH = 4

SPAWN_STDERR_TO_DEV_NULL = 16

SPAWN_STDOUT_TO_DEV_NULL = 8

SQRT2 = 1.414214

STR_DELIMITERS = '_-|> <.'

SYSDEF_AF_INET = 2
SYSDEF_AF_INET6 = 23
SYSDEF_AF_UNIX = 1

SYSDEF_MSG_DONTROUTE = 4
SYSDEF_MSG_OOB = 1
SYSDEF_MSG_PEEK = 2

TEST_OPTION_ISOLATE_DIRS = 'isolate_dirs'

TEST_OPTION_NONFATAL_ASSERTIONS = 'nonfatal-assertions'

TEST_OPTION_NO_PRGNAME = 'no_g_set_prgname'

TIME_SPAN_DAY = 86400000000
TIME_SPAN_HOUR = 3600000000
TIME_SPAN_MILLISECOND = 1000
TIME_SPAN_MINUTE = 60000000
TIME_SPAN_SECOND = 1000000

UNICHAR_MAX_DECOMPOSITION_LENGTH = 18

URI_RESERVED_CHARS_GENERIC_DELIMITERS = ':/?#[]@'

URI_RESERVED_CHARS_SUBCOMPONENT_DELIMITERS = "!$&'()*+,;="

USEC_PER_SEC = 1000000

USER_DIRECTORY_DESKTOP = 0
USER_DIRECTORY_DOCUMENTS = 1
USER_DIRECTORY_DOWNLOAD = 2
USER_DIRECTORY_MUSIC = 3
USER_DIRECTORY_PICTURES = 4

USER_DIRECTORY_PUBLIC_SHARE = 5

USER_DIRECTORY_TEMPLATES = 6
USER_DIRECTORY_VIDEOS = 7

VERSION_MIN_REQUIRED = 2

WIN32_MSG_HANDLE = 19981206

_namespace = 'GLib'

_version = '2.0'

# functions

def abort(): # real signature unknown; restored from __doc__
    """ abort() """
    pass

def access(filename, mode): # real signature unknown; restored from __doc__
    """ access(filename:str, mode:int) -> int """
    return 0

def aligned_alloc(n_blocks, n_block_bytes, alignment): # real signature unknown; restored from __doc__
    """ aligned_alloc(n_blocks:int, n_block_bytes:int, alignment:int) """
    pass

def aligned_alloc0(n_blocks, n_block_bytes, alignment): # real signature unknown; restored from __doc__
    """ aligned_alloc0(n_blocks:int, n_block_bytes:int, alignment:int) """
    pass

def aligned_free(mem=None): # real signature unknown; restored from __doc__
    """ aligned_free(mem=None) """
    pass

def aligned_free_sized(mem=None, alignment, size): # real signature unknown; restored from __doc__
    """ aligned_free_sized(mem=None, alignment:int, size:int) """
    pass

def ascii_digit_value(c): # real signature unknown; restored from __doc__
    """ ascii_digit_value(c:int) -> int """
    return 0

def ascii_dtostr(buffer, buf_len, d): # real signature unknown; restored from __doc__
    """ ascii_dtostr(buffer:str, buf_len:int, d:float) -> str """
    return ""

def ascii_formatd(buffer, buf_len, format, d): # real signature unknown; restored from __doc__
    """ ascii_formatd(buffer:str, buf_len:int, format:str, d:float) -> str """
    return ""

def ascii_strcasecmp(s1, s2): # real signature unknown; restored from __doc__
    """ ascii_strcasecmp(s1:str, s2:str) -> int """
    return 0

def ascii_strdown(p_str, len): # real signature unknown; restored from __doc__
    """ ascii_strdown(str:str, len:int) -> str """
    return ""

def ascii_string_to_signed(p_str, base, min, max): # real signature unknown; restored from __doc__
    """ ascii_string_to_signed(str:str, base:int, min:int, max:int) -> bool, out_num:int """
    return False

def ascii_string_to_unsigned(p_str, base, min, max): # real signature unknown; restored from __doc__
    """ ascii_string_to_unsigned(str:str, base:int, min:int, max:int) -> bool, out_num:int """
    return False

def ascii_strncasecmp(s1, s2, n): # real signature unknown; restored from __doc__
    """ ascii_strncasecmp(s1:str, s2:str, n:int) -> int """
    return 0

def ascii_strtod(nptr): # real signature unknown; restored from __doc__
    """ ascii_strtod(nptr:str) -> float, endptr:str """
    return 0.0

def ascii_strtoll(nptr, base): # real signature unknown; restored from __doc__
    """ ascii_strtoll(nptr:str, base:int) -> int, endptr:str """
    return 0

def ascii_strtoull(nptr, base): # real signature unknown; restored from __doc__
    """ ascii_strtoull(nptr:str, base:int) -> int, endptr:str """
    return 0

def ascii_strup(p_str, len): # real signature unknown; restored from __doc__
    """ ascii_strup(str:str, len:int) -> str """
    return ""

def ascii_tolower(c): # real signature unknown; restored from __doc__
    """ ascii_tolower(c:int) -> int """
    return 0

def ascii_toupper(c): # real signature unknown; restored from __doc__
    """ ascii_toupper(c:int) -> int """
    return 0

def ascii_xdigit_value(c): # real signature unknown; restored from __doc__
    """ ascii_xdigit_value(c:int) -> int """
    return 0

def assertion_message(domain, file, line, func, message): # real signature unknown; restored from __doc__
    """ assertion_message(domain:str, file:str, line:int, func:str, message:str) """
    pass

def assertion_message_cmpint(domain, file, line, func, expr, arg1, cmp, arg2, numtype): # real signature unknown; restored from __doc__
    """ assertion_message_cmpint(domain:str, file:str, line:int, func:str, expr:str, arg1:int, cmp:str, arg2:int, numtype:int) """
    pass

def assertion_message_cmpstr(domain, file, line, func, expr, arg1, cmp, arg2): # real signature unknown; restored from __doc__
    """ assertion_message_cmpstr(domain:str, file:str, line:int, func:str, expr:str, arg1:str, cmp:str, arg2:str) """
    pass

def assertion_message_cmpstrv(domain, file, line, func, expr, arg1, arg2, first_wrong_idx): # real signature unknown; restored from __doc__
    """ assertion_message_cmpstrv(domain:str, file:str, line:int, func:str, expr:str, arg1:str, arg2:str, first_wrong_idx:int) """
    pass

def assertion_message_error(domain, file, line, func, expr, error, error_domain, error_code): # real signature unknown; restored from __doc__
    """ assertion_message_error(domain:str, file:str, line:int, func:str, expr:str, error:error, error_domain:int, error_code:int) """
    pass

def assert_warning(log_domain, file, line, pretty_function, expression): # real signature unknown; restored from __doc__
    """ assert_warning(log_domain:str, file:str, line:int, pretty_function:str, expression:str) """
    pass

def async_queue_new(): # real signature unknown; restored from __doc__
    """ async_queue_new() -> GLib.AsyncQueue """
    pass

def async_queue_new_full(item_free_func=None): # real signature unknown; restored from __doc__
    """ async_queue_new_full(item_free_func:GLib.DestroyNotify=None) -> GLib.AsyncQueue """
    pass

def atexit(func): # real signature unknown; restored from __doc__
    """ atexit(func:GLib.VoidFunc) """
    pass

def atomic_int_add(atomic=None, val): # real signature unknown; restored from __doc__
    """ atomic_int_add(atomic=None, val:int) -> int """
    return 0

def atomic_int_and(atomic=None, val): # real signature unknown; restored from __doc__
    """ atomic_int_and(atomic=None, val:int) -> int """
    return 0

def atomic_int_compare_and_exchange(atomic=None, oldval, newval): # real signature unknown; restored from __doc__
    """ atomic_int_compare_and_exchange(atomic=None, oldval:int, newval:int) -> bool """
    return False

def atomic_int_compare_and_exchange_full(atomic=None, oldval, newval): # real signature unknown; restored from __doc__
    """ atomic_int_compare_and_exchange_full(atomic=None, oldval:int, newval:int) -> bool, preval:int """
    return False

def atomic_int_dec_and_test(atomic=None): # real signature unknown; restored from __doc__
    """ atomic_int_dec_and_test(atomic=None) -> bool """
    return False

def atomic_int_exchange(atomic=None, newval): # real signature unknown; restored from __doc__
    """ atomic_int_exchange(atomic=None, newval:int) -> int """
    return 0

def atomic_int_exchange_and_add(atomic=None, val): # real signature unknown; restored from __doc__
    """ atomic_int_exchange_and_add(atomic=None, val:int) -> int """
    return 0

def atomic_int_get(atomic=None): # real signature unknown; restored from __doc__
    """ atomic_int_get(atomic=None) -> int """
    return 0

def atomic_int_inc(atomic=None): # real signature unknown; restored from __doc__
    """ atomic_int_inc(atomic=None) """
    pass

def atomic_int_or(atomic=None, val): # real signature unknown; restored from __doc__
    """ atomic_int_or(atomic=None, val:int) -> int """
    return 0

def atomic_int_set(atomic=None, newval): # real signature unknown; restored from __doc__
    """ atomic_int_set(atomic=None, newval:int) """
    pass

def atomic_int_xor(atomic=None, val): # real signature unknown; restored from __doc__
    """ atomic_int_xor(atomic=None, val:int) -> int """
    return 0

def atomic_pointer_add(atomic, val): # real signature unknown; restored from __doc__
    """ atomic_pointer_add(atomic, val:int) -> int """
    return 0

def atomic_pointer_and(atomic, val): # real signature unknown; restored from __doc__
    """ atomic_pointer_and(atomic, val:int) -> int """
    return 0

def atomic_pointer_compare_and_exchange(atomic, oldval=None, newval=None): # real signature unknown; restored from __doc__
    """ atomic_pointer_compare_and_exchange(atomic, oldval=None, newval=None) -> bool """
    return False

def atomic_pointer_compare_and_exchange_full(atomic, oldval=None, newval=None): # real signature unknown; restored from __doc__
    """ atomic_pointer_compare_and_exchange_full(atomic, oldval=None, newval=None) -> bool, preval """
    return False

def atomic_pointer_exchange(atomic=None, newval=None): # real signature unknown; restored from __doc__
    """ atomic_pointer_exchange(atomic=None, newval=None) """
    pass

def atomic_pointer_get(atomic): # real signature unknown; restored from __doc__
    """ atomic_pointer_get(atomic) """
    pass

def atomic_pointer_or(atomic, val): # real signature unknown; restored from __doc__
    """ atomic_pointer_or(atomic, val:int) -> int """
    return 0

def atomic_pointer_set(atomic, newval=None): # real signature unknown; restored from __doc__
    """ atomic_pointer_set(atomic, newval=None) """
    pass

def atomic_pointer_xor(atomic, val): # real signature unknown; restored from __doc__
    """ atomic_pointer_xor(atomic, val:int) -> int """
    return 0

def atomic_rc_box_acquire(mem_block): # real signature unknown; restored from __doc__
    """ atomic_rc_box_acquire(mem_block) """
    pass

def atomic_rc_box_alloc(block_size): # real signature unknown; restored from __doc__
    """ atomic_rc_box_alloc(block_size:int) """
    pass

def atomic_rc_box_alloc0(block_size): # real signature unknown; restored from __doc__
    """ atomic_rc_box_alloc0(block_size:int) """
    pass

def atomic_rc_box_dup(block_size, mem_block): # real signature unknown; restored from __doc__
    """ atomic_rc_box_dup(block_size:int, mem_block) """
    pass

def atomic_rc_box_get_size(mem_block): # real signature unknown; restored from __doc__
    """ atomic_rc_box_get_size(mem_block) -> int """
    return 0

def atomic_rc_box_release(mem_block): # real signature unknown; restored from __doc__
    """ atomic_rc_box_release(mem_block) """
    pass

def atomic_rc_box_release_full(mem_block, clear_func): # real signature unknown; restored from __doc__
    """ atomic_rc_box_release_full(mem_block, clear_func:GLib.DestroyNotify) """
    pass

def atomic_ref_count_compare(arc, val): # real signature unknown; restored from __doc__
    """ atomic_ref_count_compare(arc:int, val:int) -> bool """
    return False

def atomic_ref_count_dec(arc): # real signature unknown; restored from __doc__
    """ atomic_ref_count_dec(arc:int) -> bool """
    return False

def atomic_ref_count_inc(arc): # real signature unknown; restored from __doc__
    """ atomic_ref_count_inc(arc:int) """
    pass

def atomic_ref_count_init(): # real signature unknown; restored from __doc__
    """ atomic_ref_count_init() -> arc:int """
    pass

def base64_decode(text): # real signature unknown; restored from __doc__
    """ base64_decode(text:str) -> list """
    return []

def base64_decode_inplace(text): # real signature unknown; restored from __doc__
    """ base64_decode_inplace(text:list) -> int, text:list """
    return 0

def base64_encode(data=None): # real signature unknown; restored from __doc__
    """ base64_encode(data:list=None) -> str """
    return ""

def base64_encode_close(break_lines, state, save): # real signature unknown; restored from __doc__
    """ base64_encode_close(break_lines:bool, state:int, save:int) -> int, out:list, state:int, save:int """
    return 0

def base64_encode_step(in_, break_lines, state, save): # real signature unknown; restored from __doc__
    """ base64_encode_step(in_:list, break_lines:bool, state:int, save:int) -> int, out:list, state:int, save:int """
    return 0

def basename(file_name): # real signature unknown; restored from __doc__
    """ basename(file_name:str) -> str """
    return ""

def bit_lock(address=None, lock_bit): # real signature unknown; restored from __doc__
    """ bit_lock(address=None, lock_bit:int) """
    pass

def bit_lock_and_get(address=None, lock_bit): # real signature unknown; restored from __doc__
    """ bit_lock_and_get(address=None, lock_bit:int) -> out_val:int """
    pass

def bit_nth_lsf(mask, nth_bit): # real signature unknown; restored from __doc__
    """ bit_nth_lsf(mask:int, nth_bit:int) -> int """
    return 0

def bit_nth_msf(mask, nth_bit): # real signature unknown; restored from __doc__
    """ bit_nth_msf(mask:int, nth_bit:int) -> int """
    return 0

def bit_storage(number): # real signature unknown; restored from __doc__
    """ bit_storage(number:int) -> int """
    return 0

def bit_trylock(address=None, lock_bit): # real signature unknown; restored from __doc__
    """ bit_trylock(address=None, lock_bit:int) -> bool """
    return False

def bit_unlock(address=None, lock_bit): # real signature unknown; restored from __doc__
    """ bit_unlock(address=None, lock_bit:int) """
    pass

def bit_unlock_and_set(address=None, lock_bit, new_val, preserve_mask): # real signature unknown; restored from __doc__
    """ bit_unlock_and_set(address=None, lock_bit:int, new_val:int, preserve_mask:int) """
    pass

def blow_chunks(): # real signature unknown; restored from __doc__
    """ blow_chunks() """
    pass

def bookmark_file_error_quark(): # real signature unknown; restored from __doc__
    """ bookmark_file_error_quark() -> int """
    return 0

def build_filenamev(args): # real signature unknown; restored from __doc__
    """ build_filenamev(args:list) -> str """
    return ""

def build_pathv(separator, args): # real signature unknown; restored from __doc__
    """ build_pathv(separator:str, args:list) -> str """
    return ""

def byte_array_append(array, data): # real signature unknown; restored from __doc__
    """ byte_array_append(array:list, data:list) -> list """
    return []

def byte_array_free(array, free_segment): # real signature unknown; restored from __doc__
    """ byte_array_free(array:list, free_segment:bool) -> list or None """
    return []

def byte_array_free_to_bytes(array): # real signature unknown; restored from __doc__
    """ byte_array_free_to_bytes(array:list) -> GLib.Bytes """
    pass

def byte_array_new(): # real signature unknown; restored from __doc__
    """ byte_array_new() -> list """
    return []

def byte_array_new_take(data): # real signature unknown; restored from __doc__
    """ byte_array_new_take(data:list) -> list """
    return []

def byte_array_prepend(array, data): # real signature unknown; restored from __doc__
    """ byte_array_prepend(array:list, data:list) -> list """
    return []

def byte_array_ref(array): # real signature unknown; restored from __doc__
    """ byte_array_ref(array:list) -> list """
    return []

def byte_array_remove_index(array, index_): # real signature unknown; restored from __doc__
    """ byte_array_remove_index(array:list, index_:int) -> list """
    return []

def byte_array_remove_index_fast(array, index_): # real signature unknown; restored from __doc__
    """ byte_array_remove_index_fast(array:list, index_:int) -> list """
    return []

def byte_array_remove_range(array, index_, length): # real signature unknown; restored from __doc__
    """ byte_array_remove_range(array:list, index_:int, length:int) -> list """
    return []

def byte_array_set_size(array, length): # real signature unknown; restored from __doc__
    """ byte_array_set_size(array:list, length:int) -> list """
    return []

def byte_array_sized_new(reserved_size): # real signature unknown; restored from __doc__
    """ byte_array_sized_new(reserved_size:int) -> list """
    return []

def byte_array_sort(array, compare_func): # real signature unknown; restored from __doc__
    """ byte_array_sort(array:list, compare_func:GLib.CompareFunc) """
    pass

def byte_array_sort_with_data(array, compare_func, user_data=None): # real signature unknown; restored from __doc__
    """ byte_array_sort_with_data(array:list, compare_func:GLib.CompareDataFunc, user_data=None) """
    pass

def byte_array_steal(array): # real signature unknown; restored from __doc__
    """ byte_array_steal(array:list) -> list """
    return []

def byte_array_unref(array): # real signature unknown; restored from __doc__
    """ byte_array_unref(array:list) """
    pass

def canonicalize_filename(filename, relative_to=None): # real signature unknown; restored from __doc__
    """ canonicalize_filename(filename:str, relative_to:str=None) -> str """
    return ""

def chdir(path): # real signature unknown; restored from __doc__
    """ chdir(path:str) -> int """
    return 0

def checksum_type_get_length(checksum_type): # real signature unknown; restored from __doc__
    """ checksum_type_get_length(checksum_type:GLib.ChecksumType) -> int """
    return 0

def check_version(required_major, required_minor, required_micro): # real signature unknown; restored from __doc__
    """ check_version(required_major:int, required_minor:int, required_micro:int) -> str or None """
    return ""

def child_watch_add(*args, **kwargs): # reliably restored by inspect
    """ child_watch_add(priority, pid, function, *data). """
    pass

def child_watch_source_new(pid): # real signature unknown; restored from __doc__
    """ child_watch_source_new(pid) -> GLib.Source """
    pass

def chmod(filename, mode): # real signature unknown; restored from __doc__
    """ chmod(filename:str, mode:int) -> int """
    return 0

def clear_error(): # real signature unknown; restored from __doc__
    """ clear_error() """
    pass

def close(fd): # real signature unknown; restored from __doc__
    """ close(fd:int) -> bool """
    return False

def compute_checksum_for_bytes(checksum_type, data): # real signature unknown; restored from __doc__
    """ compute_checksum_for_bytes(checksum_type:GLib.ChecksumType, data:GLib.Bytes) -> str or None """
    return ""

def compute_checksum_for_data(checksum_type, data): # real signature unknown; restored from __doc__
    """ compute_checksum_for_data(checksum_type:GLib.ChecksumType, data:list) -> str or None """
    return ""

def compute_checksum_for_string(checksum_type, p_str, length): # real signature unknown; restored from __doc__
    """ compute_checksum_for_string(checksum_type:GLib.ChecksumType, str:str, length:int) -> str or None """
    return ""

def compute_hmac_for_bytes(digest_type, key, data): # real signature unknown; restored from __doc__
    """ compute_hmac_for_bytes(digest_type:GLib.ChecksumType, key:GLib.Bytes, data:GLib.Bytes) -> str """
    return ""

def compute_hmac_for_data(digest_type, key, data): # real signature unknown; restored from __doc__
    """ compute_hmac_for_data(digest_type:GLib.ChecksumType, key:list, data:list) -> str """
    return ""

def compute_hmac_for_string(digest_type, key, p_str, length): # real signature unknown; restored from __doc__
    """ compute_hmac_for_string(digest_type:GLib.ChecksumType, key:list, str:str, length:int) -> str """
    return ""

def convert(p_str, to_codeset, from_codeset): # real signature unknown; restored from __doc__
    """ convert(str:list, to_codeset:str, from_codeset:str) -> list, bytes_read:int """
    return []

def convert_error_quark(): # real signature unknown; restored from __doc__
    """ convert_error_quark() -> int """
    return 0

def convert_with_fallback(p_str, to_codeset, from_codeset, fallback): # real signature unknown; restored from __doc__
    """ convert_with_fallback(str:list, to_codeset:str, from_codeset:str, fallback:str) -> list, bytes_read:int """
    return []

def creat(filename, mode): # real signature unknown; restored from __doc__
    """ creat(filename:str, mode:int) -> int """
    return 0

def datalist_foreach(datalist, func, user_data=None): # real signature unknown; restored from __doc__
    """ datalist_foreach(datalist:GLib.Data, func:GLib.DataForeachFunc, user_data=None) """
    pass

def datalist_get_data(datalist, key): # real signature unknown; restored from __doc__
    """ datalist_get_data(datalist:GLib.Data, key:str) """
    pass

def datalist_get_flags(datalist): # real signature unknown; restored from __doc__
    """ datalist_get_flags(datalist:GLib.Data) -> int """
    return 0

def datalist_id_get_data(datalist, key_id): # real signature unknown; restored from __doc__
    """ datalist_id_get_data(datalist:GLib.Data, key_id:int) """
    pass

def datalist_id_remove_multiple(datalist, keys): # real signature unknown; restored from __doc__
    """ datalist_id_remove_multiple(datalist:GLib.Data, keys:list) """
    pass

def datalist_set_flags(datalist, flags): # real signature unknown; restored from __doc__
    """ datalist_set_flags(datalist:GLib.Data, flags:int) """
    pass

def datalist_unset_flags(datalist, flags): # real signature unknown; restored from __doc__
    """ datalist_unset_flags(datalist:GLib.Data, flags:int) """
    pass

def dataset_destroy(dataset_location): # real signature unknown; restored from __doc__
    """ dataset_destroy(dataset_location) """
    pass

def dataset_foreach(dataset_location, func, user_data=None): # real signature unknown; restored from __doc__
    """ dataset_foreach(dataset_location, func:GLib.DataForeachFunc, user_data=None) """
    pass

def dataset_id_get_data(dataset_location, key_id): # real signature unknown; restored from __doc__
    """ dataset_id_get_data(dataset_location, key_id:int) """
    pass

def date_get_days_in_month(month, year): # real signature unknown; restored from __doc__
    """ date_get_days_in_month(month:GLib.DateMonth, year:int) -> int """
    return 0

def date_get_monday_weeks_in_year(year): # real signature unknown; restored from __doc__
    """ date_get_monday_weeks_in_year(year:int) -> int """
    return 0

def date_get_sunday_weeks_in_year(year): # real signature unknown; restored from __doc__
    """ date_get_sunday_weeks_in_year(year:int) -> int """
    return 0

def date_get_weeks_in_year(year, first_day_of_week): # real signature unknown; restored from __doc__
    """ date_get_weeks_in_year(year:int, first_day_of_week:GLib.DateWeekday) -> int """
    return 0

def date_is_leap_year(year): # real signature unknown; restored from __doc__
    """ date_is_leap_year(year:int) -> bool """
    return False

def date_strftime(s, slen, format, date): # real signature unknown; restored from __doc__
    """ date_strftime(s:str, slen:int, format:str, date:GLib.Date) -> int """
    return 0

def date_valid_day(day): # real signature unknown; restored from __doc__
    """ date_valid_day(day:int) -> bool """
    return False

def date_valid_dmy(day, month, year): # real signature unknown; restored from __doc__
    """ date_valid_dmy(day:int, month:GLib.DateMonth, year:int) -> bool """
    return False

def date_valid_julian(julian_date): # real signature unknown; restored from __doc__
    """ date_valid_julian(julian_date:int) -> bool """
    return False

def date_valid_month(month): # real signature unknown; restored from __doc__
    """ date_valid_month(month:GLib.DateMonth) -> bool """
    return False

def date_valid_weekday(weekday): # real signature unknown; restored from __doc__
    """ date_valid_weekday(weekday:GLib.DateWeekday) -> bool """
    return False

def date_valid_year(year): # real signature unknown; restored from __doc__
    """ date_valid_year(year:int) -> bool """
    return False

def dcgettext(domain=None, msgid, category): # real signature unknown; restored from __doc__
    """ dcgettext(domain:str=None, msgid:str, category:int) -> str """
    return ""

def dgettext(domain=None, msgid): # real signature unknown; restored from __doc__
    """ dgettext(domain:str=None, msgid:str) -> str """
    return ""

def direct_equal(v1=None, v2=None): # real signature unknown; restored from __doc__
    """ direct_equal(v1=None, v2=None) -> bool """
    return False

def direct_hash(v=None): # real signature unknown; restored from __doc__
    """ direct_hash(v=None) -> int """
    return 0

def dir_make_tmp(tmpl=None): # real signature unknown; restored from __doc__
    """ dir_make_tmp(tmpl:str=None) -> str """
    return ""

def dngettext(domain=None, msgid, msgid_plural, n): # real signature unknown; restored from __doc__
    """ dngettext(domain:str=None, msgid:str, msgid_plural:str, n:int) -> str """
    return ""

def double_equal(v1, v2): # real signature unknown; restored from __doc__
    """ double_equal(v1, v2) -> bool """
    return False

def double_hash(v): # real signature unknown; restored from __doc__
    """ double_hash(v) -> int """
    return 0

def dpgettext(domain=None, msgctxtid, msgidoffset): # real signature unknown; restored from __doc__
    """ dpgettext(domain:str=None, msgctxtid:str, msgidoffset:int) -> str """
    return ""

def dpgettext2(domain=None, context, msgid): # real signature unknown; restored from __doc__
    """ dpgettext2(domain:str=None, context:str, msgid:str) -> str """
    return ""

def environ_getenv(envp=None, variable): # real signature unknown; restored from __doc__
    """ environ_getenv(envp:list=None, variable:str) -> str or None """
    return ""

def environ_setenv(envp=None, variable, value, overwrite): # real signature unknown; restored from __doc__
    """ environ_setenv(envp:list=None, variable:str, value:str, overwrite:bool) -> list """
    return []

def environ_unsetenv(envp=None, variable): # real signature unknown; restored from __doc__
    """ environ_unsetenv(envp:list=None, variable:str) -> list """
    return []

def error_domain_register(error_type_name, error_type_private_size, error_type_init, error_type_copy, error_type_clear): # real signature unknown; restored from __doc__
    """ error_domain_register(error_type_name:str, error_type_private_size:int, error_type_init:GLib.ErrorInitFunc, error_type_copy:GLib.ErrorCopyFunc, error_type_clear:GLib.ErrorClearFunc) -> int """
    return 0

def error_domain_register_static(error_type_name, error_type_private_size, error_type_init, error_type_copy, error_type_clear): # real signature unknown; restored from __doc__
    """ error_domain_register_static(error_type_name:str, error_type_private_size:int, error_type_init:GLib.ErrorInitFunc, error_type_copy:GLib.ErrorCopyFunc, error_type_clear:GLib.ErrorClearFunc) -> int """
    return 0

def filename_display_basename(filename): # real signature unknown; restored from __doc__
    """ filename_display_basename(filename:str) -> str """
    return ""

def filename_display_name(filename): # real signature unknown; restored from __doc__
    """ filename_display_name(filename:str) -> str """
    return ""

def filename_from_uri(uri): # real signature unknown; restored from __doc__
    """ filename_from_uri(uri:str) -> str, hostname:str """
    return ""

def filename_from_utf8(utf8string, len=-1): # reliably restored by inspect
    # no doc
    pass

def filename_to_uri(filename, hostname=None): # real signature unknown; restored from __doc__
    """ filename_to_uri(filename:str, hostname:str=None) -> str """
    return ""

def filename_to_utf8(opsysstring, len): # real signature unknown; restored from __doc__
    """ filename_to_utf8(opsysstring:str, len:int) -> str, bytes_read:int, bytes_written:int """
    return ""

def file_error_from_errno(err_no): # real signature unknown; restored from __doc__
    """ file_error_from_errno(err_no:int) -> GLib.FileError """
    pass

def file_error_quark(): # real signature unknown; restored from __doc__
    """ file_error_quark() -> int """
    return 0

def file_get_contents(filename): # real signature unknown; restored from __doc__
    """ file_get_contents(filename:str) -> bool, contents:list """
    return False

def file_open_tmp(tmpl=None): # real signature unknown; restored from __doc__
    """ file_open_tmp(tmpl:str=None) -> int, name_used:str """
    return 0

def file_read_link(filename): # real signature unknown; restored from __doc__
    """ file_read_link(filename:str) -> str """
    return ""

def file_set_contents(filename, contents): # real signature unknown; restored from __doc__
    """ file_set_contents(filename:str, contents:list) -> bool """
    return False

def file_set_contents_full(filename, contents, flags, mode): # real signature unknown; restored from __doc__
    """ file_set_contents_full(filename:str, contents:list, flags:GLib.FileSetContentsFlags, mode:int) -> bool """
    return False

def file_test(filename, test): # real signature unknown; restored from __doc__
    """ file_test(filename:str, test:GLib.FileTest) -> bool """
    return False

def find_program_in_path(program): # real signature unknown; restored from __doc__
    """ find_program_in_path(program:str) -> str or None """
    return ""

def fopen(filename, mode): # real signature unknown; restored from __doc__
    """ fopen(filename:str, mode:str) """
    pass

def format_size(size): # real signature unknown; restored from __doc__
    """ format_size(size:int) -> str """
    return ""

def format_size_for_display(size): # real signature unknown; restored from __doc__
    """ format_size_for_display(size:int) -> str """
    return ""

def format_size_full(size, flags): # real signature unknown; restored from __doc__
    """ format_size_full(size:int, flags:GLib.FormatSizeFlags) -> str """
    return ""

def free(mem=None): # real signature unknown; restored from __doc__
    """ free(mem=None) """
    pass

def free_sized(mem=None, size): # real signature unknown; restored from __doc__
    """ free_sized(mem=None, size:int) """
    pass

def freopen(filename, mode, stream=None): # real signature unknown; restored from __doc__
    """ freopen(filename:str, mode:str, stream=None) """
    pass

def fsync(fd): # real signature unknown; restored from __doc__
    """ fsync(fd:int) -> int """
    return 0

def getenv(variable): # real signature unknown; restored from __doc__
    """ getenv(variable:str) -> str or None """
    return ""

def get_application_name(): # real signature unknown; restored from __doc__
    """ get_application_name() -> str or None """
    return ""

def get_charset(): # real signature unknown; restored from __doc__
    """ get_charset() -> bool, charset:str """
    return False

def get_codeset(): # real signature unknown; restored from __doc__
    """ get_codeset() -> str """
    return ""

def get_console_charset(): # real signature unknown; restored from __doc__
    """ get_console_charset() -> bool, charset:str """
    return False

def get_current_dir(): # real signature unknown; restored from __doc__
    """ get_current_dir() -> str """
    return ""

def get_current_time(*args, **kwargs): # reliably restored by inspect
    # no doc
    pass

def get_environ(): # real signature unknown; restored from __doc__
    """ get_environ() -> list """
    return []

def get_filename_charsets(): # real signature unknown; restored from __doc__
    """ get_filename_charsets() -> bool, filename_charsets:list """
    return False

def get_home_dir(): # real signature unknown; restored from __doc__
    """ get_home_dir() -> str """
    return ""

def get_host_name(): # real signature unknown; restored from __doc__
    """ get_host_name() -> str """
    return ""

def get_language_names(): # real signature unknown; restored from __doc__
    """ get_language_names() -> list """
    return []

def get_language_names_with_category(category_name): # real signature unknown; restored from __doc__
    """ get_language_names_with_category(category_name:str) -> list """
    return []

def get_locale_variants(locale): # real signature unknown; restored from __doc__
    """ get_locale_variants(locale:str) -> list """
    return []

def get_monotonic_time(): # real signature unknown; restored from __doc__
    """ get_monotonic_time() -> int """
    return 0

def get_num_processors(): # real signature unknown; restored from __doc__
    """ get_num_processors() -> int """
    return 0

def get_os_info(key_name): # real signature unknown; restored from __doc__
    """ get_os_info(key_name:str) -> str or None """
    return ""

def get_prgname(): # real signature unknown; restored from __doc__
    """ get_prgname() -> str or None """
    return ""

def get_real_name(): # real signature unknown; restored from __doc__
    """ get_real_name() -> str """
    return ""

def get_real_time(): # real signature unknown; restored from __doc__
    """ get_real_time() -> int """
    return 0

def get_system_config_dirs(): # real signature unknown; restored from __doc__
    """ get_system_config_dirs() -> list """
    return []

def get_system_data_dirs(): # real signature unknown; restored from __doc__
    """ get_system_data_dirs() -> list """
    return []

def get_tmp_dir(): # real signature unknown; restored from __doc__
    """ get_tmp_dir() -> str """
    return ""

def get_user_cache_dir(): # real signature unknown; restored from __doc__
    """ get_user_cache_dir() -> str """
    return ""

def get_user_config_dir(): # real signature unknown; restored from __doc__
    """ get_user_config_dir() -> str """
    return ""

def get_user_data_dir(): # real signature unknown; restored from __doc__
    """ get_user_data_dir() -> str """
    return ""

def get_user_name(): # real signature unknown; restored from __doc__
    """ get_user_name() -> str """
    return ""

def get_user_runtime_dir(): # real signature unknown; restored from __doc__
    """ get_user_runtime_dir() -> str """
    return ""

def get_user_special_dir(directory): # real signature unknown; restored from __doc__
    """ get_user_special_dir(directory:GLib.UserDirectory) -> str or None """
    return ""

def get_user_state_dir(): # real signature unknown; restored from __doc__
    """ get_user_state_dir() -> str """
    return ""

def hash_table_add(hash_table, key=None): # real signature unknown; restored from __doc__
    """ hash_table_add(hash_table:dict, key=None) -> bool """
    return False

def hash_table_contains(hash_table, key=None): # real signature unknown; restored from __doc__
    """ hash_table_contains(hash_table:dict, key=None) -> bool """
    return False

def hash_table_destroy(hash_table): # real signature unknown; restored from __doc__
    """ hash_table_destroy(hash_table:dict) """
    pass

def hash_table_find(hash_table, predicate, user_data=None): # real signature unknown; restored from __doc__
    """ hash_table_find(hash_table:dict, predicate:GLib.HRFunc, user_data=None) """
    pass

def hash_table_foreach(hash_table, func, user_data=None): # real signature unknown; restored from __doc__
    """ hash_table_foreach(hash_table:dict, func:GLib.HFunc, user_data=None) """
    pass

def hash_table_foreach_remove(hash_table, func, user_data=None): # real signature unknown; restored from __doc__
    """ hash_table_foreach_remove(hash_table:dict, func:GLib.HRFunc, user_data=None) -> int """
    return 0

def hash_table_foreach_steal(hash_table, func, user_data=None): # real signature unknown; restored from __doc__
    """ hash_table_foreach_steal(hash_table:dict, func:GLib.HRFunc, user_data=None) -> int """
    return 0

def hash_table_insert(hash_table, key=None, value=None): # real signature unknown; restored from __doc__
    """ hash_table_insert(hash_table:dict, key=None, value=None) -> bool """
    return False

def hash_table_lookup(hash_table, key=None): # real signature unknown; restored from __doc__
    """ hash_table_lookup(hash_table:dict, key=None) """
    pass

def hash_table_lookup_extended(hash_table, lookup_key=None): # real signature unknown; restored from __doc__
    """ hash_table_lookup_extended(hash_table:dict, lookup_key=None) -> bool, orig_key, value """
    return False

def hash_table_new_similar(other_hash_table): # real signature unknown; restored from __doc__
    """ hash_table_new_similar(other_hash_table:dict) -> dict """
    return {}

def hash_table_ref(hash_table): # real signature unknown; restored from __doc__
    """ hash_table_ref(hash_table:dict) -> dict """
    return {}

def hash_table_remove(hash_table, key=None): # real signature unknown; restored from __doc__
    """ hash_table_remove(hash_table:dict, key=None) -> bool """
    return False

def hash_table_remove_all(hash_table): # real signature unknown; restored from __doc__
    """ hash_table_remove_all(hash_table:dict) """
    pass

def hash_table_replace(hash_table, key=None, value=None): # real signature unknown; restored from __doc__
    """ hash_table_replace(hash_table:dict, key=None, value=None) -> bool """
    return False

def hash_table_size(hash_table): # real signature unknown; restored from __doc__
    """ hash_table_size(hash_table:dict) -> int """
    return 0

def hash_table_steal(hash_table, key=None): # real signature unknown; restored from __doc__
    """ hash_table_steal(hash_table:dict, key=None) -> bool """
    return False

def hash_table_steal_all(hash_table): # real signature unknown; restored from __doc__
    """ hash_table_steal_all(hash_table:dict) """
    pass

def hash_table_steal_extended(hash_table, lookup_key=None): # real signature unknown; restored from __doc__
    """ hash_table_steal_extended(hash_table:dict, lookup_key=None) -> bool, stolen_key, stolen_value """
    return False

def hash_table_unref(hash_table): # real signature unknown; restored from __doc__
    """ hash_table_unref(hash_table:dict) """
    pass

def hook_destroy(hook_list, hook_id): # real signature unknown; restored from __doc__
    """ hook_destroy(hook_list:GLib.HookList, hook_id:int) -> bool """
    return False

def hook_destroy_link(hook_list, hook): # real signature unknown; restored from __doc__
    """ hook_destroy_link(hook_list:GLib.HookList, hook:GLib.Hook) """
    pass

def hook_free(hook_list, hook): # real signature unknown; restored from __doc__
    """ hook_free(hook_list:GLib.HookList, hook:GLib.Hook) """
    pass

def hook_insert_before(hook_list, sibling=None, hook): # real signature unknown; restored from __doc__
    """ hook_insert_before(hook_list:GLib.HookList, sibling:GLib.Hook=None, hook:GLib.Hook) """
    pass

def hook_insert_sorted(hook_list, hook, func): # real signature unknown; restored from __doc__
    """ hook_insert_sorted(hook_list:GLib.HookList, hook:GLib.Hook, func:GLib.HookCompareFunc) """
    pass

def hook_prepend(hook_list, hook): # real signature unknown; restored from __doc__
    """ hook_prepend(hook_list:GLib.HookList, hook:GLib.Hook) """
    pass

def hook_unref(hook_list, hook): # real signature unknown; restored from __doc__
    """ hook_unref(hook_list:GLib.HookList, hook:GLib.Hook) """
    pass

def hostname_is_ascii_encoded(hostname): # real signature unknown; restored from __doc__
    """ hostname_is_ascii_encoded(hostname:str) -> bool """
    return False

def hostname_is_ip_address(hostname): # real signature unknown; restored from __doc__
    """ hostname_is_ip_address(hostname:str) -> bool """
    return False

def hostname_is_non_ascii(hostname): # real signature unknown; restored from __doc__
    """ hostname_is_non_ascii(hostname:str) -> bool """
    return False

def hostname_to_ascii(hostname): # real signature unknown; restored from __doc__
    """ hostname_to_ascii(hostname:str) -> str or None """
    return ""

def hostname_to_unicode(hostname): # real signature unknown; restored from __doc__
    """ hostname_to_unicode(hostname:str) -> str or None """
    return ""

def idle_add(function, *user_data, priority=200): # reliably restored by inspect
    # no doc
    pass

def idle_remove_by_data(data=None): # real signature unknown; restored from __doc__
    """ idle_remove_by_data(data=None) -> bool """
    return False

def idle_source_new(): # real signature unknown; restored from __doc__
    """ idle_source_new() -> GLib.Source """
    pass

def int64_equal(v1, v2): # real signature unknown; restored from __doc__
    """ int64_equal(v1, v2) -> bool """
    return False

def int64_hash(v): # real signature unknown; restored from __doc__
    """ int64_hash(v) -> int """
    return 0

def intern_static_string(string=None): # real signature unknown; restored from __doc__
    """ intern_static_string(string:str=None) -> str """
    return ""

def intern_string(string=None): # real signature unknown; restored from __doc__
    """ intern_string(string:str=None) -> str """
    return ""

def int_equal(v1, v2): # real signature unknown; restored from __doc__
    """ int_equal(v1, v2) -> bool """
    return False

def int_hash(v): # real signature unknown; restored from __doc__
    """ int_hash(v) -> int """
    return 0

def io_add_watch(*args, **kwargs): # reliably restored by inspect
    """ io_add_watch(channel, priority, condition, func, *user_data) -> event_source_id. """
    pass

def io_channel_error_from_errno(en): # real signature unknown; restored from __doc__
    """ io_channel_error_from_errno(en:int) -> GLib.IOChannelError """
    pass

def io_channel_error_quark(): # real signature unknown; restored from __doc__
    """ io_channel_error_quark() -> int """
    return 0

def io_channel_win32_poll(fds, n_fds, timeout_): # real signature unknown; restored from __doc__
    """ io_channel_win32_poll(fds:GLib.PollFD, n_fds:int, timeout_:int) -> int """
    return 0

def io_create_watch(channel, condition): # real signature unknown; restored from __doc__
    """ io_create_watch(channel:GLib.IOChannel, condition:GLib.IOCondition) -> GLib.Source """
    pass

def key_file_error_quark(): # real signature unknown; restored from __doc__
    """ key_file_error_quark() -> int """
    return 0

def listenv(): # real signature unknown; restored from __doc__
    """ listenv() -> list """
    return []

def list_pop_allocator(): # real signature unknown; restored from __doc__
    """ list_pop_allocator() """
    pass

def list_push_allocator(allocator): # real signature unknown; restored from __doc__
    """ list_push_allocator(allocator:GLib.Allocator) """
    pass

def locale_from_utf8(utf8string, len): # real signature unknown; restored from __doc__
    """ locale_from_utf8(utf8string:str, len:int) -> list, bytes_read:int """
    return []

def locale_to_utf8(opsysstring): # real signature unknown; restored from __doc__
    """ locale_to_utf8(opsysstring:list) -> str, bytes_read:int, bytes_written:int """
    return ""

def log_default_handler(log_domain=None, log_level, message=None, unused_data=None): # real signature unknown; restored from __doc__
    """ log_default_handler(log_domain:str=None, log_level:GLib.LogLevelFlags, message:str=None, unused_data=None) """
    pass

def log_get_always_fatal(): # real signature unknown; restored from __doc__
    """ log_get_always_fatal() -> GLib.LogLevelFlags """
    pass

def log_get_debug_enabled(): # real signature unknown; restored from __doc__
    """ log_get_debug_enabled() -> bool """
    return False

def log_remove_handler(log_domain, handler_id): # real signature unknown; restored from __doc__
    """ log_remove_handler(log_domain:str, handler_id:int) """
    pass

def log_set_always_fatal(fatal_mask): # real signature unknown; restored from __doc__
    """ log_set_always_fatal(fatal_mask:GLib.LogLevelFlags) -> GLib.LogLevelFlags """
    pass

def log_set_debug_enabled(enabled): # real signature unknown; restored from __doc__
    """ log_set_debug_enabled(enabled:bool) """
    pass

def log_set_fatal_mask(log_domain, fatal_mask): # real signature unknown; restored from __doc__
    """ log_set_fatal_mask(log_domain:str, fatal_mask:GLib.LogLevelFlags) -> GLib.LogLevelFlags """
    pass

def log_set_handler(log_domain=None, log_levels, log_func, user_data=None): # real signature unknown; restored from __doc__
    """ log_set_handler(log_domain:str=None, log_levels:GLib.LogLevelFlags, log_func:GLib.LogFunc, user_data=None) -> int """
    return 0

def log_set_writer_func(user_data=None): # real signature unknown; restored from __doc__
    """ log_set_writer_func(user_data=None) """
    pass

def log_structured_array(log_level, fields): # real signature unknown; restored from __doc__
    """ log_structured_array(log_level:GLib.LogLevelFlags, fields:list) """
    pass

def log_variant(log_domain=None, log_level, fields): # real signature unknown; restored from __doc__
    """ log_variant(log_domain:str=None, log_level:GLib.LogLevelFlags, fields:GLib.Variant) """
    pass

def log_writer_default(log_level, fields, user_data=None): # real signature unknown; restored from __doc__
    """ log_writer_default(log_level:GLib.LogLevelFlags, fields:list, user_data=None) -> GLib.LogWriterOutput """
    pass

def log_writer_default_set_debug_domains(domains=None): # real signature unknown; restored from __doc__
    """ log_writer_default_set_debug_domains(domains:str=None) """
    pass

def log_writer_default_set_use_stderr(use_stderr): # real signature unknown; restored from __doc__
    """ log_writer_default_set_use_stderr(use_stderr:bool) """
    pass

def log_writer_default_would_drop(log_level, log_domain=None): # real signature unknown; restored from __doc__
    """ log_writer_default_would_drop(log_level:GLib.LogLevelFlags, log_domain:str=None) -> bool """
    return False

def log_writer_format_fields(log_level, fields, use_color): # real signature unknown; restored from __doc__
    """ log_writer_format_fields(log_level:GLib.LogLevelFlags, fields:list, use_color:bool) -> str """
    return ""

def log_writer_is_journald(output_fd): # real signature unknown; restored from __doc__
    """ log_writer_is_journald(output_fd:int) -> bool """
    return False

def log_writer_journald(log_level, fields, user_data=None): # real signature unknown; restored from __doc__
    """ log_writer_journald(log_level:GLib.LogLevelFlags, fields:list, user_data=None) -> GLib.LogWriterOutput """
    pass

def log_writer_standard_streams(log_level, fields, user_data=None): # real signature unknown; restored from __doc__
    """ log_writer_standard_streams(log_level:GLib.LogLevelFlags, fields:list, user_data=None) -> GLib.LogWriterOutput """
    pass

def log_writer_supports_color(output_fd): # real signature unknown; restored from __doc__
    """ log_writer_supports_color(output_fd:int) -> bool """
    return False

def log_writer_syslog(log_level, fields, user_data=None): # real signature unknown; restored from __doc__
    """ log_writer_syslog(log_level:GLib.LogLevelFlags, fields:list, user_data=None) -> GLib.LogWriterOutput """
    pass

def lstat(filename, buf): # real signature unknown; restored from __doc__
    """ lstat(filename:str, buf:GLib.StatBuf) -> int """
    return 0

def main_context_default(): # real signature unknown; restored from __doc__
    """ main_context_default() -> GLib.MainContext """
    pass

def main_context_get_thread_default(): # real signature unknown; restored from __doc__
    """ main_context_get_thread_default() -> GLib.MainContext or None """
    pass

def main_context_ref_thread_default(): # real signature unknown; restored from __doc__
    """ main_context_ref_thread_default() -> GLib.MainContext """
    pass

def main_current_source(): # real signature unknown; restored from __doc__
    """ main_current_source() -> GLib.Source or None """
    pass

def main_depth(): # real signature unknown; restored from __doc__
    """ main_depth() -> int """
    return 0

def malloc(n_bytes): # real signature unknown; restored from __doc__
    """ malloc(n_bytes:int) """
    pass

def malloc0(n_bytes): # real signature unknown; restored from __doc__
    """ malloc0(n_bytes:int) """
    pass

def malloc0_n(n_blocks, n_block_bytes): # real signature unknown; restored from __doc__
    """ malloc0_n(n_blocks:int, n_block_bytes:int) """
    pass

def malloc_n(n_blocks, n_block_bytes): # real signature unknown; restored from __doc__
    """ malloc_n(n_blocks:int, n_block_bytes:int) """
    pass

def markup_error_quark(): # real signature unknown; restored from __doc__
    """ markup_error_quark() -> int """
    return 0

def markup_escape_text(text, length=-1): # reliably restored by inspect
    # no doc
    pass

def memdup(mem=None, byte_size): # real signature unknown; restored from __doc__
    """ memdup(mem=None, byte_size:int) """
    pass

def memdup2(mem=None, byte_size): # real signature unknown; restored from __doc__
    """ memdup2(mem=None, byte_size:int) """
    pass

def mem_chunk_info(): # real signature unknown; restored from __doc__
    """ mem_chunk_info() """
    pass

def mem_is_system_malloc(): # real signature unknown; restored from __doc__
    """ mem_is_system_malloc() -> bool """
    return False

def mem_profile(): # real signature unknown; restored from __doc__
    """ mem_profile() """
    pass

def mem_set_vtable(vtable): # real signature unknown; restored from __doc__
    """ mem_set_vtable(vtable:GLib.MemVTable) """
    pass

def mkdir(filename, mode): # real signature unknown; restored from __doc__
    """ mkdir(filename:str, mode:int) -> int """
    return 0

def mkdir_with_parents(pathname, mode): # real signature unknown; restored from __doc__
    """ mkdir_with_parents(pathname:str, mode:int) -> int """
    return 0

def node_pop_allocator(): # real signature unknown; restored from __doc__
    """ node_pop_allocator() """
    pass

def node_push_allocator(allocator): # real signature unknown; restored from __doc__
    """ node_push_allocator(allocator:GLib.Allocator) """
    pass

def nullify_pointer(nullify_location): # real signature unknown; restored from __doc__
    """ nullify_pointer(nullify_location) """
    pass

def number_parser_error_quark(): # real signature unknown; restored from __doc__
    """ number_parser_error_quark() -> int """
    return 0

def once_init_enter(location): # real signature unknown; restored from __doc__
    """ once_init_enter(location) -> bool, location """
    return False

def once_init_enter_impl(location): # real signature unknown; restored from __doc__
    """ once_init_enter_impl(location:int) -> bool """
    return False

def once_init_enter_pointer(location): # real signature unknown; restored from __doc__
    """ once_init_enter_pointer(location) -> bool """
    return False

def once_init_leave(location, result): # real signature unknown; restored from __doc__
    """ once_init_leave(location, result:int) -> location """
    pass

def once_init_leave_pointer(location, result=None): # real signature unknown; restored from __doc__
    """ once_init_leave_pointer(location, result=None) """
    pass

def on_error_query(prg_name): # real signature unknown; restored from __doc__
    """ on_error_query(prg_name:str) """
    pass

def on_error_stack_trace(prg_name=None): # real signature unknown; restored from __doc__
    """ on_error_stack_trace(prg_name:str=None) """
    pass

def open(filename, flags, mode): # real signature unknown; restored from __doc__
    """ open(filename:str, flags:int, mode:int) -> int """
    return 0

def option_error_quark(): # real signature unknown; restored from __doc__
    """ option_error_quark() -> int """
    return 0

def parse_debug_string(string=None, keys): # real signature unknown; restored from __doc__
    """ parse_debug_string(string:str=None, keys:list) -> int """
    return 0

def path_buf_equal(v1, v2): # real signature unknown; restored from __doc__
    """ path_buf_equal(v1, v2) -> bool """
    return False

def path_get_basename(file_name): # real signature unknown; restored from __doc__
    """ path_get_basename(file_name:str) -> str """
    return ""

def path_get_dirname(file_name): # real signature unknown; restored from __doc__
    """ path_get_dirname(file_name:str) -> str """
    return ""

def path_is_absolute(file_name): # real signature unknown; restored from __doc__
    """ path_is_absolute(file_name:str) -> bool """
    return False

def path_skip_root(file_name): # real signature unknown; restored from __doc__
    """ path_skip_root(file_name:str) -> str or None """
    return ""

def pattern_match_simple(pattern, string): # real signature unknown; restored from __doc__
    """ pattern_match_simple(pattern:str, string:str) -> bool """
    return False

def pointer_bit_lock(address, lock_bit): # real signature unknown; restored from __doc__
    """ pointer_bit_lock(address, lock_bit:int) """
    pass

def pointer_bit_lock_and_get(address, lock_bit): # real signature unknown; restored from __doc__
    """ pointer_bit_lock_and_get(address, lock_bit:int) -> out_ptr:int """
    pass

def pointer_bit_lock_mask_ptr(ptr=None, lock_bit, set, preserve_mask, preserve_ptr=None): # real signature unknown; restored from __doc__
    """ pointer_bit_lock_mask_ptr(ptr=None, lock_bit:int, set:bool, preserve_mask:int, preserve_ptr=None) """
    pass

def pointer_bit_trylock(address, lock_bit): # real signature unknown; restored from __doc__
    """ pointer_bit_trylock(address, lock_bit:int) -> bool """
    return False

def pointer_bit_unlock(address, lock_bit): # real signature unknown; restored from __doc__
    """ pointer_bit_unlock(address, lock_bit:int) """
    pass

def pointer_bit_unlock_and_set(address, lock_bit, ptr=None, preserve_mask): # real signature unknown; restored from __doc__
    """ pointer_bit_unlock_and_set(address, lock_bit:int, ptr=None, preserve_mask:int) """
    pass

def poll(fds, nfds, timeout): # real signature unknown; restored from __doc__
    """ poll(fds:GLib.PollFD, nfds:int, timeout:int) -> int """
    return 0

def prefix_error_literal(err=None, prefix): # real signature unknown; restored from __doc__
    """ prefix_error_literal(err:error=None, prefix:str) -> err:error """
    pass

def propagate_error(src): # real signature unknown; restored from __doc__
    """ propagate_error(src:error) -> dest:error """
    pass

def qsort_with_data(pbase, total_elems, size, compare_func, user_data=None): # real signature unknown; restored from __doc__
    """ qsort_with_data(pbase, total_elems:int, size:int, compare_func:GLib.CompareDataFunc, user_data=None) """
    pass

def quark_from_static_string(string=None): # real signature unknown; restored from __doc__
    """ quark_from_static_string(string:str=None) -> int """
    return 0

def quark_from_string(string=None): # real signature unknown; restored from __doc__
    """ quark_from_string(string:str=None) -> int """
    return 0

def quark_to_string(quark): # real signature unknown; restored from __doc__
    """ quark_to_string(quark:int) -> str """
    return ""

def quark_try_string(string=None): # real signature unknown; restored from __doc__
    """ quark_try_string(string:str=None) -> int """
    return 0

def random_double(): # real signature unknown; restored from __doc__
    """ random_double() -> float """
    return 0.0

def random_double_range(begin, end): # real signature unknown; restored from __doc__
    """ random_double_range(begin:float, end:float) -> float """
    return 0.0

def random_int(): # real signature unknown; restored from __doc__
    """ random_int() -> int """
    return 0

def random_int_range(begin, end): # real signature unknown; restored from __doc__
    """ random_int_range(begin:int, end:int) -> int """
    return 0

def random_set_seed(seed): # real signature unknown; restored from __doc__
    """ random_set_seed(seed:int) """
    pass

def rc_box_acquire(mem_block): # real signature unknown; restored from __doc__
    """ rc_box_acquire(mem_block) """
    pass

def rc_box_alloc(block_size): # real signature unknown; restored from __doc__
    """ rc_box_alloc(block_size:int) """
    pass

def rc_box_alloc0(block_size): # real signature unknown; restored from __doc__
    """ rc_box_alloc0(block_size:int) """
    pass

def rc_box_dup(block_size, mem_block): # real signature unknown; restored from __doc__
    """ rc_box_dup(block_size:int, mem_block) """
    pass

def rc_box_get_size(mem_block): # real signature unknown; restored from __doc__
    """ rc_box_get_size(mem_block) -> int """
    return 0

def rc_box_release(mem_block): # real signature unknown; restored from __doc__
    """ rc_box_release(mem_block) """
    pass

def rc_box_release_full(mem_block, clear_func): # real signature unknown; restored from __doc__
    """ rc_box_release_full(mem_block, clear_func:GLib.DestroyNotify) """
    pass

def realloc(mem=None, n_bytes): # real signature unknown; restored from __doc__
    """ realloc(mem=None, n_bytes:int) """
    pass

def realloc_n(mem=None, n_blocks, n_block_bytes): # real signature unknown; restored from __doc__
    """ realloc_n(mem=None, n_blocks:int, n_block_bytes:int) """
    pass

def ref_count_compare(rc, val): # real signature unknown; restored from __doc__
    """ ref_count_compare(rc:int, val:int) -> bool """
    return False

def ref_count_dec(rc): # real signature unknown; restored from __doc__
    """ ref_count_dec(rc:int) -> bool, rc:int """
    return False

def ref_count_inc(rc): # real signature unknown; restored from __doc__
    """ ref_count_inc(rc:int) -> rc:int """
    pass

def ref_count_init(): # real signature unknown; restored from __doc__
    """ ref_count_init() -> rc:int """
    pass

def ref_string_acquire(p_str): # real signature unknown; restored from __doc__
    """ ref_string_acquire(str:str) -> str """
    return ""

def ref_string_equal(str1, str2): # real signature unknown; restored from __doc__
    """ ref_string_equal(str1:str, str2:str) -> bool """
    return False

def ref_string_length(p_str): # real signature unknown; restored from __doc__
    """ ref_string_length(str:str) -> int """
    return 0

def ref_string_new(p_str): # real signature unknown; restored from __doc__
    """ ref_string_new(str:str) -> str """
    return ""

def ref_string_new_intern(p_str): # real signature unknown; restored from __doc__
    """ ref_string_new_intern(str:str) -> str """
    return ""

def ref_string_new_len(p_str, len): # real signature unknown; restored from __doc__
    """ ref_string_new_len(str:str, len:int) -> str """
    return ""

def ref_string_release(p_str): # real signature unknown; restored from __doc__
    """ ref_string_release(str:str) """
    pass

def regex_check_replacement(replacement): # real signature unknown; restored from __doc__
    """ regex_check_replacement(replacement:str) -> bool, has_references:bool """
    return False

def regex_error_quark(): # real signature unknown; restored from __doc__
    """ regex_error_quark() -> int """
    return 0

def regex_escape_nul(string, length): # real signature unknown; restored from __doc__
    """ regex_escape_nul(string:str, length:int) -> str """
    return ""

def regex_escape_string(string, length): # real signature unknown; restored from __doc__
    """ regex_escape_string(string:str, length:int) -> str """
    return ""

def regex_match_simple(pattern, string, compile_options, match_options): # real signature unknown; restored from __doc__
    """ regex_match_simple(pattern:str, string:str, compile_options:GLib.RegexCompileFlags, match_options:GLib.RegexMatchFlags) -> bool """
    return False

def regex_split_simple(pattern, string, compile_options, match_options): # real signature unknown; restored from __doc__
    """ regex_split_simple(pattern:str, string:str, compile_options:GLib.RegexCompileFlags, match_options:GLib.RegexMatchFlags) -> list """
    return []

def reload_user_special_dirs_cache(): # real signature unknown; restored from __doc__
    """ reload_user_special_dirs_cache() """
    pass

def remove(filename): # real signature unknown; restored from __doc__
    """ remove(filename:str) -> int """
    return 0

def rename(oldfilename, newfilename): # real signature unknown; restored from __doc__
    """ rename(oldfilename:str, newfilename:str) -> int """
    return 0

def rmdir(filename): # real signature unknown; restored from __doc__
    """ rmdir(filename:str) -> int """
    return 0

def sequence_foreach_range(begin, end, func, user_data=None): # real signature unknown; restored from __doc__
    """ sequence_foreach_range(begin:GLib.SequenceIter, end:GLib.SequenceIter, func:GLib.Func, user_data=None) """
    pass

def sequence_get(iter): # real signature unknown; restored from __doc__
    """ sequence_get(iter:GLib.SequenceIter) """
    pass

def sequence_insert_before(iter, data=None): # real signature unknown; restored from __doc__
    """ sequence_insert_before(iter:GLib.SequenceIter, data=None) -> GLib.SequenceIter """
    pass

def sequence_move(src, dest): # real signature unknown; restored from __doc__
    """ sequence_move(src:GLib.SequenceIter, dest:GLib.SequenceIter) """
    pass

def sequence_move_range(dest, begin, end): # real signature unknown; restored from __doc__
    """ sequence_move_range(dest:GLib.SequenceIter, begin:GLib.SequenceIter, end:GLib.SequenceIter) """
    pass

def sequence_range_get_midpoint(begin, end): # real signature unknown; restored from __doc__
    """ sequence_range_get_midpoint(begin:GLib.SequenceIter, end:GLib.SequenceIter) -> GLib.SequenceIter """
    pass

def sequence_remove(iter): # real signature unknown; restored from __doc__
    """ sequence_remove(iter:GLib.SequenceIter) """
    pass

def sequence_remove_range(begin, end): # real signature unknown; restored from __doc__
    """ sequence_remove_range(begin:GLib.SequenceIter, end:GLib.SequenceIter) """
    pass

def sequence_set(iter, data=None): # real signature unknown; restored from __doc__
    """ sequence_set(iter:GLib.SequenceIter, data=None) """
    pass

def sequence_sort_changed(iter, cmp_func, cmp_data=None): # real signature unknown; restored from __doc__
    """ sequence_sort_changed(iter:GLib.SequenceIter, cmp_func:GLib.CompareDataFunc, cmp_data=None) """
    pass

def sequence_sort_changed_iter(iter, iter_cmp, cmp_data=None): # real signature unknown; restored from __doc__
    """ sequence_sort_changed_iter(iter:GLib.SequenceIter, iter_cmp:GLib.SequenceIterCompareFunc, cmp_data=None) """
    pass

def sequence_swap(a, b): # real signature unknown; restored from __doc__
    """ sequence_swap(a:GLib.SequenceIter, b:GLib.SequenceIter) """
    pass

def setenv(variable, value, overwrite): # real signature unknown; restored from __doc__
    """ setenv(variable:str, value:str, overwrite:bool) -> bool """
    return False

def set_application_name(application_name): # real signature unknown; restored from __doc__
    """ set_application_name(application_name:str) """
    pass

def set_error_literal(domain, code, message): # real signature unknown; restored from __doc__
    """ set_error_literal(domain:int, code:int, message:str) -> err:error """
    pass

def set_prgname(prgname): # real signature unknown; restored from __doc__
    """ set_prgname(prgname:str) """
    pass

def shell_error_quark(): # real signature unknown; restored from __doc__
    """ shell_error_quark() -> int """
    return 0

def shell_parse_argv(command_line): # real signature unknown; restored from __doc__
    """ shell_parse_argv(command_line:str) -> bool, argvp:list """
    return False

def shell_quote(unquoted_string): # real signature unknown; restored from __doc__
    """ shell_quote(unquoted_string:str) -> str """
    return ""

def shell_unquote(quoted_string): # real signature unknown; restored from __doc__
    """ shell_unquote(quoted_string:str) -> str """
    return ""

def slice_alloc(block_size): # real signature unknown; restored from __doc__
    """ slice_alloc(block_size:int) """
    pass

def slice_alloc0(block_size): # real signature unknown; restored from __doc__
    """ slice_alloc0(block_size:int) """
    pass

def slice_copy(block_size, mem_block=None): # real signature unknown; restored from __doc__
    """ slice_copy(block_size:int, mem_block=None) """
    pass

def slice_free1(block_size, mem_block=None): # real signature unknown; restored from __doc__
    """ slice_free1(block_size:int, mem_block=None) """
    pass

def slice_free_chain_with_offset(block_size, mem_chain=None, next_offset): # real signature unknown; restored from __doc__
    """ slice_free_chain_with_offset(block_size:int, mem_chain=None, next_offset:int) """
    pass

def slice_get_config(ckey): # real signature unknown; restored from __doc__
    """ slice_get_config(ckey:GLib.SliceConfig) -> int """
    return 0

def slice_get_config_state(ckey, address, n_values): # real signature unknown; restored from __doc__
    """ slice_get_config_state(ckey:GLib.SliceConfig, address:int, n_values:int) -> int """
    return 0

def slice_set_config(ckey, value): # real signature unknown; restored from __doc__
    """ slice_set_config(ckey:GLib.SliceConfig, value:int) """
    pass

def slist_pop_allocator(): # real signature unknown; restored from __doc__
    """ slist_pop_allocator() """
    pass

def slist_push_allocator(allocator): # real signature unknown; restored from __doc__
    """ slist_push_allocator(allocator:GLib.Allocator) """
    pass

def source_remove(tag): # real signature unknown; restored from __doc__
    """ source_remove(tag:int) -> bool """
    return False

def source_remove_by_funcs_user_data(funcs, user_data=None): # real signature unknown; restored from __doc__
    """ source_remove_by_funcs_user_data(funcs:GLib.SourceFuncs, user_data=None) -> bool """
    return False

def source_remove_by_user_data(user_data=None): # real signature unknown; restored from __doc__
    """ source_remove_by_user_data(user_data=None) -> bool """
    return False

def source_set_name_by_id(tag, name): # real signature unknown; restored from __doc__
    """ source_set_name_by_id(tag:int, name:str) """
    pass

def spaced_primes_closest(num): # real signature unknown; restored from __doc__
    """ spaced_primes_closest(num:int) -> int """
    return 0

def spawn_async_with_fds(working_directory=None, argv, envp=None, flags, child_setup=None, user_data=None, stdin_fd, stdout_fd, stderr_fd): # real signature unknown; restored from __doc__
    """ spawn_async_with_fds(working_directory:str=None, argv:list, envp:list=None, flags:GLib.SpawnFlags, child_setup:GLib.SpawnChildSetupFunc=None, user_data=None, stdin_fd:int, stdout_fd:int, stderr_fd:int) -> bool, child_pid """
    return False

def spawn_async_with_pipes(working_directory=None, argv, envp=None, flags, child_setup=None, user_data=None): # real signature unknown; restored from __doc__
    """ spawn_async_with_pipes(working_directory:str=None, argv:list, envp:list=None, flags:GLib.SpawnFlags, child_setup:GLib.SpawnChildSetupFunc=None, user_data=None) -> bool, child_pid, standard_input:int, standard_output:int, standard_error:int """
    return False

def spawn_async_with_pipes_and_fds(working_directory=None, argv, envp=None, flags, child_setup=None, user_data=None, stdin_fd, stdout_fd, stderr_fd, source_fds=None, target_fds=None): # real signature unknown; restored from __doc__
    """ spawn_async_with_pipes_and_fds(working_directory:str=None, argv:list, envp:list=None, flags:GLib.SpawnFlags, child_setup:GLib.SpawnChildSetupFunc=None, user_data=None, stdin_fd:int, stdout_fd:int, stderr_fd:int, source_fds:list=None, target_fds:list=None) -> bool, child_pid_out, stdin_pipe_out:int, stdout_pipe_out:int, stderr_pipe_out:int """
    return False

def spawn_check_exit_status(wait_status): # real signature unknown; restored from __doc__
    """ spawn_check_exit_status(wait_status:int) -> bool """
    return False

def spawn_check_wait_status(wait_status): # real signature unknown; restored from __doc__
    """ spawn_check_wait_status(wait_status:int) -> bool """
    return False

def spawn_close_pid(pid): # real signature unknown; restored from __doc__
    """ spawn_close_pid(pid) """
    pass

def spawn_command_line_async(command_line): # real signature unknown; restored from __doc__
    """ spawn_command_line_async(command_line:str) -> bool """
    return False

def spawn_command_line_sync(command_line): # real signature unknown; restored from __doc__
    """ spawn_command_line_sync(command_line:str) -> bool, standard_output:list, standard_error:list, wait_status:int """
    return False

def spawn_error_quark(): # real signature unknown; restored from __doc__
    """ spawn_error_quark() -> int """
    return 0

def spawn_exit_error_quark(): # real signature unknown; restored from __doc__
    """ spawn_exit_error_quark() -> int """
    return 0

def spawn_sync(working_directory=None, argv, envp=None, flags, child_setup=None, user_data=None): # real signature unknown; restored from __doc__
    """ spawn_sync(working_directory:str=None, argv:list, envp:list=None, flags:GLib.SpawnFlags, child_setup:GLib.SpawnChildSetupFunc=None, user_data=None) -> bool, standard_output:list, standard_error:list, wait_status:int """
    return False

def stat(filename, buf): # real signature unknown; restored from __doc__
    """ stat(filename:str, buf:GLib.StatBuf) -> int """
    return 0

def stpcpy(dest, src): # real signature unknown; restored from __doc__
    """ stpcpy(dest:str, src:str) -> str """
    return ""

def strcanon(string, valid_chars, substitutor): # real signature unknown; restored from __doc__
    """ strcanon(string:str, valid_chars:str, substitutor:int) -> str """
    return ""

def strcasecmp(s1, s2): # real signature unknown; restored from __doc__
    """ strcasecmp(s1:str, s2:str) -> int """
    return 0

def strchomp(string): # real signature unknown; restored from __doc__
    """ strchomp(string:str) -> str """
    return ""

def strchug(string): # real signature unknown; restored from __doc__
    """ strchug(string:str) -> str """
    return ""

def strcmp0(str1=None, str2=None): # real signature unknown; restored from __doc__
    """ strcmp0(str1:str=None, str2:str=None) -> int """
    return 0

def strcompress(source): # real signature unknown; restored from __doc__
    """ strcompress(source:str) -> str """
    return ""

def strdelimit(string, delimiters=None, new_delimiter): # real signature unknown; restored from __doc__
    """ strdelimit(string:str, delimiters:str=None, new_delimiter:int) -> str """
    return ""

def strdown(string): # real signature unknown; restored from __doc__
    """ strdown(string:str) -> str """
    return ""

def strdup(p_str=None): # real signature unknown; restored from __doc__
    """ strdup(str:str=None) -> str """
    return ""

def strdupv(str_array=None): # real signature unknown; restored from __doc__
    """ strdupv(str_array:list=None) -> list or None """
    return []

def strerror(errnum): # real signature unknown; restored from __doc__
    """ strerror(errnum:int) -> str """
    return ""

def strescape(source, exceptions=None): # real signature unknown; restored from __doc__
    """ strescape(source:str, exceptions:str=None) -> str """
    return ""

def strfreev(str_array=None): # real signature unknown; restored from __doc__
    """ strfreev(str_array:list=None) """
    pass

def strip_context(msgid, msgval): # real signature unknown; restored from __doc__
    """ strip_context(msgid:str, msgval:str) -> str """
    return ""

def strjoinv(separator=None, str_array): # real signature unknown; restored from __doc__
    """ strjoinv(separator:str=None, str_array:list) -> str """
    return ""

def strlcat(dest, src, dest_size): # real signature unknown; restored from __doc__
    """ strlcat(dest:str, src:str, dest_size:int) -> int """
    return 0

def strlcpy(dest, src, dest_size): # real signature unknown; restored from __doc__
    """ strlcpy(dest:str, src:str, dest_size:int) -> int """
    return 0

def strncasecmp(s1, s2, n): # real signature unknown; restored from __doc__
    """ strncasecmp(s1:str, s2:str, n:int) -> int """
    return 0

def strndup(p_str=None, n): # real signature unknown; restored from __doc__
    """ strndup(str:str=None, n:int) -> str or None """
    return ""

def strnfill(length, fill_char): # real signature unknown; restored from __doc__
    """ strnfill(length:int, fill_char:int) -> str """
    return ""

def strreverse(string): # real signature unknown; restored from __doc__
    """ strreverse(string:str) -> str """
    return ""

def strrstr(haystack, needle): # real signature unknown; restored from __doc__
    """ strrstr(haystack:str, needle:str) -> str or None """
    return ""

def strrstr_len(haystack, haystack_len, needle): # real signature unknown; restored from __doc__
    """ strrstr_len(haystack:str, haystack_len:int, needle:str) -> str or None """
    return ""

def strsignal(signum): # real signature unknown; restored from __doc__
    """ strsignal(signum:int) -> str """
    return ""

def strsplit(string, delimiter, max_tokens): # real signature unknown; restored from __doc__
    """ strsplit(string:str, delimiter:str, max_tokens:int) -> list """
    return []

def strsplit_set(string, delimiters, max_tokens): # real signature unknown; restored from __doc__
    """ strsplit_set(string:str, delimiters:str, max_tokens:int) -> list """
    return []

def strstr_len(haystack, haystack_len, needle): # real signature unknown; restored from __doc__
    """ strstr_len(haystack:str, haystack_len:int, needle:str) -> str or None """
    return ""

def strtod(nptr): # real signature unknown; restored from __doc__
    """ strtod(nptr:str) -> float, endptr:str """
    return 0.0

def strup(string): # real signature unknown; restored from __doc__
    """ strup(string:str) -> str """
    return ""

def strv_contains(strv, p_str): # real signature unknown; restored from __doc__
    """ strv_contains(strv:list, str:str) -> bool """
    return False

def strv_equal(strv1, strv2): # real signature unknown; restored from __doc__
    """ strv_equal(strv1:list, strv2:list) -> bool """
    return False

def strv_get_type(): # real signature unknown; restored from __doc__
    """ strv_get_type() -> GType """
    pass

def strv_length(str_array): # real signature unknown; restored from __doc__
    """ strv_length(str_array:list) -> int """
    return 0

def str_equal(v1, v2): # real signature unknown; restored from __doc__
    """ str_equal(v1, v2) -> bool """
    return False

def str_hash(v): # real signature unknown; restored from __doc__
    """ str_hash(v) -> int """
    return 0

def str_has_prefix(p_str, prefix): # real signature unknown; restored from __doc__
    """ str_has_prefix(str:str, prefix:str) -> bool """
    return False

def str_has_suffix(p_str, suffix): # real signature unknown; restored from __doc__
    """ str_has_suffix(str:str, suffix:str) -> bool """
    return False

def str_is_ascii(p_str): # real signature unknown; restored from __doc__
    """ str_is_ascii(str:str) -> bool """
    return False

def str_match_string(search_term, potential_hit, accept_alternates): # real signature unknown; restored from __doc__
    """ str_match_string(search_term:str, potential_hit:str, accept_alternates:bool) -> bool """
    return False

def str_tokenize_and_fold(string, translit_locale=None): # real signature unknown; restored from __doc__
    """ str_tokenize_and_fold(string:str, translit_locale:str=None) -> list, ascii_alternates:list """
    return []

def str_to_ascii(p_str, from_locale=None): # real signature unknown; restored from __doc__
    """ str_to_ascii(str:str, from_locale:str=None) -> str """
    return ""

def test_add_data_func(testpath, test_data=None, test_func): # real signature unknown; restored from __doc__
    """ test_add_data_func(testpath:str, test_data=None, test_func:GLib.TestDataFunc) """
    pass

def test_add_data_func_full(testpath, test_data=None, test_func): # real signature unknown; restored from __doc__
    """ test_add_data_func_full(testpath:str, test_data=None, test_func:GLib.TestDataFunc) """
    pass

def test_add_func(testpath, test_func): # real signature unknown; restored from __doc__
    """ test_add_func(testpath:str, test_func:GLib.TestFunc) """
    pass

def test_assert_expected_messages_internal(domain, file, line, func): # real signature unknown; restored from __doc__
    """ test_assert_expected_messages_internal(domain:str, file:str, line:int, func:str) """
    pass

def test_bug(bug_uri_snippet): # real signature unknown; restored from __doc__
    """ test_bug(bug_uri_snippet:str) """
    pass

def test_bug_base(uri_pattern): # real signature unknown; restored from __doc__
    """ test_bug_base(uri_pattern:str) """
    pass

def test_disable_crash_reporting(): # real signature unknown; restored from __doc__
    """ test_disable_crash_reporting() """
    pass

def test_expect_message(log_domain=None, log_level, pattern): # real signature unknown; restored from __doc__
    """ test_expect_message(log_domain:str=None, log_level:GLib.LogLevelFlags, pattern:str) """
    pass

def test_fail(): # real signature unknown; restored from __doc__
    """ test_fail() """
    pass

def test_failed(): # real signature unknown; restored from __doc__
    """ test_failed() -> bool """
    return False

def test_get_dir(file_type): # real signature unknown; restored from __doc__
    """ test_get_dir(file_type:GLib.TestFileType) -> str """
    return ""

def test_get_path(): # real signature unknown; restored from __doc__
    """ test_get_path() -> str """
    return ""

def test_incomplete(msg=None): # real signature unknown; restored from __doc__
    """ test_incomplete(msg:str=None) """
    pass

def test_log_type_name(log_type): # real signature unknown; restored from __doc__
    """ test_log_type_name(log_type:GLib.TestLogType) -> str """
    return ""

def test_queue_destroy(destroy_func, destroy_data=None): # real signature unknown; restored from __doc__
    """ test_queue_destroy(destroy_func:GLib.DestroyNotify, destroy_data=None) """
    pass

def test_queue_free(gfree_pointer=None): # real signature unknown; restored from __doc__
    """ test_queue_free(gfree_pointer=None) """
    pass

def test_rand_double(): # real signature unknown; restored from __doc__
    """ test_rand_double() -> float """
    return 0.0

def test_rand_double_range(range_start, range_end): # real signature unknown; restored from __doc__
    """ test_rand_double_range(range_start:float, range_end:float) -> float """
    return 0.0

def test_rand_int(): # real signature unknown; restored from __doc__
    """ test_rand_int() -> int """
    return 0

def test_rand_int_range(begin, end): # real signature unknown; restored from __doc__
    """ test_rand_int_range(begin:int, end:int) -> int """
    return 0

def test_run(): # real signature unknown; restored from __doc__
    """ test_run() -> int """
    return 0

def test_run_suite(suite): # real signature unknown; restored from __doc__
    """ test_run_suite(suite:GLib.TestSuite) -> int """
    return 0

def test_set_nonfatal_assertions(): # real signature unknown; restored from __doc__
    """ test_set_nonfatal_assertions() """
    pass

def test_skip(msg=None): # real signature unknown; restored from __doc__
    """ test_skip(msg:str=None) """
    pass

def test_subprocess(): # real signature unknown; restored from __doc__
    """ test_subprocess() -> bool """
    return False

def test_summary(summary): # real signature unknown; restored from __doc__
    """ test_summary(summary:str) """
    pass

def test_timer_elapsed(): # real signature unknown; restored from __doc__
    """ test_timer_elapsed() -> float """
    return 0.0

def test_timer_last(): # real signature unknown; restored from __doc__
    """ test_timer_last() -> float """
    return 0.0

def test_timer_start(): # real signature unknown; restored from __doc__
    """ test_timer_start() """
    pass

def test_trap_assertions(domain, file, line, func, assertion_flags, pattern): # real signature unknown; restored from __doc__
    """ test_trap_assertions(domain:str, file:str, line:int, func:str, assertion_flags:int, pattern:str) """
    pass

def test_trap_fork(usec_timeout, test_trap_flags): # real signature unknown; restored from __doc__
    """ test_trap_fork(usec_timeout:int, test_trap_flags:GLib.TestTrapFlags) -> bool """
    return False

def test_trap_has_passed(): # real signature unknown; restored from __doc__
    """ test_trap_has_passed() -> bool """
    return False

def test_trap_reached_timeout(): # real signature unknown; restored from __doc__
    """ test_trap_reached_timeout() -> bool """
    return False

def test_trap_subprocess(test_path=None, usec_timeout, test_flags): # real signature unknown; restored from __doc__
    """ test_trap_subprocess(test_path:str=None, usec_timeout:int, test_flags:GLib.TestSubprocessFlags) """
    pass

def test_trap_subprocess_with_envp(test_path=None, envp=None, usec_timeout, test_flags): # real signature unknown; restored from __doc__
    """ test_trap_subprocess_with_envp(test_path:str=None, envp:list=None, usec_timeout:int, test_flags:GLib.TestSubprocessFlags) """
    pass

def threads_init(): # reliably restored by inspect
    # no doc
    pass

def thread_error_quark(): # real signature unknown; restored from __doc__
    """ thread_error_quark() -> int """
    return 0

def thread_exit(retval=None): # real signature unknown; restored from __doc__
    """ thread_exit(retval=None) """
    pass

def thread_pool_get_max_idle_time(): # real signature unknown; restored from __doc__
    """ thread_pool_get_max_idle_time() -> int """
    return 0

def thread_pool_get_max_unused_threads(): # real signature unknown; restored from __doc__
    """ thread_pool_get_max_unused_threads() -> int """
    return 0

def thread_pool_get_num_unused_threads(): # real signature unknown; restored from __doc__
    """ thread_pool_get_num_unused_threads() -> int """
    return 0

def thread_pool_set_max_idle_time(interval): # real signature unknown; restored from __doc__
    """ thread_pool_set_max_idle_time(interval:int) """
    pass

def thread_pool_set_max_unused_threads(max_threads): # real signature unknown; restored from __doc__
    """ thread_pool_set_max_unused_threads(max_threads:int) """
    pass

def thread_pool_stop_unused_threads(): # real signature unknown; restored from __doc__
    """ thread_pool_stop_unused_threads() """
    pass

def thread_self(): # real signature unknown; restored from __doc__
    """ thread_self() -> GLib.Thread """
    pass

def thread_yield(): # real signature unknown; restored from __doc__
    """ thread_yield() """
    pass

def timeout_add(interval, function, *user_data, priority=0): # reliably restored by inspect
    # no doc
    pass

def timeout_add_seconds(interval, function, *user_data, priority=0): # reliably restored by inspect
    # no doc
    pass

def timeout_source_new(interval): # real signature unknown; restored from __doc__
    """ timeout_source_new(interval:int) -> GLib.Source """
    pass

def timeout_source_new_seconds(interval): # real signature unknown; restored from __doc__
    """ timeout_source_new_seconds(interval:int) -> GLib.Source """
    pass

def time_val_from_iso8601(iso_date): # real signature unknown; restored from __doc__
    """ time_val_from_iso8601(iso_date:str) -> bool, time_:GLib.TimeVal """
    return False

def trash_stack_height(stack_p): # real signature unknown; restored from __doc__
    """ trash_stack_height(stack_p:GLib.TrashStack) -> int """
    return 0

def trash_stack_peek(stack_p): # real signature unknown; restored from __doc__
    """ trash_stack_peek(stack_p:GLib.TrashStack) """
    pass

def trash_stack_pop(stack_p): # real signature unknown; restored from __doc__
    """ trash_stack_pop(stack_p:GLib.TrashStack) """
    pass

def trash_stack_push(stack_p, data_p): # real signature unknown; restored from __doc__
    """ trash_stack_push(stack_p:GLib.TrashStack, data_p) """
    pass

def try_malloc(n_bytes): # real signature unknown; restored from __doc__
    """ try_malloc(n_bytes:int) """
    pass

def try_malloc0(n_bytes): # real signature unknown; restored from __doc__
    """ try_malloc0(n_bytes:int) """
    pass

def try_malloc0_n(n_blocks, n_block_bytes): # real signature unknown; restored from __doc__
    """ try_malloc0_n(n_blocks:int, n_block_bytes:int) """
    pass

def try_malloc_n(n_blocks, n_block_bytes): # real signature unknown; restored from __doc__
    """ try_malloc_n(n_blocks:int, n_block_bytes:int) """
    pass

def try_realloc(mem=None, n_bytes): # real signature unknown; restored from __doc__
    """ try_realloc(mem=None, n_bytes:int) """
    pass

def try_realloc_n(mem=None, n_blocks, n_block_bytes): # real signature unknown; restored from __doc__
    """ try_realloc_n(mem=None, n_blocks:int, n_block_bytes:int) """
    pass

def ucs4_to_utf16(p_str): # real signature unknown; restored from __doc__
    """ ucs4_to_utf16(str:list) -> int, items_read:int, items_written:int """
    return 0

def ucs4_to_utf8(p_str): # real signature unknown; restored from __doc__
    """ ucs4_to_utf8(str:list) -> str, items_read:int, items_written:int """
    return ""

def unichar_break_type(c): # real signature unknown; restored from __doc__
    """ unichar_break_type(c:str) -> GLib.UnicodeBreakType """
    pass

def unichar_combining_class(uc): # real signature unknown; restored from __doc__
    """ unichar_combining_class(uc:str) -> int """
    return 0

def unichar_compose(a, b): # real signature unknown; restored from __doc__
    """ unichar_compose(a:str, b:str) -> bool, ch:str """
    return False

def unichar_decompose(ch): # real signature unknown; restored from __doc__
    """ unichar_decompose(ch:str) -> bool, a:str, b:str """
    return False

def unichar_digit_value(c): # real signature unknown; restored from __doc__
    """ unichar_digit_value(c:str) -> int """
    return 0

def unichar_fully_decompose(ch, compat, result_len): # real signature unknown; restored from __doc__
    """ unichar_fully_decompose(ch:str, compat:bool, result_len:int) -> int, result:str """
    return 0

def unichar_get_mirror_char(ch): # real signature unknown; restored from __doc__
    """ unichar_get_mirror_char(ch:str) -> bool, mirrored_ch:str """
    return False

def unichar_get_script(ch): # real signature unknown; restored from __doc__
    """ unichar_get_script(ch:str) -> GLib.UnicodeScript """
    pass

def unichar_isalnum(c): # real signature unknown; restored from __doc__
    """ unichar_isalnum(c:str) -> bool """
    return False

def unichar_isalpha(c): # real signature unknown; restored from __doc__
    """ unichar_isalpha(c:str) -> bool """
    return False

def unichar_iscntrl(c): # real signature unknown; restored from __doc__
    """ unichar_iscntrl(c:str) -> bool """
    return False

def unichar_isdefined(c): # real signature unknown; restored from __doc__
    """ unichar_isdefined(c:str) -> bool """
    return False

def unichar_isdigit(c): # real signature unknown; restored from __doc__
    """ unichar_isdigit(c:str) -> bool """
    return False

def unichar_isgraph(c): # real signature unknown; restored from __doc__
    """ unichar_isgraph(c:str) -> bool """
    return False

def unichar_islower(c): # real signature unknown; restored from __doc__
    """ unichar_islower(c:str) -> bool """
    return False

def unichar_ismark(c): # real signature unknown; restored from __doc__
    """ unichar_ismark(c:str) -> bool """
    return False

def unichar_isprint(c): # real signature unknown; restored from __doc__
    """ unichar_isprint(c:str) -> bool """
    return False

def unichar_ispunct(c): # real signature unknown; restored from __doc__
    """ unichar_ispunct(c:str) -> bool """
    return False

def unichar_isspace(c): # real signature unknown; restored from __doc__
    """ unichar_isspace(c:str) -> bool """
    return False

def unichar_istitle(c): # real signature unknown; restored from __doc__
    """ unichar_istitle(c:str) -> bool """
    return False

def unichar_isupper(c): # real signature unknown; restored from __doc__
    """ unichar_isupper(c:str) -> bool """
    return False

def unichar_iswide(c): # real signature unknown; restored from __doc__
    """ unichar_iswide(c:str) -> bool """
    return False

def unichar_iswide_cjk(c): # real signature unknown; restored from __doc__
    """ unichar_iswide_cjk(c:str) -> bool """
    return False

def unichar_isxdigit(c): # real signature unknown; restored from __doc__
    """ unichar_isxdigit(c:str) -> bool """
    return False

def unichar_iszerowidth(c): # real signature unknown; restored from __doc__
    """ unichar_iszerowidth(c:str) -> bool """
    return False

def unichar_tolower(c): # real signature unknown; restored from __doc__
    """ unichar_tolower(c:str) -> str """
    return ""

def unichar_totitle(c): # real signature unknown; restored from __doc__
    """ unichar_totitle(c:str) -> str """
    return ""

def unichar_toupper(c): # real signature unknown; restored from __doc__
    """ unichar_toupper(c:str) -> str """
    return ""

def unichar_to_utf8(c): # real signature unknown; restored from __doc__
    """ unichar_to_utf8(c:str) -> int, outbuf:str """
    return 0

def unichar_type(c): # real signature unknown; restored from __doc__
    """ unichar_type(c:str) -> GLib.UnicodeType """
    pass

def unichar_validate(ch): # real signature unknown; restored from __doc__
    """ unichar_validate(ch:str) -> bool """
    return False

def unichar_xdigit_value(c): # real signature unknown; restored from __doc__
    """ unichar_xdigit_value(c:str) -> int """
    return 0

def unicode_canonical_decomposition(ch, result_len): # real signature unknown; restored from __doc__
    """ unicode_canonical_decomposition(ch:str, result_len:int) -> str """
    return ""

def unicode_canonical_ordering(string): # real signature unknown; restored from __doc__
    """ unicode_canonical_ordering(string:list) """
    pass

def unicode_script_from_iso15924(iso15924): # real signature unknown; restored from __doc__
    """ unicode_script_from_iso15924(iso15924:int) -> GLib.UnicodeScript """
    pass

def unicode_script_to_iso15924(script): # real signature unknown; restored from __doc__
    """ unicode_script_to_iso15924(script:GLib.UnicodeScript) -> int """
    return 0

def unlink(filename): # real signature unknown; restored from __doc__
    """ unlink(filename:str) -> int """
    return 0

def unsetenv(variable): # real signature unknown; restored from __doc__
    """ unsetenv(variable:str) """
    pass

def uri_build(flags, scheme, userinfo=None, host=None, port, path, query=None, fragment=None): # real signature unknown; restored from __doc__
    """ uri_build(flags:GLib.UriFlags, scheme:str, userinfo:str=None, host:str=None, port:int, path:str, query:str=None, fragment:str=None) -> GLib.Uri """
    pass

def uri_build_with_user(flags, scheme, user=None, password=None, auth_params=None, host=None, port, path, query=None, fragment=None): # real signature unknown; restored from __doc__
    """ uri_build_with_user(flags:GLib.UriFlags, scheme:str, user:str=None, password:str=None, auth_params:str=None, host:str=None, port:int, path:str, query:str=None, fragment:str=None) -> GLib.Uri """
    pass

def uri_error_quark(): # real signature unknown; restored from __doc__
    """ uri_error_quark() -> int """
    return 0

def uri_escape_bytes(unescaped, reserved_chars_allowed=None): # real signature unknown; restored from __doc__
    """ uri_escape_bytes(unescaped:list, reserved_chars_allowed:str=None) -> str """
    return ""

def uri_escape_string(unescaped, reserved_chars_allowed=None, allow_utf8): # real signature unknown; restored from __doc__
    """ uri_escape_string(unescaped:str, reserved_chars_allowed:str=None, allow_utf8:bool) -> str """
    return ""

def uri_is_valid(uri_string, flags): # real signature unknown; restored from __doc__
    """ uri_is_valid(uri_string:str, flags:GLib.UriFlags) -> bool """
    return False

def uri_join(flags, scheme=None, userinfo=None, host=None, port, path, query=None, fragment=None): # real signature unknown; restored from __doc__
    """ uri_join(flags:GLib.UriFlags, scheme:str=None, userinfo:str=None, host:str=None, port:int, path:str, query:str=None, fragment:str=None) -> str """
    return ""

def uri_join_with_user(flags, scheme=None, user=None, password=None, auth_params=None, host=None, port, path, query=None, fragment=None): # real signature unknown; restored from __doc__
    """ uri_join_with_user(flags:GLib.UriFlags, scheme:str=None, user:str=None, password:str=None, auth_params:str=None, host:str=None, port:int, path:str, query:str=None, fragment:str=None) -> str """
    return ""

def uri_list_extract_uris(uri_list): # real signature unknown; restored from __doc__
    """ uri_list_extract_uris(uri_list:str) -> list """
    return []

def uri_parse(uri_string, flags): # real signature unknown; restored from __doc__
    """ uri_parse(uri_string:str, flags:GLib.UriFlags) -> GLib.Uri """
    pass

def uri_parse_params(params, length, separators, flags): # real signature unknown; restored from __doc__
    """ uri_parse_params(params:str, length:int, separators:str, flags:GLib.UriParamsFlags) -> dict """
    return {}

def uri_parse_scheme(uri): # real signature unknown; restored from __doc__
    """ uri_parse_scheme(uri:str) -> str or None """
    return ""

def uri_peek_scheme(uri): # real signature unknown; restored from __doc__
    """ uri_peek_scheme(uri:str) -> str or None """
    return ""

def uri_resolve_relative(base_uri_string=None, uri_ref, flags): # real signature unknown; restored from __doc__
    """ uri_resolve_relative(base_uri_string:str=None, uri_ref:str, flags:GLib.UriFlags) -> str """
    return ""

def uri_split(uri_ref, flags): # real signature unknown; restored from __doc__
    """ uri_split(uri_ref:str, flags:GLib.UriFlags) -> scheme:str, userinfo:str, host:str, port:int, path:str, query:str, fragment:str """
    pass

def uri_split_network(uri_string, flags): # real signature unknown; restored from __doc__
    """ uri_split_network(uri_string:str, flags:GLib.UriFlags) -> scheme:str, host:str, port:int """
    pass

def uri_split_with_user(uri_ref, flags): # real signature unknown; restored from __doc__
    """ uri_split_with_user(uri_ref:str, flags:GLib.UriFlags) -> scheme:str, user:str, password:str, auth_params:str, host:str, port:int, path:str, query:str, fragment:str """
    pass

def uri_unescape_bytes(escaped_string, length, illegal_characters=None): # real signature unknown; restored from __doc__
    """ uri_unescape_bytes(escaped_string:str, length:int, illegal_characters:str=None) -> GLib.Bytes """
    pass

def uri_unescape_segment(escaped_string=None, escaped_string_end=None, illegal_characters=None): # real signature unknown; restored from __doc__
    """ uri_unescape_segment(escaped_string:str=None, escaped_string_end:str=None, illegal_characters:str=None) -> str or None """
    return ""

def uri_unescape_string(escaped_string, illegal_characters=None): # real signature unknown; restored from __doc__
    """ uri_unescape_string(escaped_string:str, illegal_characters:str=None) -> str or None """
    return ""

def usleep(microseconds): # real signature unknown; restored from __doc__
    """ usleep(microseconds:int) """
    pass

def utf16_to_ucs4(p_str): # real signature unknown; restored from __doc__
    """ utf16_to_ucs4(str:list) -> str, items_read:int, items_written:int """
    return ""

def utf16_to_utf8(p_str): # real signature unknown; restored from __doc__
    """ utf16_to_utf8(str:list) -> str, items_read:int, items_written:int """
    return ""

def utf8_casefold(p_str, len): # real signature unknown; restored from __doc__
    """ utf8_casefold(str:str, len:int) -> str """
    return ""

def utf8_collate(str1, str2): # real signature unknown; restored from __doc__
    """ utf8_collate(str1:str, str2:str) -> int """
    return 0

def utf8_collate_key(p_str, len): # real signature unknown; restored from __doc__
    """ utf8_collate_key(str:str, len:int) -> str """
    return ""

def utf8_collate_key_for_filename(p_str, len): # real signature unknown; restored from __doc__
    """ utf8_collate_key_for_filename(str:str, len:int) -> str """
    return ""

def utf8_find_next_char(p, end=None): # real signature unknown; restored from __doc__
    """ utf8_find_next_char(p:str, end:str=None) -> str or None """
    return ""

def utf8_find_prev_char(p_str, p): # real signature unknown; restored from __doc__
    """ utf8_find_prev_char(str:str, p:str) -> str or None """
    return ""

def utf8_get_char(p): # real signature unknown; restored from __doc__
    """ utf8_get_char(p:str) -> str """
    return ""

def utf8_get_char_validated(p, max_len): # real signature unknown; restored from __doc__
    """ utf8_get_char_validated(p:str, max_len:int) -> str """
    return ""

def utf8_make_valid(p_str, len): # real signature unknown; restored from __doc__
    """ utf8_make_valid(str:str, len:int) -> str """
    return ""

def utf8_normalize(p_str, len, mode): # real signature unknown; restored from __doc__
    """ utf8_normalize(str:str, len:int, mode:GLib.NormalizeMode) -> str or None """
    return ""

def utf8_offset_to_pointer(p_str, offset): # real signature unknown; restored from __doc__
    """ utf8_offset_to_pointer(str:str, offset:int) -> str """
    return ""

def utf8_pointer_to_offset(p_str, pos): # real signature unknown; restored from __doc__
    """ utf8_pointer_to_offset(str:str, pos:str) -> int """
    return 0

def utf8_prev_char(p): # real signature unknown; restored from __doc__
    """ utf8_prev_char(p:str) -> str """
    return ""

def utf8_strchr(p, len, c): # real signature unknown; restored from __doc__
    """ utf8_strchr(p:str, len:int, c:str) -> str or None """
    return ""

def utf8_strdown(p_str, len): # real signature unknown; restored from __doc__
    """ utf8_strdown(str:str, len:int) -> str """
    return ""

def utf8_strlen(p, max): # real signature unknown; restored from __doc__
    """ utf8_strlen(p:str, max:int) -> int """
    return 0

def utf8_strncpy(dest, src, n): # real signature unknown; restored from __doc__
    """ utf8_strncpy(dest:str, src:str, n:int) -> str """
    return ""

def utf8_strrchr(p, len, c): # real signature unknown; restored from __doc__
    """ utf8_strrchr(p:str, len:int, c:str) -> str or None """
    return ""

def utf8_strreverse(p_str, len): # real signature unknown; restored from __doc__
    """ utf8_strreverse(str:str, len:int) -> str """
    return ""

def utf8_strup(p_str, len): # real signature unknown; restored from __doc__
    """ utf8_strup(str:str, len:int) -> str """
    return ""

def utf8_substring(p_str, start_pos, end_pos): # real signature unknown; restored from __doc__
    """ utf8_substring(str:str, start_pos:int, end_pos:int) -> str """
    return ""

def utf8_to_ucs4(p_str, len): # real signature unknown; restored from __doc__
    """ utf8_to_ucs4(str:str, len:int) -> str, items_read:int, items_written:int """
    return ""

def utf8_to_ucs4_fast(p_str, len): # real signature unknown; restored from __doc__
    """ utf8_to_ucs4_fast(str:str, len:int) -> str, items_written:int """
    return ""

def utf8_to_utf16(p_str, len): # real signature unknown; restored from __doc__
    """ utf8_to_utf16(str:str, len:int) -> int, items_read:int, items_written:int """
    return 0

def utf8_truncate_middle(string, truncate_length): # real signature unknown; restored from __doc__
    """ utf8_truncate_middle(string:str, truncate_length:int) -> str """
    return ""

def utf8_validate(p_str): # real signature unknown; restored from __doc__
    """ utf8_validate(str:list) -> bool, end:list """
    return False

def utf8_validate_len(p_str): # real signature unknown; restored from __doc__
    """ utf8_validate_len(str:list) -> bool, end:list """
    return False

def utime(filename, utb=None): # real signature unknown; restored from __doc__
    """ utime(filename:str, utb=None) -> int """
    return 0

def uuid_string_is_valid(p_str): # real signature unknown; restored from __doc__
    """ uuid_string_is_valid(str:str) -> bool """
    return False

def uuid_string_random(): # real signature unknown; restored from __doc__
    """ uuid_string_random() -> str """
    return ""

def variant_get_gtype(): # real signature unknown; restored from __doc__
    """ variant_get_gtype() -> GType """
    pass

def variant_is_object_path(string): # real signature unknown; restored from __doc__
    """ variant_is_object_path(string:str) -> bool """
    return False

def variant_is_signature(string): # real signature unknown; restored from __doc__
    """ variant_is_signature(string:str) -> bool """
    return False

def variant_parse(type=None, text, limit=None, endptr=None): # real signature unknown; restored from __doc__
    """ variant_parse(type:GLib.VariantType=None, text:str, limit:str=None, endptr:str=None) -> GLib.Variant """
    pass

def variant_parser_get_error_quark(): # real signature unknown; restored from __doc__
    """ variant_parser_get_error_quark() -> int """
    return 0

def variant_parse_error_print_context(error, source_str): # real signature unknown; restored from __doc__
    """ variant_parse_error_print_context(error:error, source_str:str) -> str """
    return ""

def variant_parse_error_quark(): # real signature unknown; restored from __doc__
    """ variant_parse_error_quark() -> int """
    return 0

def variant_type_checked_(type_string): # real signature unknown; restored from __doc__
    """ variant_type_checked_(type_string:str) -> GLib.VariantType """
    pass

def variant_type_string_get_depth_(type_string): # real signature unknown; restored from __doc__
    """ variant_type_string_get_depth_(type_string:str) -> int """
    return 0

def variant_type_string_is_valid(type_string): # real signature unknown; restored from __doc__
    """ variant_type_string_is_valid(type_string:str) -> bool """
    return False

def variant_type_string_scan(string, limit=None): # real signature unknown; restored from __doc__
    """ variant_type_string_scan(string:str, limit:str=None) -> bool, endptr:str """
    return False

def win32_check_windows_version(major, minor, spver, os_type): # real signature unknown; restored from __doc__
    """ win32_check_windows_version(major:int, minor:int, spver:int, os_type:GLib.Win32OSType) -> bool """
    return False

def win32_error_message(error): # real signature unknown; restored from __doc__
    """ win32_error_message(error:int) -> str """
    return ""

def win32_ftruncate(f, size): # real signature unknown; restored from __doc__
    """ win32_ftruncate(f:int, size:int) -> int """
    return 0

def win32_getlocale(): # real signature unknown; restored from __doc__
    """ win32_getlocale() -> str """
    return ""

def win32_get_command_line(): # real signature unknown; restored from __doc__
    """ win32_get_command_line() -> list """
    return []

def win32_get_package_installation_directory(package=None, dll_name=None): # real signature unknown; restored from __doc__
    """ win32_get_package_installation_directory(package:str=None, dll_name:str=None) -> str """
    return ""

def win32_get_package_installation_directory_of_module(hmodule=None): # real signature unknown; restored from __doc__
    """ win32_get_package_installation_directory_of_module(hmodule=None) -> str """
    return ""

def win32_get_package_installation_subdirectory(package=None, dll_name=None, subdir): # real signature unknown; restored from __doc__
    """ win32_get_package_installation_subdirectory(package:str=None, dll_name:str=None, subdir:str) -> str """
    return ""

def win32_get_system_data_dirs_for_module(address_of_function=None): # real signature unknown; restored from __doc__
    """ win32_get_system_data_dirs_for_module(address_of_function=None) -> list """
    return []

def win32_get_windows_version(): # real signature unknown; restored from __doc__
    """ win32_get_windows_version() -> int """
    return 0

def win32_locale_filename_from_utf8(utf8filename): # real signature unknown; restored from __doc__
    """ win32_locale_filename_from_utf8(utf8filename:str) -> str """
    return ""

def _child_watch_add_get_args(priority_or_pid, pid_or_callback, *args, **kwargs): # reliably restored by inspect
    # no doc
    pass

def _io_add_watch_get_args(channel, priority_, condition, *cb_and_user_data, **kwargs): # reliably restored by inspect
    # no doc
    pass

# classes

from .Allocator import Allocator
from .Array import Array
from .AsciiType import AsciiType
from .AsyncQueue import AsyncQueue
from .BookmarkFile import BookmarkFile
from .BookmarkFileError import BookmarkFileError
from .ByteArray import ByteArray
from .Bytes import Bytes
from .Cache import Cache
from .Checksum import Checksum
from .ChecksumType import ChecksumType
from .Completion import Completion
from .Cond import Cond
from .ConvertError import ConvertError
from .Data import Data
from .Date import Date
from .DateDMY import DateDMY
from .DateMonth import DateMonth
from .DateTime import DateTime
from .DateWeekday import DateWeekday
from .DebugKey import DebugKey
from .Dir import Dir
from .DoubleIEEE754 import DoubleIEEE754
from .GError import GError
from .Error import Error
from .ErrorType import ErrorType
from .FileError import FileError
from .FileSetContentsFlags import FileSetContentsFlags
from .FileTest import FileTest
from .FloatIEEE754 import FloatIEEE754
from .FormatSizeFlags import FormatSizeFlags
from .HashTable import HashTable
from .HashTableIter import HashTableIter
from .Hmac import Hmac
from .Hook import Hook
from .HookFlagMask import HookFlagMask
from .HookList import HookList
from .Source import Source
from .Idle import Idle
from .IOChannel import IOChannel
from .IOChannelError import IOChannelError
from .IOCondition import IOCondition
from .IOError import IOError
from .IOFlags import IOFlags
from .IOFuncs import IOFuncs
from .IOStatus import IOStatus
from .KeyFile import KeyFile
from .KeyFileError import KeyFileError
from .KeyFileFlags import KeyFileFlags
from .List import List
from .LogField import LogField
from .LogLevelFlags import LogLevelFlags
from .LogWriterOutput import LogWriterOutput
from .MainContext import MainContext
from .MainContextFlags import MainContextFlags
from .MainLoop import MainLoop
from .MappedFile import MappedFile
from .MarkupCollectType import MarkupCollectType
from .MarkupError import MarkupError
from .MarkupParseContext import MarkupParseContext
from .MarkupParseFlags import MarkupParseFlags
from .MarkupParser import MarkupParser
from .MatchInfo import MatchInfo
from .MemChunk import MemChunk
from .MemVTable import MemVTable
from .Mutex import Mutex
from .Node import Node
from .NormalizeMode import NormalizeMode
from .NumberParserError import NumberParserError
from .Once import Once
from .OnceStatus import OnceStatus
from .OptionArg import OptionArg
from .OptionContext import OptionContext
from .OptionEntry import OptionEntry
from .OptionError import OptionError
from .OptionFlags import OptionFlags
from .OptionGroup import OptionGroup
from .PathBuf import PathBuf
from .PatternSpec import PatternSpec
from .PollFD import PollFD
from .Private import Private
from .PtrArray import PtrArray
from .Queue import Queue
from .Rand import Rand
from .RecMutex import RecMutex
from .Regex import Regex
from .RegexCompileFlags import RegexCompileFlags
from .RegexError import RegexError
from .RegexMatchFlags import RegexMatchFlags
from .Relation import Relation
from .RWLock import RWLock
from .Scanner import Scanner
from .ScannerConfig import ScannerConfig
from .SeekType import SeekType
from .Sequence import Sequence
from .SequenceIter import SequenceIter
from .ShellError import ShellError
from .SliceConfig import SliceConfig
from .SList import SList
from .SourceCallbackFuncs import SourceCallbackFuncs
from .SourceFuncs import SourceFuncs
from .SourcePrivate import SourcePrivate
from .SpawnError import SpawnError
from .SpawnFlags import SpawnFlags
from .StatBuf import StatBuf
from .String import String
from .StringChunk import StringChunk
from .StrvBuilder import StrvBuilder
from .TestCase import TestCase
from .TestConfig import TestConfig
from .TestFileType import TestFileType
from .TestLogBuffer import TestLogBuffer
from .TestLogMsg import TestLogMsg
from .TestLogType import TestLogType
from .TestResult import TestResult
from .TestSubprocessFlags import TestSubprocessFlags
from .TestSuite import TestSuite
from .TestTrapFlags import TestTrapFlags
from .Thread import Thread
from .ThreadError import ThreadError
from .ThreadPool import ThreadPool
from .Timeout import Timeout
from .Timer import Timer
from .TimeType import TimeType
from .TimeVal import TimeVal
from .TimeZone import TimeZone
from .TokenType import TokenType
from .TokenValue import TokenValue
from .TrashStack import TrashStack
from .TraverseFlags import TraverseFlags
from .TraverseType import TraverseType
from .Tree import Tree
from .TreeNode import TreeNode
from .Tuples import Tuples
from .UnicodeBreakType import UnicodeBreakType
from .UnicodeScript import UnicodeScript
from .UnicodeType import UnicodeType
from .Uri import Uri
from .UriError import UriError
from .UriFlags import UriFlags
from .UriHideFlags import UriHideFlags
from .UriParamsFlags import UriParamsFlags
from .UriParamsIter import UriParamsIter
from .UserDirectory import UserDirectory
from .Variant import Variant
from .VariantBuilder import VariantBuilder
from .VariantClass import VariantClass
from .VariantDict import VariantDict
from .VariantParseError import VariantParseError
from .VariantType import VariantType
from .Win32OSType import Win32OSType
# variables with complex values

glib_version = (
    2,
    86,
    4,
)

pyglib_version = (
    3,
    56,
    0,
)

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x0000018e9fdbc440>'

__path__ = []

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GLib', loader=<gi.importer.DynamicImporter object at 0x0000018e9fdbc440>)"

