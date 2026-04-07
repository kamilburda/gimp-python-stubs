# encoding: utf-8
# module gi.repository.Gtk
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


from .Gesture import Gesture

class GestureSingle(Gesture):
    """
    :Constructors:
    
    ::
    
        GestureSingle(**properties)
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

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_constructed(self, *args, **kwargs): # real signature unknown
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
        """ get_bounding_box(self) -> bool, rect:Gdk.Rectangle """
        return False

    def get_bounding_box_center(self): # real signature unknown; restored from __doc__
        """ get_bounding_box_center(self) -> bool, x:float, y:float """
        return False

    def get_button(self): # real signature unknown; restored from __doc__
        """ get_button(self) -> int """
        return 0

    def get_current_button(self): # real signature unknown; restored from __doc__
        """ get_current_button(self) -> int """
        return 0

    def get_current_sequence(self): # real signature unknown; restored from __doc__
        """ get_current_sequence(self) -> Gdk.EventSequence or None """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_device(self): # real signature unknown; restored from __doc__
        """ get_device(self) -> Gdk.Device or None """
        pass

    def get_exclusive(self): # real signature unknown; restored from __doc__
        """ get_exclusive(self) -> bool """
        return False

    def get_group(self): # real signature unknown; restored from __doc__
        """ get_group(self) -> list """
        return []

    def get_last_event(self, sequence=None): # real signature unknown; restored from __doc__
        """ get_last_event(self, sequence:Gdk.EventSequence=None) -> Gdk.Event or None """
        pass

    def get_last_updated_sequence(self): # real signature unknown; restored from __doc__
        """ get_last_updated_sequence(self) -> Gdk.EventSequence or None """
        pass

    def get_point(self, sequence=None): # real signature unknown; restored from __doc__
        """ get_point(self, sequence:Gdk.EventSequence=None) -> bool, x:float, y:float """
        return False

    def get_propagation_phase(self): # real signature unknown; restored from __doc__
        """ get_propagation_phase(self) -> Gtk.PropagationPhase """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_sequences(self): # real signature unknown; restored from __doc__
        """ get_sequences(self) -> list """
        return []

    def get_sequence_state(self, sequence): # real signature unknown; restored from __doc__
        """ get_sequence_state(self, sequence:Gdk.EventSequence) -> Gtk.EventSequenceState """
        pass

    def get_touch_only(self): # real signature unknown; restored from __doc__
        """ get_touch_only(self) -> bool """
        return False

    def get_widget(self): # real signature unknown; restored from __doc__
        """ get_widget(self) -> Gtk.Widget """
        pass

    def get_window(self): # real signature unknown; restored from __doc__
        """ get_window(self) -> Gdk.Window or None """
        pass

    def group(self, gesture): # real signature unknown; restored from __doc__
        """ group(self, gesture:Gtk.Gesture) """
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

    def handles_sequence(self, sequence=None): # real signature unknown; restored from __doc__
        """ handles_sequence(self, sequence:Gdk.EventSequence=None) -> bool """
        return False

    def handle_event(self, event): # real signature unknown; restored from __doc__
        """ handle_event(self, event:Gdk.Event) -> bool """
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

    def is_active(self): # real signature unknown; restored from __doc__
        """ is_active(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_grouped_with(self, other): # real signature unknown; restored from __doc__
        """ is_grouped_with(self, other:Gtk.Gesture) -> bool """
        return False

    def is_recognized(self): # real signature unknown; restored from __doc__
        """ is_recognized(self) -> bool """
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

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def set_button(self, button): # real signature unknown; restored from __doc__
        """ set_button(self, button:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_exclusive(self, exclusive): # real signature unknown; restored from __doc__
        """ set_exclusive(self, exclusive:bool) """
        pass

    def set_propagation_phase(self, phase): # real signature unknown; restored from __doc__
        """ set_propagation_phase(self, phase:Gtk.PropagationPhase) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_sequence_state(self, sequence, state): # real signature unknown; restored from __doc__
        """ set_sequence_state(self, sequence:Gdk.EventSequence, state:Gtk.EventSequenceState) -> bool """
        return False

    def set_state(self, state): # real signature unknown; restored from __doc__
        """ set_state(self, state:Gtk.EventSequenceState) -> bool """
        return False

    def set_touch_only(self, touch_only): # real signature unknown; restored from __doc__
        """ set_touch_only(self, touch_only:bool) """
        pass

    def set_window(self, window=None): # real signature unknown; restored from __doc__
        """ set_window(self, window:Gdk.Window=None) """
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

    def ungroup(self): # real signature unknown; restored from __doc__
        """ ungroup(self) """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002bfd1803730>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(GestureSingle), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkGestureSingle (3537675600)>, '__doc__': None, '__gsignals__': {}, 'get_button': gi.FunctionInfo(get_button), 'get_current_button': gi.FunctionInfo(get_current_button), 'get_current_sequence': gi.FunctionInfo(get_current_sequence), 'get_exclusive': gi.FunctionInfo(get_exclusive), 'get_touch_only': gi.FunctionInfo(get_touch_only), 'set_button': gi.FunctionInfo(set_button), 'set_exclusive': gi.FunctionInfo(set_exclusive), 'set_touch_only': gi.FunctionInfo(set_touch_only)})"
    __firstlineno__ = 651
    __gdoc__ = 'Object GtkGestureSingle\n\nProperties from GtkGestureSingle:\n  touch-only -> gboolean: Handle only touch events\n    Whether the gesture handles only touch events\n  exclusive -> gboolean: Whether the gesture is exclusive\n    Whether the gesture is exclusive\n  button -> guint: Button number\n    Button number to listen to\n\nSignals from GtkGesture:\n  cancel (GdkEventSequence)\n  begin (GdkEventSequence)\n  end (GdkEventSequence)\n  update (GdkEventSequence)\n  sequence-state-changed (GdkEventSequence, GtkEventSequenceState)\n\nProperties from GtkGesture:\n  n-points -> guint: Number of points\n    Number of points needed to trigger the gesture\n  window -> GdkWindow: GdkWindow to receive events about\n    GdkWindow to receive events about\n\nProperties from GtkEventController:\n  widget -> GtkWidget: Widget\n    Widget the gesture relates to\n  propagation-phase -> GtkPropagationPhase: Propagation phase\n    Propagation phase at which this controller is run\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkGestureSingle (3537675600)>'
    __info__ = ObjectInfo(GestureSingle)
    __static_attributes__ = ()


