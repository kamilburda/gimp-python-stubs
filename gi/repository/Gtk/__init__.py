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


# Variables with simple values

BINARY_AGE = 2451

INPUT_ERROR = -1

INTERFACE_AGE = 32

LEVEL_BAR_OFFSET_FULL = 'full'
LEVEL_BAR_OFFSET_HIGH = 'high'
LEVEL_BAR_OFFSET_LOW = 'low'

MAJOR_VERSION = 3

MAX_COMPOSE_LEN = 7

MICRO_VERSION = 51

MINOR_VERSION = 24

PAPER_NAME_A3 = 'iso_a3'
PAPER_NAME_A4 = 'iso_a4'
PAPER_NAME_A5 = 'iso_a5'
PAPER_NAME_B5 = 'iso_b5'
PAPER_NAME_EXECUTIVE = 'na_executive'
PAPER_NAME_LEGAL = 'na_legal'
PAPER_NAME_LETTER = 'na_letter'

PATH_PRIO_MASK = 15

PRINT_SETTINGS_COLLATE = 'collate'

PRINT_SETTINGS_DEFAULT_SOURCE = 'default-source'

PRINT_SETTINGS_DITHER = 'dither'
PRINT_SETTINGS_DUPLEX = 'duplex'
PRINT_SETTINGS_FINISHINGS = 'finishings'

PRINT_SETTINGS_MEDIA_TYPE = 'media-type'

PRINT_SETTINGS_NUMBER_UP = 'number-up'

PRINT_SETTINGS_NUMBER_UP_LAYOUT = 'number-up-layout'

PRINT_SETTINGS_N_COPIES = 'n-copies'

PRINT_SETTINGS_ORIENTATION = 'orientation'

PRINT_SETTINGS_OUTPUT_BASENAME = 'output-basename'
PRINT_SETTINGS_OUTPUT_BIN = 'output-bin'
PRINT_SETTINGS_OUTPUT_DIR = 'output-dir'

PRINT_SETTINGS_OUTPUT_FILE_FORMAT = 'output-file-format'

PRINT_SETTINGS_OUTPUT_URI = 'output-uri'

PRINT_SETTINGS_PAGE_RANGES = 'page-ranges'
PRINT_SETTINGS_PAGE_SET = 'page-set'

PRINT_SETTINGS_PAPER_FORMAT = 'paper-format'
PRINT_SETTINGS_PAPER_HEIGHT = 'paper-height'
PRINT_SETTINGS_PAPER_WIDTH = 'paper-width'

PRINT_SETTINGS_PRINTER = 'printer'

PRINT_SETTINGS_PRINTER_LPI = 'printer-lpi'

PRINT_SETTINGS_PRINT_PAGES = 'print-pages'

PRINT_SETTINGS_QUALITY = 'quality'
PRINT_SETTINGS_RESOLUTION = 'resolution'

PRINT_SETTINGS_RESOLUTION_X = 'resolution-x'
PRINT_SETTINGS_RESOLUTION_Y = 'resolution-y'

PRINT_SETTINGS_REVERSE = 'reverse'
PRINT_SETTINGS_SCALE = 'scale'

PRINT_SETTINGS_USE_COLOR = 'use-color'

PRINT_SETTINGS_WIN32_DRIVER_EXTRA = 'win32-driver-extra'
PRINT_SETTINGS_WIN32_DRIVER_VERSION = 'win32-driver-version'

PRIORITY_RESIZE = 110

STOCK_ABOUT = 'gtk-about'
STOCK_ADD = 'gtk-add'
STOCK_APPLY = 'gtk-apply'
STOCK_BOLD = 'gtk-bold'
STOCK_CANCEL = 'gtk-cancel'

STOCK_CAPS_LOCK_WARNING = 'gtk-caps-lock-warning'

STOCK_CDROM = 'gtk-cdrom'
STOCK_CLEAR = 'gtk-clear'
STOCK_CLOSE = 'gtk-close'

STOCK_COLOR_PICKER = 'gtk-color-picker'

STOCK_CONNECT = 'gtk-connect'
STOCK_CONVERT = 'gtk-convert'
STOCK_COPY = 'gtk-copy'
STOCK_CUT = 'gtk-cut'
STOCK_DELETE = 'gtk-delete'

STOCK_DIALOG_AUTHENTICATION = 'gtk-dialog-authentication'
STOCK_DIALOG_ERROR = 'gtk-dialog-error'
STOCK_DIALOG_INFO = 'gtk-dialog-info'
STOCK_DIALOG_QUESTION = 'gtk-dialog-question'
STOCK_DIALOG_WARNING = 'gtk-dialog-warning'

STOCK_DIRECTORY = 'gtk-directory'
STOCK_DISCARD = 'gtk-discard'
STOCK_DISCONNECT = 'gtk-disconnect'
STOCK_DND = 'gtk-dnd'

STOCK_DND_MULTIPLE = 'gtk-dnd-multiple'

STOCK_EDIT = 'gtk-edit'
STOCK_EXECUTE = 'gtk-execute'
STOCK_FILE = 'gtk-file'
STOCK_FIND = 'gtk-find'

STOCK_FIND_AND_REPLACE = 'gtk-find-and-replace'

STOCK_FLOPPY = 'gtk-floppy'
STOCK_FULLSCREEN = 'gtk-fullscreen'

STOCK_GOTO_BOTTOM = 'gtk-goto-bottom'
STOCK_GOTO_FIRST = 'gtk-goto-first'
STOCK_GOTO_LAST = 'gtk-goto-last'
STOCK_GOTO_TOP = 'gtk-goto-top'

STOCK_GO_BACK = 'gtk-go-back'
STOCK_GO_DOWN = 'gtk-go-down'
STOCK_GO_FORWARD = 'gtk-go-forward'
STOCK_GO_UP = 'gtk-go-up'

STOCK_HARDDISK = 'gtk-harddisk'
STOCK_HELP = 'gtk-help'
STOCK_HOME = 'gtk-home'
STOCK_INDENT = 'gtk-indent'
STOCK_INDEX = 'gtk-index'
STOCK_INFO = 'gtk-info'
STOCK_ITALIC = 'gtk-italic'

STOCK_JUMP_TO = 'gtk-jump-to'

STOCK_JUSTIFY_CENTER = 'gtk-justify-center'
STOCK_JUSTIFY_FILL = 'gtk-justify-fill'
STOCK_JUSTIFY_LEFT = 'gtk-justify-left'
STOCK_JUSTIFY_RIGHT = 'gtk-justify-right'

STOCK_LEAVE_FULLSCREEN = 'gtk-leave-fullscreen'

STOCK_MEDIA_FORWARD = 'gtk-media-forward'
STOCK_MEDIA_NEXT = 'gtk-media-next'
STOCK_MEDIA_PAUSE = 'gtk-media-pause'
STOCK_MEDIA_PLAY = 'gtk-media-play'
STOCK_MEDIA_PREVIOUS = 'gtk-media-previous'
STOCK_MEDIA_RECORD = 'gtk-media-record'
STOCK_MEDIA_REWIND = 'gtk-media-rewind'
STOCK_MEDIA_STOP = 'gtk-media-stop'

STOCK_MISSING_IMAGE = 'gtk-missing-image'

STOCK_NETWORK = 'gtk-network'
STOCK_NEW = 'gtk-new'
STOCK_NO = 'gtk-no'
STOCK_OK = 'gtk-ok'
STOCK_OPEN = 'gtk-open'

STOCK_ORIENTATION_LANDSCAPE = 'gtk-orientation-landscape'
STOCK_ORIENTATION_PORTRAIT = 'gtk-orientation-portrait'

STOCK_ORIENTATION_REVERSE_LANDSCAPE = 'gtk-orientation-reverse-landscape'
STOCK_ORIENTATION_REVERSE_PORTRAIT = 'gtk-orientation-reverse-portrait'

STOCK_PAGE_SETUP = 'gtk-page-setup'

STOCK_PASTE = 'gtk-paste'
STOCK_PREFERENCES = 'gtk-preferences'
STOCK_PRINT = 'gtk-print'

STOCK_PRINT_ERROR = 'gtk-print-error'
STOCK_PRINT_PAUSED = 'gtk-print-paused'
STOCK_PRINT_PREVIEW = 'gtk-print-preview'
STOCK_PRINT_REPORT = 'gtk-print-report'
STOCK_PRINT_WARNING = 'gtk-print-warning'

STOCK_PROPERTIES = 'gtk-properties'
STOCK_QUIT = 'gtk-quit'
STOCK_REDO = 'gtk-redo'
STOCK_REFRESH = 'gtk-refresh'
STOCK_REMOVE = 'gtk-remove'

STOCK_REVERT_TO_SAVED = 'gtk-revert-to-saved'

STOCK_SAVE = 'gtk-save'

STOCK_SAVE_AS = 'gtk-save-as'

STOCK_SELECT_ALL = 'gtk-select-all'
STOCK_SELECT_COLOR = 'gtk-select-color'
STOCK_SELECT_FONT = 'gtk-select-font'

STOCK_SORT_ASCENDING = 'gtk-sort-ascending'
STOCK_SORT_DESCENDING = 'gtk-sort-descending'

STOCK_SPELL_CHECK = 'gtk-spell-check'

STOCK_STOP = 'gtk-stop'
STOCK_STRIKETHROUGH = 'gtk-strikethrough'
STOCK_UNDELETE = 'gtk-undelete'
STOCK_UNDERLINE = 'gtk-underline'
STOCK_UNDO = 'gtk-undo'
STOCK_UNINDENT = 'gtk-unindent'
STOCK_YES = 'gtk-yes'

STOCK_ZOOM_100 = 'gtk-zoom-100'
STOCK_ZOOM_FIT = 'gtk-zoom-fit'
STOCK_ZOOM_IN = 'gtk-zoom-in'
STOCK_ZOOM_OUT = 'gtk-zoom-out'

STYLE_CLASS_ACCELERATOR = 'accelerator'
STYLE_CLASS_ARROW = 'arrow'
STYLE_CLASS_BACKGROUND = 'background'
STYLE_CLASS_BOTTOM = 'bottom'
STYLE_CLASS_BUTTON = 'button'
STYLE_CLASS_CALENDAR = 'calendar'
STYLE_CLASS_CELL = 'cell'
STYLE_CLASS_CHECK = 'check'

STYLE_CLASS_COMBOBOX_ENTRY = 'combobox-entry'

STYLE_CLASS_CONTEXT_MENU = 'context-menu'

STYLE_CLASS_CSD = 'csd'

STYLE_CLASS_CURSOR_HANDLE = 'cursor-handle'

STYLE_CLASS_DEFAULT = 'default'

STYLE_CLASS_DESTRUCTIVE_ACTION = 'destructive-action'

STYLE_CLASS_DIM_LABEL = 'dim-label'

STYLE_CLASS_DND = 'dnd'
STYLE_CLASS_DOCK = 'dock'
STYLE_CLASS_ENTRY = 'entry'
STYLE_CLASS_ERROR = 'error'
STYLE_CLASS_EXPANDER = 'expander'
STYLE_CLASS_FLAT = 'flat'
STYLE_CLASS_FRAME = 'frame'
STYLE_CLASS_GRIP = 'grip'
STYLE_CLASS_HEADER = 'header'
STYLE_CLASS_HIGHLIGHT = 'highlight'
STYLE_CLASS_HORIZONTAL = 'horizontal'
STYLE_CLASS_IMAGE = 'image'
STYLE_CLASS_INFO = 'info'

STYLE_CLASS_INLINE_TOOLBAR = 'inline-toolbar'

STYLE_CLASS_INSERTION_CURSOR = 'insertion-cursor'

STYLE_CLASS_LABEL = 'label'
STYLE_CLASS_LEFT = 'left'

STYLE_CLASS_LEVEL_BAR = 'level-bar'

STYLE_CLASS_LINKED = 'linked'
STYLE_CLASS_LIST = 'list'

STYLE_CLASS_LIST_ROW = 'list-row'

STYLE_CLASS_MARK = 'mark'
STYLE_CLASS_MENU = 'menu'
STYLE_CLASS_MENUBAR = 'menubar'
STYLE_CLASS_MENUITEM = 'menuitem'

STYLE_CLASS_MESSAGE_DIALOG = 'message-dialog'

STYLE_CLASS_MONOSPACE = 'monospace'

STYLE_CLASS_NEEDS_ATTENTION = 'needs-attention'

STYLE_CLASS_NOTEBOOK = 'notebook'
STYLE_CLASS_OSD = 'osd'
STYLE_CLASS_OVERSHOOT = 'overshoot'

