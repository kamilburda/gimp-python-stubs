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


from .StyleProvider import StyleProvider

class Settings(__gi_overrides_GObject.Object, StyleProvider):
    """
    :Constructors:
    
    ::
    
        Settings(**properties)
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

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> Gtk.Settings or None """
        pass

    def get_for_screen(self, screen): # real signature unknown; restored from __doc__
        """ get_for_screen(screen:Gdk.Screen) -> Gtk.Settings """
        pass

    def get_icon_factory(self, path): # real signature unknown; restored from __doc__
        """ get_icon_factory(self, path:Gtk.WidgetPath) -> Gtk.IconFactory or None """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_style(self, path): # real signature unknown; restored from __doc__
        """ get_style(self, path:Gtk.WidgetPath) -> Gtk.StyleProperties or None """
        pass

    def get_style_property(self, path, state, pspec): # real signature unknown; restored from __doc__
        """ get_style_property(self, path:Gtk.WidgetPath, state:Gtk.StateFlags, pspec:GObject.ParamSpec) -> bool, value:GObject.Value """
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

    def install_property(self, pspec): # real signature unknown; restored from __doc__
        """ install_property(pspec:GObject.ParamSpec) """
        pass

    def install_property_parser(self, pspec, parser): # real signature unknown; restored from __doc__
        """ install_property_parser(pspec:GObject.ParamSpec, parser:Gtk.RcPropertyParser) """
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

    def reset_property(self, name): # real signature unknown; restored from __doc__
        """ reset_property(self, name:str) """
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_double_property(self, name, v_double, origin): # real signature unknown; restored from __doc__
        """ set_double_property(self, name:str, v_double:float, origin:str) """
        pass

    def set_long_property(self, name, v_long, origin): # real signature unknown; restored from __doc__
        """ set_long_property(self, name:str, v_long:int, origin:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_property_value(self, name, svalue): # real signature unknown; restored from __doc__
        """ set_property_value(self, name:str, svalue:Gtk.SettingsValue) """
        pass

    def set_string_property(self, name, v_string, origin): # real signature unknown; restored from __doc__
        """ set_string_property(self, name:str, v_string:str, origin:str) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002bfd19094b0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Settings), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkSettings (3540065440)>, '__doc__': None, '__gsignals__': {}, 'get_default': <staticmethod(gi.FunctionInfo(get_default))>, 'get_for_screen': <staticmethod(gi.FunctionInfo(get_for_screen))>, 'install_property': <staticmethod(gi.FunctionInfo(install_property))>, 'install_property_parser': <staticmethod(gi.FunctionInfo(install_property_parser))>, 'reset_property': gi.FunctionInfo(reset_property), 'set_double_property': gi.FunctionInfo(set_double_property), 'set_long_property': gi.FunctionInfo(set_long_property), 'set_property_value': gi.FunctionInfo(set_property_value), 'set_string_property': gi.FunctionInfo(set_string_property), 'parent_instance': <property object at 0x000002bfd1931da0>, 'priv': <property object at 0x000002bfd1931ee0>})"
    __firstlineno__ = 651
    __gdoc__ = "Object GtkSettings\n\nProperties from GtkSettings:\n  gtk-double-click-time -> gint: Double Click Time\n    Maximum time allowed between two clicks for them to be considered a double click (in milliseconds)\n  gtk-double-click-distance -> gint: Double Click Distance\n    Maximum distance allowed between two clicks for them to be considered a double click (in pixels)\n  gtk-cursor-blink -> gboolean: Cursor Blink\n    Whether the cursor should blink\n  gtk-cursor-blink-time -> gint: Cursor Blink Time\n    Length of the cursor blink cycle, in milliseconds\n  gtk-cursor-blink-timeout -> gint: Cursor Blink Timeout\n    Time after which the cursor stops blinking, in seconds\n  gtk-split-cursor -> gboolean: Split Cursor\n    Whether two cursors should be displayed for mixed left-to-right and right-to-left text\n  gtk-cursor-aspect-ratio -> gfloat: Cursor Aspect Ratio\n    The aspect ratio of the text caret\n  gtk-theme-name -> gchararray: Theme Name\n    Name of theme to load\n  gtk-icon-theme-name -> gchararray: Icon Theme Name\n    Name of icon theme to use\n  gtk-fallback-icon-theme -> gchararray: Fallback Icon Theme Name\n    Name of a icon theme to fall back to\n  gtk-key-theme-name -> gchararray: Key Theme Name\n    Name of key theme to load\n  gtk-menu-bar-accel -> gchararray: Menu bar accelerator\n    Keybinding to activate the menu bar\n  gtk-dnd-drag-threshold -> gint: Drag threshold\n    Number of pixels the cursor can move before dragging\n  gtk-font-name -> gchararray: Font Name\n    The default font family and size to use\n  gtk-icon-sizes -> gchararray: Icon Sizes\n    List of icon sizes (gtk-menu=16,16:gtk-button=20,20...\n  gtk-modules -> gchararray: GTK Modules\n    List of currently active GTK modules\n  gtk-xft-antialias -> gint: Xft Antialias\n    Whether to antialias Xft fonts; 0=no, 1=yes, -1=default\n  gtk-xft-hinting -> gint: Xft Hinting\n    Whether to hint Xft fonts; 0=no, 1=yes, -1=default\n  gtk-xft-hintstyle -> gchararray: Xft Hint Style\n    What degree of hinting to use; hintnone, hintslight, hintmedium, or hintfull\n  gtk-xft-rgba -> gchararray: Xft RGBA\n    Type of subpixel antialiasing; none, rgb, bgr, vrgb, vbgr\n  gtk-xft-dpi -> gint: Xft DPI\n    Resolution for Xft, in 1024 * dots/inch. -1 to use default value\n  gtk-cursor-theme-name -> gchararray: Cursor theme name\n    Name of the cursor theme to use, or NULL to use the default theme\n  gtk-cursor-theme-size -> gint: Cursor theme size\n    Size to use for cursors, or 0 to use the default size\n  gtk-alternative-button-order -> gboolean: Alternative button order\n    Whether buttons in dialogs should use the alternative button order\n  gtk-alternative-sort-arrows -> gboolean: Alternative sort indicator direction\n    Whether the direction of the sort indicators in list and tree views is inverted compared to the default (where down means ascending)\n  gtk-show-input-method-menu -> gboolean: Show the 'Input Methods' menu\n    Whether the context menus of entries and text views should offer to change the input method\n  gtk-show-unicode-menu -> gboolean: Show the 'Insert Unicode Control Character' menu\n    Whether the context menus of entries and text views should offer to insert control characters\n  gtk-timeout-initial -> gint: Start timeout\n    Starting value for timeouts, when button is pressed\n  gtk-timeout-repeat -> gint: Repeat timeout\n    Repeat value for timeouts, when button is pressed\n  gtk-timeout-expand -> gint: Expand timeout\n    Expand value for timeouts, when a widget is expanding a new region\n  gtk-color-scheme -> gchararray: Color scheme\n    A palette of named colors for use in themes\n  gtk-enable-animations -> gboolean: Enable Animations\n    Whether to enable toolkit-wide animations.\n  gtk-touchscreen-mode -> gboolean: Enable Touchscreen Mode\n    When TRUE, there are no motion notify events delivered on this screen\n  gtk-tooltip-timeout -> gint: Tooltip timeout\n    Timeout before tooltip is shown\n  gtk-tooltip-browse-timeout -> gint: Tooltip browse timeout\n    Timeout before tooltip is shown when browse mode is enabled\n  gtk-tooltip-browse-mode-timeout -> gint: Tooltip browse mode timeout\n    Timeout after which browse mode is disabled\n  gtk-keynav-cursor-only -> gboolean: Keynav Cursor Only\n    When TRUE, there are only cursor keys available to navigate widgets\n  gtk-keynav-wrap-around -> gboolean: Keynav Wrap Around\n    Whether to wrap around when keyboard-navigating widgets\n  gtk-error-bell -> gboolean: Error Bell\n    When TRUE, keyboard navigation and other errors will cause a beep\n  color-hash -> GHashTable: Color Hash\n    A hash table representation of the color scheme.\n  gtk-file-chooser-backend -> gchararray: Default file chooser backend\n    Name of the GtkFileChooser backend to use by default\n  gtk-print-backends -> gchararray: Default print backend\n    List of the GtkPrintBackend backends to use by default\n  gtk-print-preview-command -> gchararray: Default command to run when displaying a print preview\n    Command to run when displaying a print preview\n  gtk-enable-mnemonics -> gboolean: Enable Mnemonics\n    Whether labels should have mnemonics\n  gtk-enable-accels -> gboolean: Enable Accelerators\n    Whether menu items should have accelerators\n  gtk-recent-files-limit -> gint: Recent Files Limit\n    Number of recently used files\n  gtk-im-module -> gchararray: Default IM module\n    Which IM module should be used by default\n  gtk-recent-files-max-age -> gint: Recent Files Max Age\n    Maximum age of recently used files, in days\n  gtk-fontconfig-timestamp -> guint: Fontconfig configuration timestamp\n    Timestamp of current fontconfig configuration\n  gtk-sound-theme-name -> gchararray: Sound Theme Name\n    XDG sound theme name\n  gtk-enable-input-feedback-sounds -> gboolean: Audible Input Feedback\n    Whether to play event sounds as feedback to user input\n  gtk-enable-event-sounds -> gboolean: Enable Event Sounds\n    Whether to play any event sounds at all\n  gtk-enable-tooltips -> gboolean: Enable Tooltips\n    Whether tooltips should be shown on widgets\n  gtk-toolbar-style -> GtkToolbarStyle: Toolbar style\n    Whether default toolbars have text only, text and icons, icons only, etc.\n  gtk-toolbar-icon-size -> GtkIconSize: Toolbar Icon Size\n    The size of icons in default toolbars.\n  gtk-auto-mnemonics -> gboolean: Auto Mnemonics\n    Whether mnemonics should be automatically shown and hidden when the user presses the mnemonic activator.\n  gtk-primary-button-warps-slider -> gboolean: Primary button warps slider\n    Whether a primary click on the trough should warp the slider into position\n  gtk-visible-focus -> GtkPolicyType: Visible Focus\n    Whether 'focus rectangles' should be hidden until the user starts to use the keyboard.\n  gtk-application-prefer-dark-theme -> gboolean: Application prefers a dark theme\n    Whether the application prefers to have a dark theme.\n  gtk-button-images -> gboolean: Show button images\n    Whether images should be shown on buttons\n  gtk-entry-select-on-focus -> gboolean: Select on focus\n    Whether to select the contents of an entry when it is focused\n  gtk-entry-password-hint-timeout -> guint: Password Hint Timeout\n    How long to show the last input character in hidden entries\n  gtk-menu-images -> gboolean: Show menu images\n    Whether images should be shown in menus\n  gtk-menu-bar-popup-delay -> gint: Delay before drop down menus appear\n    Delay before the submenus of a menu bar appear\n  gtk-scrolled-window-placement -> GtkCornerType: Scrolled Window Placement\n    Where the contents of scrolled windows are located with respect to the scrollbars, if not overridden by the scrolled window's own placement.\n  gtk-can-change-accels -> gboolean: Can change accelerators\n    Whether menu accelerators can be changed by pressing a key over the menu item\n  gtk-menu-popup-delay -> gint: Delay before submenus appear\n    Minimum time the pointer must stay over a menu item before the submenu appear\n  gtk-menu-popdown-delay -> gint: Delay before hiding a submenu\n    The time before hiding a submenu when the pointer is moving towards the submenu\n  gtk-label-select-on-focus -> gboolean: Select on focus\n    Whether to select the contents of a selectable label when it is focused\n  gtk-color-palette -> gchararray: Custom palette\n    Palette to use in the color selector\n  gtk-im-preedit-style -> GtkIMPreeditStyle: IM Preedit style\n    How to draw the input method preedit string\n  gtk-im-status-style -> GtkIMStatusStyle: IM Status style\n    How to draw the input method statusbar\n  gtk-shell-shows-app-menu -> gboolean: Desktop shell shows app menu\n    Set to TRUE if the desktop environment is displaying the app menu, FALSE if the app should display it itself.\n  gtk-shell-shows-menubar -> gboolean: Desktop shell shows the menubar\n    Set to TRUE if the desktop environment is displaying the menubar, FALSE if the app should display it itself.\n  gtk-shell-shows-desktop -> gboolean: Desktop environment shows the desktop folder\n    Set to TRUE if the desktop environment is displaying the desktop folder, FALSE if not.\n  gtk-decoration-layout -> gchararray: Decoration Layout\n    The layout for window decorations\n  gtk-titlebar-double-click -> gchararray: Titlebar double-click action\n    The action to take on titlebar double-click\n  gtk-titlebar-middle-click -> gchararray: Titlebar middle-click action\n    The action to take on titlebar middle-click\n  gtk-titlebar-right-click -> gchararray: Titlebar right-click action\n    The action to take on titlebar right-click\n  gtk-dialogs-use-header -> gboolean: Dialogs use header bar\n    Whether builtin GTK+ dialogs should use a header bar instead of an action area.\n  gtk-enable-primary-paste -> gboolean: Enable primary paste\n    Whether a middle click on a mouse should paste the 'PRIMARY' clipboard content at the cursor location.\n  gtk-recent-files-enabled -> gboolean: Recent Files Enabled\n    Whether GTK+ remembers recent files\n  gtk-long-press-time -> guint: Long press time\n    Time for a button/touch press to be considered a long press (in milliseconds)\n  gtk-keynav-use-caret -> gboolean: Whether to show cursor in text\n    Whether to show cursor in text\n  gtk-overlay-scrolling -> gboolean: Whether to use overlay scrollbars\n    Whether to use overlay scrollbars\n\nSignals from GtkStyleProviderPrivate:\n  -gtk-private-changed ()\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkSettings (3540065440)>'
    __info__ = ObjectInfo(Settings)
    __static_attributes__ = ()


