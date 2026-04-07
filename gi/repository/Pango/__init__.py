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


# Variables with simple values

ANALYSIS_FLAG_CENTERED_BASELINE = 1

ANALYSIS_FLAG_IS_ELLIPSIS = 2

ANALYSIS_FLAG_NEED_HYPHEN = 4

ATTR_INDEX_FROM_TEXT_BEGINNING = 0

ATTR_INDEX_TO_TEXT_END = 4294967295

GLYPH_EMPTY = 268435455

GLYPH_INVALID_INPUT = 4294967295

GLYPH_UNKNOWN_FLAG = 268435456

SCALE = 1024

VERSION_MAJOR = 1
VERSION_MICRO = 4
VERSION_MINOR = 56
VERSION_STRING = '1.56.4'

_namespace = 'Pango'

_version = '1.0'

# functions

def attr_allow_breaks_new(allow_breaks): # real signature unknown; restored from __doc__
    """ attr_allow_breaks_new(allow_breaks:bool) -> Pango.Attribute """
    pass

def attr_background_alpha_new(alpha): # real signature unknown; restored from __doc__
    """ attr_background_alpha_new(alpha:int) -> Pango.Attribute """
    pass

def attr_background_new(red, green, blue): # real signature unknown; restored from __doc__
    """ attr_background_new(red:int, green:int, blue:int) -> Pango.Attribute """
    pass

def attr_baseline_shift_new(shift): # real signature unknown; restored from __doc__
    """ attr_baseline_shift_new(shift:int) -> Pango.Attribute """
    pass

def attr_break(text, length, attr_list, offset): # real signature unknown; restored from __doc__
    """ attr_break(text:str, length:int, attr_list:Pango.AttrList, offset:int) -> attrs:list """
    pass

def attr_fallback_new(enable_fallback): # real signature unknown; restored from __doc__
    """ attr_fallback_new(enable_fallback:bool) -> Pango.Attribute """
    pass

def attr_family_new(family): # real signature unknown; restored from __doc__
    """ attr_family_new(family:str) -> Pango.Attribute """
    pass

def attr_font_desc_new(desc): # real signature unknown; restored from __doc__
    """ attr_font_desc_new(desc:Pango.FontDescription) -> Pango.Attribute """
    pass

def attr_font_features_new(features): # real signature unknown; restored from __doc__
    """ attr_font_features_new(features:str) -> Pango.Attribute """
    pass

def attr_font_scale_new(scale): # real signature unknown; restored from __doc__
    """ attr_font_scale_new(scale:Pango.FontScale) -> Pango.Attribute """
    pass

def attr_foreground_alpha_new(alpha): # real signature unknown; restored from __doc__
    """ attr_foreground_alpha_new(alpha:int) -> Pango.Attribute """
    pass

def attr_foreground_new(red, green, blue): # real signature unknown; restored from __doc__
    """ attr_foreground_new(red:int, green:int, blue:int) -> Pango.Attribute """
    pass

def attr_gravity_hint_new(hint): # real signature unknown; restored from __doc__
    """ attr_gravity_hint_new(hint:Pango.GravityHint) -> Pango.Attribute """
    pass

def attr_gravity_new(gravity): # real signature unknown; restored from __doc__
    """ attr_gravity_new(gravity:Pango.Gravity) -> Pango.Attribute """
    pass

def attr_insert_hyphens_new(insert_hyphens): # real signature unknown; restored from __doc__
    """ attr_insert_hyphens_new(insert_hyphens:bool) -> Pango.Attribute """
    pass

def attr_language_new(language): # real signature unknown; restored from __doc__
    """ attr_language_new(language:Pango.Language) -> Pango.Attribute """
    pass

def attr_letter_spacing_new(letter_spacing): # real signature unknown; restored from __doc__
    """ attr_letter_spacing_new(letter_spacing:int) -> Pango.Attribute """
    pass

def attr_line_height_new(factor): # real signature unknown; restored from __doc__
    """ attr_line_height_new(factor:float) -> Pango.Attribute """
    pass

def attr_line_height_new_absolute(height): # real signature unknown; restored from __doc__
    """ attr_line_height_new_absolute(height:int) -> Pango.Attribute """
    pass

