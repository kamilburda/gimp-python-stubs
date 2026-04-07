# encoding: utf-8
# module gi.repository.GimpUi
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gimp as __gi_repository_Gimp
import gi.repository.Gtk as __gi_repository_Gtk
import gi._gi as __gi__gi


# Variables with simple values

COLOR_SELECTOR_BAR_SIZE = 15

COLOR_SELECTOR_SIZE = 150

ICON_APPLICATION_EXIT = 'application-exit'

ICON_ASPECT_LANDSCAPE = 'gimp-landscape'
ICON_ASPECT_PORTRAIT = 'gimp-portrait'

ICON_ATTACH = 'gimp-attach'

ICON_BUSINESS_CARD = 'gimp-business-card'

ICON_CAP_BUTT = 'gimp-cap-butt'
ICON_CAP_ROUND = 'gimp-cap-round'
ICON_CAP_SQUARE = 'gimp-cap-square'

ICON_CENTER = 'gimp-center'

ICON_CENTER_HORIZONTAL = 'gimp-hcenter'
ICON_CENTER_VERTICAL = 'gimp-vcenter'

ICON_CHAIN_HORIZONTAL = 'gimp-hchain'

ICON_CHAIN_HORIZONTAL_BROKEN = 'gimp-hchain-broken'

ICON_CHAIN_VERTICAL = 'gimp-vchain'

ICON_CHAIN_VERTICAL_BROKEN = 'gimp-vchain-broken'

ICON_CHANNEL = 'gimp-channel'

ICON_CHANNEL_ALPHA = 'gimp-channel-alpha'
ICON_CHANNEL_BLUE = 'gimp-channel-blue'
ICON_CHANNEL_GRAY = 'gimp-channel-gray'
ICON_CHANNEL_GREEN = 'gimp-channel-green'
ICON_CHANNEL_INDEXED = 'gimp-channel-indexed'
ICON_CHANNEL_RED = 'gimp-channel-red'

ICON_CHAR_PICKER = 'gimp-char-picker'

ICON_CLOSE = 'gimp-close'

ICON_CLOSE_ALL = 'gimp-close-all'

ICON_COLORMAP = 'gimp-colormap'

ICON_COLORS_DEFAULT = 'gimp-default-colors'
ICON_COLORS_SWAP = 'gimp-swap-colors'

ICON_COLOR_PICKER_BLACK = 'gimp-color-picker-black'
ICON_COLOR_PICKER_GRAY = 'gimp-color-picker-gray'
ICON_COLOR_PICKER_WHITE = 'gimp-color-picker-white'

ICON_COLOR_PICK_FROM_SCREEN = 'gimp-color-pick-from-screen'

ICON_COLOR_SELECTOR_CMYK = 'gimp-color-cmyk'
ICON_COLOR_SELECTOR_TRIANGLE = 'gimp-color-triangle'
ICON_COLOR_SELECTOR_WATER = 'gimp-color-water'

ICON_COLOR_SPACE_LINEAR = 'gimp-color-space-linear'

ICON_COLOR_SPACE_NON_LINEAR = 'gimp-color-space-non-linear'

ICON_COLOR_SPACE_PERCEPTUAL = 'gimp-color-space-perceptual'

ICON_CONTROLLER = 'gimp-controller'

ICON_CONTROLLER_KEYBOARD = 'gimp-controller-keyboard'

ICON_CONTROLLER_LINUX_INPUT = 'gimp-controller-linux-input'

ICON_CONTROLLER_MIDI = 'gimp-controller-midi'
ICON_CONTROLLER_WHEEL = 'gimp-controller-wheel'

ICON_CONVERT_GRAYSCALE = 'gimp-convert-grayscale'
ICON_CONVERT_INDEXED = 'gimp-convert-indexed'
ICON_CONVERT_RGB = 'gimp-convert-rgb'

ICON_CURSOR = 'gimp-cursor'

ICON_CURVE_FREE = 'gimp-curve-free'
ICON_CURVE_SMOOTH = 'gimp-curve-smooth'

ICON_DETACH = 'gimp-detach'

ICON_DIALOG_CHANNELS = 'gimp-channels'
ICON_DIALOG_DASHBOARD = 'gimp-dashboard'

ICON_DIALOG_DEVICE_STATUS = 'gimp-device-status'

ICON_DIALOG_ERROR = 'dialog-error'
ICON_DIALOG_IMAGES = 'gimp-images'
ICON_DIALOG_INFORMATION = 'dialog-information'
ICON_DIALOG_LAYERS = 'gimp-layers'
ICON_DIALOG_NAVIGATION = 'gimp-navigation'
ICON_DIALOG_PATHS = 'gimp-paths'
ICON_DIALOG_QUESTION = 'dialog-question'

ICON_DIALOG_RESHOW_FILTER = 'gimp-reshow-filter'

ICON_DIALOG_TOOLS = 'gimp-tools'

ICON_DIALOG_TOOL_OPTIONS = 'gimp-tool-options'

ICON_DIALOG_UNDO_HISTORY = 'gimp-undo-history'

ICON_DIALOG_WARNING = 'dialog-warning'

ICON_DISPLAY = 'gimp-display'

ICON_DISPLAY_FILTER = 'gimp-display-filter'

ICON_DISPLAY_FILTER_CLIP_WARNING = 'gimp-display-filter-clip-warning'

ICON_DISPLAY_FILTER_COLORBLIND = 'gimp-display-filter-colorblind'
ICON_DISPLAY_FILTER_CONTRAST = 'gimp-display-filter-contrast'
ICON_DISPLAY_FILTER_GAMMA = 'gimp-display-filter-gamma'
ICON_DISPLAY_FILTER_LCMS = 'gimp-display-filter-lcms'
ICON_DISPLAY_FILTER_PROOF = 'gimp-display-filter-proof'

ICON_DOCUMENT_NEW = 'document-new'
ICON_DOCUMENT_OPEN = 'document-open'

ICON_DOCUMENT_OPEN_RECENT = 'document-open-recent'

ICON_DOCUMENT_PAGE_SETUP = 'document-page-setup'

ICON_DOCUMENT_PRINT = 'document-print'

ICON_DOCUMENT_PRINT_RESOLUTION = 'document-print'

ICON_DOCUMENT_PROPERTIES = 'document-properties'
ICON_DOCUMENT_REVERT = 'document-revert'
ICON_DOCUMENT_SAVE = 'document-save'

ICON_DOCUMENT_SAVE_AS = 'document-save-as'

ICON_DYNAMICS = 'gimp-dynamics'
ICON_EDIT = 'gtk-edit'

ICON_EDIT_CLEAR = 'edit-clear'
ICON_EDIT_COPY = 'edit-copy'
ICON_EDIT_CUT = 'edit-cut'
ICON_EDIT_DELETE = 'edit-delete'
ICON_EDIT_FIND = 'edit-find'
ICON_EDIT_PASTE = 'edit-paste'

ICON_EDIT_PASTE_AS_NEW = 'gimp-paste-as-new'

ICON_EDIT_PASTE_INTO = 'gimp-paste-into'

ICON_EDIT_REDO = 'edit-redo'
ICON_EDIT_UNDO = 'edit-undo'

ICON_EFFECT = 'gimp-effects'

ICON_EVEN_HORIZONTAL_GAP = 'gimp-even-horizontal-gap'

