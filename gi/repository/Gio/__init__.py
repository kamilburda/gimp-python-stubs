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


# Variables with simple values

DBUS_METHOD_INVOCATION_HANDLED = True
DBUS_METHOD_INVOCATION_UNHANDLED = False

DEBUG_CONTROLLER_EXTENSION_POINT_NAME = 'gio-debug-controller'

DRIVE_IDENTIFIER_KIND_UNIX_DEVICE = 'unix-device'

FILE_ATTRIBUTE_ACCESS_CAN_DELETE = 'access::can-delete'
FILE_ATTRIBUTE_ACCESS_CAN_EXECUTE = 'access::can-execute'
FILE_ATTRIBUTE_ACCESS_CAN_READ = 'access::can-read'
FILE_ATTRIBUTE_ACCESS_CAN_RENAME = 'access::can-rename'
FILE_ATTRIBUTE_ACCESS_CAN_TRASH = 'access::can-trash'
FILE_ATTRIBUTE_ACCESS_CAN_WRITE = 'access::can-write'

FILE_ATTRIBUTE_DOS_IS_ARCHIVE = 'dos::is-archive'
FILE_ATTRIBUTE_DOS_IS_MOUNTPOINT = 'dos::is-mountpoint'
FILE_ATTRIBUTE_DOS_IS_SYSTEM = 'dos::is-system'

FILE_ATTRIBUTE_DOS_REPARSE_POINT_TAG = 'dos::reparse-point-tag'

FILE_ATTRIBUTE_ETAG_VALUE = 'etag::value'

FILE_ATTRIBUTE_FILESYSTEM_FREE = 'filesystem::free'
FILE_ATTRIBUTE_FILESYSTEM_READONLY = 'filesystem::readonly'
FILE_ATTRIBUTE_FILESYSTEM_REMOTE = 'filesystem::remote'
FILE_ATTRIBUTE_FILESYSTEM_SIZE = 'filesystem::size'
FILE_ATTRIBUTE_FILESYSTEM_TYPE = 'filesystem::type'
FILE_ATTRIBUTE_FILESYSTEM_USED = 'filesystem::used'

FILE_ATTRIBUTE_FILESYSTEM_USE_PREVIEW = 'filesystem::use-preview'

FILE_ATTRIBUTE_GVFS_BACKEND = 'gvfs::backend'

FILE_ATTRIBUTE_ID_FILE = 'id::file'
FILE_ATTRIBUTE_ID_FILESYSTEM = 'id::filesystem'

FILE_ATTRIBUTE_MOUNTABLE_CAN_EJECT = 'mountable::can-eject'
FILE_ATTRIBUTE_MOUNTABLE_CAN_MOUNT = 'mountable::can-mount'
FILE_ATTRIBUTE_MOUNTABLE_CAN_POLL = 'mountable::can-poll'
FILE_ATTRIBUTE_MOUNTABLE_CAN_START = 'mountable::can-start'

FILE_ATTRIBUTE_MOUNTABLE_CAN_START_DEGRADED = 'mountable::can-start-degraded'

FILE_ATTRIBUTE_MOUNTABLE_CAN_STOP = 'mountable::can-stop'
FILE_ATTRIBUTE_MOUNTABLE_CAN_UNMOUNT = 'mountable::can-unmount'

FILE_ATTRIBUTE_MOUNTABLE_HAL_UDI = 'mountable::hal-udi'

FILE_ATTRIBUTE_MOUNTABLE_IS_MEDIA_CHECK_AUTOMATIC = 'mountable::is-media-check-automatic'

FILE_ATTRIBUTE_MOUNTABLE_START_STOP_TYPE = 'mountable::start-stop-type'

FILE_ATTRIBUTE_MOUNTABLE_UNIX_DEVICE = 'mountable::unix-device'

FILE_ATTRIBUTE_MOUNTABLE_UNIX_DEVICE_FILE = 'mountable::unix-device-file'

FILE_ATTRIBUTE_OWNER_GROUP = 'owner::group'
FILE_ATTRIBUTE_OWNER_USER = 'owner::user'

FILE_ATTRIBUTE_OWNER_USER_REAL = 'owner::user-real'

FILE_ATTRIBUTE_PREVIEW_ICON = 'preview::icon'

FILE_ATTRIBUTE_RECENT_MODIFIED = 'recent::modified'

FILE_ATTRIBUTE_SELINUX_CONTEXT = 'selinux::context'

FILE_ATTRIBUTE_STANDARD_ALLOCATED_SIZE = 'standard::allocated-size'

FILE_ATTRIBUTE_STANDARD_CONTENT_TYPE = 'standard::content-type'

FILE_ATTRIBUTE_STANDARD_COPY_NAME = 'standard::copy-name'

FILE_ATTRIBUTE_STANDARD_DESCRIPTION = 'standard::description'

FILE_ATTRIBUTE_STANDARD_DISPLAY_NAME = 'standard::display-name'

FILE_ATTRIBUTE_STANDARD_EDIT_NAME = 'standard::edit-name'

FILE_ATTRIBUTE_STANDARD_FAST_CONTENT_TYPE = 'standard::fast-content-type'

FILE_ATTRIBUTE_STANDARD_ICON = 'standard::icon'

FILE_ATTRIBUTE_STANDARD_IS_BACKUP = 'standard::is-backup'
FILE_ATTRIBUTE_STANDARD_IS_HIDDEN = 'standard::is-hidden'
FILE_ATTRIBUTE_STANDARD_IS_SYMLINK = 'standard::is-symlink'
FILE_ATTRIBUTE_STANDARD_IS_VIRTUAL = 'standard::is-virtual'
FILE_ATTRIBUTE_STANDARD_IS_VOLATILE = 'standard::is-volatile'

FILE_ATTRIBUTE_STANDARD_NAME = 'standard::name'
FILE_ATTRIBUTE_STANDARD_SIZE = 'standard::size'

FILE_ATTRIBUTE_STANDARD_SORT_ORDER = 'standard::sort-order'

FILE_ATTRIBUTE_STANDARD_SYMBOLIC_ICON = 'standard::symbolic-icon'

FILE_ATTRIBUTE_STANDARD_SYMLINK_TARGET = 'standard::symlink-target'

FILE_ATTRIBUTE_STANDARD_TARGET_URI = 'standard::target-uri'

FILE_ATTRIBUTE_STANDARD_TYPE = 'standard::type'

FILE_ATTRIBUTE_THUMBNAILING_FAILED = 'thumbnail::failed'

FILE_ATTRIBUTE_THUMBNAILING_FAILED_LARGE = 'thumbnail::failed-large'
FILE_ATTRIBUTE_THUMBNAILING_FAILED_NORMAL = 'thumbnail::failed-normal'
FILE_ATTRIBUTE_THUMBNAILING_FAILED_XLARGE = 'thumbnail::failed-xlarge'
FILE_ATTRIBUTE_THUMBNAILING_FAILED_XXLARGE = 'thumbnail::failed-xxlarge'

FILE_ATTRIBUTE_THUMBNAIL_IS_VALID = 'thumbnail::is-valid'

FILE_ATTRIBUTE_THUMBNAIL_IS_VALID_LARGE = 'thumbnail::is-valid-large'
FILE_ATTRIBUTE_THUMBNAIL_IS_VALID_NORMAL = 'thumbnail::is-valid-normal'
FILE_ATTRIBUTE_THUMBNAIL_IS_VALID_XLARGE = 'thumbnail::is-valid-xlarge'
FILE_ATTRIBUTE_THUMBNAIL_IS_VALID_XXLARGE = 'thumbnail::is-valid-xxlarge'