def attr_list_from_string(text): # real signature unknown; restored from __doc__
    """ attr_list_from_string(text:str) -> Pango.AttrList or None """
    pass

def attr_overline_color_new(red, green, blue): # real signature unknown; restored from __doc__
    """ attr_overline_color_new(red:int, green:int, blue:int) -> Pango.Attribute """
    pass

def attr_overline_new(overline): # real signature unknown; restored from __doc__
    """ attr_overline_new(overline:Pango.Overline) -> Pango.Attribute """
    pass

def attr_rise_new(rise): # real signature unknown; restored from __doc__
    """ attr_rise_new(rise:int) -> Pango.Attribute """
    pass

def attr_scale_new(scale_factor): # real signature unknown; restored from __doc__
    """ attr_scale_new(scale_factor:float) -> Pango.Attribute """
    pass

def attr_sentence_new(): # real signature unknown; restored from __doc__
    """ attr_sentence_new() -> Pango.Attribute """
    pass

def attr_shape_new(ink_rect, logical_rect): # real signature unknown; restored from __doc__
    """ attr_shape_new(ink_rect:Pango.Rectangle, logical_rect:Pango.Rectangle) -> Pango.Attribute """
    pass

def attr_shape_new_with_data(ink_rect, logical_rect, data=None, copy_func=None): # real signature unknown; restored from __doc__
    """ attr_shape_new_with_data(ink_rect:Pango.Rectangle, logical_rect:Pango.Rectangle, data=None, copy_func:Pango.AttrDataCopyFunc=None) -> Pango.Attribute """
    pass

def attr_show_new(flags): # real signature unknown; restored from __doc__
    """ attr_show_new(flags:Pango.ShowFlags) -> Pango.Attribute """
    pass

def attr_size_new(size): # real signature unknown; restored from __doc__
    """ attr_size_new(size:int) -> Pango.Attribute """
    pass

def attr_size_new_absolute(size): # real signature unknown; restored from __doc__
    """ attr_size_new_absolute(size:int) -> Pango.Attribute """
    pass

def attr_stretch_new(stretch): # real signature unknown; restored from __doc__
    """ attr_stretch_new(stretch:Pango.Stretch) -> Pango.Attribute """
    pass

def attr_strikethrough_color_new(red, green, blue): # real signature unknown; restored from __doc__
    """ attr_strikethrough_color_new(red:int, green:int, blue:int) -> Pango.Attribute """
    pass

def attr_strikethrough_new(strikethrough): # real signature unknown; restored from __doc__
    """ attr_strikethrough_new(strikethrough:bool) -> Pango.Attribute """
    pass

def attr_style_new(style): # real signature unknown; restored from __doc__
    """ attr_style_new(style:Pango.Style) -> Pango.Attribute """
    pass

def attr_text_transform_new(transform): # real signature unknown; restored from __doc__
    """ attr_text_transform_new(transform:Pango.TextTransform) -> Pango.Attribute """
    pass

def attr_type_get_name(type): # real signature unknown; restored from __doc__
    """ attr_type_get_name(type:Pango.AttrType) -> str or None """
    return ""

def attr_type_register(name): # real signature unknown; restored from __doc__
    """ attr_type_register(name:str) -> Pango.AttrType """
    pass

def attr_underline_color_new(red, green, blue): # real signature unknown; restored from __doc__
    """ attr_underline_color_new(red:int, green:int, blue:int) -> Pango.Attribute """
    pass

def attr_underline_new(underline): # real signature unknown; restored from __doc__
    """ attr_underline_new(underline:Pango.Underline) -> Pango.Attribute """
    pass

def attr_variant_new(variant): # real signature unknown; restored from __doc__
    """ attr_variant_new(variant:Pango.Variant) -> Pango.Attribute """
    pass

def attr_weight_new(weight): # real signature unknown; restored from __doc__
    """ attr_weight_new(weight:Pango.Weight) -> Pango.Attribute """
    pass

def attr_word_new(): # real signature unknown; restored from __doc__
    """ attr_word_new() -> Pango.Attribute """
    pass

def bidi_type_for_unichar(ch): # real signature unknown; restored from __doc__
    """ bidi_type_for_unichar(ch:str) -> Pango.BidiType """
    pass