ICON_EVEN_VERTICAL_GAP = 'gimp-even-vertical-gap'

ICON_FILE_MANAGER = 'gimp-file-manager'

ICON_FILL_HORIZONTAL = 'gimp-hfill'
ICON_FILL_VERTICAL = 'gimp-vfill'

ICON_FOLDER_NEW = 'folder-new'

ICON_FONT = 'gtk-select-font'

ICON_FORMAT_INDENT_LESS = 'format-indent-less'
ICON_FORMAT_INDENT_MORE = 'format-indent-more'

ICON_FORMAT_JUSTIFY_CENTER = 'format-justify-center'
ICON_FORMAT_JUSTIFY_FILL = 'format-justify-fill'
ICON_FORMAT_JUSTIFY_LEFT = 'format-justify-left'
ICON_FORMAT_JUSTIFY_RIGHT = 'format-justify-right'

ICON_FORMAT_TEXT_BOLD = 'format-text-bold'

ICON_FORMAT_TEXT_DIRECTION_LTR = 'format-text-direction-ltr'
ICON_FORMAT_TEXT_DIRECTION_RTL = 'format-text-direction-rtl'

ICON_FORMAT_TEXT_DIRECTION_TTB_LTR = 'gimp-text-dir-ttb-ltr'

ICON_FORMAT_TEXT_DIRECTION_TTB_LTR_UPRIGHT = 'gimp-text-dir-ttb-ltr-upright'

ICON_FORMAT_TEXT_DIRECTION_TTB_RTL = 'gimp-text-dir-ttb-rtl'

ICON_FORMAT_TEXT_DIRECTION_TTB_RTL_UPRIGHT = 'gimp-text-dir-ttb-rtl-upright'

ICON_FORMAT_TEXT_ITALIC = 'format-text-italic'

ICON_FORMAT_TEXT_SPACING_LETTER = 'gimp-letter-spacing'
ICON_FORMAT_TEXT_SPACING_LINE = 'gimp-line-spacing'

ICON_FORMAT_TEXT_STRIKETHROUGH = 'format-text-strikethrough'
ICON_FORMAT_TEXT_UNDERLINE = 'format-text-underline'

ICON_FRAME = 'gimp-frame'
ICON_GEGL = 'gimp-gegl'

ICON_GO_BOTTOM = 'go-bottom'
ICON_GO_DOWN = 'go-down'
ICON_GO_FIRST = 'go-first'
ICON_GO_HOME = 'go-home'
ICON_GO_LAST = 'go-last'
ICON_GO_NEXT = 'go-next'
ICON_GO_PREVIOUS = 'go-previous'
ICON_GO_TOP = 'go-top'
ICON_GO_UP = 'go-up'

ICON_GRADIENT_BILINEAR = 'gimp-gradient-bilinear'

ICON_GRADIENT_CONICAL_ASYMMETRIC = 'gimp-gradient-conical-asymmetric'
ICON_GRADIENT_CONICAL_SYMMETRIC = 'gimp-gradient-conical-symmetric'

ICON_GRADIENT_LINEAR = 'gimp-gradient-linear'
ICON_GRADIENT_RADIAL = 'gimp-gradient-radial'

ICON_GRADIENT_SHAPEBURST_ANGULAR = 'gimp-gradient-shapeburst-angular'
ICON_GRADIENT_SHAPEBURST_DIMPLED = 'gimp-gradient-shapeburst-dimpled'
ICON_GRADIENT_SHAPEBURST_SPHERICAL = 'gimp-gradient-shapeburst-spherical'

ICON_GRADIENT_SPIRAL_ANTICLOCKWISE = 'gimp-gradient-spiral-anticlockwise'
ICON_GRADIENT_SPIRAL_CLOCKWISE = 'gimp-gradient-spiral-clockwise'

ICON_GRADIENT_SQUARE = 'gimp-gradient-square'

ICON_GRAVITY_EAST = 'gimp-gravity-east'
ICON_GRAVITY_NORTH = 'gimp-gravity-north'

ICON_GRAVITY_NORTH_EAST = 'gimp-gravity-north-east'
ICON_GRAVITY_NORTH_WEST = 'gimp-gravity-north-west'

ICON_GRAVITY_SOUTH = 'gimp-gravity-south'

ICON_GRAVITY_SOUTH_EAST = 'gimp-gravity-south-east'
ICON_GRAVITY_SOUTH_WEST = 'gimp-gravity-south-west'

ICON_GRAVITY_WEST = 'gimp-gravity-west'

ICON_GRID = 'gimp-grid'
ICON_HELP = 'system-help'

ICON_HELP_ABOUT = 'help-about'

ICON_HELP_USER_MANUAL = 'gimp-user-manual'

ICON_HISTOGRAM = 'gimp-histogram'

ICON_HISTOGRAM_LINEAR = 'gimp-histogram-linear'
ICON_HISTOGRAM_LOGARITHMIC = 'gimp-histogram-logarithmic'

ICON_IMAGE = 'gimp-image'

ICON_IMAGE_OPEN = 'gimp-image-open'
ICON_IMAGE_RELOAD = 'gimp-image-reload'

ICON_INPUT_DEVICE = 'gimp-input-device'

ICON_INVERT = 'gimp-invert'

ICON_JOIN_BEVEL = 'gimp-join-bevel'
ICON_JOIN_MITER = 'gimp-join-miter'
ICON_JOIN_ROUND = 'gimp-join-round'

ICON_LAYER = 'gimp-layer'

ICON_LAYER_ANCHOR = 'gimp-anchor'

ICON_LAYER_FLOATING_SELECTION = 'gimp-floating-selection'

ICON_LAYER_LINK_LAYER = 'emblem-symbolic-link'

ICON_LAYER_MASK = 'gimp-layer-mask'

ICON_LAYER_MERGE_DOWN = 'gimp-merge-down'

ICON_LAYER_TEXT_LAYER = 'gimp-text-layer'

ICON_LAYER_TO_IMAGESIZE = 'gimp-layer-to-imagesize'

ICON_LAYER_VECTOR_LAYER = 'gimp-tool-path'

ICON_LINKED = 'gimp-linked'
ICON_LIST = 'gimp-list'

ICON_LIST_ADD = 'list-add'
ICON_LIST_REMOVE = 'list-remove'

ICON_LOCK = 'gimp-lock'

ICON_LOCK_ALPHA = 'gimp-lock-alpha'
ICON_LOCK_CONTENT = 'gimp-lock-content'
ICON_LOCK_MULTI = 'gimp-lock-multi'
ICON_LOCK_PATH = 'gimp-lock-path'
ICON_LOCK_POSITION = 'gimp-lock-position'
ICON_LOCK_VISIBILITY = 'gimp-lock-visibility'

ICON_MARKER = 'gimp-marker'

ICON_MENU_LEFT = 'gimp-menu-left'
ICON_MENU_RIGHT = 'gimp-menu-right'

ICON_OBJECT_DUPLICATE = 'gimp-duplicate'

ICON_OBJECT_FLIP_HORIZONTAL = 'object-flip-horizontal'
ICON_OBJECT_FLIP_VERTICAL = 'object-flip-vertical'

ICON_OBJECT_RESIZE = 'gimp-resize'

