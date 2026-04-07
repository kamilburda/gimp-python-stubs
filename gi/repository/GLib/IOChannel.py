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


from .IOChannel import IOChannel

class IOChannel(IOChannel):
    """
    :Constructors:
    
    ::
    
        IOChannel()
        new_file(filename:str, mode:str) -> GLib.IOChannel
        unix_new(fd:int) -> GLib.IOChannel
        win32_new_fd(fd:int) -> GLib.IOChannel
        win32_new_messages(hwnd:int) -> GLib.IOChannel
        win32_new_socket(socket:int) -> GLib.IOChannel
        win32_new_stream_socket(socket:int) -> GLib.IOChannel
    """
    def add_watch(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def error_from_errno(self, en): # real signature unknown; restored from __doc__
        """ error_from_errno(en:int) -> GLib.IOChannelError """
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> GLib.IOStatus """
        pass

    def get_buffered(self): # real signature unknown; restored from __doc__
        """ get_buffered(self) -> bool """
        return False

    def get_buffer_condition(self): # real signature unknown; restored from __doc__
        """ get_buffer_condition(self) -> GLib.IOCondition """
        pass

    def get_buffer_size(self): # real signature unknown; restored from __doc__
        """ get_buffer_size(self) -> int """
        return 0

    def get_close_on_unref(self): # real signature unknown; restored from __doc__
        """ get_close_on_unref(self) -> bool """
        return False

    def get_encoding(self): # real signature unknown; restored from __doc__
        """ get_encoding(self) -> str """
        return ""

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> GLib.IOFlags """
        pass

    def get_line_term(self): # real signature unknown; restored from __doc__
        """ get_line_term(self) -> str, length:int """
        return ""

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) """
        pass

    def new_file(self, filename, mode): # real signature unknown; restored from __doc__
        """ new_file(filename:str, mode:str) -> GLib.IOChannel """
        pass

    def read(self, max_count=-1): # reliably restored by inspect
        """ Reads data from a :obj:`~gi.repository.GLib.IOChannel`. """
        pass

    def readline(self, size_hint=-1): # reliably restored by inspect
        # no doc
        pass

    def readlines(self, size_hint=-1): # reliably restored by inspect
        # no doc
        pass

    def read_chars(self, max_count=-1): # reliably restored by inspect
        """ Alias for GLib.IOChannel.read(). """
        pass

    def read_line(self): # real signature unknown; restored from __doc__
        """ read_line(self) -> GLib.IOStatus, str_return:str, length:int, terminator_pos:int """
        pass

    def read_line_string(self, buffer, terminator_pos=None): # real signature unknown; restored from __doc__
        """ read_line_string(self, buffer:GLib.String, terminator_pos:int=None) -> GLib.IOStatus """
        pass

    def read_to_end(self): # real signature unknown; restored from __doc__
        """ read_to_end(self) -> GLib.IOStatus, str_return:list """
        pass

    def read_unichar(self): # real signature unknown; restored from __doc__
        """ read_unichar(self) -> GLib.IOStatus, thechar:str """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.IOChannel """
        pass

    def seek(self, offset, whence=0): # reliably restored by inspect
        # no doc
        pass

    def seek_position(self, offset, type): # real signature unknown; restored from __doc__
        """ seek_position(self, offset:int, type:GLib.SeekType) -> GLib.IOStatus """
        pass

    def set_buffered(self, buffered): # real signature unknown; restored from __doc__
        """ set_buffered(self, buffered:bool) """
        pass

    def set_buffer_size(self, size): # real signature unknown; restored from __doc__
        """ set_buffer_size(self, size:int) """
        pass

    def set_close_on_unref(self, do_close): # real signature unknown; restored from __doc__
        """ set_close_on_unref(self, do_close:bool) """
        pass

    def set_encoding(self, encoding=None): # real signature unknown; restored from __doc__
        """ set_encoding(self, encoding:str=None) -> GLib.IOStatus """
        pass

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:GLib.IOFlags) -> GLib.IOStatus """
        pass

    def set_line_term(self, line_term=None, length): # real signature unknown; restored from __doc__
        """ set_line_term(self, line_term:str=None, length:int) """
        pass

    def shutdown(self, flush): # real signature unknown; restored from __doc__
        """ shutdown(self, flush:bool) -> GLib.IOStatus """
        pass

    def unix_get_fd(self): # real signature unknown; restored from __doc__
        """ unix_get_fd(self) -> int """
        return 0

    def unix_new(self, fd): # real signature unknown; restored from __doc__
        """ unix_new(fd:int) -> GLib.IOChannel """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def win32_get_fd(self): # real signature unknown; restored from __doc__
        """ win32_get_fd(self) -> int """
        return 0

    def win32_make_pollfd(self, condition, fd): # real signature unknown; restored from __doc__
        """ win32_make_pollfd(self, condition:GLib.IOCondition, fd:GLib.PollFD) """
        pass

    def win32_new_fd(self, fd): # real signature unknown; restored from __doc__
        """ win32_new_fd(fd:int) -> GLib.IOChannel """
        pass

    def win32_new_messages(self, hwnd): # real signature unknown; restored from __doc__
        """ win32_new_messages(hwnd:int) -> GLib.IOChannel """
        pass

    def win32_new_socket(self, socket): # real signature unknown; restored from __doc__
        """ win32_new_socket(socket:int) -> GLib.IOChannel """
        pass

    def win32_new_stream_socket(self, socket): # real signature unknown; restored from __doc__
        """ win32_new_stream_socket(socket:int) -> GLib.IOChannel """
        pass

    def win32_poll(self, fds, n_fds, timeout_): # real signature unknown; restored from __doc__
        """ win32_poll(fds:GLib.PollFD, n_fds:int, timeout_:int) -> int """
        return 0

    def win32_set_debug(self, flag): # real signature unknown; restored from __doc__
        """ win32_set_debug(self, flag:bool) """
        pass

    def write(self, buf, buflen=-1): # reliably restored by inspect
        # no doc
        pass

    def writelines(self, lines): # reliably restored by inspect
        # no doc
        pass

    def write_chars(self, buf, count): # real signature unknown; restored from __doc__
        """ write_chars(self, buf:list, count:int) -> GLib.IOStatus, bytes_written:int """
        pass

    def write_unichar(self, thechar): # real signature unknown; restored from __doc__
        """ write_unichar(self, thechar:str) -> GLib.IOStatus """
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

    def __init__(self, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(cls, filedes=None, filename=None, mode=None, hwnd=None): # reliably restored by inspect
        # no doc
        pass

    def __next__(self): # reliably restored by inspect
        # no doc
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

    buf_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    close_on_unref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    do_encode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encoded_read_buf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    funcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_readable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_seekable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_writeable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    line_term = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    line_term_len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    partial_write_buf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_buf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_cd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write_buf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write_cd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _whence_map = {
        0: 1,
        1: 0,
        2: 2,
    }
    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.GLib', '__firstlineno__': 834, '__new__': <staticmethod(<function IOChannel.__new__ at 0x0000018e9feeaa30>)>, '__init__': <function IOChannel.__init__ at 0x0000018e9feeaae0>, 'read': <function IOChannel.read at 0x0000018e9feeac40>, 'read_chars': <function IOChannel.read_chars at 0x0000018e9feeada0>, 'readline': <function IOChannel.readline at 0x0000018e9feeaf00>, 'readlines': <function IOChannel.readlines at 0x0000018e9feeb060>, 'write': <function IOChannel.write at 0x0000018e9feeb1c0>, 'writelines': <function IOChannel.writelines at 0x0000018e9feeb320>, '_whence_map': {0: <SeekType.SET: 1>, 1: <SeekType.CUR: 0>, 2: <SeekType.END: 2>}, 'seek': <function IOChannel.seek at 0x0000018e9feeb480>, 'add_watch': <function IOChannel.add_watch at 0x0000018e9feeb690>, '__iter__': <function IOChannel.__iter__ at 0x0000018e9feeb740>, '__next__': <function IOChannel.__next__ at 0x0000018e9feeb8a0>, '__static_attributes__': (), '__doc__': None})"
    __firstlineno__ = 834
    __gtype__ = None # (!) real value is '<GType GIOChannel (2640112096)>'
    __info__ = StructInfo(IOChannel)
    __static_attributes__ = ()


