# encoding: utf-8
# module gi.repository.Pango
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi._gi as __gi__gi


class Renderer(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Renderer(**properties)
    """
    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
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

    def deactivate(self): # real signature unknown; restored from __doc__
        """ deactivate(self) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_begin(self, *args, **kwargs): # real signature unknown
        """ begin(self) """
        pass

    def do_constructed(self, *args, **kwargs): # real signature unknown
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def do_draw_error_underline(self, *args, **kwargs): # real signature unknown
        """ draw_error_underline(self, x:int, y:int, width:int, height:int) """
        pass

    def do_draw_glyph(self, *args, **kwargs): # real signature unknown
        """ draw_glyph(self, font:Pango.Font, glyph:int, x:float, y:float) """
        pass

    def do_draw_glyphs(self, *args, **kwargs): # real signature unknown
        """ draw_glyphs(self, font:Pango.Font, glyphs:Pango.GlyphString, x:int, y:int) """
        pass

    def do_draw_glyph_item(self, *args, **kwargs): # real signature unknown
        """ draw_glyph_item(self, text:str=None, glyph_item:Pango.GlyphItem, x:int, y:int) """
        pass

    def do_draw_rectangle(self, *args, **kwargs): # real signature unknown
        """ draw_rectangle(self, part:Pango.RenderPart, x:int, y:int, width:int, height:int) """
        pass

    def do_draw_shape(self, *args, **kwargs): # real signature unknown
        """ draw_shape(self, attr:Pango.AttrShape, x:int, y:int) """
        pass

    def do_draw_trapezoid(self, *args, **kwargs): # real signature unknown
        """ draw_trapezoid(self, part:Pango.RenderPart, y1_:float, x11:float, x21:float, y2:float, x12:float, x22:float) """
        pass

    def do_end(self, *args, **kwargs): # real signature unknown
        """ end(self) """
        pass

    def do_part_changed(self, *args, **kwargs): # real signature unknown
        """ part_changed(self, part:Pango.RenderPart) """
        pass

    def do_prepare_run(self, *args, **kwargs): # real signature unknown
        """ prepare_run(self, run:Pango.GlyphItem) """
        pass

    def draw_error_underline(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ draw_error_underline(self, x:int, y:int, width:int, height:int) """
        pass

    def draw_glyph(self, font, glyph, x, y): # real signature unknown; restored from __doc__
        """ draw_glyph(self, font:Pango.Font, glyph:int, x:float, y:float) """
        pass

    def draw_glyphs(self, font, glyphs, x, y): # real signature unknown; restored from __doc__
        """ draw_glyphs(self, font:Pango.Font, glyphs:Pango.GlyphString, x:int, y:int) """
        pass

    def draw_glyph_item(self, text=None, glyph_item, x, y): # real signature unknown; restored from __doc__
        """ draw_glyph_item(self, text:str=None, glyph_item:Pango.GlyphItem, x:int, y:int) """
        pass

    def draw_layout(self, layout, x, y): # real signature unknown; restored from __doc__
        """ draw_layout(self, layout:Pango.Layout, x:int, y:int) """
        pass

    def draw_layout_line(self, line, x, y): # real signature unknown; restored from __doc__
        """ draw_layout_line(self, line:Pango.LayoutLine, x:int, y:int) """
        pass

    def draw_rectangle(self, part, x, y, width, height): # real signature unknown; restored from __doc__
        """ draw_rectangle(self, part:Pango.RenderPart, x:int, y:int, width:int, height:int) """
        pass

    def draw_trapezoid(self, part, y1_, x11, x21, y2, x12, x22): # real signature unknown; restored from __doc__
        """ draw_trapezoid(self, part:Pango.RenderPart, y1_:float, x11:float, x21:float, y2:float, x12:float, x22:float) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_alpha(self, part): # real signature unknown; restored from __doc__
        """ get_alpha(self, part:Pango.RenderPart) -> int """
        return 0

    def get_color(self, part): # real signature unknown; restored from __doc__
        """ get_color(self, part:Pango.RenderPart) -> Pango.Color or None """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_layout(self): # real signature unknown; restored from __doc__
        """ get_layout(self) -> Pango.Layout or None """
        pass

    def get_layout_line(self): # real signature unknown; restored from __doc__
        """ get_layout_line(self) -> Pango.LayoutLine or None """
        pass

    def get_matrix(self): # real signature unknown; restored from __doc__
        """ get_matrix(self) -> Pango.Matrix or None """
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

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def part_changed(self, part): # real signature unknown; restored from __doc__
        """ part_changed(self, part:Pango.RenderPart) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def set_alpha(self, part, alpha): # real signature unknown; restored from __doc__
        """ set_alpha(self, part:Pango.RenderPart, alpha:int) """
        pass

    def set_color(self, part, color=None): # real signature unknown; restored from __doc__
        """ set_color(self, part:Pango.RenderPart, color:Pango.Color=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_matrix(self, matrix=None): # real signature unknown; restored from __doc__
        """ set_matrix(self, matrix:Pango.Matrix=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

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

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
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

    active_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    matrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    strikethrough = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    underline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x0000028033701360>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Renderer), '__module__': 'gi.repository.Pango', '__gtype__': <GType PangoRenderer (843936192)>, '__doc__': None, '__gsignals__': {}, 'activate': gi.FunctionInfo(activate), 'deactivate': gi.FunctionInfo(deactivate), 'draw_error_underline': gi.FunctionInfo(draw_error_underline), 'draw_glyph': gi.FunctionInfo(draw_glyph), 'draw_glyph_item': gi.FunctionInfo(draw_glyph_item), 'draw_glyphs': gi.FunctionInfo(draw_glyphs), 'draw_layout': gi.FunctionInfo(draw_layout), 'draw_layout_line': gi.FunctionInfo(draw_layout_line), 'draw_rectangle': gi.FunctionInfo(draw_rectangle), 'draw_trapezoid': gi.FunctionInfo(draw_trapezoid), 'get_alpha': gi.FunctionInfo(get_alpha), 'get_color': gi.FunctionInfo(get_color), 'get_layout': gi.FunctionInfo(get_layout), 'get_layout_line': gi.FunctionInfo(get_layout_line), 'get_matrix': gi.FunctionInfo(get_matrix), 'part_changed': gi.FunctionInfo(part_changed), 'set_alpha': gi.FunctionInfo(set_alpha), 'set_color': gi.FunctionInfo(set_color), 'set_matrix': gi.FunctionInfo(set_matrix), 'do_begin': gi.VFuncInfo(begin), 'do_draw_error_underline': gi.VFuncInfo(draw_error_underline), 'do_draw_glyph': gi.VFuncInfo(draw_glyph), 'do_draw_glyph_item': gi.VFuncInfo(draw_glyph_item), 'do_draw_glyphs': gi.VFuncInfo(draw_glyphs), 'do_draw_rectangle': gi.VFuncInfo(draw_rectangle), 'do_draw_shape': gi.VFuncInfo(draw_shape), 'do_draw_trapezoid': gi.VFuncInfo(draw_trapezoid), 'do_end': gi.VFuncInfo(end), 'do_part_changed': gi.VFuncInfo(part_changed), 'do_prepare_run': gi.VFuncInfo(prepare_run), 'parent_instance': <property object at 0x00000280355cc400>, 'underline': <property object at 0x00000280355cc310>, 'strikethrough': <property object at 0x00000280355cc5e0>, 'active_count': <property object at 0x00000280355cc6d0>, 'matrix': <property object at 0x00000280355cc7c0>, 'priv': <property object at 0x00000280355cc8b0>})"
    __firstlineno__ = 651
    __gdoc__ = 'Object PangoRenderer\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType PangoRenderer (843936192)>'
    __info__ = ObjectInfo(Renderer)
    __static_attributes__ = ()