STYLE_CLASS_PANE_SEPARATOR = 'pane-separator'

STYLE_CLASS_PAPER = 'paper'
STYLE_CLASS_POPOVER = 'popover'
STYLE_CLASS_POPUP = 'popup'

STYLE_CLASS_PRIMARY_TOOLBAR = 'primary-toolbar'

STYLE_CLASS_PROGRESSBAR = 'progressbar'
STYLE_CLASS_PULSE = 'pulse'
STYLE_CLASS_QUESTION = 'question'
STYLE_CLASS_RADIO = 'radio'
STYLE_CLASS_RAISED = 'raised'

STYLE_CLASS_READ_ONLY = 'read-only'

STYLE_CLASS_RIGHT = 'right'
STYLE_CLASS_RUBBERBAND = 'rubberband'
STYLE_CLASS_SCALE = 'scale'

STYLE_CLASS_SCALE_HAS_MARKS_ABOVE = 'scale-has-marks-above'
STYLE_CLASS_SCALE_HAS_MARKS_BELOW = 'scale-has-marks-below'

STYLE_CLASS_SCROLLBAR = 'scrollbar'

STYLE_CLASS_SCROLLBARS_JUNCTION = 'scrollbars-junction'

STYLE_CLASS_SEPARATOR = 'separator'
STYLE_CLASS_SIDEBAR = 'sidebar'
STYLE_CLASS_SLIDER = 'slider'
STYLE_CLASS_SPINBUTTON = 'spinbutton'
STYLE_CLASS_SPINNER = 'spinner'
STYLE_CLASS_STATUSBAR = 'statusbar'
STYLE_CLASS_SUBTITLE = 'subtitle'

STYLE_CLASS_SUGGESTED_ACTION = 'suggested-action'

STYLE_CLASS_TITLE = 'title'
STYLE_CLASS_TITLEBAR = 'titlebar'
STYLE_CLASS_TOOLBAR = 'toolbar'
STYLE_CLASS_TOOLTIP = 'tooltip'
STYLE_CLASS_TOP = 'top'

STYLE_CLASS_TOUCH_SELECTION = 'touch-selection'

STYLE_CLASS_TROUGH = 'trough'
STYLE_CLASS_UNDERSHOOT = 'undershoot'
STYLE_CLASS_VERTICAL = 'vertical'
STYLE_CLASS_VIEW = 'view'
STYLE_CLASS_WARNING = 'warning'
STYLE_CLASS_WIDE = 'wide'

STYLE_PROPERTY_BACKGROUND_COLOR = 'background-color'
STYLE_PROPERTY_BACKGROUND_IMAGE = 'background-image'

STYLE_PROPERTY_BORDER_COLOR = 'border-color'
STYLE_PROPERTY_BORDER_RADIUS = 'border-radius'
STYLE_PROPERTY_BORDER_STYLE = 'border-style'
STYLE_PROPERTY_BORDER_WIDTH = 'border-width'

STYLE_PROPERTY_COLOR = 'color'
STYLE_PROPERTY_FONT = 'font'
STYLE_PROPERTY_MARGIN = 'margin'
STYLE_PROPERTY_PADDING = 'padding'

STYLE_PROVIDER_PRIORITY_APPLICATION = 600
STYLE_PROVIDER_PRIORITY_FALLBACK = 1
STYLE_PROVIDER_PRIORITY_SETTINGS = 400
STYLE_PROVIDER_PRIORITY_THEME = 200
STYLE_PROVIDER_PRIORITY_USER = 800

STYLE_REGION_COLUMN = 'column'

STYLE_REGION_COLUMN_HEADER = 'column-header'

STYLE_REGION_ROW = 'row'
STYLE_REGION_TAB = 'tab'

TEXT_VIEW_PRIORITY_VALIDATE = 125

TREE_SORTABLE_DEFAULT_SORT_COLUMN_ID = -1

TREE_SORTABLE_UNSORTED_SORT_COLUMN_ID = -2

_namespace = 'Gtk'

_version = '3.0'

# functions

def accelerator_get_default_mod_mask(): # real signature unknown; restored from __doc__
    """ accelerator_get_default_mod_mask() -> Gdk.ModifierType """
    pass

def accelerator_get_label(accelerator_key, accelerator_mods): # real signature unknown; restored from __doc__
    """ accelerator_get_label(accelerator_key:int, accelerator_mods:Gdk.ModifierType) -> str """
    return ""

def accelerator_get_label_with_keycode(display=None, accelerator_key, keycode, accelerator_mods): # real signature unknown; restored from __doc__
    """ accelerator_get_label_with_keycode(display:Gdk.Display=None, accelerator_key:int, keycode:int, accelerator_mods:Gdk.ModifierType) -> str """
    return ""

def accelerator_name(accelerator_key, accelerator_mods): # real signature unknown; restored from __doc__
    """ accelerator_name(accelerator_key:int, accelerator_mods:Gdk.ModifierType) -> str """
    return ""

def accelerator_name_with_keycode(display=None, accelerator_key, keycode, accelerator_mods): # real signature unknown; restored from __doc__
    """ accelerator_name_with_keycode(display:Gdk.Display=None, accelerator_key:int, keycode:int, accelerator_mods:Gdk.ModifierType) -> str """
    return ""

def accelerator_parse(accelerator): # real signature unknown; restored from __doc__
    """ accelerator_parse(accelerator:str) -> accelerator_key:int, accelerator_mods:Gdk.ModifierType """
    pass

def accelerator_parse_with_keycode(accelerator): # real signature unknown; restored from __doc__
    """ accelerator_parse_with_keycode(accelerator:str) -> accelerator_key:int, accelerator_codes:list, accelerator_mods:Gdk.ModifierType """
    pass

def accelerator_set_default_mod_mask(default_mod_mask): # real signature unknown; restored from __doc__
    """ accelerator_set_default_mod_mask(default_mod_mask:Gdk.ModifierType) """
    pass

def accelerator_valid(keyval, modifiers): # real signature unknown; restored from __doc__
    """ accelerator_valid(keyval:int, modifiers:Gdk.ModifierType) -> bool """
    return False

def accel_groups_activate(p_object, accel_key, accel_mods): # real signature unknown; restored from __doc__
    """ accel_groups_activate(object:GObject.Object, accel_key:int, accel_mods:Gdk.ModifierType) -> bool """
    return False

def accel_groups_from_object(p_object): # real signature unknown; restored from __doc__
    """ accel_groups_from_object(object:GObject.Object) -> list """
    return []

def alternative_dialog_button_order(screen=None): # real signature unknown; restored from __doc__
    """ alternative_dialog_button_order(screen:Gdk.Screen=None) -> bool """
    return False

def bindings_activate(p_object, keyval, modifiers): # real signature unknown; restored from __doc__
    """ bindings_activate(object:GObject.Object, keyval:int, modifiers:Gdk.ModifierType) -> bool """
    return False

def bindings_activate_event(p_object, event): # real signature unknown; restored from __doc__
    """ bindings_activate_event(object:GObject.Object, event:Gdk.EventKey) -> bool """
    return False

def binding_entry_add_signall(binding_set, keyval, modifiers, signal_name, binding_args): # real signature unknown; restored from __doc__
    """ binding_entry_add_signall(binding_set:Gtk.BindingSet, keyval:int, modifiers:Gdk.ModifierType, signal_name:str, binding_args:list) """
    pass

def binding_entry_add_signal_from_string(binding_set, signal_desc): # real signature unknown; restored from __doc__
    """ binding_entry_add_signal_from_string(binding_set:Gtk.BindingSet, signal_desc:str) -> GLib.TokenType """
    pass

def binding_entry_remove(binding_set, keyval, modifiers): # real signature unknown; restored from __doc__
    """ binding_entry_remove(binding_set:Gtk.BindingSet, keyval:int, modifiers:Gdk.ModifierType) """
    pass

def binding_entry_skip(binding_set, keyval, modifiers): # real signature unknown; restored from __doc__
    """ binding_entry_skip(binding_set:Gtk.BindingSet, keyval:int, modifiers:Gdk.ModifierType) """
    pass

def binding_set_find(set_name): # real signature unknown; restored from __doc__
    """ binding_set_find(set_name:str) -> Gtk.BindingSet or None """
    pass

def builder_error_quark(): # real signature unknown; restored from __doc__
    """ builder_error_quark() -> int """
    return 0

def cairo_should_draw_window(cr, window): # real signature unknown; restored from __doc__
    """ cairo_should_draw_window(cr:cairo.Context, window:Gdk.Window) -> bool """
    return False

def cairo_transform_to_window(cr, widget, window): # real signature unknown; restored from __doc__
    """ cairo_transform_to_window(cr:cairo.Context, widget:Gtk.Widget, window:Gdk.Window) """
    pass

def check_version(required_major, required_minor, required_micro): # real signature unknown; restored from __doc__
    """ check_version(required_major:int, required_minor:int, required_micro:int) -> str or None """
    return ""

def css_provider_error_quark(): # real signature unknown; restored from __doc__
    """ css_provider_error_quark() -> int """
    return 0

def device_grab_add(widget, device, block_others): # real signature unknown; restored from __doc__
    """ device_grab_add(widget:Gtk.Widget, device:Gdk.Device, block_others:bool) """
    pass

def device_grab_remove(widget, device): # real signature unknown; restored from __doc__
    """ device_grab_remove(widget:Gtk.Widget, device:Gdk.Device) """
    pass

def disable_setlocale(): # real signature unknown; restored from __doc__
    """ disable_setlocale() """
    pass

def distribute_natural_allocation(extra_space, n_requested_sizes, sizes): # real signature unknown; restored from __doc__
    """ distribute_natural_allocation(extra_space:int, n_requested_sizes:int, sizes:Gtk.RequestedSize) -> int """
    return 0

def drag_cancel(context): # real signature unknown; restored from __doc__
    """ drag_cancel(context:Gdk.DragContext) """
    pass

def drag_finish(context, success, del_, time_): # real signature unknown; restored from __doc__
    """ drag_finish(context:Gdk.DragContext, success:bool, del_:bool, time_:int) """
    pass

def drag_get_source_widget(context): # real signature unknown; restored from __doc__
    """ drag_get_source_widget(context:Gdk.DragContext) -> Gtk.Widget or None """
    pass

def drag_set_icon_default(context): # real signature unknown; restored from __doc__
    """ drag_set_icon_default(context:Gdk.DragContext) """
    pass

def drag_set_icon_gicon(context, icon, hot_x, hot_y): # real signature unknown; restored from __doc__
    """ drag_set_icon_gicon(context:Gdk.DragContext, icon:Gio.Icon, hot_x:int, hot_y:int) """
    pass

def drag_set_icon_name(context, icon_name, hot_x, hot_y): # real signature unknown; restored from __doc__
    """ drag_set_icon_name(context:Gdk.DragContext, icon_name:str, hot_x:int, hot_y:int) """
    pass

def drag_set_icon_pixbuf(context, pixbuf, hot_x, hot_y): # real signature unknown; restored from __doc__
    """ drag_set_icon_pixbuf(context:Gdk.DragContext, pixbuf:GdkPixbuf.Pixbuf, hot_x:int, hot_y:int) """
    pass

def drag_set_icon_stock(context, stock_id, hot_x, hot_y): # real signature unknown; restored from __doc__
    """ drag_set_icon_stock(context:Gdk.DragContext, stock_id:str, hot_x:int, hot_y:int) """
    pass

def drag_set_icon_surface(context, surface): # real signature unknown; restored from __doc__
    """ drag_set_icon_surface(context:Gdk.DragContext, surface:cairo.Surface) """
    pass

def drag_set_icon_widget(context, widget, hot_x, hot_y): # real signature unknown; restored from __doc__
    """ drag_set_icon_widget(context:Gdk.DragContext, widget:Gtk.Widget, hot_x:int, hot_y:int) """
    pass

def draw_insertion_cursor(widget, cr, location, is_primary, direction, draw_arrow): # real signature unknown; restored from __doc__
    """ draw_insertion_cursor(widget:Gtk.Widget, cr:cairo.Context, location:Gdk.Rectangle, is_primary:bool, direction:Gtk.TextDirection, draw_arrow:bool) """
    pass

def events_pending(): # real signature unknown; restored from __doc__
    """ events_pending() -> bool """
    return False

def false(): # real signature unknown; restored from __doc__
    """ false() -> bool """
    return False

def file_chooser_error_quark(): # real signature unknown; restored from __doc__
    """ file_chooser_error_quark() -> int """
    return 0

