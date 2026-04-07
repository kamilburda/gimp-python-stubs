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


from .PrintOperationPreview import PrintOperationPreview

class PrintOperation(__gi_overrides_GObject.Object, PrintOperationPreview):
    """
    :Constructors:
    
    ::
    
        PrintOperation(**properties)
        new() -> Gtk.PrintOperation
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel(self) """
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

    def do_begin_print(self, *args, **kwargs): # real signature unknown
        """ begin_print(self, context:Gtk.PrintContext) """
        pass

    def do_constructed(self, *args, **kwargs): # real signature unknown
        pass

    def do_custom_widget_apply(self, *args, **kwargs): # real signature unknown
        """ custom_widget_apply(self, widget:Gtk.Widget) """
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def do_done(self, *args, **kwargs): # real signature unknown
        """ done(self, result:Gtk.PrintOperationResult) """
        pass

    def do_draw_page(self, *args, **kwargs): # real signature unknown
        """ draw_page(self, context:Gtk.PrintContext, page_nr:int) """
        pass

    def do_end_print(self, *args, **kwargs): # real signature unknown
        """ end_print(self, context:Gtk.PrintContext) """
        pass

    def do_paginate(self, *args, **kwargs): # real signature unknown
        """ paginate(self, context:Gtk.PrintContext) -> bool """
        pass

    def do_preview(self, *args, **kwargs): # real signature unknown
        """ preview(self, preview:Gtk.PrintOperationPreview, context:Gtk.PrintContext, parent:Gtk.Window) -> bool """
        pass

    def do_request_page_setup(self, *args, **kwargs): # real signature unknown
        """ request_page_setup(self, context:Gtk.PrintContext, page_nr:int, setup:Gtk.PageSetup) """
        pass

    def do_status_changed(self, *args, **kwargs): # real signature unknown
        """ status_changed(self) """
        pass

    def do_update_custom_widget(self, *args, **kwargs): # real signature unknown
        """ update_custom_widget(self, widget:Gtk.Widget, setup:Gtk.PageSetup, settings:Gtk.PrintSettings) """
        pass

    def draw_page_finish(self): # real signature unknown; restored from __doc__
        """ draw_page_finish(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def end_preview(self): # real signature unknown; restored from __doc__
        """ end_preview(self) """
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

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_page_setup(self): # real signature unknown; restored from __doc__
        """ get_default_page_setup(self) -> Gtk.PageSetup """
        pass

    def get_embed_page_setup(self): # real signature unknown; restored from __doc__
        """ get_embed_page_setup(self) -> bool """
        return False

    def get_error(self): # real signature unknown; restored from __doc__
        """ get_error(self) """
        pass

    def get_has_selection(self): # real signature unknown; restored from __doc__
        """ get_has_selection(self) -> bool """
        return False

    def get_n_pages_to_print(self): # real signature unknown; restored from __doc__
        """ get_n_pages_to_print(self) -> int """
        return 0

    def get_print_settings(self): # real signature unknown; restored from __doc__
        """ get_print_settings(self) -> Gtk.PrintSettings """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_status(self): # real signature unknown; restored from __doc__
        """ get_status(self) -> Gtk.PrintStatus """
        pass

    def get_status_string(self): # real signature unknown; restored from __doc__
        """ get_status_string(self) -> str """
        return ""

    def get_support_selection(self): # real signature unknown; restored from __doc__
        """ get_support_selection(self) -> bool """
        return False

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

    def is_finished(self): # real signature unknown; restored from __doc__
        """ is_finished(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_selected(self, page_nr): # real signature unknown; restored from __doc__
        """ is_selected(self, page_nr:int) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> Gtk.PrintOperation """
        pass

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

    def render_page(self, page_nr): # real signature unknown; restored from __doc__
        """ render_page(self, page_nr:int) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run(self, action, parent=None): # real signature unknown; restored from __doc__
        """ run(self, action:Gtk.PrintOperationAction, parent:Gtk.Window=None) -> Gtk.PrintOperationResult """
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def set_allow_async(self, allow_async): # real signature unknown; restored from __doc__
        """ set_allow_async(self, allow_async:bool) """
        pass

    def set_current_page(self, current_page): # real signature unknown; restored from __doc__
        """ set_current_page(self, current_page:int) """
        pass

    def set_custom_tab_label(self, label=None): # real signature unknown; restored from __doc__
        """ set_custom_tab_label(self, label:str=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_page_setup(self, default_page_setup=None): # real signature unknown; restored from __doc__
        """ set_default_page_setup(self, default_page_setup:Gtk.PageSetup=None) """
        pass

    def set_defer_drawing(self): # real signature unknown; restored from __doc__
        """ set_defer_drawing(self) """
        pass

    def set_embed_page_setup(self, embed): # real signature unknown; restored from __doc__
        """ set_embed_page_setup(self, embed:bool) """
        pass

    def set_export_filename(self, filename): # real signature unknown; restored from __doc__
        """ set_export_filename(self, filename:str) """
        pass

    def set_has_selection(self, has_selection): # real signature unknown; restored from __doc__
        """ set_has_selection(self, has_selection:bool) """
        pass

    def set_job_name(self, job_name): # real signature unknown; restored from __doc__
        """ set_job_name(self, job_name:str) """
        pass

    def set_n_pages(self, n_pages): # real signature unknown; restored from __doc__
        """ set_n_pages(self, n_pages:int) """
        pass

    def set_print_settings(self, print_settings=None): # real signature unknown; restored from __doc__
        """ set_print_settings(self, print_settings:Gtk.PrintSettings=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_show_progress(self, show_progress): # real signature unknown; restored from __doc__
        """ set_show_progress(self, show_progress:bool) """
        pass

    def set_support_selection(self, support_selection): # real signature unknown; restored from __doc__
        """ set_support_selection(self, support_selection:bool) """
        pass

    def set_track_print_status(self, track_status): # real signature unknown; restored from __doc__
        """ set_track_print_status(self, track_status:bool) """
        pass

    def set_unit(self, unit): # real signature unknown; restored from __doc__
        """ set_unit(self, unit:Gtk.Unit) """
        pass

    def set_use_full_page(self, full_page): # real signature unknown; restored from __doc__
        """ set_use_full_page(self, full_page:bool) """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002bfd1801330>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(PrintOperation), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkPrintOperation (3540063712)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'cancel': gi.FunctionInfo(cancel), 'draw_page_finish': gi.FunctionInfo(draw_page_finish), 'get_default_page_setup': gi.FunctionInfo(get_default_page_setup), 'get_embed_page_setup': gi.FunctionInfo(get_embed_page_setup), 'get_error': gi.FunctionInfo(get_error), 'get_has_selection': gi.FunctionInfo(get_has_selection), 'get_n_pages_to_print': gi.FunctionInfo(get_n_pages_to_print), 'get_print_settings': gi.FunctionInfo(get_print_settings), 'get_status': gi.FunctionInfo(get_status), 'get_status_string': gi.FunctionInfo(get_status_string), 'get_support_selection': gi.FunctionInfo(get_support_selection), 'is_finished': gi.FunctionInfo(is_finished), 'run': gi.FunctionInfo(run), 'set_allow_async': gi.FunctionInfo(set_allow_async), 'set_current_page': gi.FunctionInfo(set_current_page), 'set_custom_tab_label': gi.FunctionInfo(set_custom_tab_label), 'set_default_page_setup': gi.FunctionInfo(set_default_page_setup), 'set_defer_drawing': gi.FunctionInfo(set_defer_drawing), 'set_embed_page_setup': gi.FunctionInfo(set_embed_page_setup), 'set_export_filename': gi.FunctionInfo(set_export_filename), 'set_has_selection': gi.FunctionInfo(set_has_selection), 'set_job_name': gi.FunctionInfo(set_job_name), 'set_n_pages': gi.FunctionInfo(set_n_pages), 'set_print_settings': gi.FunctionInfo(set_print_settings), 'set_show_progress': gi.FunctionInfo(set_show_progress), 'set_support_selection': gi.FunctionInfo(set_support_selection), 'set_track_print_status': gi.FunctionInfo(set_track_print_status), 'set_unit': gi.FunctionInfo(set_unit), 'set_use_full_page': gi.FunctionInfo(set_use_full_page), 'do_begin_print': gi.VFuncInfo(begin_print), 'do_custom_widget_apply': gi.VFuncInfo(custom_widget_apply), 'do_done': gi.VFuncInfo(done), 'do_draw_page': gi.VFuncInfo(draw_page), 'do_end_print': gi.VFuncInfo(end_print), 'do_paginate': gi.VFuncInfo(paginate), 'do_preview': gi.VFuncInfo(preview), 'do_request_page_setup': gi.VFuncInfo(request_page_setup), 'do_status_changed': gi.VFuncInfo(status_changed), 'do_update_custom_widget': gi.VFuncInfo(update_custom_widget), 'parent_instance': <property object at 0x000002bfd1891a80>, 'priv': <property object at 0x000002bfd1891e90>})"
    __firstlineno__ = 651
    __gdoc__ = 'Object GtkPrintOperation\n\nSignals from GtkPrintOperation:\n  done (GtkPrintOperationResult)\n  begin-print (GtkPrintContext)\n  paginate (GtkPrintContext) -> gboolean\n  request-page-setup (GtkPrintContext, gint, GtkPageSetup)\n  draw-page (GtkPrintContext, gint)\n  end-print (GtkPrintContext)\n  status-changed ()\n  create-custom-widget () -> GObject\n  update-custom-widget (GtkWidget, GtkPageSetup, GtkPrintSettings)\n  custom-widget-apply (GtkWidget)\n  preview (GtkPrintOperationPreview, GtkPrintContext, GtkWindow) -> gboolean\n\nProperties from GtkPrintOperation:\n  default-page-setup -> GtkPageSetup: Default Page Setup\n    The GtkPageSetup used by default\n  print-settings -> GtkPrintSettings: Print Settings\n    The GtkPrintSettings used for initializing the dialog\n  job-name -> gchararray: Job Name\n    A string used for identifying the print job.\n  n-pages -> gint: Number of Pages\n    The number of pages in the document.\n  current-page -> gint: Current Page\n    The current page in the document\n  use-full-page -> gboolean: Use full page\n    TRUE if the origin of the context should be at the corner of the page and not the corner of the imageable area\n  track-print-status -> gboolean: Track Print Status\n    TRUE if the print operation will continue to report on the print job status after the print data has been sent to the printer or print server.\n  unit -> GtkUnit: Unit\n    The unit in which distances can be measured in the context\n  show-progress -> gboolean: Show Dialog\n    TRUE if a progress dialog is shown while printing.\n  allow-async -> gboolean: Allow Async\n    TRUE if print process may run asynchronous.\n  export-filename -> gchararray: Export filename\n    Export filename\n  status -> GtkPrintStatus: Status\n    The status of the print operation\n  status-string -> gchararray: Status String\n    A human-readable description of the status\n  custom-tab-label -> gchararray: Custom tab label\n    Label for the tab containing custom widgets.\n  embed-page-setup -> gboolean: Embed Page Setup\n    TRUE if page setup combos are embedded in GtkPrintUnixDialog\n  has-selection -> gboolean: Has Selection\n    TRUE if a selection exists.\n  support-selection -> gboolean: Support Selection\n    TRUE if the print operation will support print of selection.\n  n-pages-to-print -> gint: Number of Pages To Print\n    The number of pages that will be printed.\n\nSignals from GtkPrintOperationPreview:\n  ready (GtkPrintContext)\n  got-page-size (GtkPrintContext, GtkPageSetup)\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkPrintOperation (3540063712)>'
    __info__ = ObjectInfo(PrintOperation)
    __static_attributes__ = ()