def break_(text, length, analysis): # real signature unknown; restored from __doc__
    """ break_(text:str, length:int, analysis:Pango.Analysis) -> attrs:list """
    pass

def default_break(text, length, analysis=None): # real signature unknown; restored from __doc__
    """ default_break(text:str, length:int, analysis:Pango.Analysis=None) -> attrs:list """
    pass

def extents_to_pixels(inclusive, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ extents_to_pixels(inclusive:Pango.Rectangle=<optional>, nearest:Pango.Rectangle=<optional>) -> inclusive:Pango.Rectangle, nearest:Pango.Rectangle """
    pass

def find_base_dir(text, length): # real signature unknown; restored from __doc__
    """ find_base_dir(text:str, length:int) -> Pango.Direction """
    pass

def find_paragraph_boundary(text, length): # real signature unknown; restored from __doc__
    """ find_paragraph_boundary(text:str, length:int) -> paragraph_delimiter_index:int, next_paragraph_start:int """
    pass

def font_description_from_string(p_str): # real signature unknown; restored from __doc__
    """ font_description_from_string(str:str) -> Pango.FontDescription """
    pass

def get_log_attrs(text, length, level, language): # real signature unknown; restored from __doc__
    """ get_log_attrs(text:str, length:int, level:int, language:Pango.Language) -> attrs:list """
    pass

def get_mirror_char(ch): # real signature unknown; restored from __doc__
    """ get_mirror_char(ch:str) -> bool, mirrored_ch:str """
    return False

def gravity_get_for_matrix(matrix=None): # real signature unknown; restored from __doc__
    """ gravity_get_for_matrix(matrix:Pango.Matrix=None) -> Pango.Gravity """
    pass

def gravity_get_for_script(script, base_gravity, hint): # real signature unknown; restored from __doc__
    """ gravity_get_for_script(script:Pango.Script, base_gravity:Pango.Gravity, hint:Pango.GravityHint) -> Pango.Gravity """
    pass

def gravity_get_for_script_and_width(script, wide, base_gravity, hint): # real signature unknown; restored from __doc__
    """ gravity_get_for_script_and_width(script:Pango.Script, wide:bool, base_gravity:Pango.Gravity, hint:Pango.GravityHint) -> Pango.Gravity """
    pass

def gravity_to_rotation(gravity): # real signature unknown; restored from __doc__
    """ gravity_to_rotation(gravity:Pango.Gravity) -> float """
    return 0.0

def is_zero_width(ch): # real signature unknown; restored from __doc__
    """ is_zero_width(ch:str) -> bool """
    return False

def itemize(context, text, start_index, length, attrs, cached_iter=None): # real signature unknown; restored from __doc__
    """ itemize(context:Pango.Context, text:str, start_index:int, length:int, attrs:Pango.AttrList, cached_iter:Pango.AttrIterator=None) -> list """
    return []

def itemize_with_base_dir(context, base_dir, text, start_index, length, attrs, cached_iter=None): # real signature unknown; restored from __doc__
    """ itemize_with_base_dir(context:Pango.Context, base_dir:Pango.Direction, text:str, start_index:int, length:int, attrs:Pango.AttrList, cached_iter:Pango.AttrIterator=None) -> list """
    return []

def language_from_string(language=None): # real signature unknown; restored from __doc__
    """ language_from_string(language:str=None) -> Pango.Language or None """
    pass

def language_get_default(): # real signature unknown; restored from __doc__
    """ language_get_default() -> Pango.Language """
    pass

def language_get_preferred(): # real signature unknown; restored from __doc__
    """ language_get_preferred() -> list or None """
    return []

def layout_deserialize_error_quark(): # real signature unknown; restored from __doc__
    """ layout_deserialize_error_quark() -> int """
    return 0

def log2vis_get_embedding_levels(text, length, pbase_dir): # real signature unknown; restored from __doc__
    """ log2vis_get_embedding_levels(text:str, length:int, pbase_dir:Pango.Direction) -> list, pbase_dir:Pango.Direction """
    return []

def markup_parser_finish(context): # real signature unknown; restored from __doc__
    """ markup_parser_finish(context:GLib.MarkupParseContext) -> bool, attr_list:Pango.AttrList, text:str, accel_char:str """
    return False

def markup_parser_new(accel_marker): # real signature unknown; restored from __doc__
    """ markup_parser_new(accel_marker:str) -> GLib.MarkupParseContext """
    pass

def parse_enum(type, p_str=None, warn): # real signature unknown; restored from __doc__
    """ parse_enum(type:GType, str:str=None, warn:bool) -> bool, value:int, possible_values:str """
    return False

def parse_markup(markup_text, length, accel_marker): # real signature unknown; restored from __doc__
    """ parse_markup(markup_text:str, length:int, accel_marker:str) -> bool, attr_list:Pango.AttrList, text:str, accel_char:str """
    return False

def parse_stretch(p_str, warn): # real signature unknown; restored from __doc__
    """ parse_stretch(str:str, warn:bool) -> bool, stretch:Pango.Stretch """
    return False

def parse_style(p_str, warn): # real signature unknown; restored from __doc__
    """ parse_style(str:str, warn:bool) -> bool, style:Pango.Style """
    return False

def parse_variant(p_str, warn): # real signature unknown; restored from __doc__
    """ parse_variant(str:str, warn:bool) -> bool, variant:Pango.Variant """
    return False

def parse_weight(p_str, warn): # real signature unknown; restored from __doc__
    """ parse_weight(str:str, warn:bool) -> bool, weight:Pango.Weight """
    return False

def quantize_line_geometry(thickness, position): # real signature unknown; restored from __doc__
    """ quantize_line_geometry(thickness:int, position:int) -> thickness:int, position:int """
    pass

def read_line(stream=None, p_str): # real signature unknown; restored from __doc__
    """ read_line(stream=None, str:GLib.String) -> int """
    return 0

def reorder_items(items): # real signature unknown; restored from __doc__
    """ reorder_items(items:list) -> list """
    return []

def scan_int(pos): # real signature unknown; restored from __doc__
    """ scan_int(pos:str) -> bool, pos:str, out:int """
    return False

def scan_string(pos, out): # real signature unknown; restored from __doc__
    """ scan_string(pos:str, out:GLib.String) -> bool, pos:str """
    return False

def scan_word(pos, out): # real signature unknown; restored from __doc__
    """ scan_word(pos:str, out:GLib.String) -> bool, pos:str """
    return False

def script_for_unichar(ch): # real signature unknown; restored from __doc__
    """ script_for_unichar(ch:str) -> Pango.Script """
    pass

def script_get_sample_language(script): # real signature unknown; restored from __doc__
    """ script_get_sample_language(script:Pango.Script) -> Pango.Language or None """
    pass

def shape(text, length, analysis): # real signature unknown; restored from __doc__
    """ shape(text:str, length:int, analysis:Pango.Analysis) -> glyphs:Pango.GlyphString """
    pass

def shape_full(item_text, item_length, paragraph_text=None, paragraph_length, analysis): # real signature unknown; restored from __doc__
    """ shape_full(item_text:str, item_length:int, paragraph_text:str=None, paragraph_length:int, analysis:Pango.Analysis) -> glyphs:Pango.GlyphString """
    pass

def shape_item(item, paragraph_text=None, paragraph_length, log_attrs=None, flags): # real signature unknown; restored from __doc__
    """ shape_item(item:Pango.Item, paragraph_text:str=None, paragraph_length:int, log_attrs:Pango.LogAttr=None, flags:Pango.ShapeFlags) -> glyphs:Pango.GlyphString """
    pass

def shape_with_flags(item_text, item_length, paragraph_text=None, paragraph_length, analysis, flags): # real signature unknown; restored from __doc__
    """ shape_with_flags(item_text:str, item_length:int, paragraph_text:str=None, paragraph_length:int, analysis:Pango.Analysis, flags:Pango.ShapeFlags) -> glyphs:Pango.GlyphString """
    pass

def skip_space(pos): # real signature unknown; restored from __doc__
    """ skip_space(pos:str) -> bool, pos:str """
    return False

def split_file_list(p_str): # real signature unknown; restored from __doc__
    """ split_file_list(str:str) -> list """
    return []

def tab_array_from_string(text): # real signature unknown; restored from __doc__
    """ tab_array_from_string(text:str) -> Pango.TabArray or None """
    pass

def tailor_break(text, length, analysis, offset): # real signature unknown; restored from __doc__
    """ tailor_break(text:str, length:int, analysis:Pango.Analysis, offset:int) -> attrs:list """
    pass

def trim_string(p_str): # real signature unknown; restored from __doc__
    """ trim_string(str:str) -> str """
    return ""

def unichar_direction(ch): # real signature unknown; restored from __doc__
    """ unichar_direction(ch:str) -> Pango.Direction """
    pass

def units_from_double(d): # real signature unknown; restored from __doc__
    """ units_from_double(d:float) -> int """
    return 0

def units_to_double(i): # real signature unknown; restored from __doc__
    """ units_to_double(i:int) -> float """
    return 0.0

def version(): # real signature unknown; restored from __doc__
    """ version() -> int """
    return 0

def version_check(required_major, required_minor, required_micro): # real signature unknown; restored from __doc__
    """ version_check(required_major:int, required_minor:int, required_micro:int) -> str or None """
    return ""

def version_string(): # real signature unknown; restored from __doc__
    """ version_string() -> str """
    return ""

# classes

from .Alignment import Alignment
from .Analysis import Analysis
from .AttrClass import AttrClass
from .AttrColor import AttrColor
from .AttrFloat import AttrFloat
from .AttrFontDesc import AttrFontDesc
from .AttrFontFeatures import AttrFontFeatures
from .Attribute import Attribute
from .AttrInt import AttrInt
from .AttrIterator import AttrIterator
from .AttrLanguage import AttrLanguage
from .AttrList import AttrList
from .AttrShape import AttrShape
from .AttrSize import AttrSize
from .AttrString import AttrString
from .AttrType import AttrType
from .BaselineShift import BaselineShift
from .BidiType import BidiType
from .Color import Color
from .Context import Context
from .ContextClass import ContextClass
from .Coverage import Coverage
from .CoverageLevel import CoverageLevel
from .Direction import Direction
from .EllipsizeMode import EllipsizeMode
from .Font import Font
from .FontClass import FontClass
from .FontDescription import FontDescription
from .FontFace import FontFace
from .FontFaceClass import FontFaceClass
from .FontFamily import FontFamily
from .FontFamilyClass import FontFamilyClass
from .FontMap import FontMap
from .FontMapClass import FontMapClass
from .FontMask import FontMask
from .FontMetrics import FontMetrics
from .FontScale import FontScale
from .Fontset import Fontset
from .FontsetClass import FontsetClass
from .FontsetSimple import FontsetSimple
from .FontsetSimpleClass import FontsetSimpleClass
from .GlyphGeometry import GlyphGeometry
from .GlyphInfo import GlyphInfo
from .GlyphItem import GlyphItem
from .GlyphItemIter import GlyphItemIter
from .GlyphString import GlyphString
from .GlyphVisAttr import GlyphVisAttr
from .Gravity import Gravity
from .GravityHint import GravityHint
from .Item import Item
from .Language import Language
from .Layout import Layout
from .LayoutClass import LayoutClass
from .LayoutDeserializeError import LayoutDeserializeError
from .LayoutDeserializeFlags import LayoutDeserializeFlags
from .LayoutIter import LayoutIter
from .LayoutLine import LayoutLine
from .LayoutSerializeFlags import LayoutSerializeFlags
from .LogAttr import LogAttr
from .Matrix import Matrix
from .Overline import Overline
from .Rectangle import Rectangle
from .Renderer import Renderer
from .RendererClass import RendererClass
from .RendererPrivate import RendererPrivate
from .RenderPart import RenderPart
from .Script import Script
from .ScriptIter import ScriptIter
from .ShapeFlags import ShapeFlags
from .ShowFlags import ShowFlags
from .Stretch import Stretch
from .Style import Style
from .TabAlign import TabAlign
from .TabArray import TabArray
from .TextTransform import TextTransform
from .Underline import Underline
from .Variant import Variant
from .Weight import Weight
from .WrapMode import WrapMode
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x0000028034fe8440>'

__path__ = []

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Pango', loader=<gi.importer.DynamicImporter object at 0x0000028034fe8440>)"

