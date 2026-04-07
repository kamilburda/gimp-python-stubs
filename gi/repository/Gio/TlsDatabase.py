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


class TlsDatabase(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        TlsDatabase(**properties)
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

    def create_certificate_handle(self, certificate): # real signature unknown; restored from __doc__
        """ create_certificate_handle(self, certificate:Gio.TlsCertificate) -> str or None """
        return ""

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_create_certificate_handle(self, *args, **kwargs): # real signature unknown
        """ create_certificate_handle(self, certificate:Gio.TlsCertificate) -> str or None """
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def do_lookup_certificates_issued_by(self, *args, **kwargs): # real signature unknown
        """ lookup_certificates_issued_by(self, issuer_raw_dn:list, interaction:Gio.TlsInteraction=None, flags:Gio.TlsDatabaseLookupFlags, cancellable:Gio.Cancellable=None) -> list """
        pass

    def do_lookup_certificates_issued_by_async(self, *args, **kwargs): # real signature unknown
        """ lookup_certificates_issued_by_async(self, issuer_raw_dn:list, interaction:Gio.TlsInteraction=None, flags:Gio.TlsDatabaseLookupFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_lookup_certificates_issued_by_finish(self, *args, **kwargs): # real signature unknown
        """ lookup_certificates_issued_by_finish(self, result:Gio.AsyncResult) -> list """
        pass

    def do_lookup_certificate_for_handle(self, *args, **kwargs): # real signature unknown
        """ lookup_certificate_for_handle(self, handle:str, interaction:Gio.TlsInteraction=None, flags:Gio.TlsDatabaseLookupFlags, cancellable:Gio.Cancellable=None) -> Gio.TlsCertificate or None """
        pass

    def do_lookup_certificate_for_handle_async(self, *args, **kwargs): # real signature unknown
        """ lookup_certificate_for_handle_async(self, handle:str, interaction:Gio.TlsInteraction=None, flags:Gio.TlsDatabaseLookupFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_lookup_certificate_for_handle_finish(self, *args, **kwargs): # real signature unknown
        """ lookup_certificate_for_handle_finish(self, result:Gio.AsyncResult) -> Gio.TlsCertificate """
        pass

    def do_lookup_certificate_issuer(self, *args, **kwargs): # real signature unknown
        """ lookup_certificate_issuer(self, certificate:Gio.TlsCertificate, interaction:Gio.TlsInteraction=None, flags:Gio.TlsDatabaseLookupFlags, cancellable:Gio.Cancellable=None) -> Gio.TlsCertificate """
        pass

    def do_lookup_certificate_issuer_async(self, *args, **kwargs): # real signature unknown
        """ lookup_certificate_issuer_async(self, certificate:Gio.TlsCertificate, interaction:Gio.TlsInteraction=None, flags:Gio.TlsDatabaseLookupFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_lookup_certificate_issuer_finish(self, *args, **kwargs): # real signature unknown
        """ lookup_certificate_issuer_finish(self, result:Gio.AsyncResult) -> Gio.TlsCertificate """
        pass

    def do_verify_chain(self, *args, **kwargs): # real signature unknown
        """ verify_chain(self, chain:Gio.TlsCertificate, purpose:str, identity:Gio.SocketConnectable=None, interaction:Gio.TlsInteraction=None, flags:Gio.TlsDatabaseVerifyFlags, cancellable:Gio.Cancellable=None) -> Gio.TlsCertificateFlags """
        pass

    def do_verify_chain_async(self, *args, **kwargs): # real signature unknown
        """ verify_chain_async(self, chain:Gio.TlsCertificate, purpose:str, identity:Gio.SocketConnectable=None, interaction:Gio.TlsInteraction=None, flags:Gio.TlsDatabaseVerifyFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_verify_chain_finish(self, *args, **kwargs): # real signature unknown
        """ verify_chain_finish(self, result:Gio.AsyncResult) -> Gio.TlsCertificateFlags """
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

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def lookup_certificates_issued_by(self, issuer_raw_dn, interaction=None, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ lookup_certificates_issued_by(self, issuer_raw_dn:list, interaction:Gio.TlsInteraction=None, flags:Gio.TlsDatabaseLookupFlags, cancellable:Gio.Cancellable=None) -> list """
        return []

    def lookup_certificates_issued_by_async(self, issuer_raw_dn, interaction=None, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ lookup_certificates_issued_by_async(self, issuer_raw_dn:list, interaction:Gio.TlsInteraction=None, flags:Gio.TlsDatabaseLookupFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def lookup_certificates_issued_by_finish(self, result): # real signature unknown; restored from __doc__
        """ lookup_certificates_issued_by_finish(self, result:Gio.AsyncResult) -> list """
        return []

    def lookup_certificate_for_handle(self, handle, interaction=None, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ lookup_certificate_for_handle(self, handle:str, interaction:Gio.TlsInteraction=None, flags:Gio.TlsDatabaseLookupFlags, cancellable:Gio.Cancellable=None) -> Gio.TlsCertificate or None """
        pass

    def lookup_certificate_for_handle_async(self, handle, interaction=None, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ lookup_certificate_for_handle_async(self, handle:str, interaction:Gio.TlsInteraction=None, flags:Gio.TlsDatabaseLookupFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def lookup_certificate_for_handle_finish(self, result): # real signature unknown; restored from __doc__
        """ lookup_certificate_for_handle_finish(self, result:Gio.AsyncResult) -> Gio.TlsCertificate """
        pass

    def lookup_certificate_issuer(self, certificate, interaction=None, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ lookup_certificate_issuer(self, certificate:Gio.TlsCertificate, interaction:Gio.TlsInteraction=None, flags:Gio.TlsDatabaseLookupFlags, cancellable:Gio.Cancellable=None) -> Gio.TlsCertificate """
        pass

    def lookup_certificate_issuer_async(self, certificate, interaction=None, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ lookup_certificate_issuer_async(self, certificate:Gio.TlsCertificate, interaction:Gio.TlsInteraction=None, flags:Gio.TlsDatabaseLookupFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def lookup_certificate_issuer_finish(self, result): # real signature unknown; restored from __doc__
        """ lookup_certificate_issuer_finish(self, result:Gio.AsyncResult) -> Gio.TlsCertificate """
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

    def verify_chain(self, chain, purpose, identity=None, interaction=None, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ verify_chain(self, chain:Gio.TlsCertificate, purpose:str, identity:Gio.SocketConnectable=None, interaction:Gio.TlsInteraction=None, flags:Gio.TlsDatabaseVerifyFlags, cancellable:Gio.Cancellable=None) -> Gio.TlsCertificateFlags """
        pass

    def verify_chain_async(self, chain, purpose, identity=None, interaction=None, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ verify_chain_async(self, chain:Gio.TlsCertificate, purpose:str, identity:Gio.SocketConnectable=None, interaction:Gio.TlsInteraction=None, flags:Gio.TlsDatabaseVerifyFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def verify_chain_finish(self, result): # real signature unknown; restored from __doc__
        """ verify_chain_finish(self, result:Gio.AsyncResult) -> Gio.TlsCertificateFlags """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001ea7086e440>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(TlsDatabase), '__module__': 'gi.repository.Gio', '__gtype__': <GType GTlsDatabase (1845531968)>, '__doc__': None, '__gsignals__': {}, 'create_certificate_handle': gi.FunctionInfo(create_certificate_handle), 'lookup_certificate_for_handle': gi.FunctionInfo(lookup_certificate_for_handle), 'lookup_certificate_for_handle_async': gi.FunctionInfo(lookup_certificate_for_handle_async), 'lookup_certificate_for_handle_finish': gi.FunctionInfo(lookup_certificate_for_handle_finish), 'lookup_certificate_issuer': gi.FunctionInfo(lookup_certificate_issuer), 'lookup_certificate_issuer_async': gi.FunctionInfo(lookup_certificate_issuer_async), 'lookup_certificate_issuer_finish': gi.FunctionInfo(lookup_certificate_issuer_finish), 'lookup_certificates_issued_by': gi.FunctionInfo(lookup_certificates_issued_by), 'lookup_certificates_issued_by_async': gi.FunctionInfo(lookup_certificates_issued_by_async), 'lookup_certificates_issued_by_finish': gi.FunctionInfo(lookup_certificates_issued_by_finish), 'verify_chain': gi.FunctionInfo(verify_chain), 'verify_chain_async': gi.FunctionInfo(verify_chain_async), 'verify_chain_finish': gi.FunctionInfo(verify_chain_finish), 'do_create_certificate_handle': gi.VFuncInfo(create_certificate_handle), 'do_lookup_certificate_for_handle': gi.VFuncInfo(lookup_certificate_for_handle), 'do_lookup_certificate_for_handle_async': gi.VFuncInfo(lookup_certificate_for_handle_async), 'do_lookup_certificate_for_handle_finish': gi.VFuncInfo(lookup_certificate_for_handle_finish), 'do_lookup_certificate_issuer': gi.VFuncInfo(lookup_certificate_issuer), 'do_lookup_certificate_issuer_async': gi.VFuncInfo(lookup_certificate_issuer_async), 'do_lookup_certificate_issuer_finish': gi.VFuncInfo(lookup_certificate_issuer_finish), 'do_lookup_certificates_issued_by': gi.VFuncInfo(lookup_certificates_issued_by), 'do_lookup_certificates_issued_by_async': gi.VFuncInfo(lookup_certificates_issued_by_async), 'do_lookup_certificates_issued_by_finish': gi.VFuncInfo(lookup_certificates_issued_by_finish), 'do_verify_chain': gi.VFuncInfo(verify_chain), 'do_verify_chain_async': gi.VFuncInfo(verify_chain_async), 'do_verify_chain_finish': gi.VFuncInfo(verify_chain_finish), 'parent_instance': <property object at 0x000001ea709dfab0>, 'priv': <property object at 0x000001ea709dfba0>})"
    __gdoc__ = 'Object GTlsDatabase\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GTlsDatabase (1845531968)>'
    __info__ = ObjectInfo(TlsDatabase)