def get_binary_age(): # real signature unknown; restored from __doc__
    """ get_binary_age() -> int """
    return 0

def get_current_event(): # real signature unknown; restored from __doc__
    """ get_current_event() -> Gdk.Event or None """
    pass

def get_current_event_device(): # real signature unknown; restored from __doc__
    """ get_current_event_device() -> Gdk.Device or None """
    pass

def get_current_event_state(): # real signature unknown; restored from __doc__
    """ get_current_event_state() -> bool, state:Gdk.ModifierType """
    return False

def get_current_event_time(): # real signature unknown; restored from __doc__
    """ get_current_event_time() -> int """
    return 0

def get_debug_flags(): # real signature unknown; restored from __doc__
    """ get_debug_flags() -> int """
    return 0

def get_default_language(): # real signature unknown; restored from __doc__
    """ get_default_language() -> Pango.Language """
    pass

def get_event_widget(event): # real signature unknown; restored from __doc__
    """ get_event_widget(event:Gdk.Event) -> Gtk.Widget or None """
    pass

def get_interface_age(): # real signature unknown; restored from __doc__
    """ get_interface_age() -> int """
    return 0

def get_locale_direction(): # real signature unknown; restored from __doc__
    """ get_locale_direction() -> Gtk.TextDirection """
    pass

def get_major_version(): # real signature unknown; restored from __doc__
    """ get_major_version() -> int """
    return 0

def get_micro_version(): # real signature unknown; restored from __doc__
    """ get_micro_version() -> int """
    return 0

def get_minor_version(): # real signature unknown; restored from __doc__
    """ get_minor_version() -> int """
    return 0

def get_option_group(open_default_display): # real signature unknown; restored from __doc__
    """ get_option_group(open_default_display:bool) -> GLib.OptionGroup """
    pass

def grab_get_current(): # real signature unknown; restored from __doc__
    """ grab_get_current() -> Gtk.Widget or None """
    pass

def icon_size_from_name(name): # real signature unknown; restored from __doc__
    """ icon_size_from_name(name:str) -> int """
    return 0

def icon_size_get_name(size): # real signature unknown; restored from __doc__
    """ icon_size_get_name(size:int) -> str """
    return ""

def icon_size_lookup(size): # real signature unknown; restored from __doc__
    """ icon_size_lookup(size:int) -> bool, width:int, height:int """
    return False

def icon_size_lookup_for_settings(settings, size): # real signature unknown; restored from __doc__
    """ icon_size_lookup_for_settings(settings:Gtk.Settings, size:int) -> bool, width:int, height:int """
    return False

def icon_size_register(name, width, height): # real signature unknown; restored from __doc__
    """ icon_size_register(name:str, width:int, height:int) -> int """
    return 0

def icon_size_register_alias(alias, target): # real signature unknown; restored from __doc__
    """ icon_size_register_alias(alias:str, target:int) """
    pass

def icon_theme_error_quark(): # real signature unknown; restored from __doc__
    """ icon_theme_error_quark() -> int """
    return 0

def init(argv=None): # real signature unknown; restored from __doc__
    """ init(argv:list=None) -> argv:list """
    pass

def init_abi_check(argc, argv, num_checks, sizeof_GtkWindow, sizeof_GtkBox): # real signature unknown; restored from __doc__
    """ init_abi_check(argc:int, argv:str, num_checks:int, sizeof_GtkWindow:int, sizeof_GtkBox:int) """
    pass

def init_check(argv=None): # real signature unknown; restored from __doc__
    """ init_check(argv:list=None) -> bool, argv:list """
    return False

def init_check_abi_check(argc, argv, num_checks, sizeof_GtkWindow, sizeof_GtkBox): # real signature unknown; restored from __doc__
    """ init_check_abi_check(argc:int, argv:str, num_checks:int, sizeof_GtkWindow:int, sizeof_GtkBox:int) -> bool """
    return False

def init_with_args(argv=None, parameter_string=None, entries, translation_domain=None): # real signature unknown; restored from __doc__
    """ init_with_args(argv:list=None, parameter_string:str=None, entries:list, translation_domain:str=None) -> bool, argv:list """
    return False

def key_snooper_remove(snooper_handler_id): # real signature unknown; restored from __doc__
    """ key_snooper_remove(snooper_handler_id:int) """
    pass

def main(*args, **kwargs): # reliably restored by inspect
    # no doc
    pass

def main_do_event(event): # real signature unknown; restored from __doc__
    """ main_do_event(event:Gdk.Event) """
    pass

def main_iteration(): # reliably restored by inspect
    # no doc
    pass

def main_iteration_do(blocking): # reliably restored by inspect
    # no doc
    pass

def main_level(): # real signature unknown; restored from __doc__
    """ main_level() -> int """
    return 0

def main_quit(*args): # reliably restored by inspect
    # no doc
    pass

def paint_arrow(style, cr, state_type, shadow_type, widget=None, detail=None, arrow_type, fill, x, y, width, height): # real signature unknown; restored from __doc__
    """ paint_arrow(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget=None, detail:str=None, arrow_type:Gtk.ArrowType, fill:bool, x:int, y:int, width:int, height:int) """
    pass

def paint_box(style, cr, state_type, shadow_type, widget=None, detail=None, x, y, width, height): # real signature unknown; restored from __doc__
    """ paint_box(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget=None, detail:str=None, x:int, y:int, width:int, height:int) """
    pass

def paint_box_gap(style, cr, state_type, shadow_type, widget=None, detail=None, x, y, width, height, gap_side, gap_x, gap_width): # real signature unknown; restored from __doc__
    """ paint_box_gap(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget=None, detail:str=None, x:int, y:int, width:int, height:int, gap_side:Gtk.PositionType, gap_x:int, gap_width:int) """
    pass

def paint_check(style, cr, state_type, shadow_type, widget=None, detail=None, x, y, width, height): # real signature unknown; restored from __doc__
    """ paint_check(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget=None, detail:str=None, x:int, y:int, width:int, height:int) """
    pass

def paint_diamond(style, cr, state_type, shadow_type, widget=None, detail=None, x, y, width, height): # real signature unknown; restored from __doc__
    """ paint_diamond(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget=None, detail:str=None, x:int, y:int, width:int, height:int) """
    pass

def paint_expander(style, cr, state_type, widget=None, detail=None, x, y, expander_style): # real signature unknown; restored from __doc__
    """ paint_expander(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, widget:Gtk.Widget=None, detail:str=None, x:int, y:int, expander_style:Gtk.ExpanderStyle) """
    pass

def paint_extension(style, cr, state_type, shadow_type, widget=None, detail=None, x, y, width, height, gap_side): # real signature unknown; restored from __doc__
    """ paint_extension(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget=None, detail:str=None, x:int, y:int, width:int, height:int, gap_side:Gtk.PositionType) """
    pass

def paint_flat_box(style, cr, state_type, shadow_type, widget=None, detail=None, x, y, width, height): # real signature unknown; restored from __doc__
    """ paint_flat_box(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget=None, detail:str=None, x:int, y:int, width:int, height:int) """
    pass

def paint_focus(style, cr, state_type, widget=None, detail=None, x, y, width, height): # real signature unknown; restored from __doc__
    """ paint_focus(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, widget:Gtk.Widget=None, detail:str=None, x:int, y:int, width:int, height:int) """
    pass

def paint_handle(style, cr, state_type, shadow_type, widget=None, detail=None, x, y, width, height, orientation): # real signature unknown; restored from __doc__
    """ paint_handle(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget=None, detail:str=None, x:int, y:int, width:int, height:int, orientation:Gtk.Orientation) """
    pass

def paint_hline(style, cr, state_type, widget=None, detail=None, x1, x2, y): # real signature unknown; restored from __doc__
    """ paint_hline(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, widget:Gtk.Widget=None, detail:str=None, x1:int, x2:int, y:int) """
    pass

def paint_layout(style, cr, state_type, use_text, widget=None, detail=None, x, y, layout): # real signature unknown; restored from __doc__
    """ paint_layout(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, use_text:bool, widget:Gtk.Widget=None, detail:str=None, x:int, y:int, layout:Pango.Layout) """
    pass

def paint_option(style, cr, state_type, shadow_type, widget=None, detail=None, x, y, width, height): # real signature unknown; restored from __doc__
    """ paint_option(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget=None, detail:str=None, x:int, y:int, width:int, height:int) """
    pass

def paint_resize_grip(style, cr, state_type, widget=None, detail=None, edge, x, y, width, height): # real signature unknown; restored from __doc__
    """ paint_resize_grip(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, widget:Gtk.Widget=None, detail:str=None, edge:Gdk.WindowEdge, x:int, y:int, width:int, height:int) """
    pass

def paint_shadow(style, cr, state_type, shadow_type, widget=None, detail=None, x, y, width, height): # real signature unknown; restored from __doc__
    """ paint_shadow(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget=None, detail:str=None, x:int, y:int, width:int, height:int) """
    pass

def paint_shadow_gap(style, cr, state_type, shadow_type, widget=None, detail=None, x, y, width, height, gap_side, gap_x, gap_width): # real signature unknown; restored from __doc__
    """ paint_shadow_gap(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget=None, detail:str=None, x:int, y:int, width:int, height:int, gap_side:Gtk.PositionType, gap_x:int, gap_width:int) """
    pass

def paint_slider(style, cr, state_type, shadow_type, widget=None, detail=None, x, y, width, height, orientation): # real signature unknown; restored from __doc__
    """ paint_slider(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget=None, detail:str=None, x:int, y:int, width:int, height:int, orientation:Gtk.Orientation) """
    pass

def paint_spinner(style, cr, state_type, widget=None, detail=None, step, x, y, width, height): # real signature unknown; restored from __doc__
    """ paint_spinner(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, widget:Gtk.Widget=None, detail:str=None, step:int, x:int, y:int, width:int, height:int) """
    pass

def paint_tab(style, cr, state_type, shadow_type, widget=None, detail=None, x, y, width, height): # real signature unknown; restored from __doc__
    """ paint_tab(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget=None, detail:str=None, x:int, y:int, width:int, height:int) """
    pass

def paint_vline(style, cr, state_type, widget=None, detail=None, y1_, y2_, x): # real signature unknown; restored from __doc__
    """ paint_vline(style:Gtk.Style, cr:cairo.Context, state_type:Gtk.StateType, widget:Gtk.Widget=None, detail:str=None, y1_:int, y2_:int, x:int) """
    pass

def paper_size_get_default(): # real signature unknown; restored from __doc__
    """ paper_size_get_default() -> str """
    return ""

def paper_size_get_paper_sizes(include_custom): # real signature unknown; restored from __doc__
    """ paper_size_get_paper_sizes(include_custom:bool) -> list """
    return []

def parse_args(argv): # real signature unknown; restored from __doc__
    """ parse_args(argv:list) -> bool, argv:list """
    return False

def print_error_quark(): # real signature unknown; restored from __doc__
    """ print_error_quark() -> int """
    return 0

def propagate_event(widget, event): # real signature unknown; restored from __doc__
    """ propagate_event(widget:Gtk.Widget, event:Gdk.Event) """
    pass

def rc_add_default_file(filename): # real signature unknown; restored from __doc__
    """ rc_add_default_file(filename:str) """
    pass

def rc_find_module_in_path(module_file): # real signature unknown; restored from __doc__
    """ rc_find_module_in_path(module_file:str) -> str """
    return ""

def rc_find_pixmap_in_path(settings, scanner, pixmap_file): # real signature unknown; restored from __doc__
    """ rc_find_pixmap_in_path(settings:Gtk.Settings, scanner:GLib.Scanner, pixmap_file:str) -> str """
    return ""

def rc_get_default_files(): # real signature unknown; restored from __doc__
    """ rc_get_default_files() -> list """
    return []

def rc_get_im_module_file(): # real signature unknown; restored from __doc__
    """ rc_get_im_module_file() -> str """
    return ""

def rc_get_im_module_path(): # real signature unknown; restored from __doc__
    """ rc_get_im_module_path() -> str """
    return ""

def rc_get_module_dir(): # real signature unknown; restored from __doc__
    """ rc_get_module_dir() -> str """
    return ""

def rc_get_style(widget): # real signature unknown; restored from __doc__
    """ rc_get_style(widget:Gtk.Widget) -> Gtk.Style """
    pass

def rc_get_style_by_paths(settings, widget_path=None, class_path=None, type): # real signature unknown; restored from __doc__
    """ rc_get_style_by_paths(settings:Gtk.Settings, widget_path:str=None, class_path:str=None, type:GType) -> Gtk.Style or None """
    pass

