# encoding: utf-8
# module gi.repository.Gimp
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GExiv2 as __gi_overrides_GExiv2
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


# Variables with simple values

API_VERSION = '3.0'

CHECK_DARK = 0.4
CHECK_LIGHT = 0.6
CHECK_SIZE = 8

CHECK_SIZE_SM = 4

CONFIG_PARAM_AGGREGATE = 2
CONFIG_PARAM_CONFIRM = 8
CONFIG_PARAM_DEFAULTS = 16

CONFIG_PARAM_DONT_COMPARE = 64

CONFIG_PARAM_FLAGS = 7

CONFIG_PARAM_FLAG_SHIFT = 7

CONFIG_PARAM_IGNORE = 32
CONFIG_PARAM_RESTART = 4
CONFIG_PARAM_SERIALIZE = 1

MAJOR_VERSION = 3

MAX_IMAGE_SIZE = 524288

MAX_MEMSIZE = 0
MAX_RESOLUTION = 1048576.0

MICRO_VERSION = 0

MINOR_VERSION = 2

MIN_IMAGE_SIZE = 1

MIN_RESOLUTION = 0.005

MODULE_ABI_VERSION = 5

PARAM_DONT_SERIALIZE = 2

PARAM_FLAG_SHIFT = 2

PARAM_NO_VALIDATE = 1

PARAM_READABLE = 1
PARAM_READWRITE = 3

PARAM_STATIC_STRINGS = 224

PARAM_WRITABLE = 2

PARASITE_ATTACH_GRANDPARENT = 8388608
PARASITE_ATTACH_PARENT = 32768

PARASITE_GRANDPARENT_PERSISTENT = 0
PARASITE_GRANDPARENT_UNDOABLE = 0

PARASITE_PARENT_PERSISTENT = 0
PARASITE_PARENT_UNDOABLE = 0

PARASITE_PERSISTENT = 1
PARASITE_UNDOABLE = 2

PIXPIPE_MAXDIM = 4

VERSION = '3.2.0-RC3'

_namespace = 'Gimp'

_version = '3.0'

# functions

def adaptive_supersample_area(x1, y1, x2, y2, max_depth, threshold, render_func, render_data=None, put_pixel_func, put_pixel_data=None, progress_func, progress_data=None): # real signature unknown; restored from __doc__
    """ adaptive_supersample_area(x1:int, y1:int, x2:int, y2:int, max_depth:int, threshold:float, render_func:Gimp.RenderFunc, render_data=None, put_pixel_func:Gimp.PutPixelFunc, put_pixel_data=None, progress_func:Gimp.ProgressFunc, progress_data=None) -> int """
    return 0

def airbrush(drawable, pressure, strokes): # real signature unknown; restored from __doc__
    """ airbrush(drawable:Gimp.Drawable, pressure:float, strokes:list) -> bool """
    return False

def airbrush_default(drawable, strokes): # real signature unknown; restored from __doc__
    """ airbrush_default(drawable:Gimp.Drawable, strokes:list) -> bool """
    return False

def attach_parasite(parasite): # real signature unknown; restored from __doc__
    """ attach_parasite(parasite:Gimp.Parasite) -> bool """
    return False

def babl_format_get_type(): # real signature unknown; restored from __doc__
    """ babl_format_get_type() -> GType """
    pass

def bilinear(x, y, values): # real signature unknown; restored from __doc__
    """ bilinear(x:float, y:float, values:list) -> float """
    return 0.0

def bilinear_16(x, y, values): # real signature unknown; restored from __doc__
    """ bilinear_16(x:float, y:float, values:list) -> int """
    return 0

def bilinear_32(x, y, values): # real signature unknown; restored from __doc__
    """ bilinear_32(x:float, y:float, values:list) -> int """
    return 0

def bilinear_8(x, y, values): # real signature unknown; restored from __doc__
    """ bilinear_8(x:float, y:float, values:list) -> int """
    return 0

def bilinear_rgb(x, y, values, has_alpha, retvalues): # real signature unknown; restored from __doc__
    """ bilinear_rgb(x:float, y:float, values:list, has_alpha:bool, retvalues:list) """
    pass

def bind_text_domain(domain_name, dir_name): # real signature unknown; restored from __doc__
    """ bind_text_domain(domain_name:str, dir_name:str) """
    pass

def brushes_close_popup(brush_callback): # real signature unknown; restored from __doc__
    """ brushes_close_popup(brush_callback:str) -> bool """
    return False

def brushes_get_list(filter): # real signature unknown; restored from __doc__
    """ brushes_get_list(filter:str) -> list """
    return []

def brushes_popup(brush_callback, popup_title, initial_brush=None, parent_window=None): # real signature unknown; restored from __doc__
    """ brushes_popup(brush_callback:str, popup_title:str, initial_brush:Gimp.Brush=None, parent_window:GLib.Bytes=None) -> bool """
    return False

def brushes_refresh(): # real signature unknown; restored from __doc__
    """ brushes_refresh() -> bool """
    return False

def brushes_set_popup(brush_callback, brush): # real signature unknown; restored from __doc__
    """ brushes_set_popup(brush_callback:str, brush:Gimp.Brush) -> bool """
    return False

def buffers_get_name_list(filter=None): # real signature unknown; restored from __doc__
    """ buffers_get_name_list(filter:str=None) -> list """
    return []

def buffer_delete(buffer_name): # real signature unknown; restored from __doc__
    """ buffer_delete(buffer_name:str) -> bool """
    return False

def buffer_get_bytes(buffer_name): # real signature unknown; restored from __doc__
    """ buffer_get_bytes(buffer_name:str) -> int """
    return 0

def buffer_get_height(buffer_name): # real signature unknown; restored from __doc__
    """ buffer_get_height(buffer_name:str) -> int """
    return 0

def buffer_get_image_type(buffer_name): # real signature unknown; restored from __doc__
    """ buffer_get_image_type(buffer_name:str) -> Gimp.ImageType """
    pass

def buffer_get_width(buffer_name): # real signature unknown; restored from __doc__
    """ buffer_get_width(buffer_name:str) -> int """
    return 0

def buffer_rename(buffer_name, new_name): # real signature unknown; restored from __doc__
    """ buffer_rename(buffer_name:str, new_name:str) -> str """
    return ""

def cache_directory(): # real signature unknown; restored from __doc__
    """ cache_directory() -> str """
    return ""

def cairo_checkerboard_create(cr, size, light, dark): # real signature unknown; restored from __doc__
    """ cairo_checkerboard_create(cr:cairo.Context, size:int, light:Gegl.Color, dark:Gegl.Color) -> cairo.Pattern """
    pass

def cairo_surface_create_buffer(surface, format): # real signature unknown; restored from __doc__
    """ cairo_surface_create_buffer(surface:cairo.Surface, format:Babl.Object) -> Gegl.Buffer """
    pass

def cairo_surface_get_buffer(surface, format, sync_back): # real signature unknown; restored from __doc__
    """ cairo_surface_get_buffer(surface:cairo.Surface, format:Babl.Object, sync_back:bool) -> Gegl.Buffer """
    pass

def cairo_surface_get_format(surface): # real signature unknown; restored from __doc__
    """ cairo_surface_get_format(surface:cairo.Surface) -> Babl.Object """
    pass

def canonicalize_identifier(identifier): # real signature unknown; restored from __doc__
    """ canonicalize_identifier(identifier:str) -> str """
    return ""

def checks_get_colors(type, color1, color2): # real signature unknown; restored from __doc__
    """ checks_get_colors(type:Gimp.CheckType, color1:Gegl.Color, color2:Gegl.Color) -> color1:Gegl.Color, color2:Gegl.Color """
    pass

def check_custom_color1(): # real signature unknown; restored from __doc__
    """ check_custom_color1() -> Gegl.Color """
    pass

def check_custom_color2(): # real signature unknown; restored from __doc__
    """ check_custom_color2() -> Gegl.Color """
    pass

def check_size(): # real signature unknown; restored from __doc__
    """ check_size() -> Gimp.CheckSize """
    pass

def check_type(): # real signature unknown; restored from __doc__
    """ check_type() -> Gimp.CheckType """
    pass

def clone(drawable, src_drawable, clone_type, src_x, src_y, strokes): # real signature unknown; restored from __doc__
    """ clone(drawable:Gimp.Drawable, src_drawable:Gimp.Drawable, clone_type:Gimp.CloneType, src_x:float, src_y:float, strokes:list) -> bool """
    return False

def clone_default(drawable, strokes): # real signature unknown; restored from __doc__
    """ clone_default(drawable:Gimp.Drawable, strokes:list) -> bool """
    return False

def color_array_copy(array): # real signature unknown; restored from __doc__
    """ color_array_copy(array:Gegl.Color) -> Gegl.Color """
    pass

def color_array_free(array): # real signature unknown; restored from __doc__
    """ color_array_free(array:Gegl.Color) """
    pass

def color_array_get_length(array): # real signature unknown; restored from __doc__
    """ color_array_get_length(array:Gegl.Color) -> int """
    return 0

def color_array_get_type(): # real signature unknown; restored from __doc__
    """ color_array_get_type() -> GType """
    pass

def color_is_out_of_gamut(color, space): # real signature unknown; restored from __doc__
    """ color_is_out_of_gamut(color:Gegl.Color, space:Babl.Object) -> bool """
    return False

def color_is_out_of_self_gamut(color): # real signature unknown; restored from __doc__
    """ color_is_out_of_self_gamut(color:Gegl.Color) -> bool """
    return False

def color_is_perceptually_identical(color1, color2): # real signature unknown; restored from __doc__
    """ color_is_perceptually_identical(color1:Gegl.Color, color2:Gegl.Color) -> bool """
    return False

def color_list_names(): # real signature unknown; restored from __doc__
    """ color_list_names() -> list, colors:list """
    return []

def color_parse_css(css): # real signature unknown; restored from __doc__
    """ color_parse_css(css:str) -> Gegl.Color """
    pass

def color_parse_hex(hex): # real signature unknown; restored from __doc__
    """ color_parse_hex(hex:str) -> Gegl.Color """
    pass

def color_parse_name(name): # real signature unknown; restored from __doc__
    """ color_parse_name(name:str) -> Gegl.Color """
    pass

def color_set_alpha(color, alpha): # real signature unknown; restored from __doc__
    """ color_set_alpha(color:Gegl.Color, alpha:float) """
    pass