ICON_OBJECT_ROTATE_180 = 'gimp-rotate-180'
ICON_OBJECT_ROTATE_270 = 'object-rotate-left'
ICON_OBJECT_ROTATE_90 = 'object-rotate-right'

ICON_OBJECT_SCALE = 'gimp-scale'

ICON_PALETTE = 'gtk-select-color'
ICON_PATH = 'gimp-path'

ICON_PATH_STROKE = 'gimp-path-stroke'

ICON_PATTERN = 'gimp-pattern'

ICON_PIVOT_CENTER = 'gimp-pivot-center'
ICON_PIVOT_EAST = 'gimp-pivot-east'
ICON_PIVOT_NORTH = 'gimp-pivot-north'

ICON_PIVOT_NORTH_EAST = 'gimp-pivot-north-east'
ICON_PIVOT_NORTH_WEST = 'gimp-pivot-north-west'

ICON_PIVOT_SOUTH = 'gimp-pivot-south'

ICON_PIVOT_SOUTH_EAST = 'gimp-pivot-south-east'
ICON_PIVOT_SOUTH_WEST = 'gimp-pivot-south-west'

ICON_PIVOT_WEST = 'gimp-pivot-west'

ICON_PLUGIN = 'gimp-plugin'

ICON_PREFERENCES_SYSTEM = 'preferences-system'

ICON_PROCESS_STOP = 'process-stop'

ICON_QUICK_MASK_OFF = 'gimp-quick-mask-off'
ICON_QUICK_MASK_ON = 'gimp-quick-mask-on'

ICON_RECORD = 'media-record'
ICON_RESET = 'gimp-reset'

ICON_SAMPLE_POINT = 'gimp-sample-point'

ICON_SELECTION = 'gimp-selection'

ICON_SELECTION_ADD = 'gimp-selection-add'
ICON_SELECTION_ALL = 'gimp-selection-all'
ICON_SELECTION_BORDER = 'gimp-selection-border'
ICON_SELECTION_GROW = 'gimp-selection-grow'
ICON_SELECTION_INTERSECT = 'gimp-selection-intersect'
ICON_SELECTION_NONE = 'gimp-selection-none'
ICON_SELECTION_REPLACE = 'gimp-selection-replace'
ICON_SELECTION_SHRINK = 'gimp-selection-shrink'
ICON_SELECTION_STROKE = 'gimp-selection-stroke'
ICON_SELECTION_SUBTRACT = 'gimp-selection-subtract'

ICON_SELECTION_TO_CHANNEL = 'gimp-selection-to-channel'
ICON_SELECTION_TO_PATH = 'gimp-selection-to-path'

ICON_SHAPE_CIRCLE = 'gimp-shape-circle'
ICON_SHAPE_DIAMOND = 'gimp-shape-diamond'
ICON_SHAPE_SQUARE = 'gimp-shape-square'

ICON_SHRED = 'gimp-shred'
ICON_SMARTPHONE = 'gimp-smartphone'
ICON_SYMMETRY = 'gimp-symmetry'

ICON_SYSTEM_RUN = 'system-run'

ICON_TEMPLATE = 'gimp-template'
ICON_TEXTURE = 'gimp-texture'

ICON_TOOL_AIRBRUSH = 'gimp-tool-airbrush'
ICON_TOOL_ALIGN = 'gimp-tool-align'
ICON_TOOL_BLUR = 'gimp-tool-blur'

ICON_TOOL_BRIGHTNESS_CONTRAST = 'gimp-tool-brightness-contrast'

ICON_TOOL_BUCKET_FILL = 'gimp-tool-bucket-fill'

ICON_TOOL_BY_COLOR_SELECT = 'gimp-tool-by-color-select'

ICON_TOOL_CAGE = 'gimp-tool-cage'
ICON_TOOL_CLONE = 'gimp-tool-clone'
ICON_TOOL_COLORIZE = 'gimp-tool-colorize'

ICON_TOOL_COLOR_BALANCE = 'gimp-tool-color-balance'
ICON_TOOL_COLOR_PICKER = 'gimp-tool-color-picker'
ICON_TOOL_COLOR_TEMPERATURE = 'gimp-tool-color-temperature'

ICON_TOOL_CROP = 'gimp-tool-crop'
ICON_TOOL_CURVES = 'gimp-tool-curves'
ICON_TOOL_DESATURATE = 'gimp-tool-desaturate'
ICON_TOOL_DODGE = 'gimp-tool-dodge'

ICON_TOOL_ELLIPSE_SELECT = 'gimp-tool-ellipse-select'

ICON_TOOL_ERASER = 'gimp-tool-eraser'
ICON_TOOL_EXPOSURE = 'gimp-tool-exposure'
ICON_TOOL_FLIP = 'gimp-tool-flip'

ICON_TOOL_FOREGROUND_SELECT = 'gimp-tool-foreground-select'

ICON_TOOL_FREE_SELECT = 'gimp-tool-free-select'

ICON_TOOL_FUZZY_SELECT = 'gimp-tool-fuzzy-select'

ICON_TOOL_GRADIENT = 'gimp-tool-gradient'

ICON_TOOL_HANDLE_TRANSFORM = 'gimp-tool-handle-transform'

ICON_TOOL_HEAL = 'gimp-tool-heal'

ICON_TOOL_HUE_SATURATION = 'gimp-tool-hue-saturation'

ICON_TOOL_INK = 'gimp-tool-ink'
ICON_TOOL_ISCISSORS = 'gimp-tool-iscissors'
ICON_TOOL_LEVELS = 'gimp-tool-levels'
ICON_TOOL_MEASURE = 'gimp-tool-measure'
ICON_TOOL_MOVE = 'gimp-tool-move'

ICON_TOOL_MYPAINT_BRUSH = 'gimp-tool-mypaint-brush'

ICON_TOOL_N_POINT_DEFORMATION = 'gimp-tool-n-point-deformation'

ICON_TOOL_OFFSET = 'gimp-tool-offset'
ICON_TOOL_PAINTBRUSH = 'gimp-tool-paintbrush'

ICON_TOOL_PAINT_SELECT = 'gimp-tool-paint-select'

ICON_TOOL_PATH = 'gimp-tool-path'
ICON_TOOL_PENCIL = 'gimp-tool-pencil'
ICON_TOOL_PERSPECTIVE = 'gimp-tool-perspective'

ICON_TOOL_PERSPECTIVE_CLONE = 'gimp-tool-perspective-clone'

ICON_TOOL_POSTERIZE = 'gimp-tool-posterize'
ICON_TOOL_PRESET = 'gimp-tool-preset'

ICON_TOOL_RECT_SELECT = 'gimp-tool-rect-select'

ICON_TOOL_ROTATE = 'gimp-tool-rotate'
ICON_TOOL_SCALE = 'gimp-tool-scale'

ICON_TOOL_SEAMLESS_CLONE = 'gimp-tool-seamless-clone'

ICON_TOOL_SHADOWS_HIGHLIGHTS = 'gimp-tool-shadows-highlights'

ICON_TOOL_SHEAR = 'gimp-tool-shear'
ICON_TOOL_SMUDGE = 'gimp-tool-smudge'
ICON_TOOL_TEXT = 'gimp-tool-text'
ICON_TOOL_THRESHOLD = 'gimp-tool-threshold'

