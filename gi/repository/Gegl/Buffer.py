# encoding: utf-8
# module gi.repository.Gegl
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


from .TileHandler import TileHandler

class Buffer(TileHandler):
    """
    :Constructors:
    
    ::
    
        Buffer(**properties)
        new(format_name:str, x:int, y:int, width:int, height:int) -> Gegl.Buffer
        new_for_backend(extent:Gegl.Rectangle, backend:Gegl.TileBackend) -> Gegl.Buffer
    """
    def add_handler(self, handler=None): # real signature unknown; restored from __doc__
        """ add_handler(self, handler=None) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, roi): # real signature unknown; restored from __doc__
        """ clear(self, roi:Gegl.Rectangle) """
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, connect_flags=0): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def copy(self, src_rect, repeat_mode, dst, dst_rect): # real signature unknown; restored from __doc__
        """ copy(self, src_rect:Gegl.Rectangle, repeat_mode:Gegl.AbyssPolicy, dst:Gegl.Buffer, dst_rect:Gegl.Rectangle) """
        pass

    def create_sub_buffer(self, extent): # real signature unknown; restored from __doc__
        """ create_sub_buffer(self, extent:Gegl.Rectangle) -> Gegl.Buffer """
        pass

    def damage_rect(self, rect): # real signature unknown; restored from __doc__
        """ damage_rect(self, rect:Gegl.Rectangle) """
        pass

    def damage_tile(self, x, y, z, damage): # real signature unknown; restored from __doc__
        """ damage_tile(self, x:int, y:int, z:int, damage:int) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> Gegl.Buffer """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) """
        pass

    def flush_ext(self, rect): # real signature unknown; restored from __doc__
        """ flush_ext(self, rect:Gegl.Rectangle) """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_changed(self): # real signature unknown; restored from __doc__
        """ freeze_changed(self) """
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def get(self, rect, scale, format_name=None, repeat_mode): # real signature unknown; restored from __doc__
        """ get(self, rect:Gegl.Rectangle, scale:float, format_name:str=None, repeat_mode:Gegl.AbyssPolicy) -> list """
        return []

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_abyss(self): # real signature unknown; restored from __doc__
        """ get_abyss(self) -> Gegl.Rectangle """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_extent(self): # real signature unknown; restored from __doc__
        """ get_extent(self) -> Gegl.Rectangle """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def handler_block(obj, handler_id): # reliably restored by inspect
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

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def linear_close(self, linear=None): # real signature unknown; restored from __doc__
        """ linear_close(self, linear=None) """
        pass

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def load(self, path): # real signature unknown; restored from __doc__
        """ load(path:str) -> Gegl.Buffer """
        pass

    def lock(self): # real signature unknown; restored from __doc__
        """ lock(self) """
        pass

    @classmethod
    def new(cls, format_name, x, y, width, height): # real signature unknown; restored from __doc__
        """ new(format_name:str, x:int, y:int, width:int, height:int) -> Gegl.Buffer """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    @classmethod
    def new_for_backend(cls, extent, backend): # real signature unknown; restored from __doc__
        """ new_for_backend(extent:Gegl.Rectangle, backend:Gegl.TileBackend) -> Gegl.Buffer """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def open(self, path): # real signature unknown; restored from __doc__
        """ open(path:str) -> Gegl.Buffer """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_handler(self, handler=None): # real signature unknown; restored from __doc__
        """ remove_handler(self, handler=None) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def sample_cleanup(self): # real signature unknown; restored from __doc__
        """ sample_cleanup(self) """
        pass

    def save(self, path, roi): # real signature unknown; restored from __doc__
        """ save(self, path:str, roi:Gegl.Rectangle) """
        pass

    def set(self, rect, format_name, src): # real signature unknown; restored from __doc__
        """ set(self, rect:Gegl.Rectangle, format_name:str, src:list) """
        pass

    def set_abyss(self, abyss): # real signature unknown; restored from __doc__
        """ set_abyss(self, abyss:Gegl.Rectangle) -> bool """
        return False

    def set_color(self, rect, color): # real signature unknown; restored from __doc__
        """ set_color(self, rect:Gegl.Rectangle, color:Gegl.Color) """
        pass

    def set_color_from_pixel(self, rect, pixel=None, pixel_format): # real signature unknown; restored from __doc__
        """ set_color_from_pixel(self, rect:Gegl.Rectangle, pixel=None, pixel_format:Babl.Object) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_extent(self, extent): # real signature unknown; restored from __doc__
        """ set_extent(self, extent:Gegl.Rectangle) -> bool """
        return False

    def set_pattern(self, rect, pattern, x_offset, y_offset): # real signature unknown; restored from __doc__
        """ set_pattern(self, rect:Gegl.Rectangle, pattern:Gegl.Buffer, x_offset:int, y_offset:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_source(self, source): # real signature unknown; restored from __doc__
        """ set_source(self, source:Gegl.TileSource) """
        pass

    def share_storage(self, buffer2): # real signature unknown; restored from __doc__
        """ share_storage(self, buffer2:Gegl.Buffer) -> bool """
        return False

    def signal_connect(self, detailed_signal, c_handler, data=None): # real signature unknown; restored from __doc__
        """ signal_connect(self, detailed_signal:str, c_handler:GObject.Callback, data=None) -> int """
        return 0

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def swap_create_file(self, suffix=None): # real signature unknown; restored from __doc__
        """ swap_create_file(suffix:str=None) -> str or None """
        return ""

    def swap_has_file(self, path): # real signature unknown; restored from __doc__
        """ swap_has_file(path:str) -> bool """
        return False

    def swap_remove_file(self, path): # real signature unknown; restored from __doc__
        """ swap_remove_file(path:str) """
        pass

    def thaw_changed(self): # real signature unknown; restored from __doc__
        """ thaw_changed(self) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unlock(self): # real signature unknown; restored from __doc__
        """ unlock(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self): # reliably restored by inspect
        """ Deprecated, do not explicitly float GObjects. """
        pass

    def _ref(self): # reliably restored by inspect
        """ Deprecated, do not explicitly reference GObjects. """
        pass

    def _ref_sink(self): # reliably restored by inspect
        """ Deprecated, do not explicitly reference GObjects. """
        pass

    def _unref(self): # reliably restored by inspect
        """ Deprecated, do not explicitly reference GObjects. """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001ebdc0e4a90>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Buffer), '__module__': 'gi.repository.Gegl', '__gtype__': <GType GeglBuffer (3645254704)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'new_for_backend': <classmethod(gi.FunctionInfo(new_for_backend))>, 'load': <staticmethod(gi.FunctionInfo(load))>, 'open': <staticmethod(gi.FunctionInfo(open))>, 'swap_create_file': <staticmethod(gi.FunctionInfo(swap_create_file))>, 'swap_has_file': <staticmethod(gi.FunctionInfo(swap_has_file))>, 'swap_remove_file': <staticmethod(gi.FunctionInfo(swap_remove_file))>, 'add_handler': gi.FunctionInfo(add_handler), 'clear': gi.FunctionInfo(clear), 'copy': gi.FunctionInfo(copy), 'create_sub_buffer': gi.FunctionInfo(create_sub_buffer), 'dup': gi.FunctionInfo(dup), 'flush': gi.FunctionInfo(flush), 'flush_ext': gi.FunctionInfo(flush_ext), 'freeze_changed': gi.FunctionInfo(freeze_changed), 'get_abyss': gi.FunctionInfo(get_abyss), 'get_extent': gi.FunctionInfo(get_extent), 'get': gi.FunctionInfo(get), 'set': gi.FunctionInfo(set), 'linear_close': gi.FunctionInfo(linear_close), 'remove_handler': gi.FunctionInfo(remove_handler), 'sample_cleanup': gi.FunctionInfo(sample_cleanup), 'save': gi.FunctionInfo(save), 'set_abyss': gi.FunctionInfo(set_abyss), 'set_color': gi.FunctionInfo(set_color), 'set_color_from_pixel': gi.FunctionInfo(set_color_from_pixel), 'set_extent': gi.FunctionInfo(set_extent), 'set_pattern': gi.FunctionInfo(set_pattern), 'share_storage': gi.FunctionInfo(share_storage), 'signal_connect': gi.FunctionInfo(signal_connect), 'thaw_changed': gi.FunctionInfo(thaw_changed)})"
    __gdoc__ = "Object GeglBuffer\n\nSignals from GeglBuffer:\n  changed (GeglRectangle)\n\nProperties from GeglBuffer:\n  x -> gint: x\n    local origin's offset relative to source origin\n  y -> gint: y\n    local origin's offset relative to source origin\n  width -> gint: width\n    pixel width of buffer\n  height -> gint: height\n    pixel height of buffer\n  shift-x -> gint: shift-x\n    \n  shift-y -> gint: shift-y\n    \n  abyss-x -> gint: abyss-x\n    \n  abyss-y -> gint: abyss-y\n    \n  abyss-width -> gint: abyss-width\n    pixel width of abyss\n  abyss-height -> gint: abyss-height\n    pixel height of abyss\n  tile-width -> gint: tile-width\n    width of a tile\n  tile-height -> gint: tile-height\n    height of a tile\n  format -> gpointer: format\n    babl format\n  px-size -> gint: pixel-size\n    size of a single pixel in bytes.\n  pixels -> gint: pixels\n    total amount of pixels in image (width x height)\n  path -> gchararray: Path\n    URI to where the buffer is stored\n  backend -> GeglTileBackend: backend\n    A custom tile-backend instance to use\n  initialized -> gboolean: initialized\n\nProperties from GeglTileHandler:\n  source -> GObject: GeglBuffer\n    The tilestore to be a facade for\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeglBuffer (3645254704)>'
    __info__ = ObjectInfo(Buffer)


