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


from .File import File

class File(File):
    # no doc
    def append_to(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ append_to(self, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> Gio.FileOutputStream """
        pass

    def append_to_async(self, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ append_to_async(self, flags:Gio.FileCreateFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def append_to_finish(self, res): # real signature unknown; restored from __doc__
        """ append_to_finish(self, res:Gio.AsyncResult) -> Gio.FileOutputStream """
        pass

    def build_attribute_list_for_copy(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ build_attribute_list_for_copy(self, flags:Gio.FileCopyFlags, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def copy(self, destination, flags, cancellable=None, progress_callback=None, progress_callback_data=None): # real signature unknown; restored from __doc__
        """ copy(self, destination:Gio.File, flags:Gio.FileCopyFlags, cancellable:Gio.Cancellable=None, progress_callback:Gio.FileProgressCallback=None, progress_callback_data=None) -> bool """
        return False

    def copy_async(self, destination, flags, io_priority, cancellable=None, progress_callback_closure=None, ready_callback_closure): # real signature unknown; restored from __doc__
        """ copy_async(self, destination:Gio.File, flags:Gio.FileCopyFlags, io_priority:int, cancellable:Gio.Cancellable=None, progress_callback_closure:GObject.Closure=None, ready_callback_closure:GObject.Closure) """
        pass

    def copy_attributes(self, destination, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ copy_attributes(self, destination:Gio.File, flags:Gio.FileCopyFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def copy_finish(self, res): # real signature unknown; restored from __doc__
        """ copy_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def create(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ create(self, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> Gio.FileOutputStream """
        pass

    def create_async(self, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_async(self, flags:Gio.FileCreateFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_finish(self, res): # real signature unknown; restored from __doc__
        """ create_finish(self, res:Gio.AsyncResult) -> Gio.FileOutputStream """
        pass

    def create_readwrite(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ create_readwrite(self, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> Gio.FileIOStream """
        pass

    def create_readwrite_async(self, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_readwrite_async(self, flags:Gio.FileCreateFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_readwrite_finish(self, res): # real signature unknown; restored from __doc__
        """ create_readwrite_finish(self, res:Gio.AsyncResult) -> Gio.FileIOStream """
        pass

    def delete(self, cancellable=None): # real signature unknown; restored from __doc__
        """ delete(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def delete_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ delete_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def delete_finish(self, result): # real signature unknown; restored from __doc__
        """ delete_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> Gio.File """
        pass

    def eject_mountable(self, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ eject_mountable(self, flags:Gio.MountUnmountFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def eject_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ eject_mountable_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def eject_mountable_with_operation(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ eject_mountable_with_operation(self, flags:Gio.MountUnmountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def eject_mountable_with_operation_finish(self, result): # real signature unknown; restored from __doc__
        """ eject_mountable_with_operation_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def enumerate_children(self, attributes, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ enumerate_children(self, attributes:str, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> Gio.FileEnumerator """
        pass

    def enumerate_children_async(self, attributes, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ enumerate_children_async(self, attributes:str, flags:Gio.FileQueryInfoFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def enumerate_children_finish(self, res): # real signature unknown; restored from __doc__
        """ enumerate_children_finish(self, res:Gio.AsyncResult) -> Gio.FileEnumerator """
        pass

    def equal(self, file2): # real signature unknown; restored from __doc__
        """ equal(self, file2:Gio.File) -> bool """
        return False

    def find_enclosing_mount(self, cancellable=None): # real signature unknown; restored from __doc__
        """ find_enclosing_mount(self, cancellable:Gio.Cancellable=None) -> Gio.Mount """
        pass

    def find_enclosing_mount_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ find_enclosing_mount_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def find_enclosing_mount_finish(self, res): # real signature unknown; restored from __doc__
        """ find_enclosing_mount_finish(self, res:Gio.AsyncResult) -> Gio.Mount """
        pass

    def get_basename(self): # real signature unknown; restored from __doc__
        """ get_basename(self) -> str or None """
        return ""

    def get_child(self, name): # real signature unknown; restored from __doc__
        """ get_child(self, name:str) -> Gio.File """
        pass

    def get_child_for_display_name(self, display_name): # real signature unknown; restored from __doc__
        """ get_child_for_display_name(self, display_name:str) -> Gio.File """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gio.File or None """
        pass

    def get_parse_name(self): # real signature unknown; restored from __doc__
        """ get_parse_name(self) -> str """
        return ""

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> str or None """
        return ""

    def get_relative_path(self, descendant): # real signature unknown; restored from __doc__
        """ get_relative_path(self, descendant:Gio.File) -> str or None """
        return ""

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str """
        return ""

    def get_uri_scheme(self): # real signature unknown; restored from __doc__
        """ get_uri_scheme(self) -> str or None """
        return ""

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def has_parent(self, parent=None): # real signature unknown; restored from __doc__
        """ has_parent(self, parent:Gio.File=None) -> bool """
        return False

    def has_prefix(self, prefix): # real signature unknown; restored from __doc__
        """ has_prefix(self, prefix:Gio.File) -> bool """
        return False

    def has_uri_scheme(self, uri_scheme): # real signature unknown; restored from __doc__
        """ has_uri_scheme(self, uri_scheme:str) -> bool """
        return False

    def is_native(self): # real signature unknown; restored from __doc__
        """ is_native(self) -> bool """
        return False

    def load_bytes(self, cancellable=None): # real signature unknown; restored from __doc__
        """ load_bytes(self, cancellable:Gio.Cancellable=None) -> GLib.Bytes, etag_out:str """
        pass

    def load_bytes_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ load_bytes_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def load_bytes_finish(self, result): # real signature unknown; restored from __doc__
        """ load_bytes_finish(self, result:Gio.AsyncResult) -> GLib.Bytes, etag_out:str """
        pass

    def load_contents(self, cancellable=None): # real signature unknown; restored from __doc__
        """ load_contents(self, cancellable:Gio.Cancellable=None) -> bool, contents:list, etag_out:str """
        return False

    def load_contents_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ load_contents_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def load_contents_finish(self, res): # real signature unknown; restored from __doc__
        """ load_contents_finish(self, res:Gio.AsyncResult) -> bool, contents:list, etag_out:str """
        return False

    def load_partial_contents_finish(self, res): # real signature unknown; restored from __doc__
        """ load_partial_contents_finish(self, res:Gio.AsyncResult) -> bool, contents:list, etag_out:str """
        return False

    def make_directory(self, cancellable=None): # real signature unknown; restored from __doc__
        """ make_directory(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def make_directory_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ make_directory_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def make_directory_finish(self, result): # real signature unknown; restored from __doc__
        """ make_directory_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def make_directory_with_parents(self, cancellable=None): # real signature unknown; restored from __doc__
        """ make_directory_with_parents(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def make_symbolic_link(self, symlink_value, cancellable=None): # real signature unknown; restored from __doc__
        """ make_symbolic_link(self, symlink_value:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def make_symbolic_link_async(self, symlink_value, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ make_symbolic_link_async(self, symlink_value:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def make_symbolic_link_finish(self, result): # real signature unknown; restored from __doc__
        """ make_symbolic_link_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def measure_disk_usage(self, flags, cancellable=None, progress_callback=None, progress_data=None): # real signature unknown; restored from __doc__
        """ measure_disk_usage(self, flags:Gio.FileMeasureFlags, cancellable:Gio.Cancellable=None, progress_callback:Gio.FileMeasureProgressCallback=None, progress_data=None) -> bool, disk_usage:int, num_dirs:int, num_files:int """
        return False

    def measure_disk_usage_finish(self, result): # real signature unknown; restored from __doc__
        """ measure_disk_usage_finish(self, result:Gio.AsyncResult) -> bool, disk_usage:int, num_dirs:int, num_files:int """
        return False

    def monitor(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ monitor(self, flags:Gio.FileMonitorFlags, cancellable:Gio.Cancellable=None) -> Gio.FileMonitor """
        pass

    def monitor_directory(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ monitor_directory(self, flags:Gio.FileMonitorFlags, cancellable:Gio.Cancellable=None) -> Gio.FileMonitor """
        pass

    def monitor_file(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ monitor_file(self, flags:Gio.FileMonitorFlags, cancellable:Gio.Cancellable=None) -> Gio.FileMonitor """
        pass

    def mount_enclosing_volume(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ mount_enclosing_volume(self, flags:Gio.MountMountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def mount_enclosing_volume_finish(self, result): # real signature unknown; restored from __doc__
        """ mount_enclosing_volume_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def mount_mountable(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ mount_mountable(self, flags:Gio.MountMountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def mount_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ mount_mountable_finish(self, result:Gio.AsyncResult) -> Gio.File """
        pass

    def move(self, destination, flags, cancellable=None, progress_callback=None, progress_callback_data=None): # real signature unknown; restored from __doc__
        """ move(self, destination:Gio.File, flags:Gio.FileCopyFlags, cancellable:Gio.Cancellable=None, progress_callback:Gio.FileProgressCallback=None, progress_callback_data=None) -> bool """
        return False

    def move_async(self, destination, flags, io_priority, cancellable=None, progress_callback_closure=None, ready_callback_closure): # real signature unknown; restored from __doc__
        """ move_async(self, destination:Gio.File, flags:Gio.FileCopyFlags, io_priority:int, cancellable:Gio.Cancellable=None, progress_callback_closure:GObject.Closure=None, ready_callback_closure:GObject.Closure) """
        pass

    def move_finish(self, result): # real signature unknown; restored from __doc__
        """ move_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def new_build_filenamev(self, args): # real signature unknown; restored from __doc__
        """ new_build_filenamev(args:list) -> Gio.File """
        pass

    def new_for_commandline_arg(self, arg): # real signature unknown; restored from __doc__
        """ new_for_commandline_arg(arg:str) -> Gio.File """
        pass

    def new_for_commandline_arg_and_cwd(self, arg, cwd): # real signature unknown; restored from __doc__
        """ new_for_commandline_arg_and_cwd(arg:str, cwd:str) -> Gio.File """
        pass

    def new_for_path(self, path): # real signature unknown; restored from __doc__
        """ new_for_path(path:str) -> Gio.File """
        pass

    def new_for_uri(self, uri): # real signature unknown; restored from __doc__
        """ new_for_uri(uri:str) -> Gio.File """
        pass

    def new_tmp(self, tmpl=None): # real signature unknown; restored from __doc__
        """ new_tmp(tmpl:str=None) -> Gio.File, iostream:Gio.FileIOStream """
        pass

    def new_tmp_async(self, tmpl=None, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ new_tmp_async(tmpl:str=None, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def new_tmp_dir_async(self, tmpl=None, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ new_tmp_dir_async(tmpl:str=None, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def new_tmp_dir_finish(self, result): # real signature unknown; restored from __doc__
        """ new_tmp_dir_finish(result:Gio.AsyncResult) -> Gio.File """
        pass

    def new_tmp_finish(self, result): # real signature unknown; restored from __doc__
        """ new_tmp_finish(result:Gio.AsyncResult) -> Gio.File, iostream:Gio.FileIOStream """
        pass

    def open_readwrite(self, cancellable=None): # real signature unknown; restored from __doc__
        """ open_readwrite(self, cancellable:Gio.Cancellable=None) -> Gio.FileIOStream """
        pass

    def open_readwrite_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ open_readwrite_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def open_readwrite_finish(self, res): # real signature unknown; restored from __doc__
        """ open_readwrite_finish(self, res:Gio.AsyncResult) -> Gio.FileIOStream """
        pass

    def parse_name(self, parse_name): # real signature unknown; restored from __doc__
        """ parse_name(parse_name:str) -> Gio.File """
        pass

    def peek_path(self): # real signature unknown; restored from __doc__
        """ peek_path(self) -> str or None """
        return ""

    def poll_mountable(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ poll_mountable(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def poll_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ poll_mountable_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def query_default_handler(self, cancellable=None): # real signature unknown; restored from __doc__
        """ query_default_handler(self, cancellable:Gio.Cancellable=None) -> Gio.AppInfo """
        pass

    def query_default_handler_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ query_default_handler_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def query_default_handler_finish(self, result): # real signature unknown; restored from __doc__
        """ query_default_handler_finish(self, result:Gio.AsyncResult) -> Gio.AppInfo """
        pass

    def query_exists(self, cancellable=None): # real signature unknown; restored from __doc__
        """ query_exists(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def query_filesystem_info(self, attributes, cancellable=None): # real signature unknown; restored from __doc__
        """ query_filesystem_info(self, attributes:str, cancellable:Gio.Cancellable=None) -> Gio.FileInfo """
        pass

    def query_filesystem_info_async(self, attributes, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ query_filesystem_info_async(self, attributes:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def query_filesystem_info_finish(self, res): # real signature unknown; restored from __doc__
        """ query_filesystem_info_finish(self, res:Gio.AsyncResult) -> Gio.FileInfo """
        pass

    def query_file_type(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ query_file_type(self, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> Gio.FileType """
        pass

    def query_info(self, attributes, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ query_info(self, attributes:str, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> Gio.FileInfo """
        pass

    def query_info_async(self, attributes, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ query_info_async(self, attributes:str, flags:Gio.FileQueryInfoFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def query_info_finish(self, res): # real signature unknown; restored from __doc__
        """ query_info_finish(self, res:Gio.AsyncResult) -> Gio.FileInfo """
        pass

    def query_settable_attributes(self, cancellable=None): # real signature unknown; restored from __doc__
        """ query_settable_attributes(self, cancellable:Gio.Cancellable=None) -> Gio.FileAttributeInfoList """
        pass

    def query_writable_namespaces(self, cancellable=None): # real signature unknown; restored from __doc__
        """ query_writable_namespaces(self, cancellable:Gio.Cancellable=None) -> Gio.FileAttributeInfoList """
        pass

    def read(self, cancellable=None): # real signature unknown; restored from __doc__
        """ read(self, cancellable:Gio.Cancellable=None) -> Gio.FileInputStream """
        pass

    def read_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ read_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def read_finish(self, res): # real signature unknown; restored from __doc__
        """ read_finish(self, res:Gio.AsyncResult) -> Gio.FileInputStream """
        pass

    def replace(self, etag=None, make_backup, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ replace(self, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> Gio.FileOutputStream """
        pass

    def replace_async(self, etag=None, make_backup, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ replace_async(self, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def replace_contents(self, contents, etag=None, make_backup, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ replace_contents(self, contents:list, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> bool, new_etag:str """
        return False

    def replace_contents_async(self, contents, etag=None, make_backup, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ replace_contents_async(self, contents:list, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def replace_contents_bytes_async(self, contents, etag=None, make_backup, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ replace_contents_bytes_async(self, contents:GLib.Bytes, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def replace_contents_finish(self, res): # real signature unknown; restored from __doc__
        """ replace_contents_finish(self, res:Gio.AsyncResult) -> bool, new_etag:str """
        return False

    def replace_finish(self, res): # real signature unknown; restored from __doc__
        """ replace_finish(self, res:Gio.AsyncResult) -> Gio.FileOutputStream """
        pass

    def replace_readwrite(self, etag=None, make_backup, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ replace_readwrite(self, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> Gio.FileIOStream """
        pass

    def replace_readwrite_async(self, etag=None, make_backup, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ replace_readwrite_async(self, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def replace_readwrite_finish(self, res): # real signature unknown; restored from __doc__
        """ replace_readwrite_finish(self, res:Gio.AsyncResult) -> Gio.FileIOStream """
        pass

    def resolve_relative_path(self, relative_path): # real signature unknown; restored from __doc__
        """ resolve_relative_path(self, relative_path:str) -> Gio.File """
        pass

    def set_attribute(self, attribute, type, value_p=None, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute(self, attribute:str, type:Gio.FileAttributeType, value_p=None, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attributes_async(self, info, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_attributes_async(self, info:Gio.FileInfo, flags:Gio.FileQueryInfoFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_attributes_finish(self, result): # real signature unknown; restored from __doc__
        """ set_attributes_finish(self, result:Gio.AsyncResult) -> bool, info:Gio.FileInfo """
        return False

    def set_attributes_from_info(self, info, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attributes_from_info(self, info:Gio.FileInfo, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_byte_string(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_byte_string(self, attribute:str, value:str, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_int32(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_int32(self, attribute:str, value:int, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_int64(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_int64(self, attribute:str, value:int, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_string(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_string(self, attribute:str, value:str, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_uint32(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_uint32(self, attribute:str, value:int, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_uint64(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_uint64(self, attribute:str, value:int, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_display_name(self, display_name, cancellable=None): # real signature unknown; restored from __doc__
        """ set_display_name(self, display_name:str, cancellable:Gio.Cancellable=None) -> Gio.File """
        pass

    def set_display_name_async(self, display_name, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_display_name_async(self, display_name:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_display_name_finish(self, res): # real signature unknown; restored from __doc__
        """ set_display_name_finish(self, res:Gio.AsyncResult) -> Gio.File """
        pass

    def start_mountable(self, flags, start_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ start_mountable(self, flags:Gio.DriveStartFlags, start_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def start_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ start_mountable_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def stop_mountable(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ stop_mountable(self, flags:Gio.MountUnmountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def stop_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ stop_mountable_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def supports_thread_contexts(self): # real signature unknown; restored from __doc__
        """ supports_thread_contexts(self) -> bool """
        return False

    def trash(self, cancellable=None): # real signature unknown; restored from __doc__
        """ trash(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def trash_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ trash_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def trash_finish(self, result): # real signature unknown; restored from __doc__
        """ trash_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def unmount_mountable(self, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ unmount_mountable(self, flags:Gio.MountUnmountFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def unmount_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ unmount_mountable_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def unmount_mountable_with_operation(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ unmount_mountable_with_operation(self, flags:Gio.MountUnmountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def unmount_mountable_with_operation_finish(self, result): # real signature unknown; restored from __doc__
        """ unmount_mountable_with_operation_finish(self, result:Gio.AsyncResult) -> bool """
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

    def __fspath__(self): # reliably restored by inspect
        # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gio', '__fspath__': <function File.__fspath__ at 0x000001ea703096c0>, '__doc__': None, '__gsignals__': {}})"
    __gdoc__ = 'Interface GFile\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GFile (1838041872)>'
    __info__ = InterfaceInfo(File)


