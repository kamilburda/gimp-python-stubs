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


class FileIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        FileIface()
    """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    append_to = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    append_to_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    append_to_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_readwrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_readwrite_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_readwrite_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_file_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_file_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_mountable_with_operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_mountable_with_operation_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enumerate_children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enumerate_children_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enumerate_children_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    equal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    find_enclosing_mount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    find_enclosing_mount_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    find_enclosing_mount_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_basename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_child_for_display_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_parse_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_relative_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uri_scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_uri_scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_native = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_directory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_directory_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_directory_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_symbolic_link = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_symbolic_link_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_symbolic_link_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    measure_disk_usage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    measure_disk_usage_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    measure_disk_usage_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    monitor_dir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    monitor_file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_enclosing_volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_enclosing_volume_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    move = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    move_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    move_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_readwrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_readwrite_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_readwrite_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    poll_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    poll_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prefix_matches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_exists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_filesystem_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_filesystem_info_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_filesystem_info_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_info_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_info_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_settable_attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_writable_namespaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_fn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_readwrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_readwrite_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_readwrite_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resolve_relative_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_attribute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_attributes_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_attributes_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_attributes_from_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_display_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_display_name_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_display_name_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stop_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stop_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_thread_contexts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trash_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trash_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmount_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmount_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmount_mountable_with_operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmount_mountable_with_operation_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _query_settable_attributes_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _query_settable_attributes_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _query_writable_namespaces_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _query_writable_namespaces_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(FileIface), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'FileIface' objects>, '__weakref__': <attribute '__weakref__' of 'FileIface' objects>, '__doc__': None, 'g_iface': <property object at 0x000001ea7094f7e0>, 'dup': <property object at 0x000001ea7094f8d0>, 'hash': <property object at 0x000001ea7094f9c0>, 'equal': <property object at 0x000001ea7094fab0>, 'is_native': <property object at 0x000001ea7094fba0>, 'has_uri_scheme': <property object at 0x000001ea7094fc90>, 'get_uri_scheme': <property object at 0x000001ea7094fd80>, 'get_basename': <property object at 0x000001ea7094fe70>, 'get_path': <property object at 0x000001ea7094ff60>, 'get_uri': <property object at 0x000001ea70940090>, 'get_parse_name': <property object at 0x000001ea70940180>, 'get_parent': <property object at 0x000001ea70940270>, 'prefix_matches': <property object at 0x000001ea70940360>, 'get_relative_path': <property object at 0x000001ea70940450>, 'resolve_relative_path': <property object at 0x000001ea70940540>, 'get_child_for_display_name': <property object at 0x000001ea70940680>, 'enumerate_children': <property object at 0x000001ea70940720>, 'enumerate_children_async': <property object at 0x000001ea70940860>, 'enumerate_children_finish': <property object at 0x000001ea70940950>, 'query_info': <property object at 0x000001ea709409f0>, 'query_info_async': <property object at 0x000001ea70940ae0>, 'query_info_finish': <property object at 0x000001ea70940bd0>, 'query_filesystem_info': <property object at 0x000001ea70940cc0>, 'query_filesystem_info_async': <property object at 0x000001ea70940e00>, 'query_filesystem_info_finish': <property object at 0x000001ea70940ef0>, 'find_enclosing_mount': <property object at 0x000001ea70940f90>, 'find_enclosing_mount_async': <property object at 0x000001ea709410d0>, 'find_enclosing_mount_finish': <property object at 0x000001ea709411c0>, 'set_display_name': <property object at 0x000001ea70941260>, 'set_display_name_async': <property object at 0x000001ea70941350>, 'set_display_name_finish': <property object at 0x000001ea70941440>, 'query_settable_attributes': <property object at 0x000001ea70941580>, '_query_settable_attributes_async': <property object at 0x000001ea70941670>, '_query_settable_attributes_finish': <property object at 0x000001ea709417b0>, 'query_writable_namespaces': <property object at 0x000001ea709418f0>, '_query_writable_namespaces_async': <property object at 0x000001ea709419e0>, '_query_writable_namespaces_finish': <property object at 0x000001ea70941b20>, 'set_attribute': <property object at 0x000001ea70941c10>, 'set_attributes_from_info': <property object at 0x000001ea70941d50>, 'set_attributes_async': <property object at 0x000001ea70941df0>, 'set_attributes_finish': <property object at 0x000001ea70941ee0>, 'read_fn': <property object at 0x000001ea70941fd0>, 'read_async': <property object at 0x000001ea709420c0>, 'read_finish': <property object at 0x000001ea709421b0>, 'append_to': <property object at 0x000001ea709422a0>, 'append_to_async': <property object at 0x000001ea70942390>, 'append_to_finish': <property object at 0x000001ea70942480>, 'create': <property object at 0x000001ea70942570>, 'create_async': <property object at 0x000001ea70942660>, 'create_finish': <property object at 0x000001ea70942750>, 'replace': <property object at 0x000001ea70942840>, 'replace_async': <property object at 0x000001ea70942930>, 'replace_finish': <property object at 0x000001ea70942a20>, 'delete_file': <property object at 0x000001ea70942b10>, 'delete_file_async': <property object at 0x000001ea70942c00>, 'delete_file_finish': <property object at 0x000001ea70942cf0>, 'trash': <property object at 0x000001ea70942de0>, 'trash_async': <property object at 0x000001ea70942ed0>, 'trash_finish': <property object at 0x000001ea70942fc0>, 'make_directory': <property object at 0x000001ea709430b0>, 'make_directory_async': <property object at 0x000001ea709431a0>, 'make_directory_finish': <property object at 0x000001ea70943290>, 'make_symbolic_link': <property object at 0x000001ea70943380>, 'make_symbolic_link_async': <property object at 0x000001ea709434c0>, 'make_symbolic_link_finish': <property object at 0x000001ea709435b0>, 'copy': <property object at 0x000001ea70943650>, 'copy_async': <property object at 0x000001ea70943740>, 'copy_finish': <property object at 0x000001ea70943830>, 'move': <property object at 0x000001ea70943920>, 'move_async': <property object at 0x000001ea70943a10>, 'move_finish': <property object at 0x000001ea70943b00>, 'mount_mountable': <property object at 0x000001ea70943bf0>, 'mount_mountable_finish': <property object at 0x000001ea70943ce0>, 'unmount_mountable': <property object at 0x000001ea70943dd0>, 'unmount_mountable_finish': <property object at 0x000001ea70943f10>, 'eject_mountable': <property object at 0x000001ea70943fb0>, 'eject_mountable_finish': <property object at 0x000001ea7093c0e0>, 'mount_enclosing_volume': <property object at 0x000001ea7093c1d0>, 'mount_enclosing_volume_finish': <property object at 0x000001ea7093c310>, 'monitor_dir': <property object at 0x000001ea7093c3b0>, 'monitor_file': <property object at 0x000001ea7093c4a0>, 'open_readwrite': <property object at 0x000001ea7093c590>, 'open_readwrite_async': <property object at 0x000001ea7093c680>, 'open_readwrite_finish': <property object at 0x000001ea7093c770>, 'create_readwrite': <property object at 0x000001ea7093c860>, 'create_readwrite_async': <property object at 0x000001ea7093c950>, 'create_readwrite_finish': <property object at 0x000001ea7093ca40>, 'replace_readwrite': <property object at 0x000001ea7093cb30>, 'replace_readwrite_async': <property object at 0x000001ea7093cc20>, 'replace_readwrite_finish': <property object at 0x000001ea7093cd60>, 'start_mountable': <property object at 0x000001ea7093ce00>, 'start_mountable_finish': <property object at 0x000001ea7093cef0>, 'stop_mountable': <property object at 0x000001ea7093cfe0>, 'stop_mountable_finish': <property object at 0x000001ea7093d0d0>, 'supports_thread_contexts': <property object at 0x000001ea7093d210>, 'unmount_mountable_with_operation': <property object at 0x000001ea7093d300>, 'unmount_mountable_with_operation_finish': <property object at 0x000001ea7093d3f0>, 'eject_mountable_with_operation': <property object at 0x000001ea7093d4e0>, 'eject_mountable_with_operation_finish': <property object at 0x000001ea7093d5d0>, 'poll_mountable': <property object at 0x000001ea7093d670>, 'poll_mountable_finish': <property object at 0x000001ea7093d760>, 'measure_disk_usage': <property object at 0x000001ea7093d850>, 'measure_disk_usage_async': <property object at 0x000001ea7093d990>, 'measure_disk_usage_finish': <property object at 0x000001ea7093dad0>, 'query_exists': <property object at 0x000001ea7093db70>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(FileIface)