ICON_TOOL_TRANSFORM_3D = 'gimp-tool-transform-3d'

ICON_TOOL_UNIFIED_TRANSFORM = 'gimp-tool-unified-transform'

ICON_TOOL_WARP = 'gimp-tool-warp'
ICON_TOOL_ZOOM = 'gimp-tool-zoom'

ICON_TRANSFORM_3D_CAMERA = 'gimp-transform-3d-camera'
ICON_TRANSFORM_3D_MOVE = 'gimp-transform-3d-move'
ICON_TRANSFORM_3D_ROTATE = 'gimp-transform-3d-rotate'

ICON_TRANSPARENCY = 'gimp-transparency'
ICON_VIDEO = 'gimp-video'

ICON_VIEW_FULLSCREEN = 'view-fullscreen'
ICON_VIEW_REFRESH = 'view-refresh'

ICON_VIEW_SHRINK_WRAP = 'view-shrink-wrap'

ICON_VIEW_ZOOM_FILL = 'view-zoom-fill'

ICON_VISIBLE = 'gimp-visible'
ICON_WEB = 'gimp-web'
ICON_WILBER = 'gimp-wilber'

ICON_WILBER_EEK = 'gimp-wilber-eek'

ICON_WINDOW_CLOSE = 'window-close'

ICON_WINDOW_MOVE_TO_SCREEN = 'gimp-move-to-screen'

ICON_WINDOW_NEW = 'window-new'

ICON_ZOOM_FIT_BEST = 'zoom-fit-best'

ICON_ZOOM_FOLLOW_WINDOW = 'gimp-zoom-follow-window'

ICON_ZOOM_IN = 'zoom-in'
ICON_ZOOM_ORIGINAL = 'zoom-original'
ICON_ZOOM_OUT = 'zoom-out'

_namespace = 'GimpUi'

_version = '3.0'

# functions

def cairo_set_focus_line_pattern(cr, widget): # real signature unknown; restored from __doc__
    """ cairo_set_focus_line_pattern(cr:cairo.Context, widget:Gtk.Widget) -> bool """
    return False

def cairo_set_source_color(cr, color, config, softproof, widget=None): # real signature unknown; restored from __doc__
    """ cairo_set_source_color(cr:cairo.Context, color:Gegl.Color, config:Gimp.ColorConfig, softproof:bool, widget:Gtk.Widget=None) """
    pass

def cairo_surface_create_from_pixbuf(pixbuf): # real signature unknown; restored from __doc__
    """ cairo_surface_create_from_pixbuf(pixbuf:GdkPixbuf.Pixbuf) -> cairo.Surface """
    pass

def context_help(widget): # real signature unknown; restored from __doc__
    """ context_help(widget:Gtk.Widget) """
    pass

def coordinates_new(unit, unit_format, menu_show_pixels, menu_show_percent, spinbutton_width, update_policy, chainbutton_active, chain_constrains_ratio, xlabel, x, xres, lower_boundary_x, upper_boundary_x, xsize_0, xsize_100, ylabel, y, yres, lower_boundary_y, upper_boundary_y, ysize_0, ysize_100): # real signature unknown; restored from __doc__
    """ coordinates_new(unit:Gimp.Unit, unit_format:str, menu_show_pixels:bool, menu_show_percent:bool, spinbutton_width:int, update_policy:GimpUi.SizeEntryUpdatePolicy, chainbutton_active:bool, chain_constrains_ratio:bool, xlabel:str, x:float, xres:float, lower_boundary_x:float, upper_boundary_x:float, xsize_0:float, xsize_100:float, ylabel:str, y:float, yres:float, lower_boundary_y:float, upper_boundary_y:float, ysize_0:float, ysize_100:float) -> Gtk.Widget """
    pass

def double_adjustment_update(adjustment): # real signature unknown; restored from __doc__
    """ double_adjustment_update(adjustment:Gtk.Adjustment) -> data:float """
    pass

def enum_icon_box_new(enum_type, icon_prefix, icon_size, callback=None, callback_data=None): # real signature unknown; restored from __doc__
    """ enum_icon_box_new(enum_type:GType, icon_prefix:str, icon_size:Gtk.IconSize, callback:GObject.Callback=None, callback_data=None) -> Gtk.Widget, first_button:Gtk.Widget """
    pass

def enum_icon_box_new_with_range(enum_type, minimum, maximum, icon_prefix, icon_size, callback=None, callback_data=None): # real signature unknown; restored from __doc__
    """ enum_icon_box_new_with_range(enum_type:GType, minimum:int, maximum:int, icon_prefix:str, icon_size:Gtk.IconSize, callback:GObject.Callback=None, callback_data=None) -> Gtk.Widget, first_button:Gtk.Widget """
    pass

def enum_icon_box_set_child_padding(icon_box, xpad, ypad): # real signature unknown; restored from __doc__
    """ enum_icon_box_set_child_padding(icon_box:Gtk.Widget, xpad:int, ypad:int) """
    pass

def enum_icon_box_set_icon_size(icon_box, icon_size): # real signature unknown; restored from __doc__
    """ enum_icon_box_set_icon_size(icon_box:Gtk.Widget, icon_size:Gtk.IconSize) """
    pass

def enum_radio_box_new(enum_type, callback=None, callback_data=None): # real signature unknown; restored from __doc__
    """ enum_radio_box_new(enum_type:GType, callback:GObject.Callback=None, callback_data=None) -> Gtk.Widget, first_button:Gtk.Widget """
    pass

def enum_radio_box_new_with_range(enum_type, minimum, maximum, callback=None, callback_data=None): # real signature unknown; restored from __doc__
    """ enum_radio_box_new_with_range(enum_type:GType, minimum:int, maximum:int, callback:GObject.Callback=None, callback_data=None) -> Gtk.Widget, first_button:Gtk.Widget """
    pass

def enum_radio_frame_new(enum_type, label_widget=None, callback=None, callback_data=None): # real signature unknown; restored from __doc__
    """ enum_radio_frame_new(enum_type:GType, label_widget:Gtk.Widget=None, callback:GObject.Callback=None, callback_data=None) -> Gtk.Widget, first_button:Gtk.Widget """
    pass

def enum_radio_frame_new_with_range(enum_type, minimum, maximum, label_widget=None, callback=None, callback_data=None): # real signature unknown; restored from __doc__
    """ enum_radio_frame_new_with_range(enum_type:GType, minimum:int, maximum:int, label_widget:Gtk.Widget=None, callback:GObject.Callback=None, callback_data=None) -> Gtk.Widget, first_button:Gtk.Widget """
    pass

def event_triggers_context_menu(event, on_release): # real signature unknown; restored from __doc__
    """ event_triggers_context_menu(event:Gdk.Event, on_release:bool) -> bool """
    return False

def float_adjustment_update(adjustment): # real signature unknown; restored from __doc__
    """ float_adjustment_update(adjustment:Gtk.Adjustment) -> data:float """
    pass

def get_monitor_at_pointer(): # real signature unknown; restored from __doc__
    """ get_monitor_at_pointer() -> Gdk.Monitor """
    pass

def grid_attach_aligned(grid, left, top, label_text, label_xalign, label_yalign, widget, widget_columns): # real signature unknown; restored from __doc__
    """ grid_attach_aligned(grid:Gtk.Grid, left:int, top:int, label_text:str, label_xalign:float, label_yalign:float, widget:Gtk.Widget, widget_columns:int) -> Gtk.Widget """
    pass