def config_build_data_path(name): # real signature unknown; restored from __doc__
    """ config_build_data_path(name:str) -> str """
    return ""

def config_build_plug_in_path(name): # real signature unknown; restored from __doc__
    """ config_build_plug_in_path(name:str) -> str """
    return ""

def config_build_system_path(name): # real signature unknown; restored from __doc__
    """ config_build_system_path(name:str) -> str """
    return ""

def config_build_writable_path(name): # real signature unknown; restored from __doc__
    """ config_build_writable_path(name:str) -> str """
    return ""

def config_deserialize_return(scanner, expected_token, nest_level): # real signature unknown; restored from __doc__
    """ config_deserialize_return(scanner:GLib.Scanner, expected_token:GLib.TokenType, nest_level:int) -> bool """
    return False

def config_diff(a, b, flags): # real signature unknown; restored from __doc__
    """ config_diff(a:GObject.Object, b:GObject.Object, flags:GObject.ParamFlags) -> list """
    return []

def config_error_quark(): # real signature unknown; restored from __doc__
    """ config_error_quark() -> int """
    return 0

def config_param_spec_duplicate(pspec): # real signature unknown; restored from __doc__
    """ config_param_spec_duplicate(pspec:GObject.ParamSpec) -> GObject.ParamSpec """
    pass

def config_reset_properties(p_object): # real signature unknown; restored from __doc__
    """ config_reset_properties(object:GObject.Object) """
    pass

def config_reset_property(p_object, property_name): # real signature unknown; restored from __doc__
    """ config_reset_property(object:GObject.Object, property_name:str) """
    pass

def config_serialize_value(value, p_str, escaped): # real signature unknown; restored from __doc__
    """ config_serialize_value(value:GObject.Value, str:GLib.String, escaped:bool) -> bool """
    return False

def config_string_append_escaped(string, val): # real signature unknown; restored from __doc__
    """ config_string_append_escaped(string:GLib.String, val:str) """
    pass

def config_sync(src, dest, flags): # real signature unknown; restored from __doc__
    """ config_sync(src:GObject.Object, dest:GObject.Object, flags:GObject.ParamFlags) -> bool """
    return False

def config_type_register(parent_type, type_name, pspecs): # real signature unknown; restored from __doc__
    """ config_type_register(parent_type:GType, type_name:str, pspecs:list) -> GType """
    pass

def context_are_dynamics_enabled(): # real signature unknown; restored from __doc__
    """ context_are_dynamics_enabled() -> bool """
    return False

def context_enable_dynamics(enable): # real signature unknown; restored from __doc__
    """ context_enable_dynamics(enable:bool) -> bool """
    return False

def context_get_antialias(): # real signature unknown; restored from __doc__
    """ context_get_antialias() -> bool """
    return False

def context_get_background(): # real signature unknown; restored from __doc__
    """ context_get_background() -> Gegl.Color """
    pass

def context_get_brush(): # real signature unknown; restored from __doc__
    """ context_get_brush() -> Gimp.Brush """
    pass

def context_get_brush_angle(): # real signature unknown; restored from __doc__
    """ context_get_brush_angle() -> float """
    return 0.0

def context_get_brush_aspect_ratio(): # real signature unknown; restored from __doc__
    """ context_get_brush_aspect_ratio() -> float """
    return 0.0

def context_get_brush_force(): # real signature unknown; restored from __doc__
    """ context_get_brush_force() -> float """
    return 0.0

def context_get_brush_hardness(): # real signature unknown; restored from __doc__
    """ context_get_brush_hardness() -> float """
    return 0.0

def context_get_brush_size(): # real signature unknown; restored from __doc__
    """ context_get_brush_size() -> float """
    return 0.0

def context_get_brush_spacing(): # real signature unknown; restored from __doc__
    """ context_get_brush_spacing() -> float """
    return 0.0

def context_get_diagonal_neighbors(): # real signature unknown; restored from __doc__
    """ context_get_diagonal_neighbors() -> bool """
    return False

def context_get_distance_metric(): # real signature unknown; restored from __doc__
    """ context_get_distance_metric() -> Gegl.DistanceMetric """
    pass

def context_get_dynamics_name(): # real signature unknown; restored from __doc__
    """ context_get_dynamics_name() -> str """
    return ""

def context_get_emulate_brush_dynamics(): # real signature unknown; restored from __doc__
    """ context_get_emulate_brush_dynamics() -> bool """
    return False

def context_get_feather(): # real signature unknown; restored from __doc__
    """ context_get_feather() -> bool """
    return False

def context_get_feather_radius(): # real signature unknown; restored from __doc__
    """ context_get_feather_radius() -> bool, feather_radius_x:float, feather_radius_y:float """
    return False

def context_get_font(): # real signature unknown; restored from __doc__
    """ context_get_font() -> Gimp.Font """
    pass

def context_get_foreground(): # real signature unknown; restored from __doc__
    """ context_get_foreground() -> Gegl.Color """
    pass

def context_get_gradient(): # real signature unknown; restored from __doc__
    """ context_get_gradient() -> Gimp.Gradient """
    pass

def context_get_gradient_blend_color_space(): # real signature unknown; restored from __doc__
    """ context_get_gradient_blend_color_space() -> Gimp.GradientBlendColorSpace """
    pass

def context_get_gradient_repeat_mode(): # real signature unknown; restored from __doc__
    """ context_get_gradient_repeat_mode() -> Gimp.RepeatMode """
    pass

def context_get_gradient_reverse(): # real signature unknown; restored from __doc__
    """ context_get_gradient_reverse() -> bool """
    return False

def context_get_ink_angle(): # real signature unknown; restored from __doc__
    """ context_get_ink_angle() -> float """
    return 0.0

def context_get_ink_blob_angle(): # real signature unknown; restored from __doc__
    """ context_get_ink_blob_angle() -> float """
    return 0.0

def context_get_ink_blob_aspect_ratio(): # real signature unknown; restored from __doc__
    """ context_get_ink_blob_aspect_ratio() -> float """
    return 0.0

def context_get_ink_blob_type(): # real signature unknown; restored from __doc__
    """ context_get_ink_blob_type() -> Gimp.InkBlobType """
    pass

def context_get_ink_size(): # real signature unknown; restored from __doc__
    """ context_get_ink_size() -> float """
    return 0.0

def context_get_ink_size_sensitivity(): # real signature unknown; restored from __doc__
    """ context_get_ink_size_sensitivity() -> float """
    return 0.0

def context_get_ink_speed_sensitivity(): # real signature unknown; restored from __doc__
    """ context_get_ink_speed_sensitivity() -> float """
    return 0.0

def context_get_ink_tilt_sensitivity(): # real signature unknown; restored from __doc__
    """ context_get_ink_tilt_sensitivity() -> float """
    return 0.0

def context_get_interpolation(): # real signature unknown; restored from __doc__
    """ context_get_interpolation() -> Gimp.InterpolationType """
    pass

def context_get_line_cap_style(): # real signature unknown; restored from __doc__
    """ context_get_line_cap_style() -> Gimp.CapStyle """
    pass

def context_get_line_dash_offset(): # real signature unknown; restored from __doc__
    """ context_get_line_dash_offset() -> float """
    return 0.0

def context_get_line_dash_pattern(): # real signature unknown; restored from __doc__
    """ context_get_line_dash_pattern() -> bool, dashes:list """
    return False

def context_get_line_join_style(): # real signature unknown; restored from __doc__
    """ context_get_line_join_style() -> Gimp.JoinStyle """
    pass

def context_get_line_miter_limit(): # real signature unknown; restored from __doc__
    """ context_get_line_miter_limit() -> float """
    return 0.0

def context_get_line_width(): # real signature unknown; restored from __doc__
    """ context_get_line_width() -> float """
    return 0.0

def context_get_line_width_unit(): # real signature unknown; restored from __doc__
    """ context_get_line_width_unit() -> Gimp.Unit """
    pass

def context_get_mypaint_brush(): # real signature unknown; restored from __doc__
    """ context_get_mypaint_brush() -> str """
    return ""

def context_get_opacity(): # real signature unknown; restored from __doc__
    """ context_get_opacity() -> float """
    return 0.0

def context_get_paint_fade_length(): # real signature unknown; restored from __doc__
    """ context_get_paint_fade_length() -> float """
    return 0.0

def context_get_paint_fade_repeat(): # real signature unknown; restored from __doc__
    """ context_get_paint_fade_repeat() -> Gimp.RepeatMode """
    pass

def context_get_paint_method(): # real signature unknown; restored from __doc__
    """ context_get_paint_method() -> str """
    return ""

def context_get_paint_mode(): # real signature unknown; restored from __doc__
    """ context_get_paint_mode() -> Gimp.LayerMode """
    pass

def context_get_palette(): # real signature unknown; restored from __doc__
    """ context_get_palette() -> Gimp.Palette """
    pass

def context_get_pattern(): # real signature unknown; restored from __doc__
    """ context_get_pattern() -> Gimp.Pattern """
    pass

def context_get_sample_criterion(): # real signature unknown; restored from __doc__
    """ context_get_sample_criterion() -> Gimp.SelectCriterion """
    pass

def context_get_sample_merged(): # real signature unknown; restored from __doc__
    """ context_get_sample_merged() -> bool """
    return False

def context_get_sample_threshold(): # real signature unknown; restored from __doc__
    """ context_get_sample_threshold() -> float """
    return 0.0

def context_get_sample_threshold_int(): # real signature unknown; restored from __doc__
    """ context_get_sample_threshold_int() -> int """
    return 0

def context_get_sample_transparent(): # real signature unknown; restored from __doc__
    """ context_get_sample_transparent() -> bool """
    return False

def context_get_stroke_method(): # real signature unknown; restored from __doc__
    """ context_get_stroke_method() -> Gimp.StrokeMethod """
    pass

def context_get_transform_direction(): # real signature unknown; restored from __doc__
    """ context_get_transform_direction() -> Gimp.TransformDirection """
    pass

def context_get_transform_resize(): # real signature unknown; restored from __doc__
    """ context_get_transform_resize() -> Gimp.TransformResize """
    pass

def context_list_paint_methods(): # real signature unknown; restored from __doc__
    """ context_list_paint_methods() -> bool, paint_methods:list """
    return False

