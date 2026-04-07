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


class Node(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Node(**properties)
        new() -> Gegl.Node
        new_from_file(path:str) -> Gegl.Node
        new_from_serialized(chaindata:str, path_root:str) -> Gegl.Node
        new_from_xml(xmldata:str, path_root:str) -> Gegl.Node
    """
    def add_child(self, child): # real signature unknown; restored from __doc__
        """ add_child(self, child:Gegl.Node) -> Gegl.Node """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def blit_buffer(self, buffer=None, roi=None, level, abyss_policy): # real signature unknown; restored from __doc__
        """ blit_buffer(self, buffer:Gegl.Buffer=None, roi:Gegl.Rectangle=None, level:int, abyss_policy:Gegl.AbyssPolicy) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, a_pad_name, b, b_pad_name): # real signature unknown; restored from __doc__
        """ connect(self, a_pad_name:str, b:Gegl.Node, b_pad_name:str) -> bool """
        return False

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

    def connect_from(self, input_pad_name, source, output_pad_name): # real signature unknown; restored from __doc__
        """ connect_from(self, input_pad_name:str, source:Gegl.Node, output_pad_name:str) -> bool """
        return False

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_to(self, output_pad_name, sink, input_pad_name): # real signature unknown; restored from __doc__
        """ connect_to(self, output_pad_name:str, sink:Gegl.Node, input_pad_name:str) -> bool """
        return False

    def create_child(self, operation): # real signature unknown; restored from __doc__
        """ create_child(self, operation:str) -> Gegl.Node """
        pass

    def detect(self, x, y): # real signature unknown; restored from __doc__
        """ detect(self, x:int, y:int) -> Gegl.Node """
        pass

    def disconnect(self, input_pad): # real signature unknown; restored from __doc__
        """ disconnect(self, input_pad:str) -> bool """
        return False

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
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

    def get_bounding_box(self): # real signature unknown; restored from __doc__
        """ get_bounding_box(self) -> Gegl.Rectangle """
        pass

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> list """
        return []

    def get_consumers(self, output_pad): # real signature unknown; restored from __doc__
        """ get_consumers(self, output_pad:str) -> int, nodes:list, pads:list """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_gegl_operation(self): # real signature unknown; restored from __doc__
        """ get_gegl_operation(self) -> Gegl.Operation or None """
        pass

    def get_input_proxy(self, pad_name): # real signature unknown; restored from __doc__
        """ get_input_proxy(self, pad_name:str) -> Gegl.Node """
        pass

    def get_operation(self): # real signature unknown; restored from __doc__
        """ get_operation(self) -> str """
        return ""

    def get_output_proxy(self, pad_name): # real signature unknown; restored from __doc__
        """ get_output_proxy(self, pad_name:str) -> Gegl.Node """
        pass

    def get_pad_description(self, pad_name): # real signature unknown; restored from __doc__
        """ get_pad_description(self, pad_name:str) -> str """
        return ""

    def get_pad_label(self, pad_name): # real signature unknown; restored from __doc__
        """ get_pad_label(self, pad_name:str) -> str """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gegl.Node """
        pass

    def get_passthrough(self): # real signature unknown; restored from __doc__
        """ get_passthrough(self) -> bool """
        return False

    def get_producer(self, input_pad_name, output_pad_name=None): # real signature unknown; restored from __doc__
        """ get_producer(self, input_pad_name:str, output_pad_name:str=None) -> Gegl.Node """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, property_name): # real signature unknown; restored from __doc__
        """ get_property(self, property_name:str) -> GObject.Value """
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

    def has_pad(self, pad_name): # real signature unknown; restored from __doc__
        """ has_pad(self, pad_name:str) -> bool """
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

    def is_graph(self): # real signature unknown; restored from __doc__
        """ is_graph(self) -> bool """
        return False

    def link(self, sink): # real signature unknown; restored from __doc__
        """ link(self, sink:Gegl.Node) """
        pass

    def list_input_pads(self): # real signature unknown; restored from __doc__
        """ list_input_pads(self) -> list """
        return []

    def list_output_pads(self): # real signature unknown; restored from __doc__
        """ list_output_pads(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> Gegl.Node """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    @classmethod
    def new_from_file(cls, path): # real signature unknown; restored from __doc__
        """ new_from_file(path:str) -> Gegl.Node """
        pass

    @classmethod
    def new_from_serialized(cls, chaindata, path_root): # real signature unknown; restored from __doc__
        """ new_from_serialized(chaindata:str, path_root:str) -> Gegl.Node """
        pass

    @classmethod
    def new_from_xml(cls, xmldata, path_root): # real signature unknown; restored from __doc__
        """ new_from_xml(xmldata:str, path_root:str) -> Gegl.Node """
        pass

    def new_processor(self, rectangle): # real signature unknown; restored from __doc__
        """ new_processor(self, rectangle:Gegl.Rectangle) -> Gegl.Processor """
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

    def process(self): # real signature unknown; restored from __doc__
        """ process(self) """
        pass

    def progress(self, progress, message): # real signature unknown; restored from __doc__
        """ progress(self, progress:float, message:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_child(self, child): # real signature unknown; restored from __doc__
        """ remove_child(self, child:Gegl.Node) -> Gegl.Node """
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

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_enum_as_string(self, key, value): # real signature unknown; restored from __doc__
        """ set_enum_as_string(self, key:str, value:str) """
        pass

    def set_passthrough(self, passthrough): # real signature unknown; restored from __doc__
        """ set_passthrough(self, passthrough:bool) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, property_name, value): # real signature unknown; restored from __doc__
        """ set_property(self, property_name:str, value:GObject.Value) """
        pass

    def set_time(self, time): # real signature unknown; restored from __doc__
        """ set_time(self, time:float) """
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

    def to_xml(self, path_root): # real signature unknown; restored from __doc__
        """ to_xml(self, path_root:str) -> str """
        return ""

    def to_xml_full(self, tail=None, path_root): # real signature unknown; restored from __doc__
        """ to_xml_full(self, tail:Gegl.Node=None, path_root:str) -> str """
        return ""

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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001ebdc0e5270>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Node), '__module__': 'gi.repository.Gegl', '__gtype__': <GType GeglNode (3657335808)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'new_from_file': <classmethod(gi.FunctionInfo(new_from_file))>, 'new_from_serialized': <classmethod(gi.FunctionInfo(new_from_serialized))>, 'new_from_xml': <classmethod(gi.FunctionInfo(new_from_xml))>, 'add_child': gi.FunctionInfo(add_child), 'blit_buffer': gi.FunctionInfo(blit_buffer), 'connect': gi.FunctionInfo(connect), 'connect_from': gi.FunctionInfo(connect_from), 'connect_to': gi.FunctionInfo(connect_to), 'create_child': gi.FunctionInfo(create_child), 'detect': gi.FunctionInfo(detect), 'disconnect': gi.FunctionInfo(disconnect), 'find_property': gi.FunctionInfo(find_property), 'get_children': gi.FunctionInfo(get_children), 'get_consumers': gi.FunctionInfo(get_consumers), 'get_gegl_operation': gi.FunctionInfo(get_gegl_operation), 'get_input_proxy': gi.FunctionInfo(get_input_proxy), 'get_operation': gi.FunctionInfo(get_operation), 'get_output_proxy': gi.FunctionInfo(get_output_proxy), 'get_pad_description': gi.FunctionInfo(get_pad_description), 'get_pad_label': gi.FunctionInfo(get_pad_label), 'get_parent': gi.FunctionInfo(get_parent), 'get_passthrough': gi.FunctionInfo(get_passthrough), 'get_producer': gi.FunctionInfo(get_producer), 'has_pad': gi.FunctionInfo(has_pad), 'get_bounding_box': gi.FunctionInfo(get_bounding_box), 'get_property': gi.FunctionInfo(get_property), 'is_graph': gi.FunctionInfo(is_graph), 'link': gi.FunctionInfo(link), 'list_input_pads': gi.FunctionInfo(list_input_pads), 'list_output_pads': gi.FunctionInfo(list_output_pads), 'new_processor': gi.FunctionInfo(new_processor), 'process': gi.FunctionInfo(process), 'progress': gi.FunctionInfo(progress), 'remove_child': gi.FunctionInfo(remove_child), 'set_enum_as_string': gi.FunctionInfo(set_enum_as_string), 'set_passthrough': gi.FunctionInfo(set_passthrough), 'set_property': gi.FunctionInfo(set_property), 'set_time': gi.FunctionInfo(set_time), 'to_xml': gi.FunctionInfo(to_xml), 'to_xml_full': gi.FunctionInfo(to_xml_full)})"
    __gdoc__ = 'Object GeglNode\n\nSignals from GeglNode:\n  invalidated (GeglRectangle)\n  computed (GeglRectangle)\n  progress (gdouble)\n\nProperties from GeglNode:\n  operation -> gchararray: Operation Type\n    The type of associated GeglOperation\n  gegl-operation -> GeglOperation: Operation Object\n    The associated GeglOperation instance\n  name -> gchararray: Name\n    The name of the node\n  dont-cache -> gboolean: Do not cache\n    Do not cache the result of this operation, the property is inherited by children created from a node. (Deprecated for "cache-policy".)\n  cache-policy -> GeglCachePolicy: Cache Policy\n    Cache policy for this node, the property is inherited by children created from a node.\n  use-opencl -> gboolean: Use OpenCL\n    Use the OpenCL version of this operation if available, this property is inherited by children created from a node.\n  passthrough -> gboolean: Passthrough\n    Act as a nop, passing input unmodifed through to ouput.\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeglNode (3657335808)>'
    __info__ = ObjectInfo(Node)