def rc_get_theme_dir(): # real signature unknown; restored from __doc__
    """ rc_get_theme_dir() -> str """
    return ""

def rc_parse(filename): # real signature unknown; restored from __doc__
    """ rc_parse(filename:str) """
    pass

def rc_parse_color(scanner): # real signature unknown; restored from __doc__
    """ rc_parse_color(scanner:GLib.Scanner) -> int, color:Gdk.Color """
    return 0

def rc_parse_color_full(scanner, style=None): # real signature unknown; restored from __doc__
    """ rc_parse_color_full(scanner:GLib.Scanner, style:Gtk.RcStyle=None) -> int, color:Gdk.Color """
    return 0

def rc_parse_priority(scanner, priority): # real signature unknown; restored from __doc__
    """ rc_parse_priority(scanner:GLib.Scanner, priority:Gtk.PathPriorityType) -> int """
    return 0

def rc_parse_state(scanner): # real signature unknown; restored from __doc__
    """ rc_parse_state(scanner:GLib.Scanner) -> int, state:Gtk.StateType """
    return 0

def rc_parse_string(rc_string): # real signature unknown; restored from __doc__
    """ rc_parse_string(rc_string:str) """
    pass

def rc_property_parse_border(pspec, gstring, property_value): # real signature unknown; restored from __doc__
    """ rc_property_parse_border(pspec:GObject.ParamSpec, gstring:GLib.String, property_value:GObject.Value) -> bool """
    return False

def rc_property_parse_color(pspec, gstring, property_value): # real signature unknown; restored from __doc__
    """ rc_property_parse_color(pspec:GObject.ParamSpec, gstring:GLib.String, property_value:GObject.Value) -> bool """
    return False

def rc_property_parse_enum(pspec, gstring, property_value): # real signature unknown; restored from __doc__
    """ rc_property_parse_enum(pspec:GObject.ParamSpec, gstring:GLib.String, property_value:GObject.Value) -> bool """
    return False

def rc_property_parse_flags(pspec, gstring, property_value): # real signature unknown; restored from __doc__
    """ rc_property_parse_flags(pspec:GObject.ParamSpec, gstring:GLib.String, property_value:GObject.Value) -> bool """
    return False

def rc_property_parse_requisition(pspec, gstring, property_value): # real signature unknown; restored from __doc__
    """ rc_property_parse_requisition(pspec:GObject.ParamSpec, gstring:GLib.String, property_value:GObject.Value) -> bool """
    return False

def rc_reparse_all(): # real signature unknown; restored from __doc__
    """ rc_reparse_all() -> bool """
    return False

def rc_reparse_all_for_settings(settings, force_load): # real signature unknown; restored from __doc__
    """ rc_reparse_all_for_settings(settings:Gtk.Settings, force_load:bool) -> bool """
    return False

def rc_reset_styles(settings): # real signature unknown; restored from __doc__
    """ rc_reset_styles(settings:Gtk.Settings) """
    pass

def rc_set_default_files(filenames): # real signature unknown; restored from __doc__
    """ rc_set_default_files(filenames:list) """
    pass

def recent_chooser_error_quark(): # real signature unknown; restored from __doc__
    """ recent_chooser_error_quark() -> int """
    return 0

def recent_manager_error_quark(): # real signature unknown; restored from __doc__
    """ recent_manager_error_quark() -> int """
    return 0

def render_activity(context, cr, x, y, width, height): # real signature unknown; restored from __doc__
    """ render_activity(context:Gtk.StyleContext, cr:cairo.Context, x:float, y:float, width:float, height:float) """
    pass

def render_arrow(context, cr, angle, x, y, size): # real signature unknown; restored from __doc__
    """ render_arrow(context:Gtk.StyleContext, cr:cairo.Context, angle:float, x:float, y:float, size:float) """
    pass

def render_background(context, cr, x, y, width, height): # real signature unknown; restored from __doc__
    """ render_background(context:Gtk.StyleContext, cr:cairo.Context, x:float, y:float, width:float, height:float) """
    pass

def render_background_get_clip(context, x, y, width, height): # real signature unknown; restored from __doc__
    """ render_background_get_clip(context:Gtk.StyleContext, x:float, y:float, width:float, height:float) -> out_clip:Gdk.Rectangle """
    pass

def render_check(context, cr, x, y, width, height): # real signature unknown; restored from __doc__
    """ render_check(context:Gtk.StyleContext, cr:cairo.Context, x:float, y:float, width:float, height:float) """
    pass

def render_expander(context, cr, x, y, width, height): # real signature unknown; restored from __doc__
    """ render_expander(context:Gtk.StyleContext, cr:cairo.Context, x:float, y:float, width:float, height:float) """
    pass

def render_extension(context, cr, x, y, width, height, gap_side): # real signature unknown; restored from __doc__
    """ render_extension(context:Gtk.StyleContext, cr:cairo.Context, x:float, y:float, width:float, height:float, gap_side:Gtk.PositionType) """
    pass

def render_focus(context, cr, x, y, width, height): # real signature unknown; restored from __doc__
    """ render_focus(context:Gtk.StyleContext, cr:cairo.Context, x:float, y:float, width:float, height:float) """
    pass

def render_frame(context, cr, x, y, width, height): # real signature unknown; restored from __doc__
    """ render_frame(context:Gtk.StyleContext, cr:cairo.Context, x:float, y:float, width:float, height:float) """
    pass

def render_frame_gap(context, cr, x, y, width, height, gap_side, xy0_gap, xy1_gap): # real signature unknown; restored from __doc__
    """ render_frame_gap(context:Gtk.StyleContext, cr:cairo.Context, x:float, y:float, width:float, height:float, gap_side:Gtk.PositionType, xy0_gap:float, xy1_gap:float) """
    pass

def render_handle(context, cr, x, y, width, height): # real signature unknown; restored from __doc__
    """ render_handle(context:Gtk.StyleContext, cr:cairo.Context, x:float, y:float, width:float, height:float) """
    pass

def render_icon(context, cr, pixbuf, x, y): # real signature unknown; restored from __doc__
    """ render_icon(context:Gtk.StyleContext, cr:cairo.Context, pixbuf:GdkPixbuf.Pixbuf, x:float, y:float) """
    pass

def render_icon_pixbuf(context, source, size): # real signature unknown; restored from __doc__
    """ render_icon_pixbuf(context:Gtk.StyleContext, source:Gtk.IconSource, size:int) -> GdkPixbuf.Pixbuf """
    pass

def render_icon_surface(context, cr, surface, x, y): # real signature unknown; restored from __doc__
    """ render_icon_surface(context:Gtk.StyleContext, cr:cairo.Context, surface:cairo.Surface, x:float, y:float) """
    pass

def render_insertion_cursor(context, cr, x, y, layout, index, direction): # real signature unknown; restored from __doc__
    """ render_insertion_cursor(context:Gtk.StyleContext, cr:cairo.Context, x:float, y:float, layout:Pango.Layout, index:int, direction:Pango.Direction) """
    pass

def render_layout(context, cr, x, y, layout): # real signature unknown; restored from __doc__
    """ render_layout(context:Gtk.StyleContext, cr:cairo.Context, x:float, y:float, layout:Pango.Layout) """
    pass

def render_line(context, cr, x0, y0, x1, y1): # real signature unknown; restored from __doc__
    """ render_line(context:Gtk.StyleContext, cr:cairo.Context, x0:float, y0:float, x1:float, y1:float) """
    pass

def render_option(context, cr, x, y, width, height): # real signature unknown; restored from __doc__
    """ render_option(context:Gtk.StyleContext, cr:cairo.Context, x:float, y:float, width:float, height:float) """
    pass

def render_slider(context, cr, x, y, width, height, orientation): # real signature unknown; restored from __doc__
    """ render_slider(context:Gtk.StyleContext, cr:cairo.Context, x:float, y:float, width:float, height:float, orientation:Gtk.Orientation) """
    pass

def rgb_to_hsv(r, g, b): # real signature unknown; restored from __doc__
    """ rgb_to_hsv(r:float, g:float, b:float) -> h:float, s:float, v:float """
    pass

def selection_add_target(widget, selection, target, info): # real signature unknown; restored from __doc__
    """ selection_add_target(widget:Gtk.Widget, selection:Gdk.Atom, target:Gdk.Atom, info:int) """
    pass

def selection_add_targets(widget, selection, targets): # real signature unknown; restored from __doc__
    """ selection_add_targets(widget:Gtk.Widget, selection:Gdk.Atom, targets:list) """
    pass

def selection_clear_targets(widget, selection): # real signature unknown; restored from __doc__
    """ selection_clear_targets(widget:Gtk.Widget, selection:Gdk.Atom) """
    pass

def selection_convert(widget, selection, target, time_): # real signature unknown; restored from __doc__
    """ selection_convert(widget:Gtk.Widget, selection:Gdk.Atom, target:Gdk.Atom, time_:int) -> bool """
    return False

def selection_owner_set(widget=None, selection, time_): # real signature unknown; restored from __doc__
    """ selection_owner_set(widget:Gtk.Widget=None, selection:Gdk.Atom, time_:int) -> bool """
    return False

def selection_owner_set_for_display(display, widget=None, selection, time_): # real signature unknown; restored from __doc__
    """ selection_owner_set_for_display(display:Gdk.Display, widget:Gtk.Widget=None, selection:Gdk.Atom, time_:int) -> bool """
    return False

def selection_remove_all(widget): # real signature unknown; restored from __doc__
    """ selection_remove_all(widget:Gtk.Widget) """
    pass

def set_debug_flags(flags): # real signature unknown; restored from __doc__
    """ set_debug_flags(flags:int) """
    pass

def show_uri(screen=None, uri, timestamp): # real signature unknown; restored from __doc__
    """ show_uri(screen:Gdk.Screen=None, uri:str, timestamp:int) -> bool """
    return False

def show_uri_on_window(parent=None, uri, timestamp): # real signature unknown; restored from __doc__
    """ show_uri_on_window(parent:Gtk.Window=None, uri:str, timestamp:int) -> bool """
    return False

def stock_add(items): # real signature unknown; restored from __doc__
    """ stock_add(items:list) """
    pass

def stock_add_static(items): # real signature unknown; restored from __doc__
    """ stock_add_static(items:list) """
    pass

def stock_list_ids(): # real signature unknown; restored from __doc__
    """ stock_list_ids() -> list """
    return []

def stock_lookup(*args, **kwargs): # reliably restored by inspect
    """ stock_lookup(stock_id:str) -> bool, item:Gtk.StockItem """
    pass

def stock_set_translate_func(domain, func, data=None): # real signature unknown; restored from __doc__
    """ stock_set_translate_func(domain:str, func:Gtk.TranslateFunc, data=None) """
    pass

def targets_include_image(targets, writable): # real signature unknown; restored from __doc__
    """ targets_include_image(targets:list, writable:bool) -> bool """
    return False

def targets_include_rich_text(targets, buffer): # real signature unknown; restored from __doc__
    """ targets_include_rich_text(targets:list, buffer:Gtk.TextBuffer) -> bool """
    return False

def targets_include_text(targets): # real signature unknown; restored from __doc__
    """ targets_include_text(targets:list) -> bool """
    return False

def targets_include_uri(targets): # real signature unknown; restored from __doc__
    """ targets_include_uri(targets:list) -> bool """
    return False

def target_table_free(targets): # real signature unknown; restored from __doc__
    """ target_table_free(targets:list) """
    pass

def target_table_new_from_list(p_list): # real signature unknown; restored from __doc__
    """ target_table_new_from_list(list:Gtk.TargetList) -> list """
    return []

def test_create_simple_window(window_title, dialog_text): # real signature unknown; restored from __doc__
    """ test_create_simple_window(window_title:str, dialog_text:str) -> Gtk.Widget """
    pass

def test_find_label(widget, label_pattern): # real signature unknown; restored from __doc__
    """ test_find_label(widget:Gtk.Widget, label_pattern:str) -> Gtk.Widget """
    pass

def test_find_sibling(base_widget, widget_type): # real signature unknown; restored from __doc__
    """ test_find_sibling(base_widget:Gtk.Widget, widget_type:GType) -> Gtk.Widget """
    pass

def test_find_widget(widget, label_pattern, widget_type): # real signature unknown; restored from __doc__
    """ test_find_widget(widget:Gtk.Widget, label_pattern:str, widget_type:GType) -> Gtk.Widget or None """
    pass