def help_connect(widget, tooltip=None, help_func, help_id, help_data=None): # real signature unknown; restored from __doc__
    """ help_connect(widget:Gtk.Widget, tooltip:str=None, help_func:GimpUi.HelpFunc, help_id:str, help_data=None) """
    pass

def help_id_quark(): # real signature unknown; restored from __doc__
    """ help_id_quark() -> int """
    return 0

def help_set_help_data(widget, tooltip=None, help_id): # real signature unknown; restored from __doc__
    """ help_set_help_data(widget:Gtk.Widget, tooltip:str=None, help_id:str) """
    pass

def help_set_help_data_with_markup(widget, tooltip, help_id): # real signature unknown; restored from __doc__
    """ help_set_help_data_with_markup(widget:Gtk.Widget, tooltip:str, help_id:str) """
    pass

def icons_init(): # real signature unknown; restored from __doc__
    """ icons_init() """
    pass

def icons_set_icon_theme(path): # real signature unknown; restored from __doc__
    """ icons_set_icon_theme(path:Gio.File) -> bool """
    return False

def init(prog_name): # real signature unknown; restored from __doc__
    """ init(prog_name:str) """
    pass

def int_adjustment_update(adjustment): # real signature unknown; restored from __doc__
    """ int_adjustment_update(adjustment:Gtk.Adjustment) -> data:int """
    pass

def int_radio_group_set_active(radio_button, item_data): # real signature unknown; restored from __doc__
    """ int_radio_group_set_active(radio_button:Gtk.RadioButton, item_data:int) """
    pass

def monitor_get_color_profile(monitor): # real signature unknown; restored from __doc__
    """ monitor_get_color_profile(monitor:Gdk.Monitor) -> Gimp.ColorProfile or None """
    pass

def proc_view_new(procedure_name): # real signature unknown; restored from __doc__
    """ proc_view_new(procedure_name:str) -> Gtk.Widget """
    pass

def prop_boolean_combo_box_new(config, property_name, true_text, false_text): # real signature unknown; restored from __doc__
    """ prop_boolean_combo_box_new(config:GObject.Object, property_name:str, true_text:str, false_text:str) -> Gtk.Widget """
    pass

def prop_boolean_radio_frame_new(config, property_name, title=None, true_text, false_text): # real signature unknown; restored from __doc__
    """ prop_boolean_radio_frame_new(config:GObject.Object, property_name:str, title:str=None, true_text:str, false_text:str) -> Gtk.Widget """
    pass

def prop_brush_chooser_new(config, property_name, chooser_title=None): # real signature unknown; restored from __doc__
    """ prop_brush_chooser_new(config:GObject.Object, property_name:str, chooser_title:str=None) -> Gtk.Widget """
    pass

def prop_check_button_new(config, property_name, label=None): # real signature unknown; restored from __doc__
    """ prop_check_button_new(config:GObject.Object, property_name:str, label:str=None) -> Gtk.Widget """
    pass

def prop_choice_combo_box_new(config, property_name): # real signature unknown; restored from __doc__
    """ prop_choice_combo_box_new(config:GObject.Object, property_name:str) -> Gtk.Widget """
    pass

def prop_choice_radio_frame_new(config, property_name): # real signature unknown; restored from __doc__
    """ prop_choice_radio_frame_new(config:GObject.Object, property_name:str) -> Gtk.Widget """
    pass

def prop_color_area_new(config, property_name, width, height, type): # real signature unknown; restored from __doc__
    """ prop_color_area_new(config:GObject.Object, property_name:str, width:int, height:int, type:GimpUi.ColorAreaType) -> Gtk.Widget """
    pass

def prop_color_select_new(config, property_name, width, height, type): # real signature unknown; restored from __doc__
    """ prop_color_select_new(config:GObject.Object, property_name:str, width:int, height:int, type:GimpUi.ColorAreaType) -> Gtk.Widget """
    pass

def prop_coordinates_connect(config, x_property_name, y_property_name, unit_property_name, sizeentry, chainbutton, xresolution, yresolution): # real signature unknown; restored from __doc__
    """ prop_coordinates_connect(config:GObject.Object, x_property_name:str, y_property_name:str, unit_property_name:str, sizeentry:Gtk.Widget, chainbutton:Gtk.Widget, xresolution:float, yresolution:float) -> bool """
    return False

def prop_coordinates_new(config, x_property_name, y_property_name, unit_property_name, unit_format, update_policy, xresolution, yresolution, has_chainbutton): # real signature unknown; restored from __doc__
    """ prop_coordinates_new(config:GObject.Object, x_property_name:str, y_property_name:str, unit_property_name:str, unit_format:str, update_policy:GimpUi.SizeEntryUpdatePolicy, xresolution:float, yresolution:float, has_chainbutton:bool) -> Gtk.Widget """
    pass

def prop_drawable_chooser_new(config, property_name, chooser_title=None): # real signature unknown; restored from __doc__
    """ prop_drawable_chooser_new(config:GObject.Object, property_name:str, chooser_title:str=None) -> Gtk.Widget """
    pass

def prop_entry_new(config, property_name, max_len): # real signature unknown; restored from __doc__
    """ prop_entry_new(config:GObject.Object, property_name:str, max_len:int) -> Gtk.Widget """
    pass

def prop_enum_check_button_new(config, property_name, label=None, false_value, true_value): # real signature unknown; restored from __doc__
    """ prop_enum_check_button_new(config:GObject.Object, property_name:str, label:str=None, false_value:int, true_value:int) -> Gtk.Widget """
    pass

def prop_enum_combo_box_new(config, property_name, minimum, maximum): # real signature unknown; restored from __doc__
    """ prop_enum_combo_box_new(config:GObject.Object, property_name:str, minimum:int, maximum:int) -> Gtk.Widget """
    pass

def prop_enum_icon_box_new(config, property_name, icon_prefix, minimum, maximum): # real signature unknown; restored from __doc__
    """ prop_enum_icon_box_new(config:GObject.Object, property_name:str, icon_prefix:str, minimum:int, maximum:int) -> Gtk.Widget """
    pass

def prop_enum_label_new(config, property_name): # real signature unknown; restored from __doc__
    """ prop_enum_label_new(config:GObject.Object, property_name:str) -> Gtk.Widget """
    pass

def prop_enum_radio_box_new(config, property_name, minimum, maximum): # real signature unknown; restored from __doc__
    """ prop_enum_radio_box_new(config:GObject.Object, property_name:str, minimum:int, maximum:int) -> Gtk.Widget """
    pass

def prop_enum_radio_frame_new(config, property_name, title=None, minimum, maximum): # real signature unknown; restored from __doc__
    """ prop_enum_radio_frame_new(config:GObject.Object, property_name:str, title:str=None, minimum:int, maximum:int) -> Gtk.Widget """
    pass

def prop_expander_new(config, property_name, label=None): # real signature unknown; restored from __doc__
    """ prop_expander_new(config:GObject.Object, property_name:str, label:str=None) -> Gtk.Widget """
    pass

def prop_file_chooser_button_new(config, property_name, title=None, action): # real signature unknown; restored from __doc__
    """ prop_file_chooser_button_new(config:GObject.Object, property_name:str, title:str=None, action:Gtk.FileChooserAction) -> Gtk.Widget """
    pass

