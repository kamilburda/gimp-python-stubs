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


from .Metadata import Metadata

class MetadataStore(__gi_overrides_GObject.Object, Metadata):
    """
    :Constructors:
    
    ::
    
        MetadataStore(**properties)
    """
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

    def declare(self, pspec): # real signature unknown; restored from __doc__
        """ declare(self, pspec:GObject.ParamSpec) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def do_has_value(self, *args, **kwargs): # real signature unknown
        """ has_value(self, name:str) -> bool """
        pass

    def do_register_hook(self, *args, **kwargs): # real signature unknown
        """ register_hook(self, file_module_name:str, flags:int) """
        pass

    def do_set_value(self, *args, **kwargs): # real signature unknown
        """ set_value(self, name:str, value:GObject.Value) """
        pass

    def do__declare(self, *args, **kwargs): # real signature unknown
        """ _declare(self, pspec:GObject.ParamSpec, shadow:bool) """
        pass

    def do__get_value(self, *args, **kwargs): # real signature unknown
        """ _get_value(self, name:str) -> GObject.Value """
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

    def get_artist(self): # real signature unknown; restored from __doc__
        """ get_artist(self) -> str """
        return ""

    def get_comment(self): # real signature unknown; restored from __doc__
        """ get_comment(self) -> str """
        return ""

    def get_copyright(self): # real signature unknown; restored from __doc__
        """ get_copyright(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_disclaimer(self): # real signature unknown; restored from __doc__
        """ get_disclaimer(self) -> str """
        return ""

    def get_file_module_name(self): # real signature unknown; restored from __doc__
        """ get_file_module_name(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_resolution(self, unit, x, y): # real signature unknown; restored from __doc__
        """ get_resolution(self, unit:Gegl.ResolutionUnit, x:float, y:float) -> bool """
        return False

    def get_resolution_unit(self): # real signature unknown; restored from __doc__
        """ get_resolution_unit(self) -> Gegl.ResolutionUnit """
        pass

    def get_resolution_x(self): # real signature unknown; restored from __doc__
        """ get_resolution_x(self) -> float """
        return 0.0

    def get_resolution_y(self): # real signature unknown; restored from __doc__
        """ get_resolution_y(self) -> float """
        return 0.0

    def get_software(self): # real signature unknown; restored from __doc__
        """ get_software(self) -> str """
        return ""

    def get_source(self): # real signature unknown; restored from __doc__
        """ get_source(self) -> str """
        return ""

    def get_string(self, name): # real signature unknown; restored from __doc__
        """ get_string(self, name:str) -> str """
        return ""

    def get_timestamp(self): # real signature unknown; restored from __doc__
        """ get_timestamp(self) -> GLib.DateTime """
        pass

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_value(self, name, value): # real signature unknown; restored from __doc__
        """ get_value(self, name:str, value:GObject.Value) -> value:GObject.Value """
        pass

    def get_warning(self): # real signature unknown; restored from __doc__
        """ get_warning(self) -> str """
        return ""

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

    def has_value(self, name): # real signature unknown; restored from __doc__
        """ has_value(self, name:str) -> bool """
        return False

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

    def iter_get_value(self, iter, value): # real signature unknown; restored from __doc__
        """ iter_get_value(self, iter:Gegl.MetadataIter, value:GObject.Value) -> bool """
        return False

    def iter_init(self, iter): # real signature unknown; restored from __doc__
        """ iter_init(self, iter:Gegl.MetadataIter) """
        pass

    def iter_lookup(self, iter, key): # real signature unknown; restored from __doc__
        """ iter_lookup(self, iter:Gegl.MetadataIter, key:str) -> bool """
        return False

    def iter_next(self, iter): # real signature unknown; restored from __doc__
        """ iter_next(self, iter:Gegl.MetadataIter) -> str """
        return ""

    def iter_set_value(self, iter, value): # real signature unknown; restored from __doc__
        """ iter_set_value(self, iter:Gegl.MetadataIter, value:GObject.Value) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, pspec, shadow): # real signature unknown; restored from __doc__
        """ notify(self, pspec:GObject.ParamSpec, shadow:bool) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def register(self, local_name, name, transform): # real signature unknown; restored from __doc__
        """ register(self, local_name:str, name:str, transform:GObject.ValueTransform) """
        pass

    def register_map(self, file_module, flags, map): # real signature unknown; restored from __doc__
        """ register_map(self, file_module:str, flags:int, map:list) """
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

    def set_artist(self, artist): # real signature unknown; restored from __doc__
        """ set_artist(self, artist:str) """
        pass

    def set_comment(self, comment): # real signature unknown; restored from __doc__
        """ set_comment(self, comment:str) """
        pass

    def set_copyright(self, copyright): # real signature unknown; restored from __doc__
        """ set_copyright(self, copyright:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_disclaimer(self, disclaimer): # real signature unknown; restored from __doc__
        """ set_disclaimer(self, disclaimer:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_resolution(self, unit, x, y): # real signature unknown; restored from __doc__
        """ set_resolution(self, unit:Gegl.ResolutionUnit, x:float, y:float) -> bool """
        return False

    def set_resolution_unit(self, unit): # real signature unknown; restored from __doc__
        """ set_resolution_unit(self, unit:Gegl.ResolutionUnit) """
        pass

    def set_resolution_x(self, resolution_x): # real signature unknown; restored from __doc__
        """ set_resolution_x(self, resolution_x:float) """
        pass

    def set_resolution_y(self, resolution_y): # real signature unknown; restored from __doc__
        """ set_resolution_y(self, resolution_y:float) """
        pass

    def set_software(self, software): # real signature unknown; restored from __doc__
        """ set_software(self, software:str) """
        pass

    def set_source(self, source): # real signature unknown; restored from __doc__
        """ set_source(self, source:str) """
        pass

    def set_string(self, name, string): # real signature unknown; restored from __doc__
        """ set_string(self, name:str, string:str) """
        pass

    def set_timestamp(self, timestamp): # real signature unknown; restored from __doc__
        """ set_timestamp(self, timestamp:GLib.DateTime) """
        pass

    def set_title(self, title): # real signature unknown; restored from __doc__
        """ set_title(self, title:str) """
        pass

    def set_value(self, name, value): # real signature unknown; restored from __doc__
        """ set_value(self, name:str, value:GObject.Value) """
        pass

    def set_warning(self, warning): # real signature unknown; restored from __doc__
        """ set_warning(self, warning:str) """
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

    def typeof_value(self, name): # real signature unknown; restored from __doc__
        """ typeof_value(self, name:str) -> GType """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unregister_map(self): # real signature unknown; restored from __doc__
        """ unregister_map(self) """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001ebdc0e5d80>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(MetadataStore), '__module__': 'gi.repository.Gegl', '__gtype__': <GType GeglMetadataStore (3657336384)>, '__doc__': None, '__gsignals__': {}, 'declare': gi.FunctionInfo(declare), 'get_artist': gi.FunctionInfo(get_artist), 'get_comment': gi.FunctionInfo(get_comment), 'get_copyright': gi.FunctionInfo(get_copyright), 'get_description': gi.FunctionInfo(get_description), 'get_disclaimer': gi.FunctionInfo(get_disclaimer), 'get_file_module_name': gi.FunctionInfo(get_file_module_name), 'get_resolution_unit': gi.FunctionInfo(get_resolution_unit), 'get_resolution_x': gi.FunctionInfo(get_resolution_x), 'get_resolution_y': gi.FunctionInfo(get_resolution_y), 'get_software': gi.FunctionInfo(get_software), 'get_source': gi.FunctionInfo(get_source), 'get_string': gi.FunctionInfo(get_string), 'get_timestamp': gi.FunctionInfo(get_timestamp), 'get_title': gi.FunctionInfo(get_title), 'get_value': gi.FunctionInfo(get_value), 'get_warning': gi.FunctionInfo(get_warning), 'has_value': gi.FunctionInfo(has_value), 'notify': gi.FunctionInfo(notify), 'register': gi.FunctionInfo(register), 'set_artist': gi.FunctionInfo(set_artist), 'set_comment': gi.FunctionInfo(set_comment), 'set_copyright': gi.FunctionInfo(set_copyright), 'set_description': gi.FunctionInfo(set_description), 'set_disclaimer': gi.FunctionInfo(set_disclaimer), 'set_resolution_unit': gi.FunctionInfo(set_resolution_unit), 'set_resolution_x': gi.FunctionInfo(set_resolution_x), 'set_resolution_y': gi.FunctionInfo(set_resolution_y), 'set_software': gi.FunctionInfo(set_software), 'set_source': gi.FunctionInfo(set_source), 'set_string': gi.FunctionInfo(set_string), 'set_timestamp': gi.FunctionInfo(set_timestamp), 'set_title': gi.FunctionInfo(set_title), 'set_value': gi.FunctionInfo(set_value), 'set_warning': gi.FunctionInfo(set_warning), 'typeof_value': gi.FunctionInfo(typeof_value), 'do__declare': gi.VFuncInfo(_declare), 'do__get_value': gi.VFuncInfo(_get_value), 'do_has_value': gi.VFuncInfo(has_value), 'do_register_hook': gi.VFuncInfo(register_hook), 'do_set_value': gi.VFuncInfo(set_value), 'parent_instance': <property object at 0x000001ebdc263f10>})"
    __gdoc__ = 'Object GeglMetadataStore\n\nSignals from GeglMetadataStore:\n  changed (GParam)\n  mapped (gchararray, gboolean)\n  unmapped (gchararray, gchararray)\n  generate-value (GParam, GValue) -> gboolean\n  parse-value (GParam, GValue) -> gboolean\n\nProperties from GeglMetadataStore:\n  resolution-unit -> GeglResolutionUnit: Resolution Unit\n    Units for image resolution\n  resolution-x -> gdouble: Resolution X\n    X Resolution\n  resolution-y -> gdouble: Resolution Y\n    X Resolution\n  file-module-name -> gchararray: File Module Name\n    Name of currently active file module or NULL\n  title -> gchararray: Title\n    Short title or caption\n  artist -> gchararray: Artist\n    Name of image creator\n  description -> gchararray: Description\n    Description of image (possibly long)\n  copyright -> gchararray: Copyright\n    Copyright notice\n  disclaimer -> gchararray: Disclaimer\n    Legal disclaimer\n  warning -> gchararray: Warning\n    Warning of nature of content\n  comment -> gchararray: Comment\n    Miscellaneous comment\n  software -> gchararray: Software\n    Software used to create the image\n  source -> gchararray: Source\n    Device used to create the image\n  timestamp -> GDateTime: Timestamp\n    Image creation time\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeglMetadataStore (3657336384)>'
    __info__ = ObjectInfo(MetadataStore)