def context_pop(): # real signature unknown; restored from __doc__
    """ context_pop() -> bool """
    return False

def context_push(): # real signature unknown; restored from __doc__
    """ context_push() -> bool """
    return False

def context_set_antialias(antialias): # real signature unknown; restored from __doc__
    """ context_set_antialias(antialias:bool) -> bool """
    return False

def context_set_background(background): # real signature unknown; restored from __doc__
    """ context_set_background(background:Gegl.Color) -> bool """
    return False

def context_set_brush(brush): # real signature unknown; restored from __doc__
    """ context_set_brush(brush:Gimp.Brush) -> bool """
    return False

def context_set_brush_angle(angle): # real signature unknown; restored from __doc__
    """ context_set_brush_angle(angle:float) -> bool """
    return False

def context_set_brush_aspect_ratio(aspect): # real signature unknown; restored from __doc__
    """ context_set_brush_aspect_ratio(aspect:float) -> bool """
    return False

def context_set_brush_default_hardness(): # real signature unknown; restored from __doc__
    """ context_set_brush_default_hardness() -> bool """
    return False

def context_set_brush_default_size(): # real signature unknown; restored from __doc__
    """ context_set_brush_default_size() -> bool """
    return False

def context_set_brush_default_spacing(): # real signature unknown; restored from __doc__
    """ context_set_brush_default_spacing() -> bool """
    return False

def context_set_brush_force(force): # real signature unknown; restored from __doc__
    """ context_set_brush_force(force:float) -> bool """
    return False

def context_set_brush_hardness(hardness): # real signature unknown; restored from __doc__
    """ context_set_brush_hardness(hardness:float) -> bool """
    return False

def context_set_brush_size(size): # real signature unknown; restored from __doc__
    """ context_set_brush_size(size:float) -> bool """
    return False

def context_set_brush_spacing(spacing): # real signature unknown; restored from __doc__
    """ context_set_brush_spacing(spacing:float) -> bool """
    return False

def context_set_defaults(): # real signature unknown; restored from __doc__
    """ context_set_defaults() -> bool """
    return False

def context_set_default_colors(): # real signature unknown; restored from __doc__
    """ context_set_default_colors() -> bool """
    return False

def context_set_diagonal_neighbors(diagonal_neighbors): # real signature unknown; restored from __doc__
    """ context_set_diagonal_neighbors(diagonal_neighbors:bool) -> bool """
    return False

def context_set_distance_metric(metric): # real signature unknown; restored from __doc__
    """ context_set_distance_metric(metric:Gegl.DistanceMetric) -> bool """
    return False

def context_set_dynamics_name(name): # real signature unknown; restored from __doc__
    """ context_set_dynamics_name(name:str) -> bool """
    return False

def context_set_emulate_brush_dynamics(emulate_dynamics): # real signature unknown; restored from __doc__
    """ context_set_emulate_brush_dynamics(emulate_dynamics:bool) -> bool """
    return False

def context_set_feather(feather): # real signature unknown; restored from __doc__
    """ context_set_feather(feather:bool) -> bool """
    return False

def context_set_feather_radius(feather_radius_x, feather_radius_y): # real signature unknown; restored from __doc__
    """ context_set_feather_radius(feather_radius_x:float, feather_radius_y:float) -> bool """
    return False

def context_set_font(font): # real signature unknown; restored from __doc__
    """ context_set_font(font:Gimp.Font) -> bool """
    return False

def context_set_foreground(foreground): # real signature unknown; restored from __doc__
    """ context_set_foreground(foreground:Gegl.Color) -> bool """
    return False

def context_set_gradient(gradient): # real signature unknown; restored from __doc__
    """ context_set_gradient(gradient:Gimp.Gradient) -> bool """
    return False

def context_set_gradient_blend_color_space(blend_color_space): # real signature unknown; restored from __doc__
    """ context_set_gradient_blend_color_space(blend_color_space:Gimp.GradientBlendColorSpace) -> bool """
    return False

def context_set_gradient_fg_bg_hsv_ccw(): # real signature unknown; restored from __doc__
    """ context_set_gradient_fg_bg_hsv_ccw() -> bool """
    return False

def context_set_gradient_fg_bg_hsv_cw(): # real signature unknown; restored from __doc__
    """ context_set_gradient_fg_bg_hsv_cw() -> bool """
    return False

def context_set_gradient_fg_bg_rgb(): # real signature unknown; restored from __doc__
    """ context_set_gradient_fg_bg_rgb() -> bool """
    return False

def context_set_gradient_fg_transparent(): # real signature unknown; restored from __doc__
    """ context_set_gradient_fg_transparent() -> bool """
    return False

def context_set_gradient_repeat_mode(repeat_mode): # real signature unknown; restored from __doc__
    """ context_set_gradient_repeat_mode(repeat_mode:Gimp.RepeatMode) -> bool """
    return False

def context_set_gradient_reverse(reverse): # real signature unknown; restored from __doc__
    """ context_set_gradient_reverse(reverse:bool) -> bool """
    return False

def context_set_ink_angle(angle): # real signature unknown; restored from __doc__
    """ context_set_ink_angle(angle:float) -> bool """
    return False

def context_set_ink_blob_angle(angle): # real signature unknown; restored from __doc__
    """ context_set_ink_blob_angle(angle:float) -> bool """
    return False

def context_set_ink_blob_aspect_ratio(aspect): # real signature unknown; restored from __doc__
    """ context_set_ink_blob_aspect_ratio(aspect:float) -> bool """
    return False

def context_set_ink_blob_type(type): # real signature unknown; restored from __doc__
    """ context_set_ink_blob_type(type:Gimp.InkBlobType) -> bool """
    return False

def context_set_ink_size(size): # real signature unknown; restored from __doc__
    """ context_set_ink_size(size:float) -> bool """
    return False

def context_set_ink_size_sensitivity(size): # real signature unknown; restored from __doc__
    """ context_set_ink_size_sensitivity(size:float) -> bool """
    return False

def context_set_ink_speed_sensitivity(speed): # real signature unknown; restored from __doc__
    """ context_set_ink_speed_sensitivity(speed:float) -> bool """
    return False

def context_set_ink_tilt_sensitivity(tilt): # real signature unknown; restored from __doc__
    """ context_set_ink_tilt_sensitivity(tilt:float) -> bool """
    return False

def context_set_interpolation(interpolation): # real signature unknown; restored from __doc__
    """ context_set_interpolation(interpolation:Gimp.InterpolationType) -> bool """
    return False

def context_set_line_cap_style(cap_style): # real signature unknown; restored from __doc__
    """ context_set_line_cap_style(cap_style:Gimp.CapStyle) -> bool """
    return False

def context_set_line_dash_offset(dash_offset): # real signature unknown; restored from __doc__
    """ context_set_line_dash_offset(dash_offset:float) -> bool """
    return False

def context_set_line_dash_pattern(dashes): # real signature unknown; restored from __doc__
    """ context_set_line_dash_pattern(dashes:list) -> bool """
    return False

def context_set_line_join_style(join_style): # real signature unknown; restored from __doc__
    """ context_set_line_join_style(join_style:Gimp.JoinStyle) -> bool """
    return False

def context_set_line_miter_limit(miter_limit): # real signature unknown; restored from __doc__
    """ context_set_line_miter_limit(miter_limit:float) -> bool """
    return False

def context_set_line_width(line_width): # real signature unknown; restored from __doc__
    """ context_set_line_width(line_width:float) -> bool """
    return False

def context_set_line_width_unit(line_width_unit): # real signature unknown; restored from __doc__
    """ context_set_line_width_unit(line_width_unit:Gimp.Unit) -> bool """
    return False

def context_set_mypaint_brush(name): # real signature unknown; restored from __doc__
    """ context_set_mypaint_brush(name:str) -> bool """
    return False

def context_set_opacity(opacity): # real signature unknown; restored from __doc__
    """ context_set_opacity(opacity:float) -> bool """
    return False

def context_set_paint_fade_length(fade_length): # real signature unknown; restored from __doc__
    """ context_set_paint_fade_length(fade_length:float) -> bool """
    return False

def context_set_paint_fade_repeat(fade_repeat): # real signature unknown; restored from __doc__
    """ context_set_paint_fade_repeat(fade_repeat:Gimp.RepeatMode) -> bool """
    return False

def context_set_paint_method(name): # real signature unknown; restored from __doc__
    """ context_set_paint_method(name:str) -> bool """
    return False

def context_set_paint_mode(paint_mode): # real signature unknown; restored from __doc__
    """ context_set_paint_mode(paint_mode:Gimp.LayerMode) -> bool """
    return False

def context_set_palette(palette): # real signature unknown; restored from __doc__
    """ context_set_palette(palette:Gimp.Palette) -> bool """
    return False

def context_set_pattern(pattern): # real signature unknown; restored from __doc__
    """ context_set_pattern(pattern:Gimp.Pattern) -> bool """
    return False

def context_set_sample_criterion(sample_criterion): # real signature unknown; restored from __doc__
    """ context_set_sample_criterion(sample_criterion:Gimp.SelectCriterion) -> bool """
    return False

def context_set_sample_merged(sample_merged): # real signature unknown; restored from __doc__
    """ context_set_sample_merged(sample_merged:bool) -> bool """
    return False

def context_set_sample_threshold(sample_threshold): # real signature unknown; restored from __doc__
    """ context_set_sample_threshold(sample_threshold:float) -> bool """
    return False

def context_set_sample_threshold_int(sample_threshold): # real signature unknown; restored from __doc__
    """ context_set_sample_threshold_int(sample_threshold:int) -> bool """
    return False

def context_set_sample_transparent(sample_transparent): # real signature unknown; restored from __doc__
    """ context_set_sample_transparent(sample_transparent:bool) -> bool """
    return False

def context_set_stroke_method(stroke_method): # real signature unknown; restored from __doc__
    """ context_set_stroke_method(stroke_method:Gimp.StrokeMethod) -> bool """
    return False

def context_set_transform_direction(transform_direction): # real signature unknown; restored from __doc__
    """ context_set_transform_direction(transform_direction:Gimp.TransformDirection) -> bool """
    return False

def context_set_transform_resize(transform_resize): # real signature unknown; restored from __doc__
    """ context_set_transform_resize(transform_resize:Gimp.TransformResize) -> bool """
    return False