def prop_file_chooser_button_new_with_dialog(config, property_name, dialog): # real signature unknown; restored from __doc__
    """ prop_file_chooser_button_new_with_dialog(config:GObject.Object, property_name:str, dialog:Gtk.Widget) -> Gtk.Widget """
    pass

def prop_file_chooser_new(config, property_name, label=None, title=None): # real signature unknown; restored from __doc__
    """ prop_file_chooser_new(config:GObject.Object, property_name:str, label:str=None, title:str=None) -> Gtk.Widget """
    pass

def prop_font_chooser_new(config, property_name, chooser_title=None): # real signature unknown; restored from __doc__
    """ prop_font_chooser_new(config:GObject.Object, property_name:str, chooser_title:str=None) -> Gtk.Widget """
    pass

def prop_gradient_chooser_new(config, property_name, chooser_title=None): # real signature unknown; restored from __doc__
    """ prop_gradient_chooser_new(config:GObject.Object, property_name:str, chooser_title:str=None) -> Gtk.Widget """
    pass

def prop_hscale_new(config, property_name, step_increment, page_increment, digits): # real signature unknown; restored from __doc__
    """ prop_hscale_new(config:GObject.Object, property_name:str, step_increment:float, page_increment:float, digits:int) -> Gtk.Widget """
    pass

def prop_icon_image_new(config, property_name, icon_size): # real signature unknown; restored from __doc__
    """ prop_icon_image_new(config:GObject.Object, property_name:str, icon_size:Gtk.IconSize) -> Gtk.Widget """
    pass

def prop_image_chooser_new(config, property_name, chooser_title=None): # real signature unknown; restored from __doc__
    """ prop_image_chooser_new(config:GObject.Object, property_name:str, chooser_title:str=None) -> Gtk.Widget """
    pass

def prop_int_combo_box_new(config, property_name, store): # real signature unknown; restored from __doc__
    """ prop_int_combo_box_new(config:GObject.Object, property_name:str, store:GimpUi.IntStore) -> Gtk.Widget """
    pass

def prop_int_radio_frame_new(config, property_name, title=None, store): # real signature unknown; restored from __doc__
    """ prop_int_radio_frame_new(config:GObject.Object, property_name:str, title:str=None, store:GimpUi.IntStore) -> Gtk.Widget """
    pass

def prop_item_chooser_new(config, property_name, chooser_title=None): # real signature unknown; restored from __doc__
    """ prop_item_chooser_new(config:GObject.Object, property_name:str, chooser_title:str=None) -> Gtk.Widget """
    pass

def prop_label_color_new(config, property_name, editable): # real signature unknown; restored from __doc__
    """ prop_label_color_new(config:GObject.Object, property_name:str, editable:bool) -> Gtk.Widget """
    pass

def prop_label_entry_new(config, property_name, max_len): # real signature unknown; restored from __doc__
    """ prop_label_entry_new(config:GObject.Object, property_name:str, max_len:int) -> Gtk.Widget """
    pass

def prop_label_new(config, property_name): # real signature unknown; restored from __doc__
    """ prop_label_new(config:GObject.Object, property_name:str) -> Gtk.Widget """
    pass

def prop_label_spin_new(config, property_name, digits): # real signature unknown; restored from __doc__
    """ prop_label_spin_new(config:GObject.Object, property_name:str, digits:int) -> Gtk.Widget """
    pass

def prop_memsize_entry_new(config, property_name): # real signature unknown; restored from __doc__
    """ prop_memsize_entry_new(config:GObject.Object, property_name:str) -> Gtk.Widget """
    pass

def prop_palette_chooser_new(config, property_name, chooser_title=None): # real signature unknown; restored from __doc__
    """ prop_palette_chooser_new(config:GObject.Object, property_name:str, chooser_title:str=None) -> Gtk.Widget """
    pass

def prop_path_editor_new(config, path_property_name, writable_property_name, filechooser_title): # real signature unknown; restored from __doc__
    """ prop_path_editor_new(config:GObject.Object, path_property_name:str, writable_property_name:str, filechooser_title:str) -> Gtk.Widget """
    pass

def prop_pattern_chooser_new(config, property_name, chooser_title=None): # real signature unknown; restored from __doc__
    """ prop_pattern_chooser_new(config:GObject.Object, property_name:str, chooser_title:str=None) -> Gtk.Widget """
    pass

def prop_pointer_combo_box_new(config, property_name, store): # real signature unknown; restored from __doc__
    """ prop_pointer_combo_box_new(config:GObject.Object, property_name:str, store:GimpUi.IntStore) -> Gtk.Widget """
    pass

def prop_scale_entry_new(config, property_name, label=None, factor, limit_scale, lower_limit, upper_limit): # real signature unknown; restored from __doc__
    """ prop_scale_entry_new(config:GObject.Object, property_name:str, label:str=None, factor:float, limit_scale:bool, lower_limit:float, upper_limit:float) -> Gtk.Widget """
    pass

def prop_size_entry_new(config, property_name, property_is_pixel, unit_property_name, unit_format, update_policy, resolution): # real signature unknown; restored from __doc__
    """ prop_size_entry_new(config:GObject.Object, property_name:str, property_is_pixel:bool, unit_property_name:str, unit_format:str, update_policy:GimpUi.SizeEntryUpdatePolicy, resolution:float) -> Gtk.Widget """
    pass

def prop_spin_button_new(config, property_name, step_increment, page_increment, digits): # real signature unknown; restored from __doc__
    """ prop_spin_button_new(config:GObject.Object, property_name:str, step_increment:float, page_increment:float, digits:int) -> Gtk.Widget """
    pass

def prop_spin_scale_new(config, property_name, step_increment, page_increment, digits): # real signature unknown; restored from __doc__
    """ prop_spin_scale_new(config:GObject.Object, property_name:str, step_increment:float, page_increment:float, digits:int) -> Gtk.Widget """
    pass

def prop_string_combo_box_new(config, property_name, model, id_column, label_column): # real signature unknown; restored from __doc__
    """ prop_string_combo_box_new(config:GObject.Object, property_name:str, model:Gtk.TreeModel, id_column:int, label_column:int) -> Gtk.Widget """
    pass

def prop_switch_new(config, property_name, label): # real signature unknown; restored from __doc__
    """ prop_switch_new(config:GObject.Object, property_name:str, label:str) -> Gtk.Widget, label_out:Gtk.Widget, switch_out:Gtk.Widget """
    pass

def prop_text_buffer_new(config, property_name, max_len): # real signature unknown; restored from __doc__
    """ prop_text_buffer_new(config:GObject.Object, property_name:str, max_len:int) -> Gtk.TextBuffer """
    pass

def prop_toggle_new(config, property_name, icon_name, label): # real signature unknown; restored from __doc__
    """ prop_toggle_new(config:GObject.Object, property_name:str, icon_name:str, label:str) -> Gtk.Widget, image_out:Gtk.Widget """
    pass

def prop_unit_combo_box_new(config, property_name): # real signature unknown; restored from __doc__
    """ prop_unit_combo_box_new(config:GObject.Object, property_name:str) -> Gtk.Widget """
    pass