def test_list_all_types(): # real signature unknown; restored from __doc__
    """ test_list_all_types() -> list """
    return []

def test_register_all_types(): # real signature unknown; restored from __doc__
    """ test_register_all_types() """
    pass

def test_slider_get_value(widget): # real signature unknown; restored from __doc__
    """ test_slider_get_value(widget:Gtk.Widget) -> float """
    return 0.0

def test_slider_set_perc(widget, percentage): # real signature unknown; restored from __doc__
    """ test_slider_set_perc(widget:Gtk.Widget, percentage:float) """
    pass

def test_spin_button_click(spinner, button, upwards): # real signature unknown; restored from __doc__
    """ test_spin_button_click(spinner:Gtk.SpinButton, button:int, upwards:bool) -> bool """
    return False

def test_text_get(widget): # real signature unknown; restored from __doc__
    """ test_text_get(widget:Gtk.Widget) -> str """
    return ""

def test_text_set(widget, string): # real signature unknown; restored from __doc__
    """ test_text_set(widget:Gtk.Widget, string:str) """
    pass

def test_widget_click(widget, button, modifiers): # real signature unknown; restored from __doc__
    """ test_widget_click(widget:Gtk.Widget, button:int, modifiers:Gdk.ModifierType) -> bool """
    return False

def test_widget_send_key(widget, keyval, modifiers): # real signature unknown; restored from __doc__
    """ test_widget_send_key(widget:Gtk.Widget, keyval:int, modifiers:Gdk.ModifierType) -> bool """
    return False

def test_widget_wait_for_draw(widget): # real signature unknown; restored from __doc__
    """ test_widget_wait_for_draw(widget:Gtk.Widget) """
    pass

def tree_get_row_drag_data(selection_data): # real signature unknown; restored from __doc__
    """ tree_get_row_drag_data(selection_data:Gtk.SelectionData) -> bool, tree_model:Gtk.TreeModel, path:Gtk.TreePath """
    return False

def tree_row_reference_deleted(proxy, path): # real signature unknown; restored from __doc__
    """ tree_row_reference_deleted(proxy:GObject.Object, path:Gtk.TreePath) """
    pass

def tree_row_reference_inserted(proxy, path): # real signature unknown; restored from __doc__
    """ tree_row_reference_inserted(proxy:GObject.Object, path:Gtk.TreePath) """
    pass

def tree_set_row_drag_data(selection_data, tree_model, path): # real signature unknown; restored from __doc__
    """ tree_set_row_drag_data(selection_data:Gtk.SelectionData, tree_model:Gtk.TreeModel, path:Gtk.TreePath) -> bool """
    return False

def true(): # real signature unknown; restored from __doc__
    """ true() -> bool """
    return False

def _construct_target_list(targets): # reliably restored by inspect
    """
    Create a list of TargetEntry items from a list of tuples in the form (target, flags, info).
    
    The list can also contain existing TargetEntry items in which case the existing entry
    is re-used in the return list.
    """
    pass

def _extract_handler_and_args(obj_or_map, handler_name): # reliably restored by inspect
    # no doc
    pass

# classes