def context_swap_colors(): # real signature unknown; restored from __doc__
    """ context_swap_colors() -> bool """
    return False

def convolve(drawable, pressure, convolve_type, strokes): # real signature unknown; restored from __doc__
    """ convolve(drawable:Gimp.Drawable, pressure:float, convolve_type:Gimp.ConvolveType, strokes:list) -> bool """
    return False

def convolve_default(drawable, strokes): # real signature unknown; restored from __doc__
    """ convolve_default(drawable:Gimp.Drawable, strokes:list) -> bool """
    return False

def core_object_array_get_length(array): # real signature unknown; restored from __doc__
    """ core_object_array_get_length(array:GObject.Object) -> int """
    return 0

def core_object_array_get_type(): # real signature unknown; restored from __doc__
    """ core_object_array_get_type() -> GType """
    pass

def cpu_accel_get_support(): # real signature unknown; restored from __doc__
    """ cpu_accel_get_support() -> Gimp.CpuAccelFlags """
    pass

def data_directory(): # real signature unknown; restored from __doc__
    """ data_directory() -> str """
    return ""

def debug_timer_end(): # real signature unknown; restored from __doc__
    """ debug_timer_end() -> float """
    return 0.0

def debug_timer_start(): # real signature unknown; restored from __doc__
    """ debug_timer_start() -> bool """
    return False

def default_display(): # real signature unknown; restored from __doc__
    """ default_display() -> Gimp.Display """
    pass

def detach_parasite(name): # real signature unknown; restored from __doc__
    """ detach_parasite(name:str) -> bool """
    return False

def directory(): # real signature unknown; restored from __doc__
    """ directory() -> str """
    return ""

def displays_flush(): # real signature unknown; restored from __doc__
    """ displays_flush() -> bool """
    return False

def displays_reconnect(old_image, new_image): # real signature unknown; restored from __doc__
    """ displays_reconnect(old_image:Gimp.Image, new_image:Gimp.Image) -> bool """
    return False

def dodgeburn(drawable, exposure, dodgeburn_type, dodgeburn_mode, strokes): # real signature unknown; restored from __doc__
    """ dodgeburn(drawable:Gimp.Drawable, exposure:float, dodgeburn_type:Gimp.DodgeBurnType, dodgeburn_mode:Gimp.TransferMode, strokes:list) -> bool """
    return False

def dodgeburn_default(drawable, strokes): # real signature unknown; restored from __doc__
    """ dodgeburn_default(drawable:Gimp.Drawable, strokes:list) -> bool """
    return False

def double_array_get_values(array): # real signature unknown; restored from __doc__
    """ double_array_get_values(array:Gimp.Array) -> list """
    return []

def double_array_set_values(array, values, static_data): # real signature unknown; restored from __doc__
    """ double_array_set_values(array:Gimp.Array, values:list, static_data:bool) """
    pass

def drawables_close_popup(callback): # real signature unknown; restored from __doc__
    """ drawables_close_popup(callback:str) -> bool """
    return False

def drawables_popup(callback, popup_title, drawable_type, initial_drawable=None, parent_window=None): # real signature unknown; restored from __doc__
    """ drawables_popup(callback:str, popup_title:str, drawable_type:str, initial_drawable:Gimp.Drawable=None, parent_window:GLib.Bytes=None) -> bool """
    return False

def drawables_set_popup(callback, drawable): # real signature unknown; restored from __doc__
    """ drawables_set_popup(callback:str, drawable:Gimp.Drawable) -> bool """
    return False

def dynamics_get_name_list(filter=None): # real signature unknown; restored from __doc__
    """ dynamics_get_name_list(filter:str=None) -> list """
    return []

def dynamics_refresh(): # real signature unknown; restored from __doc__
    """ dynamics_refresh() -> bool """
    return False

def edit_copy(drawables): # real signature unknown; restored from __doc__
    """ edit_copy(drawables:list) -> bool """
    return False

def edit_copy_visible(image): # real signature unknown; restored from __doc__
    """ edit_copy_visible(image:Gimp.Image) -> bool """
    return False

def edit_cut(drawables): # real signature unknown; restored from __doc__
    """ edit_cut(drawables:list) -> bool """
    return False

def edit_named_copy(drawables, buffer_name): # real signature unknown; restored from __doc__
    """ edit_named_copy(drawables:list, buffer_name:str) -> str """
    return ""

def edit_named_copy_visible(image, buffer_name): # real signature unknown; restored from __doc__
    """ edit_named_copy_visible(image:Gimp.Image, buffer_name:str) -> str """
    return ""

def edit_named_cut(drawables, buffer_name): # real signature unknown; restored from __doc__
    """ edit_named_cut(drawables:list, buffer_name:str) -> str """
    return ""

def edit_named_paste(drawable, buffer_name, paste_into): # real signature unknown; restored from __doc__
    """ edit_named_paste(drawable:Gimp.Drawable, buffer_name:str, paste_into:bool) -> Gimp.Layer """
    pass

def edit_named_paste_as_new_image(buffer_name): # real signature unknown; restored from __doc__
    """ edit_named_paste_as_new_image(buffer_name:str) -> Gimp.Image """
    pass

def edit_paste(drawable, paste_into): # real signature unknown; restored from __doc__
    """ edit_paste(drawable:Gimp.Drawable, paste_into:bool) -> list """
    return []

def edit_paste_as_new_image(): # real signature unknown; restored from __doc__
    """ edit_paste_as_new_image() -> Gimp.Image """
    pass

def enums_get_type_names(): # real signature unknown; restored from __doc__
    """ enums_get_type_names() -> list """
    return []

def enums_init(): # real signature unknown; restored from __doc__
    """ enums_init() """
    pass

def enum_get_desc(enum_class, value): # real signature unknown; restored from __doc__
    """ enum_get_desc(enum_class:GObject.EnumClass, value:int) -> Gimp.EnumDesc or None """
    pass

def enum_get_value(enum_type, value): # real signature unknown; restored from __doc__
    """ enum_get_value(enum_type:GType, value:int) -> bool, value_name:str, value_nick:str, value_desc:str, value_help:str """
    return False

def enum_get_value_descriptions(enum_type): # real signature unknown; restored from __doc__
    """ enum_get_value_descriptions(enum_type:GType) -> Gimp.EnumDesc """
    pass

def enum_set_value_descriptions(enum_type, descriptions): # real signature unknown; restored from __doc__
    """ enum_set_value_descriptions(enum_type:GType, descriptions:Gimp.EnumDesc) """
    pass

def enum_value_get_abbrev(enum_class, enum_value): # real signature unknown; restored from __doc__
    """ enum_value_get_abbrev(enum_class:GObject.EnumClass, enum_value:GObject.EnumValue) -> str """
    return ""

def enum_value_get_desc(enum_class, enum_value): # real signature unknown; restored from __doc__
    """ enum_value_get_desc(enum_class:GObject.EnumClass, enum_value:GObject.EnumValue) -> str """
    return ""

def enum_value_get_help(enum_class, enum_value): # real signature unknown; restored from __doc__
    """ enum_value_get_help(enum_class:GObject.EnumClass, enum_value:GObject.EnumValue) -> str """
    return ""

def eraser(drawable, strokes, hardness, method): # real signature unknown; restored from __doc__
    """ eraser(drawable:Gimp.Drawable, strokes:list, hardness:Gimp.BrushApplicationMode, method:Gimp.PaintApplicationMode) -> bool """
    return False

def eraser_default(drawable, strokes): # real signature unknown; restored from __doc__
    """ eraser_default(drawable:Gimp.Drawable, strokes:list) -> bool """
    return False

def escape_uline(p_str=None): # real signature unknown; restored from __doc__
    """ escape_uline(str:str=None) -> str """
    return ""

def export_color_profile(): # real signature unknown; restored from __doc__
    """ export_color_profile() -> bool """
    return False

def export_comment(): # real signature unknown; restored from __doc__
    """ export_comment() -> bool """
    return False

def export_exif(): # real signature unknown; restored from __doc__
    """ export_exif() -> bool """
    return False

def export_iptc(): # real signature unknown; restored from __doc__
    """ export_iptc() -> bool """
    return False

def export_thumbnail(): # real signature unknown; restored from __doc__
    """ export_thumbnail() -> bool """
    return False

def export_xmp(): # real signature unknown; restored from __doc__
    """ export_xmp() -> bool """
    return False

def filename_to_utf8(filename): # real signature unknown; restored from __doc__
    """ filename_to_utf8(filename:str) -> str """
    return ""

def file_create_thumbnail(image, file): # real signature unknown; restored from __doc__
    """ file_create_thumbnail(image:Gimp.Image, file:Gio.File) -> bool """
    return False

def file_get_config_path(file): # real signature unknown; restored from __doc__
    """ file_get_config_path(file:Gio.File) -> str """
    return ""

def file_get_utf8_name(file): # real signature unknown; restored from __doc__
    """ file_get_utf8_name(file:Gio.File) -> str """
    return ""

def file_has_extension(file, extension): # real signature unknown; restored from __doc__
    """ file_has_extension(file:Gio.File, extension:str) -> bool """
    return False

def file_load(run_mode, file): # real signature unknown; restored from __doc__
    """ file_load(run_mode:Gimp.RunMode, file:Gio.File) -> Gimp.Image """
    pass

def file_load_layer(run_mode, image, file): # real signature unknown; restored from __doc__
    """ file_load_layer(run_mode:Gimp.RunMode, image:Gimp.Image, file:Gio.File) -> Gimp.Layer """
    pass

def file_load_layers(run_mode, image, file): # real signature unknown; restored from __doc__
    """ file_load_layers(run_mode:Gimp.RunMode, image:Gimp.Image, file:Gio.File) -> list """
    return []

def file_new_for_config_path(path): # real signature unknown; restored from __doc__
    """ file_new_for_config_path(path:str) -> Gio.File or None """
    pass

def file_save(run_mode, image, file, options=None): # real signature unknown; restored from __doc__
    """ file_save(run_mode:Gimp.RunMode, image:Gimp.Image, file:Gio.File, options:Gimp.ExportOptions=None) -> bool """
    return False

def file_show_in_file_manager(file): # real signature unknown; restored from __doc__
    """ file_show_in_file_manager(file:Gio.File) -> bool """
    return False