FILE_ATTRIBUTE_THUMBNAIL_PATH = 'thumbnail::path'

FILE_ATTRIBUTE_THUMBNAIL_PATH_LARGE = 'thumbnail::path-large'
FILE_ATTRIBUTE_THUMBNAIL_PATH_NORMAL = 'thumbnail::path-normal'
FILE_ATTRIBUTE_THUMBNAIL_PATH_XLARGE = 'thumbnail::path-xlarge'
FILE_ATTRIBUTE_THUMBNAIL_PATH_XXLARGE = 'thumbnail::path-xxlarge'

FILE_ATTRIBUTE_TIME_ACCESS = 'time::access'

FILE_ATTRIBUTE_TIME_ACCESS_NSEC = 'time::access-nsec'
FILE_ATTRIBUTE_TIME_ACCESS_USEC = 'time::access-usec'

FILE_ATTRIBUTE_TIME_CHANGED = 'time::changed'

FILE_ATTRIBUTE_TIME_CHANGED_NSEC = 'time::changed-nsec'
FILE_ATTRIBUTE_TIME_CHANGED_USEC = 'time::changed-usec'

FILE_ATTRIBUTE_TIME_CREATED = 'time::created'

FILE_ATTRIBUTE_TIME_CREATED_NSEC = 'time::created-nsec'
FILE_ATTRIBUTE_TIME_CREATED_USEC = 'time::created-usec'

FILE_ATTRIBUTE_TIME_MODIFIED = 'time::modified'

FILE_ATTRIBUTE_TIME_MODIFIED_NSEC = 'time::modified-nsec'
FILE_ATTRIBUTE_TIME_MODIFIED_USEC = 'time::modified-usec'

FILE_ATTRIBUTE_TRASH_DELETION_DATE = 'trash::deletion-date'

FILE_ATTRIBUTE_TRASH_ITEM_COUNT = 'trash::item-count'

FILE_ATTRIBUTE_TRASH_ORIG_PATH = 'trash::orig-path'

FILE_ATTRIBUTE_UNIX_BLOCKS = 'unix::blocks'

FILE_ATTRIBUTE_UNIX_BLOCK_SIZE = 'unix::block-size'

FILE_ATTRIBUTE_UNIX_DEVICE = 'unix::device'
FILE_ATTRIBUTE_UNIX_GID = 'unix::gid'
FILE_ATTRIBUTE_UNIX_INODE = 'unix::inode'

FILE_ATTRIBUTE_UNIX_IS_MOUNTPOINT = 'unix::is-mountpoint'

FILE_ATTRIBUTE_UNIX_MODE = 'unix::mode'
FILE_ATTRIBUTE_UNIX_NLINK = 'unix::nlink'
FILE_ATTRIBUTE_UNIX_RDEV = 'unix::rdev'
FILE_ATTRIBUTE_UNIX_UID = 'unix::uid'

MEMORY_MONITOR_EXTENSION_POINT_NAME = 'gio-memory-monitor'

MENU_ATTRIBUTE_ACTION = 'action'

MENU_ATTRIBUTE_ACTION_NAMESPACE = 'action-namespace'

MENU_ATTRIBUTE_ICON = 'icon'
MENU_ATTRIBUTE_LABEL = 'label'
MENU_ATTRIBUTE_TARGET = 'target'

MENU_EXPORTER_MAX_SECTION_SIZE = 1000

MENU_LINK_SECTION = 'section'
MENU_LINK_SUBMENU = 'submenu'

NATIVE_VOLUME_MONITOR_EXTENSION_POINT_NAME = 'gio-native-volume-monitor'

NETWORK_MONITOR_EXTENSION_POINT_NAME = 'gio-network-monitor'

POWER_PROFILE_MONITOR_EXTENSION_POINT_NAME = 'gio-power-profile-monitor'

PROXY_EXTENSION_POINT_NAME = 'gio-proxy'

PROXY_RESOLVER_EXTENSION_POINT_NAME = 'gio-proxy-resolver'

SETTINGS_BACKEND_EXTENSION_POINT_NAME = 'gsettings-backend'

TLS_BACKEND_EXTENSION_POINT_NAME = 'gio-tls-backend'

TLS_DATABASE_PURPOSE_AUTHENTICATE_CLIENT = '1.3.6.1.5.5.7.3.2'
TLS_DATABASE_PURPOSE_AUTHENTICATE_SERVER = '1.3.6.1.5.5.7.3.1'

VFS_EXTENSION_POINT_NAME = 'gio-vfs'

VOLUME_IDENTIFIER_KIND_CLASS = 'class'

VOLUME_IDENTIFIER_KIND_HAL_UDI = 'hal-udi'

VOLUME_IDENTIFIER_KIND_LABEL = 'label'

VOLUME_IDENTIFIER_KIND_NFS_MOUNT = 'nfs-mount'

VOLUME_IDENTIFIER_KIND_UNIX_DEVICE = 'unix-device'

VOLUME_IDENTIFIER_KIND_UUID = 'uuid'

VOLUME_MONITOR_EXTENSION_POINT_NAME = 'gio-volume-monitor'

_namespace = 'Gio'

_version = '2.0'

# functions

def action_name_is_valid(action_name): # real signature unknown; restored from __doc__
    """ action_name_is_valid(action_name:str) -> bool """
    return False

def action_parse_detailed_name(detailed_name): # real signature unknown; restored from __doc__
    """ action_parse_detailed_name(detailed_name:str) -> bool, action_name:str, target_value:GLib.Variant """
    return False

def action_print_detailed_name(action_name, target_value=None): # real signature unknown; restored from __doc__
    """ action_print_detailed_name(action_name:str, target_value:GLib.Variant=None) -> str """
    return ""

def app_info_create_from_commandline(commandline, application_name=None, flags): # real signature unknown; restored from __doc__
    """ app_info_create_from_commandline(commandline:str, application_name:str=None, flags:Gio.AppInfoCreateFlags) -> Gio.AppInfo """
    pass

def app_info_get_all(): # real signature unknown; restored from __doc__
    """ app_info_get_all() -> list """
    return []

def app_info_get_all_for_type(content_type): # real signature unknown; restored from __doc__
    """ app_info_get_all_for_type(content_type:str) -> list """
    return []

def app_info_get_default_for_type(content_type, must_support_uris): # real signature unknown; restored from __doc__
    """ app_info_get_default_for_type(content_type:str, must_support_uris:bool) -> Gio.AppInfo or None """
    pass