from .Buildable import Buildable
from .Widget import Widget
from .Container import Container
from .Bin import Bin
from .Window import Window
from .Dialog import Dialog
from .AboutDialog import AboutDialog
from .AboutDialogClass import AboutDialogClass
from .AboutDialogPrivate import AboutDialogPrivate
from .AccelFlags import AccelFlags
from .AccelGroup import AccelGroup
from .AccelGroupClass import AccelGroupClass
from .AccelGroupEntry import AccelGroupEntry
from .AccelGroupPrivate import AccelGroupPrivate
from .AccelKey import AccelKey
from .Misc import Misc
from .Label import Label
from .AccelLabel import AccelLabel
from .AccelLabelClass import AccelLabelClass
from .AccelLabelPrivate import AccelLabelPrivate
from .AccelMap import AccelMap
from .AccelMapClass import AccelMapClass
from .Accessible import Accessible
from .AccessibleClass import AccessibleClass
from .AccessiblePrivate import AccessiblePrivate
from .Action import Action
from .Actionable import Actionable
from .ActionableInterface import ActionableInterface
from .ActionBar import ActionBar
from .ActionBarClass import ActionBarClass
from .ActionBarPrivate import ActionBarPrivate
from .ActionClass import ActionClass
from .ActionEntry import ActionEntry
from .ActionGroup import ActionGroup
from .ActionGroupClass import ActionGroupClass
from .ActionGroupPrivate import ActionGroupPrivate
from .ActionPrivate import ActionPrivate
from .Activatable import Activatable
from .ActivatableIface import ActivatableIface
from .Adjustment import Adjustment
from .AdjustmentClass import AdjustmentClass
from .AdjustmentPrivate import AdjustmentPrivate
from .Align import Align
from .Alignment import Alignment
from .AlignmentClass import AlignmentClass
from .AlignmentPrivate import AlignmentPrivate
from .AppChooser import AppChooser
from .CellEditable import CellEditable
from .CellLayout import CellLayout
from .ComboBox import ComboBox
from .AppChooserButton import AppChooserButton
from .AppChooserButtonClass import AppChooserButtonClass
from .AppChooserButtonPrivate import AppChooserButtonPrivate
from .AppChooserDialog import AppChooserDialog
from .AppChooserDialogClass import AppChooserDialogClass
from .AppChooserDialogPrivate import AppChooserDialogPrivate
from .Orientable import Orientable
from .Box import Box
from .AppChooserWidget import AppChooserWidget
from .AppChooserWidgetClass import AppChooserWidgetClass
from .AppChooserWidgetPrivate import AppChooserWidgetPrivate
from .Application import Application
from .ApplicationClass import ApplicationClass
from .ApplicationInhibitFlags import ApplicationInhibitFlags
from .ApplicationPrivate import ApplicationPrivate
from .ApplicationWindow import ApplicationWindow
from .ApplicationWindowClass import ApplicationWindowClass
from .ApplicationWindowPrivate import ApplicationWindowPrivate
from .Arrow import Arrow
from .WidgetAccessible import WidgetAccessible
from .ArrowAccessible import ArrowAccessible
from .ArrowAccessibleClass import ArrowAccessibleClass
from .ArrowAccessiblePrivate import ArrowAccessiblePrivate
from .ArrowClass import ArrowClass
from .ArrowPlacement import ArrowPlacement
from .ArrowPrivate import ArrowPrivate
from .ArrowType import ArrowType
from .Frame import Frame
from .AspectFrame import AspectFrame
from .AspectFrameClass import AspectFrameClass
from .AspectFramePrivate import AspectFramePrivate
from .Assistant import Assistant
from .AssistantClass import AssistantClass
from .AssistantPageType import AssistantPageType
from .AssistantPrivate import AssistantPrivate
from .AttachOptions import AttachOptions
from .BaselinePosition import BaselinePosition
from .BinClass import BinClass
from .BindingArg import BindingArg
from .BindingEntry import BindingEntry
from .BindingSet import BindingSet
from .BindingSignal import BindingSignal
from .BinPrivate import BinPrivate
from .CellAccessible import CellAccessible
from .RendererCellAccessible import RendererCellAccessible
from .BooleanCellAccessible import BooleanCellAccessible
from .BooleanCellAccessibleClass import BooleanCellAccessibleClass
from .BooleanCellAccessiblePrivate import BooleanCellAccessiblePrivate
from .Border import Border
from .BorderStyle import BorderStyle
from .BoxClass import BoxClass
from .BoxPrivate import BoxPrivate
from .BuildableIface import BuildableIface
from .Builder import Builder
from .BuilderClass import BuilderClass
from .BuilderError import BuilderError
from .BuilderPrivate import BuilderPrivate
from .Button import Button
from .ContainerAccessible import ContainerAccessible
from .ButtonAccessible import ButtonAccessible
from .ButtonAccessibleClass import ButtonAccessibleClass
from .ButtonAccessiblePrivate import ButtonAccessiblePrivate
from .ButtonBox import ButtonBox
from .ButtonBoxClass import ButtonBoxClass
from .ButtonBoxPrivate import ButtonBoxPrivate
from .ButtonBoxStyle import ButtonBoxStyle
from .ButtonClass import ButtonClass
from .ButtonPrivate import ButtonPrivate
from .ButtonRole import ButtonRole
from .ButtonsType import ButtonsType
from .Calendar import Calendar
from .CalendarClass import CalendarClass
from .CalendarDisplayOptions import CalendarDisplayOptions
from .CalendarPrivate import CalendarPrivate
from .CellAccessibleClass import CellAccessibleClass
from .CellAccessibleParent import CellAccessibleParent
from .CellAccessibleParentIface import CellAccessibleParentIface
from .CellAccessiblePrivate import CellAccessiblePrivate
from .CellArea import CellArea
from .CellAreaBox import CellAreaBox
from .CellAreaBoxClass import CellAreaBoxClass
from .CellAreaBoxPrivate import CellAreaBoxPrivate
from .CellAreaClass import CellAreaClass
from .CellAreaContext import CellAreaContext
from .CellAreaContextClass import CellAreaContextClass
from .CellAreaContextPrivate import CellAreaContextPrivate
from .CellAreaPrivate import CellAreaPrivate
from .CellEditableIface import CellEditableIface
from .CellLayoutIface import CellLayoutIface
from .CellRenderer import CellRenderer
from .CellRendererText import CellRendererText
from .CellRendererAccel import CellRendererAccel
from .CellRendererAccelClass import CellRendererAccelClass
from .CellRendererAccelMode import CellRendererAccelMode
from .CellRendererAccelPrivate import CellRendererAccelPrivate
from .CellRendererClass import CellRendererClass
from .CellRendererClassPrivate import CellRendererClassPrivate
from .CellRendererCombo import CellRendererCombo
from .CellRendererComboClass import CellRendererComboClass
from .CellRendererComboPrivate import CellRendererComboPrivate
from .CellRendererMode import CellRendererMode
from .CellRendererPixbuf import CellRendererPixbuf
from .CellRendererPixbufClass import CellRendererPixbufClass
from .CellRendererPixbufPrivate import CellRendererPixbufPrivate
from .CellRendererPrivate import CellRendererPrivate
from .CellRendererProgress import CellRendererProgress
from .CellRendererProgressClass import CellRendererProgressClass
from .CellRendererProgressPrivate import CellRendererProgressPrivate
from .CellRendererSpin import CellRendererSpin
from .CellRendererSpinClass import CellRendererSpinClass
from .CellRendererSpinner import CellRendererSpinner
from .CellRendererSpinnerClass import CellRendererSpinnerClass
from .CellRendererSpinnerPrivate import CellRendererSpinnerPrivate
from .CellRendererSpinPrivate import CellRendererSpinPrivate
from .CellRendererState import CellRendererState
from .CellRendererTextClass import CellRendererTextClass
from .CellRendererTextPrivate import CellRendererTextPrivate
from .CellRendererToggle import CellRendererToggle
from .CellRendererToggleClass import CellRendererToggleClass
from .CellRendererTogglePrivate import CellRendererTogglePrivate
from .CellView import CellView
from .CellViewClass import CellViewClass
from .CellViewPrivate import CellViewPrivate
from .ToggleButton import ToggleButton
from .CheckButton import CheckButton
from .CheckButtonClass import CheckButtonClass
from .MenuItem import MenuItem
from .CheckMenuItem import CheckMenuItem
from .MenuItemAccessible import MenuItemAccessible
from .CheckMenuItemAccessible import CheckMenuItemAccessible
from .CheckMenuItemAccessibleClass import CheckMenuItemAccessibleClass
from .CheckMenuItemAccessiblePrivate import CheckMenuItemAccessiblePrivate
from .CheckMenuItemClass import CheckMenuItemClass
from .CheckMenuItemPrivate import CheckMenuItemPrivate
from .Clipboard import Clipboard
from .ColorChooser import ColorChooser
from .ColorButton import ColorButton
from .ColorButtonClass import ColorButtonClass
from .ColorButtonPrivate import ColorButtonPrivate
from .ColorChooserDialog import ColorChooserDialog
from .ColorChooserDialogClass import ColorChooserDialogClass
from .ColorChooserDialogPrivate import ColorChooserDialogPrivate
from .ColorChooserInterface import ColorChooserInterface
from .ColorChooserWidget import ColorChooserWidget
from .ColorChooserWidgetClass import ColorChooserWidgetClass
from .ColorChooserWidgetPrivate import ColorChooserWidgetPrivate
from .ColorSelection import ColorSelection
from .ColorSelectionClass import ColorSelectionClass
from .ColorSelectionDialog import ColorSelectionDialog
from .ColorSelectionDialogClass import ColorSelectionDialogClass
from .ColorSelectionDialogPrivate import ColorSelectionDialogPrivate
from .ColorSelectionPrivate import ColorSelectionPrivate
from .ComboBoxAccessible import ComboBoxAccessible
from .ComboBoxAccessibleClass import ComboBoxAccessibleClass
from .ComboBoxAccessiblePrivate import ComboBoxAccessiblePrivate
from .ComboBoxClass import ComboBoxClass
from .ComboBoxPrivate import ComboBoxPrivate
from .ComboBoxText import ComboBoxText
from .ComboBoxTextClass import ComboBoxTextClass
from .ComboBoxTextPrivate import ComboBoxTextPrivate
from .ContainerAccessibleClass import ContainerAccessibleClass
from .ContainerAccessiblePrivate import ContainerAccessiblePrivate
from .ContainerCellAccessible import ContainerCellAccessible
from .ContainerCellAccessibleClass import ContainerCellAccessibleClass
from .ContainerCellAccessiblePrivate import ContainerCellAccessiblePrivate
from .ContainerClass import ContainerClass
from .ContainerPrivate import ContainerPrivate
from .CornerType import CornerType
from .StyleProvider import StyleProvider
from .CssProvider import CssProvider
from .CssProviderClass import CssProviderClass
from .CssProviderError import CssProviderError
from .CssProviderPrivate import CssProviderPrivate
from .CssSection import CssSection
from .CssSectionType import CssSectionType
from .DebugFlag import DebugFlag
from .DeleteType import DeleteType
from .DestDefaults import DestDefaults
from .DialogClass import DialogClass
from .DialogFlags import DialogFlags
from .DialogPrivate import DialogPrivate
from .DirectionType import DirectionType
from .DragResult import DragResult
from .DrawingArea import DrawingArea
from .DrawingAreaClass import DrawingAreaClass
from .Editable import Editable
from .EditableInterface import EditableInterface
from .Entry import Entry
from .EntryAccessible import EntryAccessible
from .EntryAccessibleClass import EntryAccessibleClass
from .EntryAccessiblePrivate import EntryAccessiblePrivate
from .EntryBuffer import EntryBuffer
from .EntryBufferClass import EntryBufferClass
from .EntryBufferPrivate import EntryBufferPrivate
from .EntryClass import EntryClass
from .EntryCompletion import EntryCompletion
from .EntryCompletionClass import EntryCompletionClass
from .EntryCompletionPrivate import EntryCompletionPrivate
from .EntryIconAccessible import EntryIconAccessible
from .EntryIconPosition import EntryIconPosition
from .EntryPrivate import EntryPrivate
from .EventBox import EventBox
from .EventBoxClass import EventBoxClass
from .EventBoxPrivate import EventBoxPrivate
from .EventController import EventController
from .EventControllerClass import EventControllerClass
from .EventControllerKey import EventControllerKey
from .EventControllerKeyClass import EventControllerKeyClass
from .EventControllerMotion import EventControllerMotion
from .EventControllerMotionClass import EventControllerMotionClass
from .EventControllerScroll import EventControllerScroll
from .EventControllerScrollClass import EventControllerScrollClass
from .EventControllerScrollFlags import EventControllerScrollFlags
from .EventSequenceState import EventSequenceState
from .Expander import Expander
from .ExpanderAccessible import ExpanderAccessible
from .ExpanderAccessibleClass import ExpanderAccessibleClass
from .ExpanderAccessiblePrivate import ExpanderAccessiblePrivate
from .ExpanderClass import ExpanderClass
from .ExpanderPrivate import ExpanderPrivate
from .ExpanderStyle import ExpanderStyle
from .FileChooser import FileChooser
from .FileChooserAction import FileChooserAction
from .FileChooserButton import FileChooserButton
from .FileChooserButtonClass import FileChooserButtonClass
from .FileChooserButtonPrivate import FileChooserButtonPrivate
from .FileChooserConfirmation import FileChooserConfirmation
from .FileChooserDialog import FileChooserDialog
from .FileChooserDialogClass import FileChooserDialogClass
from .FileChooserDialogPrivate import FileChooserDialogPrivate
from .FileChooserError import FileChooserError
from .NativeDialog import NativeDialog
from .FileChooserNative import FileChooserNative
from .FileChooserNativeClass import FileChooserNativeClass
from .FileChooserWidget import FileChooserWidget
from .FileChooserWidgetAccessible import FileChooserWidgetAccessible
from .FileChooserWidgetAccessibleClass import FileChooserWidgetAccessibleClass
from .FileChooserWidgetAccessiblePrivate import FileChooserWidgetAccessiblePrivate
from .FileChooserWidgetClass import FileChooserWidgetClass
from .FileChooserWidgetPrivate import FileChooserWidgetPrivate
from .FileFilter import FileFilter
from .FileFilterFlags import FileFilterFlags
from .FileFilterInfo import FileFilterInfo
from .Fixed import Fixed
from .FixedChild import FixedChild
from .FixedClass import FixedClass
from .FixedPrivate import FixedPrivate
from .FlowBox import FlowBox
from .FlowBoxAccessible import FlowBoxAccessible
from .FlowBoxAccessibleClass import FlowBoxAccessibleClass
from .FlowBoxAccessiblePrivate import FlowBoxAccessiblePrivate
from .FlowBoxChild import FlowBoxChild
from .FlowBoxChildAccessible import FlowBoxChildAccessible
from .FlowBoxChildAccessibleClass import FlowBoxChildAccessibleClass
from .FlowBoxChildClass import FlowBoxChildClass
from .FlowBoxClass import FlowBoxClass
from .FontChooser import FontChooser
from .FontButton import FontButton
from .FontButtonClass import FontButtonClass
from .FontButtonPrivate import FontButtonPrivate
from .FontChooserDialog import FontChooserDialog
from .FontChooserDialogClass import FontChooserDialogClass
from .FontChooserDialogPrivate import FontChooserDialogPrivate
from .FontChooserIface import FontChooserIface
from .FontChooserLevel import FontChooserLevel
from .FontChooserWidget import FontChooserWidget
from .FontChooserWidgetClass import FontChooserWidgetClass
from .FontChooserWidgetPrivate import FontChooserWidgetPrivate
from .FontSelection import FontSelection
from .FontSelectionClass import FontSelectionClass
from .FontSelectionDialog import FontSelectionDialog
from .FontSelectionDialogClass import FontSelectionDialogClass
from .FontSelectionDialogPrivate import FontSelectionDialogPrivate
from .FontSelectionPrivate import FontSelectionPrivate
from .FrameAccessible import FrameAccessible
from .FrameAccessibleClass import FrameAccessibleClass
from .FrameAccessiblePrivate import FrameAccessiblePrivate
from .FrameClass import FrameClass
from .FramePrivate import FramePrivate
from .Gesture import Gesture
from .GestureClass import GestureClass
from .GestureSingle import GestureSingle
from .GestureDrag import GestureDrag
from .GestureDragClass import GestureDragClass
from .GestureLongPress import GestureLongPress
from .GestureLongPressClass import GestureLongPressClass
from .GestureMultiPress import GestureMultiPress
from .GestureMultiPressClass import GestureMultiPressClass
from .GesturePan import GesturePan
from .GesturePanClass import GesturePanClass
from .GestureRotate import GestureRotate
from .GestureRotateClass import GestureRotateClass
from .GestureSingleClass import GestureSingleClass
from .GestureStylus import GestureStylus
from .GestureStylusClass import GestureStylusClass
from .GestureSwipe import GestureSwipe
from .GestureSwipeClass import GestureSwipeClass
from .GestureZoom import GestureZoom
from .GestureZoomClass import GestureZoomClass
from .GLArea import GLArea
from .GLAreaClass import GLAreaClass
from .Gradient import Gradient
from .Grid import Grid
from .GridClass import GridClass
from .GridPrivate import GridPrivate
from .HandleBox import HandleBox
from .HandleBoxClass import HandleBoxClass
from .HandleBoxPrivate import HandleBoxPrivate
from .HBox import HBox
from .HBoxClass import HBoxClass
from .HButtonBox import HButtonBox
from .HButtonBoxClass import HButtonBoxClass
from .HeaderBar import HeaderBar
from .HeaderBarAccessible import HeaderBarAccessible
from .HeaderBarAccessibleClass import HeaderBarAccessibleClass
from .HeaderBarAccessiblePrivate import HeaderBarAccessiblePrivate
from .HeaderBarClass import HeaderBarClass
from .HeaderBarPrivate import HeaderBarPrivate
from .Paned import Paned
from .HPaned import HPaned
from .HPanedClass import HPanedClass
from .Range import Range
from .Scale import Scale
from .HScale import HScale
from .HScaleClass import HScaleClass
from .Scrollbar import Scrollbar
from .HScrollbar import HScrollbar
from .HScrollbarClass import HScrollbarClass
from .Separator import Separator
from .HSeparator import HSeparator
from .HSeparatorClass import HSeparatorClass
from .HSV import HSV
from .HSVClass import HSVClass
from .HSVPrivate import HSVPrivate
from .IconFactory import IconFactory
from .IconFactoryClass import IconFactoryClass
from .IconFactoryPrivate import IconFactoryPrivate
from .IconInfo import IconInfo
from .IconInfoClass import IconInfoClass
from .IconLookupFlags import IconLookupFlags
from .IconSet import IconSet
from .IconSize import IconSize
from .IconSource import IconSource
from .IconTheme import IconTheme
from .IconThemeClass import IconThemeClass
from .IconThemeError import IconThemeError
from .IconThemePrivate import IconThemePrivate
from .Scrollable import Scrollable
from .IconView import IconView
from .IconViewAccessible import IconViewAccessible
from .IconViewAccessibleClass import IconViewAccessibleClass
from .IconViewAccessiblePrivate import IconViewAccessiblePrivate
from .IconViewClass import IconViewClass
from .IconViewDropPosition import IconViewDropPosition
from .IconViewPrivate import IconViewPrivate
from .Image import Image
from .ImageAccessible import ImageAccessible
from .ImageAccessibleClass import ImageAccessibleClass
from .ImageAccessiblePrivate import ImageAccessiblePrivate
from .ImageCellAccessible import ImageCellAccessible
from .ImageCellAccessibleClass import ImageCellAccessibleClass
from .ImageCellAccessiblePrivate import ImageCellAccessiblePrivate
from .ImageClass import ImageClass
from .ImageMenuItem import ImageMenuItem
from .ImageMenuItemClass import ImageMenuItemClass
from .ImageMenuItemPrivate import ImageMenuItemPrivate
from .ImagePrivate import ImagePrivate
from .ImageType import ImageType
from .IMContext import IMContext
from .IMContextClass import IMContextClass
from .IMContextInfo import IMContextInfo
from .IMContextSimple import IMContextSimple
from .IMContextSimpleClass import IMContextSimpleClass
from .IMContextSimplePrivate import IMContextSimplePrivate
from .IMMulticontext import IMMulticontext
from .IMMulticontextClass import IMMulticontextClass
from .IMMulticontextPrivate import IMMulticontextPrivate
from .IMPreeditStyle import IMPreeditStyle
from .IMStatusStyle import IMStatusStyle
from .InfoBar import InfoBar
from .InfoBarClass import InfoBarClass
from .InfoBarPrivate import InfoBarPrivate
from .InputHints import InputHints
from .InputPurpose import InputPurpose
from .Invisible import Invisible
from .InvisibleClass import InvisibleClass
from .InvisiblePrivate import InvisiblePrivate
from .JunctionSides import JunctionSides
from .Justification import Justification
from .LabelAccessible import LabelAccessible
from .LabelAccessibleClass import LabelAccessibleClass
from .LabelAccessiblePrivate import LabelAccessiblePrivate
from .LabelClass import LabelClass
from .LabelPrivate import LabelPrivate
from .LabelSelectionInfo import LabelSelectionInfo
from .Layout import Layout
from .LayoutClass import LayoutClass
from .LayoutPrivate import LayoutPrivate
from .LevelBar import LevelBar
from .LevelBarAccessible import LevelBarAccessible
from .LevelBarAccessibleClass import LevelBarAccessibleClass
from .LevelBarAccessiblePrivate import LevelBarAccessiblePrivate
from .LevelBarClass import LevelBarClass
from .LevelBarMode import LevelBarMode
from .LevelBarPrivate import LevelBarPrivate
from .License import License
from .LinkButton import LinkButton
from .LinkButtonAccessible import LinkButtonAccessible
from .LinkButtonAccessibleClass import LinkButtonAccessibleClass
from .LinkButtonAccessiblePrivate import LinkButtonAccessiblePrivate
from .LinkButtonClass import LinkButtonClass
from .LinkButtonPrivate import LinkButtonPrivate
from .ListBox import ListBox
from .ListBoxAccessible import ListBoxAccessible
from .ListBoxAccessibleClass import ListBoxAccessibleClass
from .ListBoxAccessiblePrivate import ListBoxAccessiblePrivate
from .ListBoxClass import ListBoxClass
from .ListBoxRow import ListBoxRow
from .ListBoxRowAccessible import ListBoxRowAccessible
from .ListBoxRowAccessibleClass import ListBoxRowAccessibleClass
from .ListBoxRowClass import ListBoxRowClass
from .TreeDragDest import TreeDragDest
from .TreeDragSource import TreeDragSource
from .TreeModel import TreeModel
from .TreeSortable import TreeSortable
from .ListStore import ListStore
from .ListStoreClass import ListStoreClass
from .ListStorePrivate import ListStorePrivate
from .LockButton import LockButton
from .LockButtonAccessible import LockButtonAccessible
from .LockButtonAccessibleClass import LockButtonAccessibleClass
from .LockButtonAccessiblePrivate import LockButtonAccessiblePrivate
from .LockButtonClass import LockButtonClass
from .LockButtonPrivate import LockButtonPrivate
from .MenuShell import MenuShell
from .Menu import Menu
from .MenuShellAccessible import MenuShellAccessible
from .MenuAccessible import MenuAccessible
from .MenuAccessibleClass import MenuAccessibleClass
from .MenuAccessiblePrivate import MenuAccessiblePrivate
from .MenuBar import MenuBar
from .MenuBarClass import MenuBarClass
from .MenuBarPrivate import MenuBarPrivate
from .MenuButton import MenuButton
from .ToggleButtonAccessible import ToggleButtonAccessible
from .MenuButtonAccessible import MenuButtonAccessible
from .MenuButtonAccessibleClass import MenuButtonAccessibleClass
from .MenuButtonAccessiblePrivate import MenuButtonAccessiblePrivate
from .MenuButtonClass import MenuButtonClass
from .MenuButtonPrivate import MenuButtonPrivate
from .MenuClass import MenuClass
from .MenuDirectionType import MenuDirectionType
from .MenuItemAccessibleClass import MenuItemAccessibleClass
from .MenuItemAccessiblePrivate import MenuItemAccessiblePrivate
from .MenuItemClass import MenuItemClass
from .MenuItemPrivate import MenuItemPrivate
from .MenuPrivate import MenuPrivate
from .MenuShellAccessibleClass import MenuShellAccessibleClass
from .MenuShellAccessiblePrivate import MenuShellAccessiblePrivate
from .MenuShellClass import MenuShellClass
from .MenuShellPrivate import MenuShellPrivate
from .ToolItem import ToolItem
from .ToolButton import ToolButton
from .MenuToolButton import MenuToolButton
from .MenuToolButtonClass import MenuToolButtonClass
from .MenuToolButtonPrivate import MenuToolButtonPrivate
from .MessageDialog import MessageDialog
from .MessageDialogClass import MessageDialogClass
from .MessageDialogPrivate import MessageDialogPrivate
from .MessageType import MessageType
from .MiscClass import MiscClass
from .MiscPrivate import MiscPrivate
from .ModelButton import ModelButton
from .MountOperation import MountOperation
from .MountOperationClass import MountOperationClass
from .MountOperationPrivate import MountOperationPrivate
from .MovementStep import MovementStep
from .NativeDialogClass import NativeDialogClass
from .Notebook import Notebook
from .NotebookAccessible import NotebookAccessible
from .NotebookAccessibleClass import NotebookAccessibleClass
from .NotebookAccessiblePrivate import NotebookAccessiblePrivate
from .NotebookClass import NotebookClass
from .NotebookPageAccessible import NotebookPageAccessible
from .NotebookPageAccessibleClass import NotebookPageAccessibleClass
from .NotebookPageAccessiblePrivate import NotebookPageAccessiblePrivate
from .NotebookPrivate import NotebookPrivate
from .NotebookTab import NotebookTab
from .NumberUpLayout import NumberUpLayout
from .NumerableIcon import NumerableIcon
from .NumerableIconClass import NumerableIconClass
from .NumerableIconPrivate import NumerableIconPrivate
from .OffscreenWindow import OffscreenWindow
from .OffscreenWindowClass import OffscreenWindowClass
from .OrientableIface import OrientableIface
from .Orientation import Orientation
from .Overlay import Overlay
from .OverlayClass import OverlayClass
from .OverlayPrivate import OverlayPrivate
from .PackDirection import PackDirection
from .PackType import PackType
from .PadActionEntry import PadActionEntry
from .PadActionType import PadActionType
from .PadController import PadController
from .PadControllerClass import PadControllerClass
from .PageOrientation import PageOrientation
from .PageRange import PageRange
from .PageSet import PageSet
from .PageSetup import PageSetup
from .PanDirection import PanDirection
from .PanedAccessible import PanedAccessible
from .PanedAccessibleClass import PanedAccessibleClass
from .PanedAccessiblePrivate import PanedAccessiblePrivate
from .PanedClass import PanedClass
from .PanedPrivate import PanedPrivate
from .PaperSize import PaperSize
from .PathPriorityType import PathPriorityType
from .PathType import PathType
from .PlacesOpenFlags import PlacesOpenFlags
from .ScrolledWindow import ScrolledWindow
from .PlacesSidebar import PlacesSidebar
from .PlacesSidebarClass import PlacesSidebarClass
from .WindowAccessible import WindowAccessible
from .PlugAccessible import PlugAccessible
from .PlugAccessibleClass import PlugAccessibleClass
from .PlugAccessiblePrivate import PlugAccessiblePrivate
from .PolicyType import PolicyType
from .Popover import Popover
from .PopoverAccessible import PopoverAccessible
from .PopoverAccessibleClass import PopoverAccessibleClass
from .PopoverClass import PopoverClass
from .PopoverConstraint import PopoverConstraint
from .PopoverMenu import PopoverMenu
from .PopoverMenuClass import PopoverMenuClass
from .PopoverPrivate import PopoverPrivate
from .PositionType import PositionType
from .PrintContext import PrintContext
from .PrintDuplex import PrintDuplex
from .PrintError import PrintError
from .PrintOperationPreview import PrintOperationPreview
from .PrintOperation import PrintOperation
from .PrintOperationAction import PrintOperationAction
from .PrintOperationClass import PrintOperationClass
from .PrintOperationPreviewIface import PrintOperationPreviewIface
from .PrintOperationPrivate import PrintOperationPrivate
from .PrintOperationResult import PrintOperationResult
from .PrintPages import PrintPages
from .PrintQuality import PrintQuality
from .PrintSettings import PrintSettings
from .PrintStatus import PrintStatus
from .ProgressBar import ProgressBar
from .ProgressBarAccessible import ProgressBarAccessible
from .ProgressBarAccessibleClass import ProgressBarAccessibleClass
from .ProgressBarAccessiblePrivate import ProgressBarAccessiblePrivate
from .ProgressBarClass import ProgressBarClass
from .ProgressBarPrivate import ProgressBarPrivate
from .PropagationPhase import PropagationPhase
from .PyGTKDeprecationWarning import PyGTKDeprecationWarning
from .ToggleAction import ToggleAction
from .RadioAction import RadioAction
from .RadioActionClass import RadioActionClass
from .RadioActionEntry import RadioActionEntry
from .RadioActionPrivate import RadioActionPrivate
from .RadioButton import RadioButton
from .RadioButtonAccessible import RadioButtonAccessible
from .RadioButtonAccessibleClass import RadioButtonAccessibleClass
from .RadioButtonAccessiblePrivate import RadioButtonAccessiblePrivate
from .RadioButtonClass import RadioButtonClass
from .RadioButtonPrivate import RadioButtonPrivate
from .RadioMenuItem import RadioMenuItem
from .RadioMenuItemAccessible import RadioMenuItemAccessible
from .RadioMenuItemAccessibleClass import RadioMenuItemAccessibleClass
from .RadioMenuItemAccessiblePrivate import RadioMenuItemAccessiblePrivate
from .RadioMenuItemClass import RadioMenuItemClass
from .RadioMenuItemPrivate import RadioMenuItemPrivate
from .ToggleToolButton import ToggleToolButton
from .RadioToolButton import RadioToolButton
from .RadioToolButtonClass import RadioToolButtonClass
from .RangeAccessible import RangeAccessible
from .RangeAccessibleClass import RangeAccessibleClass
from .RangeAccessiblePrivate import RangeAccessiblePrivate
from .RangeClass import RangeClass
from .RangePrivate import RangePrivate
from .RcContext import RcContext
from .RcFlags import RcFlags
from .RcProperty import RcProperty
from .RcStyle import RcStyle
from .RcStyleClass import RcStyleClass
from .RcTokenType import RcTokenType
from .RecentChooser import RecentChooser
from .RecentAction import RecentAction
from .RecentActionClass import RecentActionClass
from .RecentActionPrivate import RecentActionPrivate
from .RecentChooserDialog import RecentChooserDialog
from .RecentChooserDialogClass import RecentChooserDialogClass
from .RecentChooserDialogPrivate import RecentChooserDialogPrivate
from .RecentChooserError import RecentChooserError
from .RecentChooserIface import RecentChooserIface
from .RecentChooserMenu import RecentChooserMenu
from .RecentChooserMenuClass import RecentChooserMenuClass
from .RecentChooserMenuPrivate import RecentChooserMenuPrivate
from .RecentChooserWidget import RecentChooserWidget
from .RecentChooserWidgetClass import RecentChooserWidgetClass
from .RecentChooserWidgetPrivate import RecentChooserWidgetPrivate
from .RecentData import RecentData
from .RecentFilter import RecentFilter
from .RecentFilterFlags import RecentFilterFlags
from .RecentFilterInfo import RecentFilterInfo
from .RecentInfo import RecentInfo
from .RecentManager import RecentManager
from .RecentManagerClass import RecentManagerClass
from .RecentManagerError import RecentManagerError
from .RecentManagerPrivate import RecentManagerPrivate
from .RecentSortType import RecentSortType
from .RegionFlags import RegionFlags
from .ReliefStyle import ReliefStyle
from .RendererCellAccessibleClass import RendererCellAccessibleClass
from .RendererCellAccessiblePrivate import RendererCellAccessiblePrivate
from .RequestedSize import RequestedSize
from .Requisition import Requisition
from .ResizeMode import ResizeMode
from .ResponseType import ResponseType
from .Revealer import Revealer
from .RevealerClass import RevealerClass
from .RevealerTransitionType import RevealerTransitionType
from .ScaleAccessible import ScaleAccessible
from .ScaleAccessibleClass import ScaleAccessibleClass
from .ScaleAccessiblePrivate import ScaleAccessiblePrivate
from .ScaleButton import ScaleButton
from .ScaleButtonAccessible import ScaleButtonAccessible
from .ScaleButtonAccessibleClass import ScaleButtonAccessibleClass
from .ScaleButtonAccessiblePrivate import ScaleButtonAccessiblePrivate
from .ScaleButtonClass import ScaleButtonClass
from .ScaleButtonPrivate import ScaleButtonPrivate
from .ScaleClass import ScaleClass
from .ScalePrivate import ScalePrivate
from .ScrollableInterface import ScrollableInterface
from .ScrollablePolicy import ScrollablePolicy
from .ScrollbarClass import ScrollbarClass
from .ScrolledWindowAccessible import ScrolledWindowAccessible
from .ScrolledWindowAccessibleClass import ScrolledWindowAccessibleClass
from .ScrolledWindowAccessiblePrivate import ScrolledWindowAccessiblePrivate
from .ScrolledWindowClass import ScrolledWindowClass
from .ScrolledWindowPrivate import ScrolledWindowPrivate
from .ScrollStep import ScrollStep
from .ScrollType import ScrollType
from .SearchBar import SearchBar
from .SearchBarClass import SearchBarClass
from .SearchEntry import SearchEntry
from .SearchEntryClass import SearchEntryClass
from .SelectionData import SelectionData
from .SelectionMode import SelectionMode
from .SensitivityType import SensitivityType
from .SeparatorClass import SeparatorClass
from .SeparatorMenuItem import SeparatorMenuItem
from .SeparatorMenuItemClass import SeparatorMenuItemClass
from .SeparatorPrivate import SeparatorPrivate
from .SeparatorToolItem import SeparatorToolItem
from .SeparatorToolItemClass import SeparatorToolItemClass
from .SeparatorToolItemPrivate import SeparatorToolItemPrivate
from .Settings import Settings
from .SettingsClass import SettingsClass
from .SettingsPrivate import SettingsPrivate
from .SettingsValue import SettingsValue
from .ShadowType import ShadowType
from .ShortcutLabel import ShortcutLabel
from .ShortcutLabelClass import ShortcutLabelClass
from .ShortcutsGroup import ShortcutsGroup
from .ShortcutsGroupClass import ShortcutsGroupClass
from .ShortcutsSection import ShortcutsSection
from .ShortcutsSectionClass import ShortcutsSectionClass
from .ShortcutsShortcut import ShortcutsShortcut
from .ShortcutsShortcutClass import ShortcutsShortcutClass
from .ShortcutsWindow import ShortcutsWindow
from .ShortcutsWindowClass import ShortcutsWindowClass
from .ShortcutType import ShortcutType
from .SizeGroup import SizeGroup
from .SizeGroupClass import SizeGroupClass
from .SizeGroupMode import SizeGroupMode
from .SizeGroupPrivate import SizeGroupPrivate
from .SizeRequestMode import SizeRequestMode
from .SocketAccessible import SocketAccessible
from .SocketAccessibleClass import SocketAccessibleClass
from .SocketAccessiblePrivate import SocketAccessiblePrivate
from .SortType import SortType
from .SpinButton import SpinButton
from .SpinButtonAccessible import SpinButtonAccessible
from .SpinButtonAccessibleClass import SpinButtonAccessibleClass
from .SpinButtonAccessiblePrivate import SpinButtonAccessiblePrivate
from .SpinButtonClass import SpinButtonClass
from .SpinButtonPrivate import SpinButtonPrivate
from .SpinButtonUpdatePolicy import SpinButtonUpdatePolicy
from .Spinner import Spinner
from .SpinnerAccessible import SpinnerAccessible
from .SpinnerAccessibleClass import SpinnerAccessibleClass
from .SpinnerAccessiblePrivate import SpinnerAccessiblePrivate
from .SpinnerClass import SpinnerClass
from .SpinnerPrivate import SpinnerPrivate
from .SpinType import SpinType
from .Stack import Stack
from .StackAccessible import StackAccessible
from .StackAccessibleClass import StackAccessibleClass
from .StackClass import StackClass
from .StackSidebar import StackSidebar
from .StackSidebarClass import StackSidebarClass
from .StackSidebarPrivate import StackSidebarPrivate
from .StackSwitcher import StackSwitcher
from .StackSwitcherClass import StackSwitcherClass
from .StackTransitionType import StackTransitionType
from .StateFlags import StateFlags
from .StateType import StateType
from .Statusbar import Statusbar
from .StatusbarAccessible import StatusbarAccessible
from .StatusbarAccessibleClass import StatusbarAccessibleClass
from .StatusbarAccessiblePrivate import StatusbarAccessiblePrivate
from .StatusbarClass import StatusbarClass
from .StatusbarPrivate import StatusbarPrivate
from .StatusIcon import StatusIcon
from .StatusIconClass import StatusIconClass
from .StatusIconPrivate import StatusIconPrivate
from .StockItem import StockItem
from .Style import Style
from .StyleClass import StyleClass
from .StyleContext import StyleContext
from .StyleContextClass import StyleContextClass
from .StyleContextPrintFlags import StyleContextPrintFlags
from .StyleContextPrivate import StyleContextPrivate
from .StyleProperties import StyleProperties
from .StylePropertiesClass import StylePropertiesClass
from .StylePropertiesPrivate import StylePropertiesPrivate
from .StyleProviderIface import StyleProviderIface
from .Switch import Switch
from .SwitchAccessible import SwitchAccessible
from .SwitchAccessibleClass import SwitchAccessibleClass
from .SwitchAccessiblePrivate import SwitchAccessiblePrivate
from .SwitchClass import SwitchClass
from .SwitchPrivate import SwitchPrivate
from .SymbolicColor import SymbolicColor
from .Table import Table
from .TableChild import TableChild
from .TableClass import TableClass
from .TablePrivate import TablePrivate
from .TableRowCol import TableRowCol
from .TargetEntry import TargetEntry
from .TargetFlags import TargetFlags
from .TargetList import TargetList
from .TargetPair import TargetPair
from .TearoffMenuItem import TearoffMenuItem
from .TearoffMenuItemClass import TearoffMenuItemClass
from .TearoffMenuItemPrivate import TearoffMenuItemPrivate
from .Template import Template
from .TextAppearance import TextAppearance
from .TextAttributes import TextAttributes
from .TextBTree import TextBTree
from .TextBuffer import TextBuffer
from .TextBufferClass import TextBufferClass
from .TextBufferPrivate import TextBufferPrivate
from .TextBufferTargetInfo import TextBufferTargetInfo
from .TextCellAccessible import TextCellAccessible
from .TextCellAccessibleClass import TextCellAccessibleClass
from .TextCellAccessiblePrivate import TextCellAccessiblePrivate
from .TextChildAnchor import TextChildAnchor
from .TextChildAnchorClass import TextChildAnchorClass
from .TextDirection import TextDirection
from .TextExtendSelection import TextExtendSelection
from .TextIter import TextIter
from .TextMark import TextMark
from .TextMarkClass import TextMarkClass
from .TextSearchFlags import TextSearchFlags
from .TextTag import TextTag
from .TextTagClass import TextTagClass
from .TextTagPrivate import TextTagPrivate
from .TextTagTable import TextTagTable
from .TextTagTableClass import TextTagTableClass
from .TextTagTablePrivate import TextTagTablePrivate
from .TextView import TextView
from .TextViewAccessible import TextViewAccessible
from .TextViewAccessibleClass import TextViewAccessibleClass
from .TextViewAccessiblePrivate import TextViewAccessiblePrivate
from .TextViewClass import TextViewClass
from .TextViewLayer import TextViewLayer
from .TextViewPrivate import TextViewPrivate
from .TextWindowType import TextWindowType
from .ThemeEngine import ThemeEngine
from .ThemingEngine import ThemingEngine
from .ThemingEngineClass import ThemingEngineClass
from .ThemingEnginePrivate import ThemingEnginePrivate
from .ToggleActionClass import ToggleActionClass
from .ToggleActionEntry import ToggleActionEntry
from .ToggleActionPrivate import ToggleActionPrivate
from .ToggleButtonAccessibleClass import ToggleButtonAccessibleClass
from .ToggleButtonAccessiblePrivate import ToggleButtonAccessiblePrivate
from .ToggleButtonClass import ToggleButtonClass
from .ToggleButtonPrivate import ToggleButtonPrivate
from .ToggleToolButtonClass import ToggleToolButtonClass
from .ToggleToolButtonPrivate import ToggleToolButtonPrivate
from .ToolShell import ToolShell
from .Toolbar import Toolbar
from .ToolbarClass import ToolbarClass
from .ToolbarPrivate import ToolbarPrivate
from .ToolbarSpaceStyle import ToolbarSpaceStyle
from .ToolbarStyle import ToolbarStyle
from .ToolButtonClass import ToolButtonClass
from .ToolButtonPrivate import ToolButtonPrivate
from .ToolItemClass import ToolItemClass
from .ToolItemGroup import ToolItemGroup
from .ToolItemGroupClass import ToolItemGroupClass
from .ToolItemGroupPrivate import ToolItemGroupPrivate
from .ToolItemPrivate import ToolItemPrivate
from .ToolPalette import ToolPalette
from .ToolPaletteClass import ToolPaletteClass
from .ToolPaletteDragTargets import ToolPaletteDragTargets
from .ToolPalettePrivate import ToolPalettePrivate
from .ToolShellIface import ToolShellIface
from .Tooltip import Tooltip
from .ToplevelAccessible import ToplevelAccessible
from .ToplevelAccessibleClass import ToplevelAccessibleClass
from .ToplevelAccessiblePrivate import ToplevelAccessiblePrivate
from .TreeDragDestIface import TreeDragDestIface
from .TreeDragSourceIface import TreeDragSourceIface
from .TreeIter import TreeIter
from .TreeModelFilter import TreeModelFilter
from .TreeModelFilterClass import TreeModelFilterClass
from .TreeModelFilterPrivate import TreeModelFilterPrivate
from .TreeModelFlags import TreeModelFlags
from .TreeModelIface import TreeModelIface
from .TreeModelRow import TreeModelRow
from .TreeModelRowIter import TreeModelRowIter
from .TreeModelSort import TreeModelSort
from .TreeModelSortClass import TreeModelSortClass
from .TreeModelSortPrivate import TreeModelSortPrivate
from .TreePath import TreePath
from .TreeRowReference import TreeRowReference
from .TreeSelection import TreeSelection
from .TreeSelectionClass import TreeSelectionClass
from .TreeSelectionPrivate import TreeSelectionPrivate
from .TreeSortableIface import TreeSortableIface
from .TreeStore import TreeStore
from .TreeStoreClass import TreeStoreClass
from .TreeStorePrivate import TreeStorePrivate
from .TreeView import TreeView
from .TreeViewAccessible import TreeViewAccessible
from .TreeViewAccessibleClass import TreeViewAccessibleClass
from .TreeViewAccessiblePrivate import TreeViewAccessiblePrivate
from .TreeViewClass import TreeViewClass
from .TreeViewColumn import TreeViewColumn
from .TreeViewColumnClass import TreeViewColumnClass
from .TreeViewColumnPrivate import TreeViewColumnPrivate
from .TreeViewColumnSizing import TreeViewColumnSizing
from .TreeViewDropPosition import TreeViewDropPosition
from .TreeViewGridLines import TreeViewGridLines
from .TreeViewPrivate import TreeViewPrivate
from .UIManager import UIManager
from .UIManagerClass import UIManagerClass
from .UIManagerItemType import UIManagerItemType
from .UIManagerPrivate import UIManagerPrivate
from .Unit import Unit
from .VBox import VBox
from .VBoxClass import VBoxClass
from .VButtonBox import VButtonBox
from .VButtonBoxClass import VButtonBoxClass
from .Viewport import Viewport
from .ViewportClass import ViewportClass
from .ViewportPrivate import ViewportPrivate
from .VolumeButton import VolumeButton
from .VolumeButtonClass import VolumeButtonClass
from .VPaned import VPaned
from .VPanedClass import VPanedClass
from .VScale import VScale
from .VScaleClass import VScaleClass
from .VScrollbar import VScrollbar
from .VScrollbarClass import VScrollbarClass
from .VSeparator import VSeparator
from .VSeparatorClass import VSeparatorClass
from .WidgetAccessibleClass import WidgetAccessibleClass
from .WidgetAccessiblePrivate import WidgetAccessiblePrivate
from .WidgetClass import WidgetClass
from .WidgetClassPrivate import WidgetClassPrivate
from .WidgetHelpType import WidgetHelpType
from .WidgetPath import WidgetPath
from .WidgetPrivate import WidgetPrivate
from .WindowAccessibleClass import WindowAccessibleClass
from .WindowAccessiblePrivate import WindowAccessiblePrivate
from .WindowClass import WindowClass
from .WindowGeometryInfo import WindowGeometryInfo
from .WindowGroup import WindowGroup
from .WindowGroupClass import WindowGroupClass
from .WindowGroupPrivate import WindowGroupPrivate
from .WindowPosition import WindowPosition
from .WindowPrivate import WindowPrivate
from .WindowType import WindowType
from .WrapMode import WrapMode
from ._MountOperationHandler import _MountOperationHandler
from ._MountOperationHandlerIface import _MountOperationHandlerIface
from ._MountOperationHandlerProxy import _MountOperationHandlerProxy
from ._MountOperationHandlerProxyClass import _MountOperationHandlerProxyClass
from ._MountOperationHandlerProxyPrivate import _MountOperationHandlerProxyPrivate
from ._MountOperationHandlerSkeleton import _MountOperationHandlerSkeleton
from ._MountOperationHandlerSkeletonClass import _MountOperationHandlerSkeletonClass
from ._MountOperationHandlerSkeletonPrivate import _MountOperationHandlerSkeletonPrivate
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x000002bfce2f4440>'

__path__ = []

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Gtk', loader=<gi.importer.DynamicImporter object at 0x000002bfce2f4440>)"