def prop_widget_set_factor(widget, factor, step_increment, page_increment, digits): # real signature unknown; restored from __doc__
    """ prop_widget_set_factor(widget:Gtk.Widget, factor:float, step_increment:float, page_increment:float, digits:int) """
    pass

def query_boolean_box(title, parent, help_func, help_id, icon_name, message, true_button, false_button, p_object, signal, callback, data=None): # real signature unknown; restored from __doc__
    """ query_boolean_box(title:str, parent:Gtk.Widget, help_func:GimpUi.HelpFunc, help_id:str, icon_name:str, message:str, true_button:str, false_button:str, object:GObject.Object, signal:str, callback:GimpUi.QueryBooleanCallback, data=None) -> Gtk.Widget """
    pass

def query_double_box(title, parent, help_func, help_id, message, initial, lower, upper, digits, p_object, signal, callback, data=None): # real signature unknown; restored from __doc__
    """ query_double_box(title:str, parent:Gtk.Widget, help_func:GimpUi.HelpFunc, help_id:str, message:str, initial:float, lower:float, upper:float, digits:int, object:GObject.Object, signal:str, callback:GimpUi.QueryDoubleCallback, data=None) -> Gtk.Widget """
    pass

def query_int_box(title, parent, help_func, help_id, message, initial, lower, upper, p_object, signal, callback, data=None): # real signature unknown; restored from __doc__
    """ query_int_box(title:str, parent:Gtk.Widget, help_func:GimpUi.HelpFunc, help_id:str, message:str, initial:int, lower:int, upper:int, object:GObject.Object, signal:str, callback:GimpUi.QueryIntCallback, data=None) -> Gtk.Widget """
    pass

def query_size_box(title, parent, help_func, help_id, message, initial, lower, upper, digits, unit, resolution, dot_for_dot, p_object, signal, callback, data=None): # real signature unknown; restored from __doc__
    """ query_size_box(title:str, parent:Gtk.Widget, help_func:GimpUi.HelpFunc, help_id:str, message:str, initial:float, lower:float, upper:float, digits:int, unit:Gimp.Unit, resolution:float, dot_for_dot:bool, object:GObject.Object, signal:str, callback:GimpUi.QuerySizeCallback, data=None) -> Gtk.Widget """
    pass

def query_string_box(title, parent, help_func, help_id, message, initial, p_object, signal, callback, data=None): # real signature unknown; restored from __doc__
    """ query_string_box(title:str, parent:Gtk.Widget, help_func:GimpUi.HelpFunc, help_id:str, message:str, initial:str, object:GObject.Object, signal:str, callback:GimpUi.QueryStringCallback, data=None) -> Gtk.Widget """
    pass

def radio_button_update(widget): # real signature unknown; restored from __doc__
    """ radio_button_update(widget:Gtk.Widget) -> data:int """
    pass

def random_seed_new(seed, random_seed): # real signature unknown; restored from __doc__
    """ random_seed_new(seed:int, random_seed:bool) -> Gtk.Widget """
    pass

def scroll_adjustment_values(sevent, hadj=None, vadj=None): # real signature unknown; restored from __doc__
    """ scroll_adjustment_values(sevent:Gdk.EventScroll, hadj:Gtk.Adjustment=None, vadj:Gtk.Adjustment=None) -> hvalue:float, vvalue:float """
    pass

def standard_help_func(help_id, help_data=None): # real signature unknown; restored from __doc__
    """ standard_help_func(help_id:str, help_data=None) """
    pass

def toggle_button_update(widget): # real signature unknown; restored from __doc__
    """ toggle_button_update(widget:Gtk.Widget) -> data:bool """
    pass

def uint_adjustment_update(adjustment): # real signature unknown; restored from __doc__
    """ uint_adjustment_update(adjustment:Gtk.Adjustment) -> data:int """
    pass

def widgets_error_quark(): # real signature unknown; restored from __doc__
    """ widgets_error_quark() -> int """
    return 0

def widget_animation_enabled(): # real signature unknown; restored from __doc__
    """ widget_animation_enabled() -> bool """
    return False

def widget_free_native_handle(widget, window_handle): # real signature unknown; restored from __doc__
    """ widget_free_native_handle(widget:Gtk.Widget, window_handle:GLib.Bytes) -> window_handle:GLib.Bytes """
    pass

def widget_get_color_profile(widget): # real signature unknown; restored from __doc__
    """ widget_get_color_profile(widget:Gtk.Widget) -> Gimp.ColorProfile or None """
    pass

def widget_get_color_transform(widget, config, src_profile, src_format, dest_format, softproof_profile, proof_intent, proof_bpc): # real signature unknown; restored from __doc__
    """ widget_get_color_transform(widget:Gtk.Widget, config:Gimp.ColorConfig, src_profile:Gimp.ColorProfile, src_format:Babl.Object, dest_format:Babl.Object, softproof_profile:Gimp.ColorProfile, proof_intent:Gimp.ColorRenderingIntent, proof_bpc:bool) -> Gimp.ColorTransform or None """
    pass

def widget_get_monitor(widget): # real signature unknown; restored from __doc__
    """ widget_get_monitor(widget:Gtk.Widget) -> Gdk.Monitor """
    pass

def widget_get_render_space(widget, config): # real signature unknown; restored from __doc__
    """ widget_get_render_space(widget:Gtk.Widget, config:Gimp.ColorConfig) -> Babl.Object """
    pass

def widget_set_native_handle(widget, window_handle): # real signature unknown; restored from __doc__
    """ widget_set_native_handle(widget:Gtk.Widget, window_handle:GLib.Bytes) -> window_handle:GLib.Bytes """
    pass

def widget_track_monitor(widget, monitor_changed_callback, user_data=None): # real signature unknown; restored from __doc__
    """ widget_track_monitor(widget:Gtk.Widget, monitor_changed_callback:GObject.Callback, user_data=None) """
    pass

def window_set_transient(window): # real signature unknown; restored from __doc__
    """ window_set_transient(window:Gtk.Window) """
    pass

def window_set_transient_for(window, handle): # real signature unknown; restored from __doc__
    """ window_set_transient_for(window:Gtk.Window, handle:GLib.Bytes) """
    pass

def window_set_transient_for_display(window, display): # real signature unknown; restored from __doc__
    """ window_set_transient_for_display(window:Gtk.Window, display:Gimp.Display) """
    pass

def zoom_button_new(model, zoom_type, icon_size): # real signature unknown; restored from __doc__
    """ zoom_button_new(model:GimpUi.ZoomModel, zoom_type:GimpUi.ZoomType, icon_size:Gtk.IconSize) -> Gtk.Widget """
    pass

# classes