def app_info_get_default_for_type_async(content_type, must_support_uris, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ app_info_get_default_for_type_async(content_type:str, must_support_uris:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def app_info_get_default_for_type_finish(result): # real signature unknown; restored from __doc__
    """ app_info_get_default_for_type_finish(result:Gio.AsyncResult) -> Gio.AppInfo """
    pass

def app_info_get_default_for_uri_scheme(uri_scheme): # real signature unknown; restored from __doc__
    """ app_info_get_default_for_uri_scheme(uri_scheme:str) -> Gio.AppInfo or None """
    pass

def app_info_get_default_for_uri_scheme_async(uri_scheme, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ app_info_get_default_for_uri_scheme_async(uri_scheme:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def app_info_get_default_for_uri_scheme_finish(result): # real signature unknown; restored from __doc__
    """ app_info_get_default_for_uri_scheme_finish(result:Gio.AsyncResult) -> Gio.AppInfo """
    pass

def app_info_get_fallback_for_type(content_type): # real signature unknown; restored from __doc__
    """ app_info_get_fallback_for_type(content_type:str) -> list """
    return []

def app_info_get_recommended_for_type(content_type): # real signature unknown; restored from __doc__
    """ app_info_get_recommended_for_type(content_type:str) -> list """
    return []

def app_info_launch_default_for_uri(uri, context=None): # real signature unknown; restored from __doc__
    """ app_info_launch_default_for_uri(uri:str, context:Gio.AppLaunchContext=None) -> bool """
    return False

def app_info_launch_default_for_uri_async(uri, context=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ app_info_launch_default_for_uri_async(uri:str, context:Gio.AppLaunchContext=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def app_info_launch_default_for_uri_finish(result): # real signature unknown; restored from __doc__
    """ app_info_launch_default_for_uri_finish(result:Gio.AsyncResult) -> bool """
    return False

def app_info_reset_type_associations(content_type): # real signature unknown; restored from __doc__
    """ app_info_reset_type_associations(content_type:str) """
    pass

def async_initable_newv_async(object_type, n_parameters, parameters, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ async_initable_newv_async(object_type:GType, n_parameters:int, parameters:GObject.Parameter, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def bus_get(bus_type, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ bus_get(bus_type:Gio.BusType, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def bus_get_finish(res): # real signature unknown; restored from __doc__
    """ bus_get_finish(res:Gio.AsyncResult) -> Gio.DBusConnection """
    pass

def bus_get_sync(bus_type, cancellable=None): # real signature unknown; restored from __doc__
    """ bus_get_sync(bus_type:Gio.BusType, cancellable:Gio.Cancellable=None) -> Gio.DBusConnection """
    pass

def bus_own_name(bus_type, name, flags, bus_acquired_closure=None, name_acquired_closure=None, name_lost_closure=None): # real signature unknown; restored from __doc__
    """ bus_own_name(bus_type:Gio.BusType, name:str, flags:Gio.BusNameOwnerFlags, bus_acquired_closure:GObject.Closure=None, name_acquired_closure:GObject.Closure=None, name_lost_closure:GObject.Closure=None) -> int """
    return 0

def bus_own_name_on_connection(connection, name, flags, name_acquired_closure=None, name_lost_closure=None): # real signature unknown; restored from __doc__
    """ bus_own_name_on_connection(connection:Gio.DBusConnection, name:str, flags:Gio.BusNameOwnerFlags, name_acquired_closure:GObject.Closure=None, name_lost_closure:GObject.Closure=None) -> int """
    return 0

def bus_unown_name(owner_id): # real signature unknown; restored from __doc__
    """ bus_unown_name(owner_id:int) """
    pass

def bus_unwatch_name(watcher_id): # real signature unknown; restored from __doc__
    """ bus_unwatch_name(watcher_id:int) """
    pass

def bus_watch_name(bus_type, name, flags, name_appeared_closure=None, name_vanished_closure=None): # real signature unknown; restored from __doc__
    """ bus_watch_name(bus_type:Gio.BusType, name:str, flags:Gio.BusNameWatcherFlags, name_appeared_closure:GObject.Closure=None, name_vanished_closure:GObject.Closure=None) -> int """
    return 0

def bus_watch_name_on_connection(connection, name, flags, name_appeared_closure=None, name_vanished_closure=None): # real signature unknown; restored from __doc__
    """ bus_watch_name_on_connection(connection:Gio.DBusConnection, name:str, flags:Gio.BusNameWatcherFlags, name_appeared_closure:GObject.Closure=None, name_vanished_closure:GObject.Closure=None) -> int """
    return 0

def content_types_get_registered(): # real signature unknown; restored from __doc__
    """ content_types_get_registered() -> list """
    return []

def content_type_can_be_executable(type): # real signature unknown; restored from __doc__
    """ content_type_can_be_executable(type:str) -> bool """
    return False

def content_type_equals(type1, type2): # real signature unknown; restored from __doc__
    """ content_type_equals(type1:str, type2:str) -> bool """
    return False

def content_type_from_mime_type(mime_type): # real signature unknown; restored from __doc__
    """ content_type_from_mime_type(mime_type:str) -> str or None """
    return ""

def content_type_get_description(type): # real signature unknown; restored from __doc__
    """ content_type_get_description(type:str) -> str """
    return ""

def content_type_get_generic_icon_name(type): # real signature unknown; restored from __doc__
    """ content_type_get_generic_icon_name(type:str) -> str or None """
    return ""

def content_type_get_icon(type): # real signature unknown; restored from __doc__
    """ content_type_get_icon(type:str) -> Gio.Icon """
    pass

def content_type_get_mime_dirs(): # real signature unknown; restored from __doc__
    """ content_type_get_mime_dirs() -> list """
    return []

def content_type_get_mime_type(type): # real signature unknown; restored from __doc__
    """ content_type_get_mime_type(type:str) -> str or None """
    return ""

def content_type_get_symbolic_icon(type): # real signature unknown; restored from __doc__
    """ content_type_get_symbolic_icon(type:str) -> Gio.Icon """
    pass

def content_type_guess(filename=None, data=None): # real signature unknown; restored from __doc__
    """ content_type_guess(filename:str=None, data:list=None) -> str, result_uncertain:bool """
    return ""

def content_type_guess_for_tree(root): # real signature unknown; restored from __doc__
    """ content_type_guess_for_tree(root:Gio.File) -> list """
    return []

def content_type_is_a(type, supertype): # real signature unknown; restored from __doc__
    """ content_type_is_a(type:str, supertype:str) -> bool """
    return False

def content_type_is_mime_type(type, mime_type): # real signature unknown; restored from __doc__
    """ content_type_is_mime_type(type:str, mime_type:str) -> bool """
    return False

def content_type_is_unknown(type): # real signature unknown; restored from __doc__
    """ content_type_is_unknown(type:str) -> bool """
    return False

def content_type_set_mime_dirs(dirs=None): # real signature unknown; restored from __doc__
    """ content_type_set_mime_dirs(dirs:list=None) """
    pass

def dbus_address_escape_value(string): # real signature unknown; restored from __doc__
    """ dbus_address_escape_value(string:str) -> str """
    return ""

def dbus_address_get_for_bus_sync(bus_type, cancellable=None): # real signature unknown; restored from __doc__
    """ dbus_address_get_for_bus_sync(bus_type:Gio.BusType, cancellable:Gio.Cancellable=None) -> str """
    return ""

def dbus_address_get_stream(address, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ dbus_address_get_stream(address:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def dbus_address_get_stream_finish(res): # real signature unknown; restored from __doc__
    """ dbus_address_get_stream_finish(res:Gio.AsyncResult) -> Gio.IOStream, out_guid:str """
    pass

def dbus_address_get_stream_sync(address, cancellable=None): # real signature unknown; restored from __doc__
    """ dbus_address_get_stream_sync(address:str, cancellable:Gio.Cancellable=None) -> Gio.IOStream, out_guid:str """
    pass

def dbus_annotation_info_lookup(annotations=None, name): # real signature unknown; restored from __doc__
    """ dbus_annotation_info_lookup(annotations:list=None, name:str) -> str or None """
    return ""

def dbus_error_encode_gerror(error): # real signature unknown; restored from __doc__
    """ dbus_error_encode_gerror(error:error) -> str """
    return ""

def dbus_error_get_remote_error(error): # real signature unknown; restored from __doc__
    """ dbus_error_get_remote_error(error:error) -> str or None """
    return ""

def dbus_error_is_remote_error(error): # real signature unknown; restored from __doc__
    """ dbus_error_is_remote_error(error:error) -> bool """
    return False

def dbus_error_new_for_dbus_error(dbus_error_name, dbus_error_message): # real signature unknown; restored from __doc__
    """ dbus_error_new_for_dbus_error(dbus_error_name:str, dbus_error_message:str) -> error """
    pass

def dbus_error_quark(): # real signature unknown; restored from __doc__
    """ dbus_error_quark() -> int """
    return 0

def dbus_error_register_error(error_domain, error_code, dbus_error_name): # real signature unknown; restored from __doc__
    """ dbus_error_register_error(error_domain:int, error_code:int, dbus_error_name:str) -> bool """
    return False

def dbus_error_register_error_domain(error_domain_quark_name, quark_volatile, entries): # real signature unknown; restored from __doc__
    """ dbus_error_register_error_domain(error_domain_quark_name:str, quark_volatile:int, entries:list) """
    pass

def dbus_error_strip_remote_error(error): # real signature unknown; restored from __doc__
    """ dbus_error_strip_remote_error(error:error) -> bool """
    return False

def dbus_error_unregister_error(error_domain, error_code, dbus_error_name): # real signature unknown; restored from __doc__
    """ dbus_error_unregister_error(error_domain:int, error_code:int, dbus_error_name:str) -> bool """
    return False

def dbus_escape_object_path(s): # real signature unknown; restored from __doc__
    """ dbus_escape_object_path(s:str) -> str """
    return ""

def dbus_escape_object_path_bytestring(bytes): # real signature unknown; restored from __doc__
    """ dbus_escape_object_path_bytestring(bytes:list) -> str """
    return ""

def dbus_generate_guid(): # real signature unknown; restored from __doc__
    """ dbus_generate_guid() -> str """
    return ""

def dbus_gvalue_to_gvariant(gvalue, type): # real signature unknown; restored from __doc__
    """ dbus_gvalue_to_gvariant(gvalue:GObject.Value, type:GLib.VariantType) -> GLib.Variant """
    pass

def dbus_gvariant_to_gvalue(value): # real signature unknown; restored from __doc__
    """ dbus_gvariant_to_gvalue(value:GLib.Variant) -> out_gvalue:GObject.Value """
    pass

def dbus_is_address(string): # real signature unknown; restored from __doc__
    """ dbus_is_address(string:str) -> bool """
    return False

def dbus_is_error_name(string): # real signature unknown; restored from __doc__
    """ dbus_is_error_name(string:str) -> bool """
    return False

def dbus_is_guid(string): # real signature unknown; restored from __doc__
    """ dbus_is_guid(string:str) -> bool """
    return False

def dbus_is_interface_name(string): # real signature unknown; restored from __doc__
    """ dbus_is_interface_name(string:str) -> bool """
    return False

def dbus_is_member_name(string): # real signature unknown; restored from __doc__
    """ dbus_is_member_name(string:str) -> bool """
    return False

def dbus_is_name(string): # real signature unknown; restored from __doc__
    """ dbus_is_name(string:str) -> bool """
    return False

def dbus_is_supported_address(string): # real signature unknown; restored from __doc__
    """ dbus_is_supported_address(string:str) -> bool """
    return False

def dbus_is_unique_name(string): # real signature unknown; restored from __doc__
    """ dbus_is_unique_name(string:str) -> bool """
    return False

def dbus_unescape_object_path(s): # real signature unknown; restored from __doc__
    """ dbus_unescape_object_path(s:str) -> list or None """
    return []

def dtls_client_connection_new(base_socket, server_identity=None): # real signature unknown; restored from __doc__
    """ dtls_client_connection_new(base_socket:Gio.DatagramBased, server_identity:Gio.SocketConnectable=None) -> Gio.DtlsClientConnection """
    pass

def dtls_server_connection_new(base_socket, certificate=None): # real signature unknown; restored from __doc__
    """ dtls_server_connection_new(base_socket:Gio.DatagramBased, certificate:Gio.TlsCertificate=None) -> Gio.DtlsServerConnection """
    pass

def file_new_build_filenamev(args): # real signature unknown; restored from __doc__
    """ file_new_build_filenamev(args:list) -> Gio.File """
    pass

def file_new_for_commandline_arg(arg): # real signature unknown; restored from __doc__
    """ file_new_for_commandline_arg(arg:str) -> Gio.File """
    pass

def file_new_for_commandline_arg_and_cwd(arg, cwd): # real signature unknown; restored from __doc__
    """ file_new_for_commandline_arg_and_cwd(arg:str, cwd:str) -> Gio.File """
    pass

def file_new_for_path(path): # real signature unknown; restored from __doc__
    """ file_new_for_path(path:str) -> Gio.File """
    pass

def file_new_for_uri(uri): # real signature unknown; restored from __doc__
    """ file_new_for_uri(uri:str) -> Gio.File """
    pass

def file_new_tmp(tmpl=None): # real signature unknown; restored from __doc__
    """ file_new_tmp(tmpl:str=None) -> Gio.File, iostream:Gio.FileIOStream """
    pass

def file_new_tmp_async(tmpl=None, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ file_new_tmp_async(tmpl:str=None, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def file_new_tmp_dir_async(tmpl=None, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ file_new_tmp_dir_async(tmpl:str=None, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def file_new_tmp_dir_finish(result): # real signature unknown; restored from __doc__
    """ file_new_tmp_dir_finish(result:Gio.AsyncResult) -> Gio.File """
    pass

def file_new_tmp_finish(result): # real signature unknown; restored from __doc__
    """ file_new_tmp_finish(result:Gio.AsyncResult) -> Gio.File, iostream:Gio.FileIOStream """
    pass

def file_parse_name(parse_name): # real signature unknown; restored from __doc__
    """ file_parse_name(parse_name:str) -> Gio.File """
    pass

def icon_deserialize(value): # real signature unknown; restored from __doc__
    """ icon_deserialize(value:GLib.Variant) -> Gio.Icon or None """
    pass

def icon_new_for_string(p_str): # real signature unknown; restored from __doc__
    """ icon_new_for_string(str:str) -> Gio.Icon """
    pass

def initable_newv(object_type, parameters, cancellable=None): # real signature unknown; restored from __doc__
    """ initable_newv(object_type:GType, parameters:list, cancellable:Gio.Cancellable=None) -> GObject.Object """
    pass

def io_error_from_errno(err_no): # real signature unknown; restored from __doc__
    """ io_error_from_errno(err_no:int) -> Gio.IOErrorEnum """
    pass

def io_error_from_file_error(file_error): # real signature unknown; restored from __doc__
    """ io_error_from_file_error(file_error:GLib.FileError) -> Gio.IOErrorEnum """
    pass

def io_error_from_win32_error(error_code): # real signature unknown; restored from __doc__
    """ io_error_from_win32_error(error_code:int) -> Gio.IOErrorEnum """
    pass

def io_error_quark(): # real signature unknown; restored from __doc__
    """ io_error_quark() -> int """
    return 0

def io_extension_point_implement(extension_point_name, type, extension_name, priority): # real signature unknown; restored from __doc__
    """ io_extension_point_implement(extension_point_name:str, type:GType, extension_name:str, priority:int) -> Gio.IOExtension """
    pass

def io_extension_point_lookup(name): # real signature unknown; restored from __doc__
    """ io_extension_point_lookup(name:str) -> Gio.IOExtensionPoint """
    pass

def io_extension_point_register(name): # real signature unknown; restored from __doc__
    """ io_extension_point_register(name:str) -> Gio.IOExtensionPoint """
    pass

def io_modules_load_all_in_directory(dirname): # real signature unknown; restored from __doc__
    """ io_modules_load_all_in_directory(dirname:str) -> list """
    return []

def io_modules_load_all_in_directory_with_scope(dirname, scope): # real signature unknown; restored from __doc__
    """ io_modules_load_all_in_directory_with_scope(dirname:str, scope:Gio.IOModuleScope) -> list """
    return []

def io_modules_scan_all_in_directory(dirname): # real signature unknown; restored from __doc__
    """ io_modules_scan_all_in_directory(dirname:str) """
    pass

def io_modules_scan_all_in_directory_with_scope(dirname, scope): # real signature unknown; restored from __doc__
    """ io_modules_scan_all_in_directory_with_scope(dirname:str, scope:Gio.IOModuleScope) """
    pass

def io_scheduler_cancel_all_jobs(): # real signature unknown; restored from __doc__
    """ io_scheduler_cancel_all_jobs() """
    pass

def io_scheduler_push_job(job_func, user_data=None, io_priority, cancellable=None): # real signature unknown; restored from __doc__
    """ io_scheduler_push_job(job_func:Gio.IOSchedulerJobFunc, user_data=None, io_priority:int, cancellable:Gio.Cancellable=None) """
    pass

def keyfile_settings_backend_new(filename, root_path, root_group=None): # real signature unknown; restored from __doc__
    """ keyfile_settings_backend_new(filename:str, root_path:str, root_group:str=None) -> Gio.SettingsBackend """
    pass

def memory_monitor_dup_default(): # real signature unknown; restored from __doc__
    """ memory_monitor_dup_default() -> Gio.MemoryMonitor """
    pass

def memory_settings_backend_new(): # real signature unknown; restored from __doc__
    """ memory_settings_backend_new() -> Gio.SettingsBackend """
    pass

def networking_init(): # real signature unknown; restored from __doc__
    """ networking_init() """
    pass

def network_monitor_get_default(): # real signature unknown; restored from __doc__
    """ network_monitor_get_default() -> Gio.NetworkMonitor """
    pass

def null_settings_backend_new(): # real signature unknown; restored from __doc__
    """ null_settings_backend_new() -> Gio.SettingsBackend """
    pass

def pollable_source_new(pollable_stream): # real signature unknown; restored from __doc__
    """ pollable_source_new(pollable_stream:GObject.Object) -> GLib.Source """
    pass

def pollable_source_new_full(pollable_stream, child_source=None, cancellable=None): # real signature unknown; restored from __doc__
    """ pollable_source_new_full(pollable_stream:GObject.Object, child_source:GLib.Source=None, cancellable:Gio.Cancellable=None) -> GLib.Source """
    pass

def pollable_stream_read(stream, buffer, blocking, cancellable=None): # real signature unknown; restored from __doc__
    """ pollable_stream_read(stream:Gio.InputStream, buffer:list, blocking:bool, cancellable:Gio.Cancellable=None) -> int """
    return 0

def pollable_stream_write(stream, buffer, blocking, cancellable=None): # real signature unknown; restored from __doc__
    """ pollable_stream_write(stream:Gio.OutputStream, buffer:list, blocking:bool, cancellable:Gio.Cancellable=None) -> int """
    return 0

def pollable_stream_write_all(stream, buffer, blocking, cancellable=None): # real signature unknown; restored from __doc__
    """ pollable_stream_write_all(stream:Gio.OutputStream, buffer:list, blocking:bool, cancellable:Gio.Cancellable=None) -> bool, bytes_written:int """
    return False

def power_profile_monitor_dup_default(): # real signature unknown; restored from __doc__
    """ power_profile_monitor_dup_default() -> Gio.PowerProfileMonitor """
    pass

def proxy_get_default_for_protocol(protocol): # real signature unknown; restored from __doc__
    """ proxy_get_default_for_protocol(protocol:str) -> Gio.Proxy or None """
    pass

def proxy_resolver_get_default(): # real signature unknown; restored from __doc__
    """ proxy_resolver_get_default() -> Gio.ProxyResolver """
    pass

def resolver_error_quark(): # real signature unknown; restored from __doc__
    """ resolver_error_quark() -> int """
    return 0

def resources_enumerate_children(path, lookup_flags): # real signature unknown; restored from __doc__
    """ resources_enumerate_children(path:str, lookup_flags:Gio.ResourceLookupFlags) -> list """
    return []

def resources_get_info(path, lookup_flags): # real signature unknown; restored from __doc__
    """ resources_get_info(path:str, lookup_flags:Gio.ResourceLookupFlags) -> bool, size:int, flags:int """
    return False

def resources_has_children(path): # real signature unknown; restored from __doc__
    """ resources_has_children(path:str) -> bool """
    return False

def resources_lookup_data(path, lookup_flags): # real signature unknown; restored from __doc__
    """ resources_lookup_data(path:str, lookup_flags:Gio.ResourceLookupFlags) -> GLib.Bytes """
    pass

def resources_open_stream(path, lookup_flags): # real signature unknown; restored from __doc__
    """ resources_open_stream(path:str, lookup_flags:Gio.ResourceLookupFlags) -> Gio.InputStream """
    pass

def resources_register(resource): # real signature unknown; restored from __doc__
    """ resources_register(resource:Gio.Resource) """
    pass

def resources_unregister(resource): # real signature unknown; restored from __doc__
    """ resources_unregister(resource:Gio.Resource) """
    pass

def resource_error_quark(): # real signature unknown; restored from __doc__
    """ resource_error_quark() -> int """
    return 0

def resource_load(filename): # real signature unknown; restored from __doc__
    """ resource_load(filename:str) -> Gio.Resource """
    pass

def settings_schema_source_get_default(): # real signature unknown; restored from __doc__
    """ settings_schema_source_get_default() -> Gio.SettingsSchemaSource or None """
    pass

def simple_async_report_gerror_in_idle(p_object=None, callback=None, user_data=None, error): # real signature unknown; restored from __doc__
    """ simple_async_report_gerror_in_idle(object:GObject.Object=None, callback:Gio.AsyncReadyCallback=None, user_data=None, error:error) """
    pass

def tls_backend_get_default(): # real signature unknown; restored from __doc__
    """ tls_backend_get_default() -> Gio.TlsBackend """
    pass

def tls_channel_binding_error_quark(): # real signature unknown; restored from __doc__
    """ tls_channel_binding_error_quark() -> int """
    return 0

def tls_client_connection_new(base_io_stream, server_identity=None): # real signature unknown; restored from __doc__
    """ tls_client_connection_new(base_io_stream:Gio.IOStream, server_identity:Gio.SocketConnectable=None) -> Gio.TlsClientConnection """
    pass

def tls_error_quark(): # real signature unknown; restored from __doc__
    """ tls_error_quark() -> int """
    return 0

def tls_file_database_new(anchors): # real signature unknown; restored from __doc__
    """ tls_file_database_new(anchors:str) -> Gio.TlsFileDatabase """
    pass

def tls_server_connection_new(base_io_stream, certificate=None): # real signature unknown; restored from __doc__
    """ tls_server_connection_new(base_io_stream:Gio.IOStream, certificate:Gio.TlsCertificate=None) -> Gio.TlsServerConnection """
    pass

# classes

from .Action import Action
from .ActionEntry import ActionEntry
from .ActionGroup import ActionGroup
from .ActionGroupInterface import ActionGroupInterface
from .ActionInterface import ActionInterface
from .ActionMap import ActionMap
from .ActionMapInterface import ActionMapInterface
from .AppInfo import AppInfo
from .AppInfoCreateFlags import AppInfoCreateFlags
from .AppInfoIface import AppInfoIface
from .AppInfoMonitor import AppInfoMonitor
from .AppLaunchContext import AppLaunchContext
from .AppLaunchContextClass import AppLaunchContextClass
from .AppLaunchContextPrivate import AppLaunchContextPrivate
from .Application import Application
from .ApplicationClass import ApplicationClass
from .ApplicationCommandLine import ApplicationCommandLine
from .ApplicationCommandLineClass import ApplicationCommandLineClass
from .ApplicationCommandLinePrivate import ApplicationCommandLinePrivate
from .ApplicationFlags import ApplicationFlags
from .ApplicationPrivate import ApplicationPrivate
from .AskPasswordFlags import AskPasswordFlags
from .AsyncInitable import AsyncInitable
from .AsyncInitableIface import AsyncInitableIface
from .AsyncResult import AsyncResult
from .AsyncResultIface import AsyncResultIface
from .InputStream import InputStream
from .FilterInputStream import FilterInputStream
from .Seekable import Seekable
from .BufferedInputStream import BufferedInputStream
from .BufferedInputStreamClass import BufferedInputStreamClass
from .BufferedInputStreamPrivate import BufferedInputStreamPrivate
from .OutputStream import OutputStream
from .FilterOutputStream import FilterOutputStream
from .BufferedOutputStream import BufferedOutputStream
from .BufferedOutputStreamClass import BufferedOutputStreamClass
from .BufferedOutputStreamPrivate import BufferedOutputStreamPrivate
from .BusNameOwnerFlags import BusNameOwnerFlags
from .BusNameWatcherFlags import BusNameWatcherFlags
from .BusType import BusType
from .Icon import Icon
from .LoadableIcon import LoadableIcon
from .BytesIcon import BytesIcon
from .Cancellable import Cancellable
from .CancellableClass import CancellableClass
from .CancellablePrivate import CancellablePrivate
from .Converter import Converter
from .Initable import Initable
from .CharsetConverter import CharsetConverter
from .CharsetConverterClass import CharsetConverterClass
from .ConverterFlags import ConverterFlags
from .ConverterIface import ConverterIface
from .PollableInputStream import PollableInputStream
from .ConverterInputStream import ConverterInputStream
from .ConverterInputStreamClass import ConverterInputStreamClass
from .ConverterInputStreamPrivate import ConverterInputStreamPrivate
from .PollableOutputStream import PollableOutputStream
from .ConverterOutputStream import ConverterOutputStream
from .ConverterOutputStreamClass import ConverterOutputStreamClass
from .ConverterOutputStreamPrivate import ConverterOutputStreamPrivate
from .ConverterResult import ConverterResult
from .Credentials import Credentials
from .CredentialsClass import CredentialsClass
from .CredentialsType import CredentialsType
from .DatagramBased import DatagramBased
from .DatagramBasedInterface import DatagramBasedInterface
from .DataInputStream import DataInputStream
from .DataInputStreamClass import DataInputStreamClass
from .DataInputStreamPrivate import DataInputStreamPrivate
from .DataOutputStream import DataOutputStream
from .DataOutputStreamClass import DataOutputStreamClass
from .DataOutputStreamPrivate import DataOutputStreamPrivate
from .DataStreamByteOrder import DataStreamByteOrder
from .DataStreamNewlineType import DataStreamNewlineType
from .RemoteActionGroup import RemoteActionGroup
from .DBusActionGroup import DBusActionGroup
from .DBusAnnotationInfo import DBusAnnotationInfo
from .DBusArgInfo import DBusArgInfo
from .DBusAuthObserver import DBusAuthObserver
from .DBusCallFlags import DBusCallFlags
from .DBusCapabilityFlags import DBusCapabilityFlags
from .DBusConnection import DBusConnection
from .DBusConnectionFlags import DBusConnectionFlags
from .DBusError import DBusError
from .DBusErrorEntry import DBusErrorEntry
from .DBusInterface import DBusInterface
from .DBusInterfaceIface import DBusInterfaceIface
from .DBusInterfaceInfo import DBusInterfaceInfo
from .DBusInterfaceSkeleton import DBusInterfaceSkeleton
from .DBusInterfaceSkeletonClass import DBusInterfaceSkeletonClass
from .DBusInterfaceSkeletonFlags import DBusInterfaceSkeletonFlags
from .DBusInterfaceSkeletonPrivate import DBusInterfaceSkeletonPrivate
from .DBusInterfaceVTable import DBusInterfaceVTable
from .MenuModel import MenuModel
from .DBusMenuModel import DBusMenuModel
from .DBusMessage import DBusMessage
from .DBusMessageByteOrder import DBusMessageByteOrder
from .DBusMessageFlags import DBusMessageFlags
from .DBusMessageHeaderField import DBusMessageHeaderField
from .DBusMessageType import DBusMessageType
from .DBusMethodInfo import DBusMethodInfo
from .DBusMethodInvocation import DBusMethodInvocation
from .DBusNodeInfo import DBusNodeInfo
from .DBusObject import DBusObject
from .DBusObjectIface import DBusObjectIface
from .DBusObjectManager import DBusObjectManager
from .DBusObjectManagerClient import DBusObjectManagerClient
from .DBusObjectManagerClientClass import DBusObjectManagerClientClass
from .DBusObjectManagerClientFlags import DBusObjectManagerClientFlags
from .DBusObjectManagerClientPrivate import DBusObjectManagerClientPrivate
from .DBusObjectManagerIface import DBusObjectManagerIface
from .DBusObjectManagerServer import DBusObjectManagerServer
from .DBusObjectManagerServerClass import DBusObjectManagerServerClass
from .DBusObjectManagerServerPrivate import DBusObjectManagerServerPrivate
from .DBusObjectProxy import DBusObjectProxy
from .DBusObjectProxyClass import DBusObjectProxyClass
from .DBusObjectProxyPrivate import DBusObjectProxyPrivate
from .DBusObjectSkeleton import DBusObjectSkeleton
from .DBusObjectSkeletonClass import DBusObjectSkeletonClass
from .DBusObjectSkeletonPrivate import DBusObjectSkeletonPrivate
from .DBusPropertyInfo import DBusPropertyInfo
from .DBusPropertyInfoFlags import DBusPropertyInfoFlags
from .DBusProxy import DBusProxy
from .DBusProxyClass import DBusProxyClass
from .DBusProxyFlags import DBusProxyFlags
from .DBusProxyPrivate import DBusProxyPrivate
from .DBusSendMessageFlags import DBusSendMessageFlags
from .DBusServer import DBusServer
from .DBusServerFlags import DBusServerFlags
from .DBusSignalFlags import DBusSignalFlags
from .DBusSignalInfo import DBusSignalInfo
from .DBusSubtreeFlags import DBusSubtreeFlags
from .DBusSubtreeVTable import DBusSubtreeVTable
from .DebugController import DebugController
from .DebugControllerDBus import DebugControllerDBus
from .DebugControllerDBusClass import DebugControllerDBusClass
from .DebugControllerInterface import DebugControllerInterface
from .Drive import Drive
from .DriveIface import DriveIface
from .DriveStartFlags import DriveStartFlags
from .DriveStartStopType import DriveStartStopType
from .DtlsClientConnection import DtlsClientConnection
from .DtlsClientConnectionInterface import DtlsClientConnectionInterface
from .DtlsConnection import DtlsConnection
from .DtlsConnectionInterface import DtlsConnectionInterface
from .DtlsServerConnection import DtlsServerConnection
from .DtlsServerConnectionInterface import DtlsServerConnectionInterface
from .Emblem import Emblem
from .EmblemClass import EmblemClass
from .EmblemedIcon import EmblemedIcon
from .EmblemedIconClass import EmblemedIconClass
from .EmblemedIconPrivate import EmblemedIconPrivate
from .EmblemOrigin import EmblemOrigin
from .File import File
from .FileAttributeInfo import FileAttributeInfo
from .FileAttributeInfoFlags import FileAttributeInfoFlags
from .FileAttributeInfoList import FileAttributeInfoList
from .FileAttributeMatcher import FileAttributeMatcher
from .FileAttributeStatus import FileAttributeStatus
from .FileAttributeType import FileAttributeType
from .FileCopyFlags import FileCopyFlags
from .FileCreateFlags import FileCreateFlags
from .FileEnumerator import FileEnumerator
from .FileEnumeratorClass import FileEnumeratorClass
from .FileEnumeratorPrivate import FileEnumeratorPrivate
from .FileIcon import FileIcon
from .FileIconClass import FileIconClass
from .FileIface import FileIface
from .FileInfo import FileInfo
from .FileInfoClass import FileInfoClass
from .FileInputStream import FileInputStream
from .FileInputStreamClass import FileInputStreamClass
from .FileInputStreamPrivate import FileInputStreamPrivate
from .IOStream import IOStream
from .FileIOStream import FileIOStream
from .FileIOStreamClass import FileIOStreamClass
from .FileIOStreamPrivate import FileIOStreamPrivate
from .FileMeasureFlags import FileMeasureFlags
from .FileMonitor import FileMonitor
from .FileMonitorClass import FileMonitorClass
from .FileMonitorEvent import FileMonitorEvent
from .FileMonitorFlags import FileMonitorFlags
from .FileMonitorPrivate import FileMonitorPrivate
from .FilenameCompleter import FilenameCompleter
from .FilenameCompleterClass import FilenameCompleterClass
from .FileOutputStream import FileOutputStream
from .FileOutputStreamClass import FileOutputStreamClass
from .FileOutputStreamPrivate import FileOutputStreamPrivate
from .FileQueryInfoFlags import FileQueryInfoFlags
from .FilesystemPreviewType import FilesystemPreviewType
from .FileType import FileType
from .FilterInputStreamClass import FilterInputStreamClass
from .FilterOutputStreamClass import FilterOutputStreamClass
from .IconIface import IconIface
from .InetAddress import InetAddress
from .InetAddressClass import InetAddressClass
from .InetAddressMask import InetAddressMask
from .InetAddressMaskClass import InetAddressMaskClass
from .InetAddressMaskPrivate import InetAddressMaskPrivate
from .InetAddressPrivate import InetAddressPrivate
from .SocketConnectable import SocketConnectable
from .SocketAddress import SocketAddress
from .InetSocketAddress import InetSocketAddress
from .InetSocketAddressClass import InetSocketAddressClass
from .InetSocketAddressPrivate import InetSocketAddressPrivate
from .InitableIface import InitableIface
from .InputMessage import InputMessage
from .InputStreamClass import InputStreamClass
from .InputStreamPrivate import InputStreamPrivate
from .InputVector import InputVector
from .IOErrorEnum import IOErrorEnum
from .IOExtension import IOExtension
from .IOExtensionPoint import IOExtensionPoint
from .IOModule import IOModule
from .IOModuleClass import IOModuleClass
from .IOModuleScope import IOModuleScope
from .IOModuleScopeFlags import IOModuleScopeFlags
from .IOSchedulerJob import IOSchedulerJob
from .IOStreamAdapter import IOStreamAdapter
from .IOStreamClass import IOStreamClass
from .IOStreamPrivate import IOStreamPrivate
from .IOStreamSpliceFlags import IOStreamSpliceFlags
from .ListModel import ListModel
from .ListModelInterface import ListModelInterface
from .ListStore import ListStore
from .ListStoreClass import ListStoreClass
from .LoadableIconIface import LoadableIconIface
from .MemoryInputStream import MemoryInputStream
from .MemoryInputStreamClass import MemoryInputStreamClass
from .MemoryInputStreamPrivate import MemoryInputStreamPrivate
from .MemoryMonitor import MemoryMonitor
from .MemoryMonitorInterface import MemoryMonitorInterface
from .MemoryMonitorWarningLevel import MemoryMonitorWarningLevel
from .MemoryOutputStream import MemoryOutputStream
from .MemoryOutputStreamClass import MemoryOutputStreamClass
from .MemoryOutputStreamPrivate import MemoryOutputStreamPrivate
from .Menu import Menu
from .MenuAttributeIter import MenuAttributeIter
from .MenuAttributeIterClass import MenuAttributeIterClass
from .MenuAttributeIterPrivate import MenuAttributeIterPrivate
from .MenuItem import MenuItem
from .MenuLinkIter import MenuLinkIter
from .MenuLinkIterClass import MenuLinkIterClass
from .MenuLinkIterPrivate import MenuLinkIterPrivate
from .MenuModelClass import MenuModelClass
from .MenuModelPrivate import MenuModelPrivate
from .Mount import Mount
from .MountIface import MountIface
from .MountMountFlags import MountMountFlags
from .MountOperation import MountOperation
from .MountOperationClass import MountOperationClass
from .MountOperationPrivate import MountOperationPrivate
from .MountOperationResult import MountOperationResult
from .MountUnmountFlags import MountUnmountFlags
from .NativeSocketAddress import NativeSocketAddress
from .NativeSocketAddressClass import NativeSocketAddressClass
from .NativeSocketAddressPrivate import NativeSocketAddressPrivate
from .VolumeMonitor import VolumeMonitor
from .NativeVolumeMonitor import NativeVolumeMonitor
from .NativeVolumeMonitorClass import NativeVolumeMonitorClass
from .NetworkAddress import NetworkAddress
from .NetworkAddressClass import NetworkAddressClass
from .NetworkAddressPrivate import NetworkAddressPrivate
from .NetworkConnectivity import NetworkConnectivity
from .NetworkMonitor import NetworkMonitor
from .NetworkMonitorInterface import NetworkMonitorInterface
from .NetworkService import NetworkService
from .NetworkServiceClass import NetworkServiceClass
from .NetworkServicePrivate import NetworkServicePrivate
from .Notification import Notification
from .NotificationPriority import NotificationPriority
from .OutputMessage import OutputMessage
from .OutputStreamClass import OutputStreamClass
from .OutputStreamPrivate import OutputStreamPrivate
from .OutputStreamSpliceFlags import OutputStreamSpliceFlags
from .OutputVector import OutputVector
from .PasswordSave import PasswordSave
from .Permission import Permission
from .PermissionClass import PermissionClass
from .PermissionPrivate import PermissionPrivate
from .PollableInputStreamInterface import PollableInputStreamInterface
from .PollableOutputStreamInterface import PollableOutputStreamInterface
from .PollableReturn import PollableReturn
from .PowerProfileMonitor import PowerProfileMonitor
from .PowerProfileMonitorInterface import PowerProfileMonitorInterface
from .PropertyAction import PropertyAction
from .Proxy import Proxy
from .ProxyAddress import ProxyAddress
from .ProxyAddressClass import ProxyAddressClass
from .SocketAddressEnumerator import SocketAddressEnumerator
from .ProxyAddressEnumerator import ProxyAddressEnumerator
from .ProxyAddressEnumeratorClass import ProxyAddressEnumeratorClass
from .ProxyAddressEnumeratorPrivate import ProxyAddressEnumeratorPrivate
from .ProxyAddressPrivate import ProxyAddressPrivate
from .ProxyInterface import ProxyInterface
from .ProxyResolver import ProxyResolver
from .ProxyResolverInterface import ProxyResolverInterface
from .RemoteActionGroupInterface import RemoteActionGroupInterface
from .Resolver import Resolver
from .ResolverClass import ResolverClass
from .ResolverError import ResolverError
from .ResolverNameLookupFlags import ResolverNameLookupFlags
from .ResolverPrivate import ResolverPrivate
from .ResolverRecordType import ResolverRecordType
from .Resource import Resource
from .ResourceError import ResourceError
from .ResourceFlags import ResourceFlags
from .ResourceLookupFlags import ResourceLookupFlags
from .SeekableIface import SeekableIface
from .Settings import Settings
from .SettingsBackend import SettingsBackend
from .SettingsBackendClass import SettingsBackendClass
from .SettingsBackendPrivate import SettingsBackendPrivate
from .SettingsBindFlags import SettingsBindFlags
from .SettingsClass import SettingsClass
from .SettingsPrivate import SettingsPrivate
from .SettingsSchema import SettingsSchema
from .SettingsSchemaKey import SettingsSchemaKey
from .SettingsSchemaSource import SettingsSchemaSource
from .SimpleAction import SimpleAction
from .SimpleActionGroup import SimpleActionGroup
from .SimpleActionGroupClass import SimpleActionGroupClass
from .SimpleActionGroupPrivate import SimpleActionGroupPrivate
from .SimpleAsyncResult import SimpleAsyncResult
from .SimpleAsyncResultClass import SimpleAsyncResultClass
from .SimpleIOStream import SimpleIOStream
from .SimplePermission import SimplePermission
from .SimpleProxyResolver import SimpleProxyResolver
from .SimpleProxyResolverClass import SimpleProxyResolverClass
from .SimpleProxyResolverPrivate import SimpleProxyResolverPrivate
from .Socket import Socket
from .SocketAddressClass import SocketAddressClass
from .SocketAddressEnumeratorClass import SocketAddressEnumeratorClass
from .SocketClass import SocketClass
from .SocketClient import SocketClient
from .SocketClientClass import SocketClientClass
from .SocketClientEvent import SocketClientEvent
from .SocketClientPrivate import SocketClientPrivate
from .SocketConnectableIface import SocketConnectableIface
from .SocketConnection import SocketConnection
from .SocketConnectionClass import SocketConnectionClass
from .SocketConnectionPrivate import SocketConnectionPrivate
from .SocketControlMessage import SocketControlMessage
from .SocketControlMessageClass import SocketControlMessageClass
from .SocketControlMessagePrivate import SocketControlMessagePrivate
from .SocketFamily import SocketFamily
from .SocketListener import SocketListener
from .SocketListenerClass import SocketListenerClass
from .SocketListenerEvent import SocketListenerEvent
from .SocketListenerPrivate import SocketListenerPrivate
from .SocketMsgFlags import SocketMsgFlags
from .SocketPrivate import SocketPrivate
from .SocketProtocol import SocketProtocol
from .SocketService import SocketService
from .SocketServiceClass import SocketServiceClass
from .SocketServicePrivate import SocketServicePrivate
from .SocketType import SocketType
from .SrvTarget import SrvTarget
from .StaticResource import StaticResource
from .Subprocess import Subprocess
from .SubprocessFlags import SubprocessFlags
from .SubprocessLauncher import SubprocessLauncher
from .Task import Task
from .TaskClass import TaskClass
from .TcpConnection import TcpConnection
from .TcpConnectionClass import TcpConnectionClass
from .TcpConnectionPrivate import TcpConnectionPrivate
from .TcpWrapperConnection import TcpWrapperConnection
from .TcpWrapperConnectionClass import TcpWrapperConnectionClass
from .TcpWrapperConnectionPrivate import TcpWrapperConnectionPrivate
from .TestDBus import TestDBus
from .TestDBusFlags import TestDBusFlags
from .ThemedIcon import ThemedIcon
from .ThemedIconClass import ThemedIconClass
from .ThreadedResolver import ThreadedResolver
from .ThreadedResolverClass import ThreadedResolverClass
from .ThreadedSocketService import ThreadedSocketService
from .ThreadedSocketServiceClass import ThreadedSocketServiceClass
from .ThreadedSocketServicePrivate import ThreadedSocketServicePrivate
from .TlsAuthenticationMode import TlsAuthenticationMode
from .TlsBackend import TlsBackend
from .TlsBackendInterface import TlsBackendInterface
from .TlsCertificate import TlsCertificate
from .TlsCertificateClass import TlsCertificateClass
from .TlsCertificateFlags import TlsCertificateFlags
from .TlsCertificatePrivate import TlsCertificatePrivate
from .TlsCertificateRequestFlags import TlsCertificateRequestFlags
from .TlsChannelBindingError import TlsChannelBindingError
from .TlsChannelBindingType import TlsChannelBindingType
from .TlsClientConnection import TlsClientConnection
from .TlsClientConnectionInterface import TlsClientConnectionInterface
from .TlsConnection import TlsConnection
from .TlsConnectionClass import TlsConnectionClass
from .TlsConnectionPrivate import TlsConnectionPrivate
from .TlsDatabase import TlsDatabase
from .TlsDatabaseClass import TlsDatabaseClass
from .TlsDatabaseLookupFlags import TlsDatabaseLookupFlags
from .TlsDatabasePrivate import TlsDatabasePrivate
from .TlsDatabaseVerifyFlags import TlsDatabaseVerifyFlags
from .TlsError import TlsError
from .TlsFileDatabase import TlsFileDatabase
from .TlsFileDatabaseInterface import TlsFileDatabaseInterface
from .TlsInteraction import TlsInteraction
from .TlsInteractionClass import TlsInteractionClass
from .TlsInteractionPrivate import TlsInteractionPrivate
from .TlsInteractionResult import TlsInteractionResult
from .TlsPassword import TlsPassword
from .TlsPasswordClass import TlsPasswordClass
from .TlsPasswordFlags import TlsPasswordFlags
from .TlsPasswordPrivate import TlsPasswordPrivate
from .TlsProtocolVersion import TlsProtocolVersion
from .TlsRehandshakeMode import TlsRehandshakeMode
from .TlsServerConnection import TlsServerConnection
from .TlsServerConnectionInterface import TlsServerConnectionInterface
from .UnixConnection import UnixConnection
from .UnixConnectionClass import UnixConnectionClass
from .UnixConnectionPrivate import UnixConnectionPrivate
from .UnixCredentialsMessage import UnixCredentialsMessage
from .UnixCredentialsMessageClass import UnixCredentialsMessageClass
from .UnixCredentialsMessagePrivate import UnixCredentialsMessagePrivate
from .UnixFDList import UnixFDList
from .UnixFDListClass import UnixFDListClass
from .UnixFDListPrivate import UnixFDListPrivate
from .UnixSocketAddress import UnixSocketAddress
from .UnixSocketAddressClass import UnixSocketAddressClass
from .UnixSocketAddressPrivate import UnixSocketAddressPrivate
from .UnixSocketAddressType import UnixSocketAddressType
from .Vfs import Vfs
from .VfsClass import VfsClass
from .Volume import Volume
from .VolumeIface import VolumeIface
from .VolumeMonitorClass import VolumeMonitorClass
from .ZlibCompressor import ZlibCompressor
from .ZlibCompressorClass import ZlibCompressorClass
from .ZlibCompressorFormat import ZlibCompressorFormat
from .ZlibDecompressor import ZlibDecompressor
from .ZlibDecompressorClass import ZlibDecompressorClass
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x000001ea6de66fc0>'

__path__ = []

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Gio', loader=<gi.importer.DynamicImporter object at 0x000001ea6de66fc0>)"