def flags_get_first_desc(flags_class, value): # real signature unknown; restored from __doc__
    """ flags_get_first_desc(flags_class:GObject.FlagsClass, value:int) -> Gimp.FlagsDesc or None """
    pass

def flags_get_first_value(flags_type, value): # real signature unknown; restored from __doc__
    """ flags_get_first_value(flags_type:GType, value:int) -> bool, value_name:str, value_nick:str, value_desc:str, value_help:str """
    return False

def flags_get_value_descriptions(flags_type): # real signature unknown; restored from __doc__
    """ flags_get_value_descriptions(flags_type:GType) -> Gimp.FlagsDesc """
    pass

def flags_set_value_descriptions(flags_type, descriptions): # real signature unknown; restored from __doc__
    """ flags_set_value_descriptions(flags_type:GType, descriptions:Gimp.FlagsDesc) """
    pass

def flags_value_get_abbrev(flags_class, flags_value): # real signature unknown; restored from __doc__
    """ flags_value_get_abbrev(flags_class:GObject.FlagsClass, flags_value:GObject.FlagsValue) -> str """
    return ""

def flags_value_get_desc(flags_class, flags_value): # real signature unknown; restored from __doc__
    """ flags_value_get_desc(flags_class:GObject.FlagsClass, flags_value:GObject.FlagsValue) -> str """
    return ""

def flags_value_get_help(flags_class, flags_value): # real signature unknown; restored from __doc__
    """ flags_value_get_help(flags_class:GObject.FlagsClass, flags_value:GObject.FlagsValue) -> str """
    return ""

def floating_sel_anchor(floating_sel): # real signature unknown; restored from __doc__
    """ floating_sel_anchor(floating_sel:Gimp.Layer) -> bool """
    return False

def floating_sel_attach(layer, drawable): # real signature unknown; restored from __doc__
    """ floating_sel_attach(layer:Gimp.Layer, drawable:Gimp.Drawable) -> bool """
    return False

def floating_sel_remove(floating_sel): # real signature unknown; restored from __doc__
    """ floating_sel_remove(floating_sel:Gimp.Layer) -> bool """
    return False

def floating_sel_to_layer(floating_sel): # real signature unknown; restored from __doc__
    """ floating_sel_to_layer(floating_sel:Gimp.Layer) -> bool """
    return False

def fonts_close_popup(font_callback): # real signature unknown; restored from __doc__
    """ fonts_close_popup(font_callback:str) -> bool """
    return False

def fonts_get_list(filter=None): # real signature unknown; restored from __doc__
    """ fonts_get_list(filter:str=None) -> list """
    return []

def fonts_popup(font_callback, popup_title, initial_font=None, parent_window=None): # real signature unknown; restored from __doc__
    """ fonts_popup(font_callback:str, popup_title:str, initial_font:Gimp.Font=None, parent_window:GLib.Bytes=None) -> bool """
    return False

def fonts_refresh(): # real signature unknown; restored from __doc__
    """ fonts_refresh() -> bool """
    return False

def fonts_set_popup(font_callback, font): # real signature unknown; restored from __doc__
    """ fonts_set_popup(font_callback:str, font:Gimp.Font) -> bool """
    return False

def getpid(): # real signature unknown; restored from __doc__
    """ getpid() -> int """
    return 0

def get_color_configuration(): # real signature unknown; restored from __doc__
    """ get_color_configuration() -> Gimp.ColorConfig """
    pass

def get_default_comment(): # real signature unknown; restored from __doc__
    """ get_default_comment() -> str """
    return ""

def get_default_unit(): # real signature unknown; restored from __doc__
    """ get_default_unit() -> Gimp.Unit """
    pass

def get_images(): # real signature unknown; restored from __doc__
    """ get_images() -> list """
    return []

def get_module_load_inhibit(): # real signature unknown; restored from __doc__
    """ get_module_load_inhibit() -> str """
    return ""

def get_monitor_resolution(): # real signature unknown; restored from __doc__
    """ get_monitor_resolution() -> bool, xres:float, yres:float """
    return False

def get_num_processors(): # real signature unknown; restored from __doc__
    """ get_num_processors() -> int """
    return 0

def get_parasite(name): # real signature unknown; restored from __doc__
    """ get_parasite(name:str) -> Gimp.Parasite """
    pass

def get_parasite_list(): # real signature unknown; restored from __doc__
    """ get_parasite_list() -> list """
    return []

def get_pdb(): # real signature unknown; restored from __doc__
    """ get_pdb() -> Gimp.PDB or None """
    pass

def get_plug_in(): # real signature unknown; restored from __doc__
    """ get_plug_in() -> Gimp.PlugIn or None """
    pass

def get_progname(): # real signature unknown; restored from __doc__
    """ get_progname() -> str """
    return ""

def gimprc_query(token): # real signature unknown; restored from __doc__
    """ gimprc_query(token:str) -> str """
    return ""

def gimprc_set(token, value): # real signature unknown; restored from __doc__
    """ gimprc_set(token:str, value:str) -> bool """
    return False

def gradients_close_popup(gradient_callback): # real signature unknown; restored from __doc__
    """ gradients_close_popup(gradient_callback:str) -> bool """
    return False

def gradients_get_list(filter=None): # real signature unknown; restored from __doc__
    """ gradients_get_list(filter:str=None) -> list """
    return []

def gradients_popup(gradient_callback, popup_title, initial_gradient=None, parent_window=None): # real signature unknown; restored from __doc__
    """ gradients_popup(gradient_callback:str, popup_title:str, initial_gradient:Gimp.Gradient=None, parent_window:GLib.Bytes=None) -> bool """
    return False

def gradients_refresh(): # real signature unknown; restored from __doc__
    """ gradients_refresh() -> bool """
    return False

def gradients_set_popup(gradient_callback, gradient): # real signature unknown; restored from __doc__
    """ gradients_set_popup(gradient_callback:str, gradient:Gimp.Gradient) -> bool """
    return False

def heal(drawable, src_drawable, src_x, src_y, strokes): # real signature unknown; restored from __doc__
    """ heal(drawable:Gimp.Drawable, src_drawable:Gimp.Drawable, src_x:float, src_y:float, strokes:list) -> bool """
    return False

def heal_default(drawable, strokes): # real signature unknown; restored from __doc__
    """ heal_default(drawable:Gimp.Drawable, strokes:list) -> bool """
    return False

def help(help_domain=None, help_id): # real signature unknown; restored from __doc__
    """ help(help_domain:str=None, help_id:str) -> bool """
    return False

def icon_theme_dir(): # real signature unknown; restored from __doc__
    """ icon_theme_dir() -> str """
    return ""

def images_close_popup(callback): # real signature unknown; restored from __doc__
    """ images_close_popup(callback:str) -> bool """
    return False

def images_popup(callback, popup_title, initial_image=None, parent_window=None): # real signature unknown; restored from __doc__
    """ images_popup(callback:str, popup_title:str, initial_image:Gimp.Image=None, parent_window:GLib.Bytes=None) -> bool """
    return False

def images_set_popup(callback, image): # real signature unknown; restored from __doc__
    """ images_set_popup(callback:str, image:Gimp.Image) -> bool """
    return False

def installation_directory(): # real signature unknown; restored from __doc__
    """ installation_directory() -> str """
    return ""

def int32_array_get_values(array): # real signature unknown; restored from __doc__
    """ int32_array_get_values(array:Gimp.Array) -> list """
    return []

def int32_array_set_values(array, values, static_data): # real signature unknown; restored from __doc__
    """ int32_array_set_values(array:Gimp.Array, values:list, static_data:bool) """
    pass

def is_canonical_identifier(identifier): # real signature unknown; restored from __doc__
    """ is_canonical_identifier(identifier:str) -> bool """
    return False

def items_close_popup(callback): # real signature unknown; restored from __doc__
    """ items_close_popup(callback:str) -> bool """
    return False

def items_popup(callback, popup_title, item_type, initial_item=None, parent_window=None): # real signature unknown; restored from __doc__
    """ items_popup(callback:str, popup_title:str, item_type:str, initial_item:Gimp.Item=None, parent_window:GLib.Bytes=None) -> bool """
    return False

def items_set_popup(callback, item): # real signature unknown; restored from __doc__
    """ items_set_popup(callback:str, item:Gimp.Item) -> bool """
    return False

def locale_directory(): # real signature unknown; restored from __doc__
    """ locale_directory() -> str """
    return ""

def main(plug_in_type, argv): # real signature unknown; restored from __doc__
    """ main(plug_in_type:GType, argv:list) -> int """
    return 0

def message(message): # real signature unknown; restored from __doc__
    """ message(message:str) -> bool """
    return False

def message_get_handler(): # real signature unknown; restored from __doc__
    """ message_get_handler() -> Gimp.MessageHandlerType """
    pass

def message_set_handler(handler): # real signature unknown; restored from __doc__
    """ message_set_handler(handler:Gimp.MessageHandlerType) -> bool """
    return False

def monitor_number(): # real signature unknown; restored from __doc__
    """ monitor_number() -> int """
    return 0

def paintbrush(drawable, fade_out, strokes, method, gradient_length): # real signature unknown; restored from __doc__
    """ paintbrush(drawable:Gimp.Drawable, fade_out:float, strokes:list, method:Gimp.PaintApplicationMode, gradient_length:float) -> bool """
    return False

def paintbrush_default(drawable, strokes): # real signature unknown; restored from __doc__
    """ paintbrush_default(drawable:Gimp.Drawable, strokes:list) -> bool """
    return False

def palettes_close_popup(palette_callback): # real signature unknown; restored from __doc__
    """ palettes_close_popup(palette_callback:str) -> bool """
    return False

def palettes_get_list(filter=None): # real signature unknown; restored from __doc__
    """ palettes_get_list(filter:str=None) -> list """
    return []

def palettes_popup(palette_callback, popup_title, initial_palette=None, parent_window=None): # real signature unknown; restored from __doc__
    """ palettes_popup(palette_callback:str, popup_title:str, initial_palette:Gimp.Palette=None, parent_window:GLib.Bytes=None) -> bool """
    return False

def palettes_refresh(): # real signature unknown; restored from __doc__
    """ palettes_refresh() -> bool """
    return False

def palettes_set_popup(palette_callback, palette): # real signature unknown; restored from __doc__
    """ palettes_set_popup(palette_callback:str, palette:Gimp.Palette) -> bool """
    return False