from .Preview import Preview
from .AspectPreview import AspectPreview
from .AspectPreviewClass import AspectPreviewClass
from .AspectType import AspectType
from .Browser import Browser
from .BrowserClass import BrowserClass
from .ResourceChooser import ResourceChooser
from .BrushChooser import BrushChooser
from .BrushChooserClass import BrushChooserClass
from .BusyBox import BusyBox
from .BusyBoxClass import BusyBoxClass
from .Button import Button
from .ButtonClass import ButtonClass
from .CellRendererColor import CellRendererColor
from .CellRendererColorClass import CellRendererColorClass
from .CellRendererToggle import CellRendererToggle
from .CellRendererToggleClass import CellRendererToggleClass
from .ChainButton import ChainButton
from .ChainButtonClass import ChainButtonClass
from .ChainPosition import ChainPosition
from .IntComboBox import IntComboBox
from .ChannelComboBox import ChannelComboBox
from .ColorArea import ColorArea
from .ColorAreaClass import ColorAreaClass
from .ColorAreaType import ColorAreaType
from .ColorButton import ColorButton
from .ColorButtonClass import ColorButtonClass
from .ColorDisplay import ColorDisplay
from .ColorDisplayClass import ColorDisplayClass
from .ColorDisplayStack import ColorDisplayStack
from .ColorDisplayStackClass import ColorDisplayStackClass
from .ColorHexEntry import ColorHexEntry
from .ColorHexEntryClass import ColorHexEntryClass
from .ColorSelector import ColorSelector
from .ColorNotebook import ColorNotebook
from .ColorNotebookClass import ColorNotebookClass
from .ColorProfileChooserDialog import ColorProfileChooserDialog
from .ColorProfileChooserDialogClass import ColorProfileChooserDialogClass
from .ColorProfileComboBox import ColorProfileComboBox
from .ColorProfileComboBoxClass import ColorProfileComboBoxClass
from .ColorProfileStore import ColorProfileStore
from .ColorProfileStoreClass import ColorProfileStoreClass
from .ColorProfileView import ColorProfileView
from .ColorProfileViewClass import ColorProfileViewClass
from .ColorScale import ColorScale
from .ColorScaleClass import ColorScaleClass
from .Labeled import Labeled
from .LabelSpin import LabelSpin
from .ScaleEntry import ScaleEntry
from .ColorScaleEntry import ColorScaleEntry
from .ColorScaleEntryClass import ColorScaleEntryClass
from .ColorScales import ColorScales
from .ColorScalesClass import ColorScalesClass
from .ColorSelect import ColorSelect
from .ColorSelectClass import ColorSelectClass
from .ColorSelection import ColorSelection
from .ColorSelectionClass import ColorSelectionClass
from .ColorSelectorChannel import ColorSelectorChannel
from .ColorSelectorClass import ColorSelectorClass
from .ColorSelectorModel import ColorSelectorModel
from .Controller import Controller
from .Dialog import Dialog
from .DialogClass import DialogClass
from .DrawableChooser import DrawableChooser
from .DrawableChooserClass import DrawableChooserClass
from .DrawableComboBox import DrawableComboBox
from .ScrolledPreview import ScrolledPreview
from .DrawablePreview import DrawablePreview
from .DrawablePreviewClass import DrawablePreviewClass
from .EnumComboBox import EnumComboBox
from .EnumComboBoxClass import EnumComboBoxClass
from .EnumLabel import EnumLabel
from .EnumLabelClass import EnumLabelClass
from .IntStore import IntStore
from .EnumStore import EnumStore
from .EnumStoreClass import EnumStoreClass
from .ProcedureDialog import ProcedureDialog
from .ExportProcedureDialog import ExportProcedureDialog
from .ExportProcedureDialogClass import ExportProcedureDialogClass
from .FileChooser import FileChooser
from .FileChooserClass import FileChooserClass
from .FileEntry import FileEntry
from .FontChooser import FontChooser
from .FontChooserClass import FontChooserClass
from .Frame import Frame
from .FrameClass import FrameClass
from .GradientChooser import GradientChooser
from .GradientChooserClass import GradientChooserClass
from .HintBox import HintBox
from .HintBoxClass import HintBoxClass
from .ImageChooser import ImageChooser
from .ImageChooserClass import ImageChooserClass
from .ImageComboBox import ImageComboBox
from .ImageComboBoxClass import ImageComboBoxClass
from .IntComboBoxClass import IntComboBoxClass
from .IntComboBoxLayout import IntComboBoxLayout
from .IntRadioFrame import IntRadioFrame
from .IntRadioFrameClass import IntRadioFrameClass
from .IntStoreClass import IntStoreClass
from .IntStoreColumns import IntStoreColumns
from .ItemChooser import ItemChooser
from .ItemChooserClass import ItemChooserClass
from .LabelColor import LabelColor
from .LabelColorClass import LabelColorClass
from .LabeledClass import LabeledClass
from .LabelEntry import LabelEntry
from .LabelEntryClass import LabelEntryClass
from .LabelIntWidget import LabelIntWidget
from .LabelIntWidgetClass import LabelIntWidgetClass
from .LabelSpinClass import LabelSpinClass
from .LabelStringWidget import LabelStringWidget
from .LabelStringWidgetClass import LabelStringWidgetClass
from .LayerComboBox import LayerComboBox
from .MemsizeEntry import MemsizeEntry
from .MemsizeEntryClass import MemsizeEntryClass
from .NumberPairEntry import NumberPairEntry
from .NumberPairEntryClass import NumberPairEntryClass
from .OffsetArea import OffsetArea
from .OffsetAreaClass import OffsetAreaClass
from .PageSelector import PageSelector
from .PageSelectorClass import PageSelectorClass
from .PageSelectorTarget import PageSelectorTarget
from .PaletteChooser import PaletteChooser
from .PaletteChooserClass import PaletteChooserClass
from .PathComboBox import PathComboBox
from .PathEditor import PathEditor
from .PathEditorClass import PathEditorClass
from .PatternChooser import PatternChooser
from .PatternChooserClass import PatternChooserClass
from .PickButton import PickButton
from .PickButtonClass import PickButtonClass
from .PreviewArea import PreviewArea
from .PreviewAreaClass import PreviewAreaClass
from .PreviewClass import PreviewClass
from .ProcBrowserDialog import ProcBrowserDialog
from .ProcBrowserDialogClass import ProcBrowserDialogClass
from .ProcedureDialogClass import ProcedureDialogClass
from .ProgressBar import ProgressBar
from .ProgressBarClass import ProgressBarClass
from .ResourceChooserClass import ResourceChooserClass
from .Ruler import Ruler
from .RulerClass import RulerClass
from .ScaleEntryClass import ScaleEntryClass
from .ScrolledPreviewClass import ScrolledPreviewClass
from .SizeEntry import SizeEntry
from .SizeEntryClass import SizeEntryClass
from .SizeEntryUpdatePolicy import SizeEntryUpdatePolicy
from .SpinButton import SpinButton
from .SpinButtonClass import SpinButtonClass
from .SpinScale import SpinScale
from .SpinScaleClass import SpinScaleClass
from .StringComboBox import StringComboBox
from .StringComboBoxClass import StringComboBoxClass
from .UnitComboBox import UnitComboBox
from .UnitComboBoxClass import UnitComboBoxClass
from .UnitStore import UnitStore
from .UnitStoreClass import UnitStoreClass
from .VectorLoadProcedureDialog import VectorLoadProcedureDialog
from .VectorLoadProcedureDialogClass import VectorLoadProcedureDialogClass
from .WidgetsError import WidgetsError
from .ZoomModel import ZoomModel
from .ZoomModelClass import ZoomModelClass
from .ZoomPreview import ZoomPreview
from .ZoomPreviewClass import ZoomPreviewClass
from .ZoomType import ZoomType
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x0000020ede1b4440>'

__path__ = []

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GimpUi', loader=<gi.importer.DynamicImporter object at 0x0000020ede1b4440>)"