def param_spec_array(name, nick, blurb, flags): # real signature unknown; restored from __doc__
    """ param_spec_array(name:str, nick:str, blurb:str, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_brush(name, nick, blurb, none_ok, default_value=None, default_to_context, flags): # real signature unknown; restored from __doc__
    """ param_spec_brush(name:str, nick:str, blurb:str, none_ok:bool, default_value:Gimp.Brush=None, default_to_context:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_channel(name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
    """ param_spec_channel(name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_choice(name, nick, blurb, choice, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_choice(name:str, nick:str, blurb:str, choice:Gimp.Choice, default_value:str, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_choice_get_choice(pspec): # real signature unknown; restored from __doc__
    """ param_spec_choice_get_choice(pspec:GObject.ParamSpec) -> Gimp.Choice """
    pass

def param_spec_choice_get_default(pspec): # real signature unknown; restored from __doc__
    """ param_spec_choice_get_default(pspec:GObject.ParamSpec) -> str """
    return ""

def param_spec_color(name, nick, blurb, has_alpha, default_color, flags): # real signature unknown; restored from __doc__
    """ param_spec_color(name:str, nick:str, blurb:str, has_alpha:bool, default_color:Gegl.Color, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_color_from_string(name, nick, blurb, has_alpha, default_color_string, flags): # real signature unknown; restored from __doc__
    """ param_spec_color_from_string(name:str, nick:str, blurb:str, has_alpha:bool, default_color_string:str, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_color_has_alpha(pspec): # real signature unknown; restored from __doc__
    """ param_spec_color_has_alpha(pspec:GObject.ParamSpec) -> bool """
    return False

def param_spec_config_path(name, nick, blurb, type, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_config_path(name:str, nick:str, blurb:str, type:Gimp.ConfigPathType, default_value:str, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_config_path_type(pspec): # real signature unknown; restored from __doc__
    """ param_spec_config_path_type(pspec:GObject.ParamSpec) -> Gimp.ConfigPathType """
    pass

def param_spec_core_object_array(name, nick, blurb, object_type, flags): # real signature unknown; restored from __doc__
    """ param_spec_core_object_array(name:str, nick:str, blurb:str, object_type:GType, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_core_object_array_get_object_type(pspec): # real signature unknown; restored from __doc__
    """ param_spec_core_object_array_get_object_type(pspec:GObject.ParamSpec) -> GType """
    pass

def param_spec_curve(name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
    """ param_spec_curve(name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_display(name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
    """ param_spec_display(name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_display_none_allowed(pspec): # real signature unknown; restored from __doc__
    """ param_spec_display_none_allowed(pspec:GObject.ParamSpec) -> bool """
    return False

def param_spec_double_array(name, nick, blurb, flags): # real signature unknown; restored from __doc__
    """ param_spec_double_array(name:str, nick:str, blurb:str, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_drawable(name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
    """ param_spec_drawable(name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_drawable_filter(name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
    """ param_spec_drawable_filter(name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_drawable_filter_none_allowed(pspec): # real signature unknown; restored from __doc__
    """ param_spec_drawable_filter_none_allowed(pspec:GObject.ParamSpec) -> bool """
    return False

def param_spec_export_options(name, nick, blurb, flags): # real signature unknown; restored from __doc__
    """ param_spec_export_options(name:str, nick:str, blurb:str, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_file(name, nick, blurb, action, none_ok, default_value=None, flags): # real signature unknown; restored from __doc__
    """ param_spec_file(name:str, nick:str, blurb:str, action:Gimp.FileChooserAction, none_ok:bool, default_value:Gio.File=None, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_file_get_action(pspec): # real signature unknown; restored from __doc__
    """ param_spec_file_get_action(pspec:GObject.ParamSpec) -> Gimp.FileChooserAction """
    pass

def param_spec_file_none_allowed(pspec): # real signature unknown; restored from __doc__
    """ param_spec_file_none_allowed(pspec:GObject.ParamSpec) -> bool """
    return False

def param_spec_file_set_action(pspec, action): # real signature unknown; restored from __doc__
    """ param_spec_file_set_action(pspec:GObject.ParamSpec, action:Gimp.FileChooserAction) """
    pass

def param_spec_font(name, nick, blurb, none_ok, default_value=None, default_to_context, flags): # real signature unknown; restored from __doc__
    """ param_spec_font(name:str, nick:str, blurb:str, none_ok:bool, default_value:Gimp.Font=None, default_to_context:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_gradient(name, nick, blurb, none_ok, default_value=None, default_to_context, flags): # real signature unknown; restored from __doc__
    """ param_spec_gradient(name:str, nick:str, blurb:str, none_ok:bool, default_value:Gimp.Gradient=None, default_to_context:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_group_layer(name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
    """ param_spec_group_layer(name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_image(name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
    """ param_spec_image(name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_image_none_allowed(pspec): # real signature unknown; restored from __doc__
    """ param_spec_image_none_allowed(pspec:GObject.ParamSpec) -> bool """
    return False

def param_spec_int32_array(name, nick, blurb, flags): # real signature unknown; restored from __doc__
    """ param_spec_int32_array(name:str, nick:str, blurb:str, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_item(name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
    """ param_spec_item(name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_item_none_allowed(pspec): # real signature unknown; restored from __doc__
    """ param_spec_item_none_allowed(pspec:GObject.ParamSpec) -> bool """
    return False

def param_spec_layer(name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
    """ param_spec_layer(name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_layer_mask(name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
    """ param_spec_layer_mask(name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_link_layer(name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
    """ param_spec_link_layer(name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_matrix2(name, nick, blurb, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_matrix2(name:str, nick:str, blurb:str, default_value:Gimp.Matrix2, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_matrix3(name, nick, blurb, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_matrix3(name:str, nick:str, blurb:str, default_value:Gimp.Matrix3, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_memsize(name, nick, blurb, minimum, maximum, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_memsize(name:str, nick:str, blurb:str, minimum:int, maximum:int, default_value:int, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_object_duplicate(pspec): # real signature unknown; restored from __doc__
    """ param_spec_object_duplicate(pspec:GObject.ParamSpec) -> GObject.ParamSpec """
    pass

def param_spec_object_get_default(pspec): # real signature unknown; restored from __doc__
    """ param_spec_object_get_default(pspec:GObject.ParamSpec) -> GObject.Object """
    pass

def param_spec_object_has_default(pspec): # real signature unknown; restored from __doc__
    """ param_spec_object_has_default(pspec:GObject.ParamSpec) -> bool """
    return False

def param_spec_object_set_default(pspec, default_value=None): # real signature unknown; restored from __doc__
    """ param_spec_object_set_default(pspec:GObject.ParamSpec, default_value:GObject.Object=None) """
    pass

def param_spec_palette(name, nick, blurb, none_ok, default_value=None, default_to_context, flags): # real signature unknown; restored from __doc__
    """ param_spec_palette(name:str, nick:str, blurb:str, none_ok:bool, default_value:Gimp.Palette=None, default_to_context:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_parasite(name, nick, blurb, flags): # real signature unknown; restored from __doc__
    """ param_spec_parasite(name:str, nick:str, blurb:str, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_path(name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
    """ param_spec_path(name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_pattern(name, nick, blurb, none_ok, default_value=None, default_to_context, flags): # real signature unknown; restored from __doc__
    """ param_spec_pattern(name:str, nick:str, blurb:str, none_ok:bool, default_value:Gimp.Pattern=None, default_to_context:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_rasterizable(name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
    """ param_spec_rasterizable(name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_resource(name, nick, blurb, resource_type, none_ok, default_value=None, default_to_context, flags): # real signature unknown; restored from __doc__
    """ param_spec_resource(name:str, nick:str, blurb:str, resource_type:GType, none_ok:bool, default_value:Gimp.Resource=None, default_to_context:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_resource_defaults_to_context(pspec): # real signature unknown; restored from __doc__
    """ param_spec_resource_defaults_to_context(pspec:GObject.ParamSpec) -> bool """
    return False

def param_spec_resource_none_allowed(pspec): # real signature unknown; restored from __doc__
    """ param_spec_resource_none_allowed(pspec:GObject.ParamSpec) -> bool """
    return False

def param_spec_selection(name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
    """ param_spec_selection(name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_text_layer(name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
    """ param_spec_text_layer(name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_unit(name, nick, blurb, allow_pixel, allow_percent, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_unit(name:str, nick:str, blurb:str, allow_pixel:bool, allow_percent:bool, default_value:Gimp.Unit, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_unit_percent_allowed(pspec): # real signature unknown; restored from __doc__
    """ param_spec_unit_percent_allowed(pspec:GObject.ParamSpec) -> bool """
    return False

def param_spec_unit_pixel_allowed(pspec): # real signature unknown; restored from __doc__
    """ param_spec_unit_pixel_allowed(pspec:GObject.ParamSpec) -> bool """
    return False

def param_spec_value_array(name, nick, blurb, element_spec=None, flags): # real signature unknown; restored from __doc__
    """ param_spec_value_array(name:str, nick:str, blurb:str, element_spec:GObject.ParamSpec=None, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_value_array_get_element_spec(pspec): # real signature unknown; restored from __doc__
    """ param_spec_value_array_get_element_spec(pspec:GObject.ParamSpec) -> GObject.ParamSpec """
    pass

def param_spec_vector_layer(name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
    """ param_spec_vector_layer(name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def patterns_close_popup(pattern_callback): # real signature unknown; restored from __doc__
    """ patterns_close_popup(pattern_callback:str) -> bool """
    return False

def patterns_get_list(filter=None): # real signature unknown; restored from __doc__
    """ patterns_get_list(filter:str=None) -> list """
    return []

def patterns_popup(pattern_callback, popup_title, initial_pattern=None, parent_window=None): # real signature unknown; restored from __doc__
    """ patterns_popup(pattern_callback:str, popup_title:str, initial_pattern:Gimp.Pattern=None, parent_window:GLib.Bytes=None) -> bool """
    return False

def patterns_refresh(): # real signature unknown; restored from __doc__
    """ patterns_refresh() -> bool """
    return False

def patterns_set_popup(pattern_callback, pattern): # real signature unknown; restored from __doc__
    """ patterns_set_popup(pattern_callback:str, pattern:Gimp.Pattern) -> bool """
    return False

def pencil(drawable, strokes): # real signature unknown; restored from __doc__
    """ pencil(drawable:Gimp.Drawable, strokes:list) -> bool """
    return False

def pixbuf_create_buffer(pixbuf): # real signature unknown; restored from __doc__
    """ pixbuf_create_buffer(pixbuf:GdkPixbuf.Pixbuf) -> Gegl.Buffer """
    pass

def pixbuf_get_format(pixbuf): # real signature unknown; restored from __doc__
    """ pixbuf_get_format(pixbuf:GdkPixbuf.Pixbuf) -> Babl.Object """
    pass

def pixbuf_get_icc_profile(pixbuf): # real signature unknown; restored from __doc__
    """ pixbuf_get_icc_profile(pixbuf:GdkPixbuf.Pixbuf) -> list or None """
    return []

def pixels_to_units(pixels, unit, resolution): # real signature unknown; restored from __doc__
    """ pixels_to_units(pixels:float, unit:Gimp.Unit, resolution:float) -> float """
    return 0.0

def pixpipe_params_build(params): # real signature unknown; restored from __doc__
    """ pixpipe_params_build(params:Gimp.PixPipeParams) -> str """
    return ""

def pixpipe_params_free(params): # real signature unknown; restored from __doc__
    """ pixpipe_params_free(params:Gimp.PixPipeParams) """
    pass

def pixpipe_params_init(params): # real signature unknown; restored from __doc__
    """ pixpipe_params_init(params:Gimp.PixPipeParams) """
    pass

def pixpipe_params_parse(parameters, params): # real signature unknown; restored from __doc__
    """ pixpipe_params_parse(parameters:str, params:Gimp.PixPipeParams) """
    pass

def progress_cancel(progress_callback): # real signature unknown; restored from __doc__
    """ progress_cancel(progress_callback:str) -> bool """
    return False

def progress_end(): # real signature unknown; restored from __doc__
    """ progress_end() -> bool """
    return False

def progress_get_window_handle(): # real signature unknown; restored from __doc__
    """ progress_get_window_handle() -> GLib.Bytes """
    pass

def progress_init(message): # real signature unknown; restored from __doc__
    """ progress_init(message:str) -> bool """
    return False

def progress_install_vtable(vtable, user_data=None, user_data_destroy=None): # real signature unknown; restored from __doc__
    """ progress_install_vtable(vtable:Gimp.ProgressVtable, user_data=None, user_data_destroy:GLib.DestroyNotify=None) -> str """
    return ""

def progress_pulse(): # real signature unknown; restored from __doc__
    """ progress_pulse() -> bool """
    return False

def progress_set_text(message=None): # real signature unknown; restored from __doc__
    """ progress_set_text(message:str=None) -> bool """
    return False

def progress_uninstall(progress_callback): # real signature unknown; restored from __doc__
    """ progress_uninstall(progress_callback:str) """
    pass

def progress_update(percentage): # real signature unknown; restored from __doc__
    """ progress_update(percentage:float) -> bool """
    return False

def quit(): # real signature unknown; restored from __doc__
    """ quit() """
    pass

def range_estimate_settings(lower, upper): # real signature unknown; restored from __doc__
    """ range_estimate_settings(lower:float, upper:float) -> step:float, page:float, digits:int """
    pass

def rectangle_intersect(x1, y1, width1, height1, x2, y2, width2, height2): # real signature unknown; restored from __doc__
    """ rectangle_intersect(x1:int, y1:int, width1:int, height1:int, x2:int, y2:int, width2:int, height2:int) -> bool, dest_x:int, dest_y:int, dest_width:int, dest_height:int """
    return False

def rectangle_union(x1, y1, width1, height1, x2, y2, width2, height2): # real signature unknown; restored from __doc__
    """ rectangle_union(x1:int, y1:int, width1:int, height1:int, x2:int, y2:int, width2:int, height2:int) -> dest_x:int, dest_y:int, dest_width:int, dest_height:int """
    pass

def show_help_button(): # real signature unknown; restored from __doc__
    """ show_help_button() -> bool """
    return False

def smudge(drawable, pressure, strokes): # real signature unknown; restored from __doc__
    """ smudge(drawable:Gimp.Drawable, pressure:float, strokes:list) -> bool """
    return False

def smudge_default(drawable, strokes): # real signature unknown; restored from __doc__
    """ smudge_default(drawable:Gimp.Drawable, strokes:list) -> bool """
    return False

def stack_trace_available(optimal): # real signature unknown; restored from __doc__
    """ stack_trace_available(optimal:bool) -> bool """
    return False

def stack_trace_print(prog_name, stream=None): # real signature unknown; restored from __doc__
    """ stack_trace_print(prog_name:str, stream=None) -> bool, trace:str """
    return False

def stack_trace_query(prog_name): # real signature unknown; restored from __doc__
    """ stack_trace_query(prog_name:str) """
    pass

def strip_uline(p_str=None): # real signature unknown; restored from __doc__
    """ strip_uline(str:str=None) -> str """
    return ""

def sysconf_directory(): # real signature unknown; restored from __doc__
    """ sysconf_directory() -> str """
    return ""

def temp_directory(): # real signature unknown; restored from __doc__
    """ temp_directory() -> str """
    return ""

def temp_file(extension=None): # real signature unknown; restored from __doc__
    """ temp_file(extension:str=None) -> Gio.File """
    pass

def text_font(image, drawable=None, x, y, text, border, antialias, size, font): # real signature unknown; restored from __doc__
    """ text_font(image:Gimp.Image, drawable:Gimp.Drawable=None, x:float, y:float, text:str, border:int, antialias:bool, size:float, font:Gimp.Font) -> Gimp.Layer or None """
    pass

def text_get_extents_font(text, size, font): # real signature unknown; restored from __doc__
    """ text_get_extents_font(text:str, size:float, font:Gimp.Font) -> bool, width:int, height:int, ascent:int, descent:int """
    return False

def tile_height(): # real signature unknown; restored from __doc__
    """ tile_height() -> int """
    return 0

def tile_width(): # real signature unknown; restored from __doc__
    """ tile_width() -> int """
    return 0

def type_get_translation_context(type): # real signature unknown; restored from __doc__
    """ type_get_translation_context(type:GType) -> str """
    return ""

def type_get_translation_domain(type): # real signature unknown; restored from __doc__
    """ type_get_translation_domain(type:GType) -> str """
    return ""

def type_set_translation_context(type, context): # real signature unknown; restored from __doc__
    """ type_set_translation_context(type:GType, context:str) """
    pass

def type_set_translation_domain(type, domain): # real signature unknown; restored from __doc__
    """ type_set_translation_domain(type:GType, domain:str) """
    pass

def units_to_pixels(value, unit, resolution): # real signature unknown; restored from __doc__
    """ units_to_pixels(value:float, unit:Gimp.Unit, resolution:float) -> float """
    return 0.0

def units_to_points(value, unit, resolution): # real signature unknown; restored from __doc__
    """ units_to_points(value:float, unit:Gimp.Unit, resolution:float) -> float """
    return 0.0

def update_metadata(): # real signature unknown; restored from __doc__
    """ update_metadata() -> bool """
    return False

def user_time(): # real signature unknown; restored from __doc__
    """ user_time() -> int """
    return 0

def utf8_strtrim(p_str=None, max_chars): # real signature unknown; restored from __doc__
    """ utf8_strtrim(str:str=None, max_chars:int) -> str """
    return ""

def value_dup_double_array(value): # real signature unknown; restored from __doc__
    """ value_dup_double_array(value:GObject.Value) -> list """
    return []

def value_dup_int32_array(value): # real signature unknown; restored from __doc__
    """ value_dup_int32_array(value:GObject.Value) -> list """
    return []

def value_get_double_array(value): # real signature unknown; restored from __doc__
    """ value_get_double_array(value:GObject.Value) -> list """
    return []

def value_get_int32_array(value): # real signature unknown; restored from __doc__
    """ value_get_int32_array(value:GObject.Value) -> list """
    return []

def value_set_double_array(value, data): # real signature unknown; restored from __doc__
    """ value_set_double_array(value:GObject.Value, data:list) """
    pass

def value_set_int32_array(value, data): # real signature unknown; restored from __doc__
    """ value_set_int32_array(value:GObject.Value, data:list) """
    pass

def value_set_static_double_array(value, data): # real signature unknown; restored from __doc__
    """ value_set_static_double_array(value:GObject.Value, data:list) """
    pass

def value_set_static_int32_array(value, data): # real signature unknown; restored from __doc__
    """ value_set_static_int32_array(value:GObject.Value, data:list) """
    pass

def value_take_double_array(value, data): # real signature unknown; restored from __doc__
    """ value_take_double_array(value:GObject.Value, data:list) """
    pass

def value_take_int32_array(value, data): # real signature unknown; restored from __doc__
    """ value_take_int32_array(value:GObject.Value, data:list) """
    pass

def vector2_add(vector1, vector2): # real signature unknown; restored from __doc__
    """ vector2_add(vector1:Gimp.Vector2, vector2:Gimp.Vector2) -> result:Gimp.Vector2 """
    pass

def vector2_sub(vector1, vector2): # real signature unknown; restored from __doc__
    """ vector2_sub(vector1:Gimp.Vector2, vector2:Gimp.Vector2) -> result:Gimp.Vector2 """
    pass

def vector3_add(vector1, vector2): # real signature unknown; restored from __doc__
    """ vector3_add(vector1:Gimp.Vector3, vector2:Gimp.Vector3) -> result:Gimp.Vector3 """
    pass

def vector3_sub(vector1, vector2): # real signature unknown; restored from __doc__
    """ vector3_sub(vector1:Gimp.Vector3, vector2:Gimp.Vector3) -> result:Gimp.Vector3 """
    pass

def vector_2d_to_3d(sx, sy, w, h, x, y, vp, p): # real signature unknown; restored from __doc__
    """ vector_2d_to_3d(sx:int, sy:int, w:int, h:int, x:int, y:int, vp:Gimp.Vector3, p:Gimp.Vector3) """
    pass

def vector_2d_to_3d_val(sx, sy, w, h, x, y, vp, p): # real signature unknown; restored from __doc__
    """ vector_2d_to_3d_val(sx:int, sy:int, w:int, h:int, x:int, y:int, vp:Gimp.Vector3, p:Gimp.Vector3) -> Gimp.Vector3 """
    pass

def vector_3d_to_2d(sx, sy, w, h, vp, p): # real signature unknown; restored from __doc__
    """ vector_3d_to_2d(sx:int, sy:int, w:int, h:int, vp:Gimp.Vector3, p:Gimp.Vector3) -> x:float, y:float """
    pass

def version(): # real signature unknown; restored from __doc__
    """ version() -> str """
    return ""

def wm_class(): # real signature unknown; restored from __doc__
    """ wm_class() -> str """
    return ""

# classes

from .AddMaskType import AddMaskType
from .ArgumentSync import ArgumentSync
from .Array import Array
from .Procedure import Procedure
from .BatchProcedure import BatchProcedure
from .BatchProcedureClass import BatchProcedureClass
from .ConfigInterface import ConfigInterface
from .Resource import Resource
from .Brush import Brush
from .BrushApplicationMode import BrushApplicationMode
from .BrushClass import BrushClass
from .BrushGeneratedShape import BrushGeneratedShape
from .CapStyle import CapStyle
from .Item import Item
from .Drawable import Drawable
from .Channel import Channel
from .ChannelClass import ChannelClass
from .ChannelOps import ChannelOps
from .ChannelType import ChannelType
from .CheckSize import CheckSize
from .CheckType import CheckType
from .Choice import Choice
from .ChoiceClass import ChoiceClass
from .CloneType import CloneType
from .ColorConfig import ColorConfig
from .ColorConfigClass import ColorConfigClass
from .ColorManaged import ColorManaged
from .ColorManagedInterface import ColorManagedInterface
from .ColorManagementMode import ColorManagementMode
from .ColorProfile import ColorProfile
from .ColorProfileClass import ColorProfileClass
from .ColorRenderingIntent import ColorRenderingIntent
from .ColorTag import ColorTag
from .ColorTransform import ColorTransform
from .ColorTransformClass import ColorTransformClass
from .ColorTransformFlags import ColorTransformFlags
from .ComponentType import ComponentType
from .Config import Config
from .ConfigError import ConfigError
from .ConfigPath import ConfigPath
from .ConfigPathType import ConfigPathType
from .ConfigWriter import ConfigWriter
from .ConvertDitherType import ConvertDitherType
from .ConvertPaletteType import ConvertPaletteType
from .ConvolveType import ConvolveType
from .CpuAccelFlags import CpuAccelFlags
from .Curve import Curve
from .CurveClass import CurveClass
from .CurvePointType import CurvePointType
from .CurveType import CurveType
from .DesaturateMode import DesaturateMode
from .Display import Display
from .DisplayClass import DisplayClass
from .DodgeBurnType import DodgeBurnType
from .DoubleArray import DoubleArray
from .DrawableClass import DrawableClass
from .DrawableFilter import DrawableFilter
from .DrawableFilterClass import DrawableFilterClass
from .DrawableFilterConfig import DrawableFilterConfig
from .DrawableFilterConfigClass import DrawableFilterConfigClass
from .EnumDesc import EnumDesc
from .ExportCapabilities import ExportCapabilities
from .ExportOptions import ExportOptions
from .ExportOptionsClass import ExportOptionsClass
from .FileProcedure import FileProcedure
from .ExportProcedure import ExportProcedure
from .ExportProcedureClass import ExportProcedureClass
from .ExportReturn import ExportReturn
from .FileChooserAction import FileChooserAction
from .FileProcedureClass import FileProcedureClass
from .FillType import FillType
from .FlagsDesc import FlagsDesc
from .Font import Font
from .FontClass import FontClass
from .ForegroundExtractMode import ForegroundExtractMode
from .Gradient import Gradient
from .GradientBlendColorSpace import GradientBlendColorSpace
from .GradientClass import GradientClass
from .GradientSegmentColor import GradientSegmentColor
from .GradientSegmentType import GradientSegmentType
from .GradientType import GradientType
from .GridStyle import GridStyle
from .Layer import Layer
from .GroupLayer import GroupLayer
from .GroupLayerClass import GroupLayerClass
from .HistogramChannel import HistogramChannel
from .HueRange import HueRange
from .IconType import IconType
from .Image import Image
from .ImageBaseType import ImageBaseType
from .ImageClass import ImageClass
from .ImageProcedure import ImageProcedure
from .ImageProcedureClass import ImageProcedureClass
from .ImageType import ImageType
from .InkBlobType import InkBlobType
from .Int32Array import Int32Array
from .InterpolationType import InterpolationType
from .ItemClass import ItemClass
from .JoinStyle import JoinStyle
from .LayerClass import LayerClass
from .LayerColorSpace import LayerColorSpace
from .LayerCompositeMode import LayerCompositeMode
from .LayerMask import LayerMask
from .LayerMaskClass import LayerMaskClass
from .LayerMode import LayerMode
from .Rasterizable import Rasterizable
from .LinkLayer import LinkLayer
from .LinkLayerClass import LinkLayerClass
from .LoadProcedure import LoadProcedure
from .LoadProcedureClass import LoadProcedureClass
from .MaskApplyMode import MaskApplyMode
from .Matrix2 import Matrix2
from .Matrix3 import Matrix3
from .Matrix4 import Matrix4
from .Memsize import Memsize
from .MergeType import MergeType
from .MessageHandlerType import MessageHandlerType
from .Metadata import Metadata
from .MetadataClass import MetadataClass
from .MetadataColorspace import MetadataColorspace
from .MetadataLoadFlags import MetadataLoadFlags
from .MetadataSaveFlags import MetadataSaveFlags
from .Module import Module
from .ModuleClass import ModuleClass
from .ModuleDB import ModuleDB
from .ModuleDBClass import ModuleDBClass
from .ModuleError import ModuleError
from .ModuleInfo import ModuleInfo
from .ModuleState import ModuleState
from .OffsetType import OffsetType
from .OrientationType import OrientationType
from .PaintApplicationMode import PaintApplicationMode
from .Palette import Palette
from .PaletteClass import PaletteClass
from .ParamArray import ParamArray
from .ParamObject import ParamObject
from .ParamResource import ParamResource
from .ParamBrush import ParamBrush
from .ParamItem import ParamItem
from .ParamDrawable import ParamDrawable
from .ParamChannel import ParamChannel
from .ParamChoice import ParamChoice
from .ParamColor import ParamColor
from .ParamConfigPath import ParamConfigPath
from .ParamCoreObjectArray import ParamCoreObjectArray
from .ParamCurve import ParamCurve
from .ParamDisplay import ParamDisplay
from .ParamDoubleArray import ParamDoubleArray
from .ParamDrawableFilter import ParamDrawableFilter
from .ParamExportOptions import ParamExportOptions
from .ParamFile import ParamFile
from .ParamFont import ParamFont
from .ParamGradient import ParamGradient
from .ParamLayer import ParamLayer
from .ParamGroupLayer import ParamGroupLayer
from .ParamImage import ParamImage
from .ParamInt32Array import ParamInt32Array
from .ParamLayerMask import ParamLayerMask
from .ParamLinkLayer import ParamLinkLayer
from .ParamMatrix2 import ParamMatrix2
from .ParamMatrix3 import ParamMatrix3
from .ParamMemsize import ParamMemsize
from .ParamPalette import ParamPalette
from .ParamParasite import ParamParasite
from .ParamPath import ParamPath
from .ParamPattern import ParamPattern
from .ParamRasterizable import ParamRasterizable
from .ParamSelection import ParamSelection
from .ParamSpecObject import ParamSpecObject
from .ParamSpecObjectClass import ParamSpecObjectClass
from .ParamTextLayer import ParamTextLayer
from .ParamUnit import ParamUnit
from .ParamValueArray import ParamValueArray
from .ParamVectorLayer import ParamVectorLayer
from .Parasite import Parasite
from .Path import Path
from .PathClass import PathClass
from .PathStrokeType import PathStrokeType
from .Pattern import Pattern
from .PatternClass import PatternClass
from .PDB import PDB
from .PDBClass import PDBClass
from .PDBErrorHandler import PDBErrorHandler
from .PDBProcType import PDBProcType
from .PDBStatusType import PDBStatusType
from .PixbufTransparency import PixbufTransparency
from .PixPipeParams import PixPipeParams
from .PlugIn import PlugIn
from .PlugInClass import PlugInClass
from .Precision import Precision
from .ProcedureClass import ProcedureClass
from .ProcedureConfig import ProcedureConfig
from .ProcedureConfigClass import ProcedureConfigClass
from .ProcedureSensitivityMask import ProcedureSensitivityMask
from .ProgressCommand import ProgressCommand
from .ProgressVtable import ProgressVtable
from .RasterizableInterface import RasterizableInterface
from .RepeatMode import RepeatMode
from .ResourceClass import ResourceClass
from .RotationType import RotationType
from .RunMode import RunMode
from .Scanner import Scanner
from .SelectCriterion import SelectCriterion
from .Selection import Selection
from .SelectionClass import SelectionClass
from .SizeType import SizeType
from .StackTraceMode import StackTraceMode
from .StrokeMethod import StrokeMethod
from .TextDirection import TextDirection
from .TextHintStyle import TextHintStyle
from .TextJustification import TextJustification
from .TextLayer import TextLayer
from .TextLayerClass import TextLayerClass
from .TextOutline import TextOutline
from .TextOutlineDirection import TextOutlineDirection
from .ThumbnailProcedure import ThumbnailProcedure
from .ThumbnailProcedureClass import ThumbnailProcedureClass
from .TransferMode import TransferMode
from .TransformDirection import TransformDirection
from .TransformResize import TransformResize
from .TRCType import TRCType
from .Unit import Unit
from .UnitClass import UnitClass
from .UnitID import UnitID
from .ValueArray import ValueArray
from .Vector2 import Vector2
from .Vector3 import Vector3
from .Vector4 import Vector4
from .VectorLayer import VectorLayer
from .VectorLayerClass import VectorLayerClass
from .VectorLoadData import VectorLoadData
from .VectorLoadProcedure import VectorLoadProcedure
from .VectorLoadProcedureClass import VectorLoadProcedureClass
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x000001268d638440>'

__path__ = []

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Gimp', loader=<gi.importer.DynamicImporter object at 0x000001268d638440>)"

