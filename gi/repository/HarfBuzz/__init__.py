# encoding: utf-8
# module gi.repository.HarfBuzz
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi


# Variables with simple values

AAT_LAYOUT_NO_SELECTOR_INDEX = 65535

BUFFER_REPLACEMENT_CODEPOINT_DEFAULT = 65533

CODEPOINT_INVALID = 4294967295

FEATURE_GLOBAL_START = 0

FONT_NO_VAR_NAMED_INSTANCE = -1

LANGUAGE_INVALID = None

OT_LAYOUT_DEFAULT_LANGUAGE_INDEX = 65535

OT_LAYOUT_NO_FEATURE_INDEX = 65535

OT_LAYOUT_NO_SCRIPT_INDEX = 65535

OT_LAYOUT_NO_VARIATIONS_INDEX = -1

OT_MAX_TAGS_PER_LANGUAGE = 3
OT_MAX_TAGS_PER_SCRIPT = 3

OT_VAR_NO_AXIS_INDEX = -1

UNICODE_COMBINING_CLASS_CCC133 = 133

UNICODE_MAX = 1114111

UNICODE_MAX_DECOMPOSITION_LEN = 19

VERSION_MAJOR = 12
VERSION_MICRO = 2
VERSION_MINOR = 3
VERSION_STRING = '12.3.2'

_namespace = 'HarfBuzz'

_version = '0.0'

# functions

def aat_layout_feature_type_get_name_id(face, feature_type): # real signature unknown; restored from __doc__
    """ aat_layout_feature_type_get_name_id(face:HarfBuzz.face_t, feature_type:HarfBuzz.aat_layout_feature_type_t) -> int """
    return 0

def aat_layout_feature_type_get_selector_infos(face, feature_type, start_offset): # real signature unknown; restored from __doc__
    """ aat_layout_feature_type_get_selector_infos(face:HarfBuzz.face_t, feature_type:HarfBuzz.aat_layout_feature_type_t, start_offset:int) -> int, selectors:list, default_index:int """
    return 0

def aat_layout_get_feature_types(face, start_offset): # real signature unknown; restored from __doc__
    """ aat_layout_get_feature_types(face:HarfBuzz.face_t, start_offset:int) -> int, features:list """
    return 0

def aat_layout_has_positioning(face): # real signature unknown; restored from __doc__
    """ aat_layout_has_positioning(face:HarfBuzz.face_t) -> int """
    return 0

def aat_layout_has_substitution(face): # real signature unknown; restored from __doc__
    """ aat_layout_has_substitution(face:HarfBuzz.face_t) -> int """
    return 0

def aat_layout_has_tracking(face): # real signature unknown; restored from __doc__
    """ aat_layout_has_tracking(face:HarfBuzz.face_t) -> int """
    return 0

def blob_copy_writable_or_fail(blob): # real signature unknown; restored from __doc__
    """ blob_copy_writable_or_fail(blob:HarfBuzz.blob_t) -> HarfBuzz.blob_t """
    pass

def blob_create_from_file(file_name): # real signature unknown; restored from __doc__
    """ blob_create_from_file(file_name:str) -> HarfBuzz.blob_t """
    pass

def blob_create_from_file_or_fail(file_name): # real signature unknown; restored from __doc__
    """ blob_create_from_file_or_fail(file_name:str) -> HarfBuzz.blob_t """
    pass

def blob_create_sub_blob(parent, offset, length): # real signature unknown; restored from __doc__
    """ blob_create_sub_blob(parent:HarfBuzz.blob_t, offset:int, length:int) -> HarfBuzz.blob_t """
    pass

def blob_get_data(blob): # real signature unknown; restored from __doc__
    """ blob_get_data(blob:HarfBuzz.blob_t) -> list or None """
    return []

def blob_get_data_writable(blob): # real signature unknown; restored from __doc__
    """ blob_get_data_writable(blob:HarfBuzz.blob_t) -> list """
    return []

def blob_get_empty(): # real signature unknown; restored from __doc__
    """ blob_get_empty() -> HarfBuzz.blob_t """
    pass

def blob_get_length(blob): # real signature unknown; restored from __doc__
    """ blob_get_length(blob:HarfBuzz.blob_t) -> int """
    return 0

def blob_is_immutable(blob): # real signature unknown; restored from __doc__
    """ blob_is_immutable(blob:HarfBuzz.blob_t) -> int """
    return 0

def blob_make_immutable(blob): # real signature unknown; restored from __doc__
    """ blob_make_immutable(blob:HarfBuzz.blob_t) """
    pass

def buffer_add(buffer, codepoint, cluster): # real signature unknown; restored from __doc__
    """ buffer_add(buffer:HarfBuzz.buffer_t, codepoint:int, cluster:int) """
    pass

def buffer_add_codepoints(buffer, text, item_offset, item_length): # real signature unknown; restored from __doc__
    """ buffer_add_codepoints(buffer:HarfBuzz.buffer_t, text:list, item_offset:int, item_length:int) """
    pass

def buffer_add_latin1(buffer, text, item_offset, item_length): # real signature unknown; restored from __doc__
    """ buffer_add_latin1(buffer:HarfBuzz.buffer_t, text:list, item_offset:int, item_length:int) """
    pass

def buffer_add_utf16(buffer, text, item_offset, item_length): # real signature unknown; restored from __doc__
    """ buffer_add_utf16(buffer:HarfBuzz.buffer_t, text:list, item_offset:int, item_length:int) """
    pass

def buffer_add_utf32(buffer, text, item_offset, item_length): # real signature unknown; restored from __doc__
    """ buffer_add_utf32(buffer:HarfBuzz.buffer_t, text:list, item_offset:int, item_length:int) """
    pass

def buffer_add_utf8(buffer, text, item_offset, item_length): # real signature unknown; restored from __doc__
    """ buffer_add_utf8(buffer:HarfBuzz.buffer_t, text:list, item_offset:int, item_length:int) """
    pass

def buffer_allocation_successful(buffer): # real signature unknown; restored from __doc__
    """ buffer_allocation_successful(buffer:HarfBuzz.buffer_t) -> int """
    return 0

def buffer_append(buffer, source, start, end): # real signature unknown; restored from __doc__
    """ buffer_append(buffer:HarfBuzz.buffer_t, source:HarfBuzz.buffer_t, start:int, end:int) """
    pass

def buffer_clear_contents(buffer): # real signature unknown; restored from __doc__
    """ buffer_clear_contents(buffer:HarfBuzz.buffer_t) """
    pass

def buffer_create(): # real signature unknown; restored from __doc__
    """ buffer_create() -> HarfBuzz.buffer_t """
    pass

def buffer_create_similar(src): # real signature unknown; restored from __doc__
    """ buffer_create_similar(src:HarfBuzz.buffer_t) -> HarfBuzz.buffer_t """
    pass

def buffer_deserialize_glyphs(buffer, buf, font=None, format): # real signature unknown; restored from __doc__
    """ buffer_deserialize_glyphs(buffer:HarfBuzz.buffer_t, buf:list, font:HarfBuzz.font_t=None, format:HarfBuzz.buffer_serialize_format_t) -> int, end_ptr:str """
    return 0

def buffer_deserialize_unicode(buffer, buf, format): # real signature unknown; restored from __doc__
    """ buffer_deserialize_unicode(buffer:HarfBuzz.buffer_t, buf:list, format:HarfBuzz.buffer_serialize_format_t) -> int, end_ptr:str """
    return 0

def buffer_diff(buffer, reference, dottedcircle_glyph, position_fuzz): # real signature unknown; restored from __doc__
    """ buffer_diff(buffer:HarfBuzz.buffer_t, reference:HarfBuzz.buffer_t, dottedcircle_glyph:int, position_fuzz:int) -> HarfBuzz.buffer_diff_flags_t """
    pass

def buffer_get_cluster_level(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_cluster_level(buffer:HarfBuzz.buffer_t) -> HarfBuzz.buffer_cluster_level_t """
    pass

def buffer_get_content_type(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_content_type(buffer:HarfBuzz.buffer_t) -> HarfBuzz.buffer_content_type_t """
    pass

def buffer_get_direction(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_direction(buffer:HarfBuzz.buffer_t) -> HarfBuzz.direction_t """
    pass

def buffer_get_empty(): # real signature unknown; restored from __doc__
    """ buffer_get_empty() -> HarfBuzz.buffer_t """
    pass

def buffer_get_flags(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_flags(buffer:HarfBuzz.buffer_t) -> HarfBuzz.buffer_flags_t """
    pass

def buffer_get_glyph_infos(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_glyph_infos(buffer:HarfBuzz.buffer_t) -> list """
    return []

def buffer_get_glyph_positions(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_glyph_positions(buffer:HarfBuzz.buffer_t) -> list """
    return []

def buffer_get_invisible_glyph(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_invisible_glyph(buffer:HarfBuzz.buffer_t) -> int """
    return 0

def buffer_get_language(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_language(buffer:HarfBuzz.buffer_t) -> HarfBuzz.language_t """
    pass

def buffer_get_length(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_length(buffer:HarfBuzz.buffer_t) -> int """
    return 0

def buffer_get_not_found_glyph(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_not_found_glyph(buffer:HarfBuzz.buffer_t) -> int """
    return 0

def buffer_get_not_found_variation_selector_glyph(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_not_found_variation_selector_glyph(buffer:HarfBuzz.buffer_t) -> int """
    return 0

def buffer_get_random_state(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_random_state(buffer:HarfBuzz.buffer_t) -> int """
    return 0

def buffer_get_replacement_codepoint(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_replacement_codepoint(buffer:HarfBuzz.buffer_t) -> int """
    return 0

def buffer_get_script(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_script(buffer:HarfBuzz.buffer_t) -> HarfBuzz.script_t """
    pass

def buffer_get_segment_properties(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_segment_properties(buffer:HarfBuzz.buffer_t) -> props:HarfBuzz.segment_properties_t """
    pass

def buffer_get_unicode_funcs(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_unicode_funcs(buffer:HarfBuzz.buffer_t) -> HarfBuzz.unicode_funcs_t """
    pass

def buffer_guess_segment_properties(buffer): # real signature unknown; restored from __doc__
    """ buffer_guess_segment_properties(buffer:HarfBuzz.buffer_t) """
    pass

def buffer_has_positions(buffer): # real signature unknown; restored from __doc__
    """ buffer_has_positions(buffer:HarfBuzz.buffer_t) -> int """
    return 0

def buffer_normalize_glyphs(buffer): # real signature unknown; restored from __doc__
    """ buffer_normalize_glyphs(buffer:HarfBuzz.buffer_t) """
    pass

def buffer_pre_allocate(buffer, size): # real signature unknown; restored from __doc__
    """ buffer_pre_allocate(buffer:HarfBuzz.buffer_t, size:int) -> int """
    return 0

def buffer_reset(buffer): # real signature unknown; restored from __doc__
    """ buffer_reset(buffer:HarfBuzz.buffer_t) """
    pass

def buffer_reverse(buffer): # real signature unknown; restored from __doc__
    """ buffer_reverse(buffer:HarfBuzz.buffer_t) """
    pass

def buffer_reverse_clusters(buffer): # real signature unknown; restored from __doc__
    """ buffer_reverse_clusters(buffer:HarfBuzz.buffer_t) """
    pass

def buffer_reverse_range(buffer, start, end): # real signature unknown; restored from __doc__
    """ buffer_reverse_range(buffer:HarfBuzz.buffer_t, start:int, end:int) """
    pass

def buffer_serialize(buffer, start, end, font=None, format, flags): # real signature unknown; restored from __doc__
    """ buffer_serialize(buffer:HarfBuzz.buffer_t, start:int, end:int, font:HarfBuzz.font_t=None, format:HarfBuzz.buffer_serialize_format_t, flags:HarfBuzz.buffer_serialize_flags_t) -> int, buf:list, buf_consumed:int """
    return 0

def buffer_serialize_format_from_string(p_str): # real signature unknown; restored from __doc__
    """ buffer_serialize_format_from_string(str:list) -> HarfBuzz.buffer_serialize_format_t """
    pass

def buffer_serialize_format_to_string(format): # real signature unknown; restored from __doc__
    """ buffer_serialize_format_to_string(format:HarfBuzz.buffer_serialize_format_t) -> str """
    return ""

def buffer_serialize_glyphs(buffer, start, end, font=None, format, flags): # real signature unknown; restored from __doc__
    """ buffer_serialize_glyphs(buffer:HarfBuzz.buffer_t, start:int, end:int, font:HarfBuzz.font_t=None, format:HarfBuzz.buffer_serialize_format_t, flags:HarfBuzz.buffer_serialize_flags_t) -> int, buf:list, buf_consumed:int """
    return 0

def buffer_serialize_list_formats(): # real signature unknown; restored from __doc__
    """ buffer_serialize_list_formats() -> list """
    return []

def buffer_serialize_unicode(buffer, start, end, format, flags): # real signature unknown; restored from __doc__
    """ buffer_serialize_unicode(buffer:HarfBuzz.buffer_t, start:int, end:int, format:HarfBuzz.buffer_serialize_format_t, flags:HarfBuzz.buffer_serialize_flags_t) -> int, buf:list, buf_consumed:int """
    return 0

def buffer_set_cluster_level(buffer, cluster_level): # real signature unknown; restored from __doc__
    """ buffer_set_cluster_level(buffer:HarfBuzz.buffer_t, cluster_level:HarfBuzz.buffer_cluster_level_t) """
    pass

def buffer_set_content_type(buffer, content_type): # real signature unknown; restored from __doc__
    """ buffer_set_content_type(buffer:HarfBuzz.buffer_t, content_type:HarfBuzz.buffer_content_type_t) """
    pass

def buffer_set_direction(buffer, direction): # real signature unknown; restored from __doc__
    """ buffer_set_direction(buffer:HarfBuzz.buffer_t, direction:HarfBuzz.direction_t) """
    pass

def buffer_set_flags(buffer, flags): # real signature unknown; restored from __doc__
    """ buffer_set_flags(buffer:HarfBuzz.buffer_t, flags:HarfBuzz.buffer_flags_t) """
    pass

def buffer_set_invisible_glyph(buffer, invisible): # real signature unknown; restored from __doc__
    """ buffer_set_invisible_glyph(buffer:HarfBuzz.buffer_t, invisible:int) """
    pass

def buffer_set_language(buffer, language): # real signature unknown; restored from __doc__
    """ buffer_set_language(buffer:HarfBuzz.buffer_t, language:HarfBuzz.language_t) """
    pass

def buffer_set_length(buffer, length): # real signature unknown; restored from __doc__
    """ buffer_set_length(buffer:HarfBuzz.buffer_t, length:int) -> int """
    return 0

def buffer_set_message_func(buffer, func, user_data=None): # real signature unknown; restored from __doc__
    """ buffer_set_message_func(buffer:HarfBuzz.buffer_t, func:HarfBuzz.buffer_message_func_t, user_data=None) """
    pass

def buffer_set_not_found_glyph(buffer, not_found): # real signature unknown; restored from __doc__
    """ buffer_set_not_found_glyph(buffer:HarfBuzz.buffer_t, not_found:int) """
    pass

def buffer_set_not_found_variation_selector_glyph(buffer, not_found_variation_selector): # real signature unknown; restored from __doc__
    """ buffer_set_not_found_variation_selector_glyph(buffer:HarfBuzz.buffer_t, not_found_variation_selector:int) """
    pass

def buffer_set_random_state(buffer, state): # real signature unknown; restored from __doc__
    """ buffer_set_random_state(buffer:HarfBuzz.buffer_t, state:int) """
    pass

def buffer_set_replacement_codepoint(buffer, replacement): # real signature unknown; restored from __doc__
    """ buffer_set_replacement_codepoint(buffer:HarfBuzz.buffer_t, replacement:int) """
    pass

def buffer_set_script(buffer, script): # real signature unknown; restored from __doc__
    """ buffer_set_script(buffer:HarfBuzz.buffer_t, script:HarfBuzz.script_t) """
    pass

def buffer_set_segment_properties(buffer, props): # real signature unknown; restored from __doc__
    """ buffer_set_segment_properties(buffer:HarfBuzz.buffer_t, props:HarfBuzz.segment_properties_t) """
    pass

def buffer_set_unicode_funcs(buffer, unicode_funcs): # real signature unknown; restored from __doc__
    """ buffer_set_unicode_funcs(buffer:HarfBuzz.buffer_t, unicode_funcs:HarfBuzz.unicode_funcs_t) """
    pass

def calloc(nmemb, size): # real signature unknown; restored from __doc__
    """ calloc(nmemb:int, size:int) """
    pass

def color_get_alpha(color): # real signature unknown; restored from __doc__
    """ color_get_alpha(color:int) -> int """
    return 0

def color_get_blue(color): # real signature unknown; restored from __doc__
    """ color_get_blue(color:int) -> int """
    return 0

def color_get_green(color): # real signature unknown; restored from __doc__
    """ color_get_green(color:int) -> int """
    return 0

def color_get_red(color): # real signature unknown; restored from __doc__
    """ color_get_red(color:int) -> int """
    return 0

def color_line_get_color_stops(color_line, start): # real signature unknown; restored from __doc__
    """ color_line_get_color_stops(color_line:HarfBuzz.color_line_t, start:int) -> int, color_stops:list """
    return 0

def color_line_get_extend(color_line): # real signature unknown; restored from __doc__
    """ color_line_get_extend(color_line:HarfBuzz.color_line_t) -> HarfBuzz.paint_extend_t """
    pass

def direction_from_string(p_str): # real signature unknown; restored from __doc__
    """ direction_from_string(str:list) -> HarfBuzz.direction_t """
    pass

def direction_to_string(direction): # real signature unknown; restored from __doc__
    """ direction_to_string(direction:HarfBuzz.direction_t) -> str """
    return ""

def draw_close_path(dfuncs, draw_data=None, st): # real signature unknown; restored from __doc__
    """ draw_close_path(dfuncs:HarfBuzz.draw_funcs_t, draw_data=None, st:HarfBuzz.draw_state_t) """
    pass

def draw_cubic_to(dfuncs, draw_data=None, st, control1_x, control1_y, control2_x, control2_y, to_x, to_y): # real signature unknown; restored from __doc__
    """ draw_cubic_to(dfuncs:HarfBuzz.draw_funcs_t, draw_data=None, st:HarfBuzz.draw_state_t, control1_x:float, control1_y:float, control2_x:float, control2_y:float, to_x:float, to_y:float) """
    pass

def draw_funcs_create(): # real signature unknown; restored from __doc__
    """ draw_funcs_create() -> HarfBuzz.draw_funcs_t """
    pass

def draw_funcs_get_empty(): # real signature unknown; restored from __doc__
    """ draw_funcs_get_empty() -> HarfBuzz.draw_funcs_t """
    pass

def draw_funcs_is_immutable(dfuncs): # real signature unknown; restored from __doc__
    """ draw_funcs_is_immutable(dfuncs:HarfBuzz.draw_funcs_t) -> int """
    return 0

def draw_funcs_make_immutable(dfuncs): # real signature unknown; restored from __doc__
    """ draw_funcs_make_immutable(dfuncs:HarfBuzz.draw_funcs_t) """
    pass

def draw_funcs_set_close_path_func(dfuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ draw_funcs_set_close_path_func(dfuncs:HarfBuzz.draw_funcs_t, func:HarfBuzz.draw_close_path_func_t, user_data=None) """
    pass

def draw_funcs_set_cubic_to_func(dfuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ draw_funcs_set_cubic_to_func(dfuncs:HarfBuzz.draw_funcs_t, func:HarfBuzz.draw_cubic_to_func_t, user_data=None) """
    pass

def draw_funcs_set_line_to_func(dfuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ draw_funcs_set_line_to_func(dfuncs:HarfBuzz.draw_funcs_t, func:HarfBuzz.draw_line_to_func_t, user_data=None) """
    pass

def draw_funcs_set_move_to_func(dfuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ draw_funcs_set_move_to_func(dfuncs:HarfBuzz.draw_funcs_t, func:HarfBuzz.draw_move_to_func_t, user_data=None) """
    pass

def draw_funcs_set_quadratic_to_func(dfuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ draw_funcs_set_quadratic_to_func(dfuncs:HarfBuzz.draw_funcs_t, func:HarfBuzz.draw_quadratic_to_func_t, user_data=None) """
    pass

def draw_line_to(dfuncs, draw_data=None, st, to_x, to_y): # real signature unknown; restored from __doc__
    """ draw_line_to(dfuncs:HarfBuzz.draw_funcs_t, draw_data=None, st:HarfBuzz.draw_state_t, to_x:float, to_y:float) """
    pass

def draw_move_to(dfuncs, draw_data=None, st, to_x, to_y): # real signature unknown; restored from __doc__
    """ draw_move_to(dfuncs:HarfBuzz.draw_funcs_t, draw_data=None, st:HarfBuzz.draw_state_t, to_x:float, to_y:float) """
    pass

def draw_quadratic_to(dfuncs, draw_data=None, st, control_x, control_y, to_x, to_y): # real signature unknown; restored from __doc__
    """ draw_quadratic_to(dfuncs:HarfBuzz.draw_funcs_t, draw_data=None, st:HarfBuzz.draw_state_t, control_x:float, control_y:float, to_x:float, to_y:float) """
    pass

def face_builder_add_table(face, tag, blob): # real signature unknown; restored from __doc__
    """ face_builder_add_table(face:HarfBuzz.face_t, tag:int, blob:HarfBuzz.blob_t) -> int """
    return 0

def face_builder_create(): # real signature unknown; restored from __doc__
    """ face_builder_create() -> HarfBuzz.face_t """
    pass

def face_builder_sort_tables(face, tags): # real signature unknown; restored from __doc__
    """ face_builder_sort_tables(face:HarfBuzz.face_t, tags:list) """
    pass

def face_collect_nominal_glyph_mapping(face): # real signature unknown; restored from __doc__
    """ face_collect_nominal_glyph_mapping(face:HarfBuzz.face_t) -> mapping:HarfBuzz.map_t, unicodes:HarfBuzz.set_t """
    pass

def face_collect_unicodes(face): # real signature unknown; restored from __doc__
    """ face_collect_unicodes(face:HarfBuzz.face_t) -> out:HarfBuzz.set_t """
    pass

def face_collect_variation_selectors(face): # real signature unknown; restored from __doc__
    """ face_collect_variation_selectors(face:HarfBuzz.face_t) -> out:HarfBuzz.set_t """
    pass

def face_collect_variation_unicodes(face, variation_selector): # real signature unknown; restored from __doc__
    """ face_collect_variation_unicodes(face:HarfBuzz.face_t, variation_selector:int) -> out:HarfBuzz.set_t """
    pass

def face_count(blob): # real signature unknown; restored from __doc__
    """ face_count(blob:HarfBuzz.blob_t) -> int """
    return 0

def face_create(blob, index): # real signature unknown; restored from __doc__
    """ face_create(blob:HarfBuzz.blob_t, index:int) -> HarfBuzz.face_t """
    pass

def face_create_for_tables(reference_table_func, user_data=None): # real signature unknown; restored from __doc__
    """ face_create_for_tables(reference_table_func:HarfBuzz.reference_table_func_t, user_data=None) -> HarfBuzz.face_t """
    pass

def face_create_from_file_or_fail(file_name, index): # real signature unknown; restored from __doc__
    """ face_create_from_file_or_fail(file_name:str, index:int) -> HarfBuzz.face_t """
    pass

def face_create_from_file_or_fail_using(file_name, index, loader_name=None): # real signature unknown; restored from __doc__
    """ face_create_from_file_or_fail_using(file_name:str, index:int, loader_name:str=None) -> HarfBuzz.face_t """
    pass

def face_create_or_fail(blob, index): # real signature unknown; restored from __doc__
    """ face_create_or_fail(blob:HarfBuzz.blob_t, index:int) -> HarfBuzz.face_t """
    pass

def face_create_or_fail_using(blob, index, loader_name=None): # real signature unknown; restored from __doc__
    """ face_create_or_fail_using(blob:HarfBuzz.blob_t, index:int, loader_name:str=None) -> HarfBuzz.face_t """
    pass

def face_get_empty(): # real signature unknown; restored from __doc__
    """ face_get_empty() -> HarfBuzz.face_t """
    pass

def face_get_glyph_count(face): # real signature unknown; restored from __doc__
    """ face_get_glyph_count(face:HarfBuzz.face_t) -> int """
    return 0

def face_get_index(face): # real signature unknown; restored from __doc__
    """ face_get_index(face:HarfBuzz.face_t) -> int """
    return 0

def face_get_table_tags(face, start_offset): # real signature unknown; restored from __doc__
    """ face_get_table_tags(face:HarfBuzz.face_t, start_offset:int) -> int, table_tags:list """
    return 0

def face_get_upem(face): # real signature unknown; restored from __doc__
    """ face_get_upem(face:HarfBuzz.face_t) -> int """
    return 0

def face_is_immutable(face): # real signature unknown; restored from __doc__
    """ face_is_immutable(face:HarfBuzz.face_t) -> int """
    return 0

def face_list_loaders(): # real signature unknown; restored from __doc__
    """ face_list_loaders() -> list """
    return []

def face_make_immutable(face): # real signature unknown; restored from __doc__
    """ face_make_immutable(face:HarfBuzz.face_t) """
    pass

def face_reference_blob(face): # real signature unknown; restored from __doc__
    """ face_reference_blob(face:HarfBuzz.face_t) -> HarfBuzz.blob_t """
    pass

def face_reference_table(face, tag): # real signature unknown; restored from __doc__
    """ face_reference_table(face:HarfBuzz.face_t, tag:int) -> HarfBuzz.blob_t """
    pass

def face_set_get_table_tags_func(face, func, user_data=None): # real signature unknown; restored from __doc__
    """ face_set_get_table_tags_func(face:HarfBuzz.face_t, func:HarfBuzz.get_table_tags_func_t, user_data=None) """
    pass

def face_set_glyph_count(face, glyph_count): # real signature unknown; restored from __doc__
    """ face_set_glyph_count(face:HarfBuzz.face_t, glyph_count:int) """
    pass

def face_set_index(face, index): # real signature unknown; restored from __doc__
    """ face_set_index(face:HarfBuzz.face_t, index:int) """
    pass

def face_set_upem(face, upem): # real signature unknown; restored from __doc__
    """ face_set_upem(face:HarfBuzz.face_t, upem:int) """
    pass

def feature_from_string(p_str): # real signature unknown; restored from __doc__
    """ feature_from_string(str:list) -> int, feature:HarfBuzz.feature_t """
    return 0

def feature_to_string(feature): # real signature unknown; restored from __doc__
    """ feature_to_string(feature:HarfBuzz.feature_t) -> buf:list """
    pass

def font_add_glyph_origin_for_direction(font, glyph, direction, x, y): # real signature unknown; restored from __doc__
    """ font_add_glyph_origin_for_direction(font:HarfBuzz.font_t, glyph:int, direction:HarfBuzz.direction_t, x:int, y:int) -> x:int, y:int """
    pass

def font_changed(font): # real signature unknown; restored from __doc__
    """ font_changed(font:HarfBuzz.font_t) """
    pass

def font_create(face): # real signature unknown; restored from __doc__
    """ font_create(face:HarfBuzz.face_t) -> HarfBuzz.font_t """
    pass

def font_create_sub_font(parent): # real signature unknown; restored from __doc__
    """ font_create_sub_font(parent:HarfBuzz.font_t) -> HarfBuzz.font_t """
    pass

def font_draw_glyph(font, glyph, dfuncs, draw_data=None): # real signature unknown; restored from __doc__
    """ font_draw_glyph(font:HarfBuzz.font_t, glyph:int, dfuncs:HarfBuzz.draw_funcs_t, draw_data=None) """
    pass

def font_draw_glyph_or_fail(font, glyph, dfuncs, draw_data=None): # real signature unknown; restored from __doc__
    """ font_draw_glyph_or_fail(font:HarfBuzz.font_t, glyph:int, dfuncs:HarfBuzz.draw_funcs_t, draw_data=None) -> int """
    return 0

def font_funcs_create(): # real signature unknown; restored from __doc__
    """ font_funcs_create() -> HarfBuzz.font_funcs_t """
    pass

def font_funcs_get_empty(): # real signature unknown; restored from __doc__
    """ font_funcs_get_empty() -> HarfBuzz.font_funcs_t """
    pass

def font_funcs_is_immutable(ffuncs): # real signature unknown; restored from __doc__
    """ font_funcs_is_immutable(ffuncs:HarfBuzz.font_funcs_t) -> int """
    return 0

def font_funcs_make_immutable(ffuncs): # real signature unknown; restored from __doc__
    """ font_funcs_make_immutable(ffuncs:HarfBuzz.font_funcs_t) """
    pass

def font_funcs_set_draw_glyph_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_draw_glyph_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_draw_glyph_func_t, user_data=None) """
    pass

def font_funcs_set_draw_glyph_or_fail_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_draw_glyph_or_fail_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_draw_glyph_or_fail_func_t, user_data=None) """
    pass

def font_funcs_set_font_h_extents_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_font_h_extents_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_font_extents_func_t, user_data=None) """
    pass

def font_funcs_set_font_v_extents_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_font_v_extents_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_font_extents_func_t, user_data=None) """
    pass

def font_funcs_set_glyph_contour_point_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_glyph_contour_point_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_glyph_contour_point_func_t, user_data=None) """
    pass

def font_funcs_set_glyph_extents_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_glyph_extents_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_glyph_extents_func_t, user_data=None) """
    pass

def font_funcs_set_glyph_from_name_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_glyph_from_name_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_glyph_from_name_func_t, user_data=None) """
    pass

def font_funcs_set_glyph_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_glyph_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_glyph_func_t, user_data=None) """
    pass

def font_funcs_set_glyph_h_advances_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_glyph_h_advances_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_glyph_advances_func_t, user_data=None) """
    pass

def font_funcs_set_glyph_h_advance_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_glyph_h_advance_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_glyph_advance_func_t, user_data=None) """
    pass

def font_funcs_set_glyph_h_kerning_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_glyph_h_kerning_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_glyph_kerning_func_t, user_data=None) """
    pass

def font_funcs_set_glyph_h_origins_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_glyph_h_origins_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_glyph_origins_func_t, user_data=None) """
    pass

def font_funcs_set_glyph_h_origin_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_glyph_h_origin_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_glyph_origin_func_t, user_data=None) """
    pass

def font_funcs_set_glyph_name_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_glyph_name_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_glyph_name_func_t, user_data=None) """
    pass

def font_funcs_set_glyph_shape_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_glyph_shape_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_glyph_shape_func_t, user_data=None) """
    pass

def font_funcs_set_glyph_v_advances_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_glyph_v_advances_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_glyph_advances_func_t, user_data=None) """
    pass

def font_funcs_set_glyph_v_advance_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_glyph_v_advance_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_glyph_advance_func_t, user_data=None) """
    pass

def font_funcs_set_glyph_v_kerning_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_glyph_v_kerning_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_glyph_kerning_func_t, user_data=None) """
    pass

def font_funcs_set_glyph_v_origins_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_glyph_v_origins_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_glyph_origins_func_t, user_data=None) """
    pass

def font_funcs_set_glyph_v_origin_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_glyph_v_origin_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_glyph_origin_func_t, user_data=None) """
    pass

def font_funcs_set_nominal_glyphs_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_nominal_glyphs_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_nominal_glyphs_func_t, user_data=None) """
    pass

def font_funcs_set_nominal_glyph_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_nominal_glyph_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_nominal_glyph_func_t, user_data=None) """
    pass

def font_funcs_set_paint_glyph_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_paint_glyph_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_paint_glyph_func_t, user_data=None) """
    pass

def font_funcs_set_paint_glyph_or_fail_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_paint_glyph_or_fail_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_paint_glyph_or_fail_func_t, user_data=None) """
    pass

def font_funcs_set_variation_glyph_func(ffuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ font_funcs_set_variation_glyph_func(ffuncs:HarfBuzz.font_funcs_t, func:HarfBuzz.font_get_variation_glyph_func_t, user_data=None) """
    pass

def font_get_empty(): # real signature unknown; restored from __doc__
    """ font_get_empty() -> HarfBuzz.font_t """
    pass

def font_get_extents_for_direction(font, direction): # real signature unknown; restored from __doc__
    """ font_get_extents_for_direction(font:HarfBuzz.font_t, direction:HarfBuzz.direction_t) -> extents:HarfBuzz.font_extents_t """
    pass

def font_get_face(font): # real signature unknown; restored from __doc__
    """ font_get_face(font:HarfBuzz.font_t) -> HarfBuzz.face_t """
    pass

def font_get_glyph(font, unicode, variation_selector): # real signature unknown; restored from __doc__
    """ font_get_glyph(font:HarfBuzz.font_t, unicode:int, variation_selector:int) -> int, glyph:int """
    return 0

def font_get_glyph_advances_for_direction(font, direction, count, first_glyph, glyph_stride): # real signature unknown; restored from __doc__
    """ font_get_glyph_advances_for_direction(font:HarfBuzz.font_t, direction:HarfBuzz.direction_t, count:int, first_glyph:int, glyph_stride:int) -> first_advance:int, advance_stride:int """
    pass

def font_get_glyph_advance_for_direction(font, glyph, direction): # real signature unknown; restored from __doc__
    """ font_get_glyph_advance_for_direction(font:HarfBuzz.font_t, glyph:int, direction:HarfBuzz.direction_t) -> x:int, y:int """
    pass

def font_get_glyph_contour_point(font, glyph, point_index): # real signature unknown; restored from __doc__
    """ font_get_glyph_contour_point(font:HarfBuzz.font_t, glyph:int, point_index:int) -> int, x:int, y:int """
    return 0

def font_get_glyph_contour_point_for_origin(font, glyph, point_index, direction): # real signature unknown; restored from __doc__
    """ font_get_glyph_contour_point_for_origin(font:HarfBuzz.font_t, glyph:int, point_index:int, direction:HarfBuzz.direction_t) -> int, x:int, y:int """
    return 0

def font_get_glyph_extents(font, glyph): # real signature unknown; restored from __doc__
    """ font_get_glyph_extents(font:HarfBuzz.font_t, glyph:int) -> int, extents:HarfBuzz.glyph_extents_t """
    return 0

def font_get_glyph_extents_for_origin(font, glyph, direction): # real signature unknown; restored from __doc__
    """ font_get_glyph_extents_for_origin(font:HarfBuzz.font_t, glyph:int, direction:HarfBuzz.direction_t) -> int, extents:HarfBuzz.glyph_extents_t """
    return 0

def font_get_glyph_from_name(font, name): # real signature unknown; restored from __doc__
    """ font_get_glyph_from_name(font:HarfBuzz.font_t, name:list) -> int, glyph:int """
    return 0

def font_get_glyph_h_advance(font, glyph): # real signature unknown; restored from __doc__
    """ font_get_glyph_h_advance(font:HarfBuzz.font_t, glyph:int) -> int """
    return 0

def font_get_glyph_h_advances(font, count, first_glyph, glyph_stride, advance_stride): # real signature unknown; restored from __doc__
    """ font_get_glyph_h_advances(font:HarfBuzz.font_t, count:int, first_glyph:int, glyph_stride:int, advance_stride:int) -> first_advance:int """
    pass

def font_get_glyph_h_kerning(font, left_glyph, right_glyph): # real signature unknown; restored from __doc__
    """ font_get_glyph_h_kerning(font:HarfBuzz.font_t, left_glyph:int, right_glyph:int) -> int """
    return 0

def font_get_glyph_h_origin(font, glyph): # real signature unknown; restored from __doc__
    """ font_get_glyph_h_origin(font:HarfBuzz.font_t, glyph:int) -> int, x:int, y:int """
    return 0

def font_get_glyph_h_origins(font, count, first_glyph, glyph_stride, x_stride, y_stride): # real signature unknown; restored from __doc__
    """ font_get_glyph_h_origins(font:HarfBuzz.font_t, count:int, first_glyph:int, glyph_stride:int, x_stride:int, y_stride:int) -> int, first_x:int, first_y:int """
    return 0

def font_get_glyph_kerning_for_direction(font, first_glyph, second_glyph, direction): # real signature unknown; restored from __doc__
    """ font_get_glyph_kerning_for_direction(font:HarfBuzz.font_t, first_glyph:int, second_glyph:int, direction:HarfBuzz.direction_t) -> x:int, y:int """
    pass

def font_get_glyph_name(font, glyph): # real signature unknown; restored from __doc__
    """ font_get_glyph_name(font:HarfBuzz.font_t, glyph:int) -> int, name:list """
    return 0

def font_get_glyph_origin_for_direction(font, glyph, direction): # real signature unknown; restored from __doc__
    """ font_get_glyph_origin_for_direction(font:HarfBuzz.font_t, glyph:int, direction:HarfBuzz.direction_t) -> x:int, y:int """
    pass

def font_get_glyph_shape(font, glyph, dfuncs, draw_data=None): # real signature unknown; restored from __doc__
    """ font_get_glyph_shape(font:HarfBuzz.font_t, glyph:int, dfuncs:HarfBuzz.draw_funcs_t, draw_data=None) """
    pass

def font_get_glyph_v_advance(font, glyph): # real signature unknown; restored from __doc__
    """ font_get_glyph_v_advance(font:HarfBuzz.font_t, glyph:int) -> int """
    return 0

def font_get_glyph_v_advances(font, count, first_glyph, glyph_stride): # real signature unknown; restored from __doc__
    """ font_get_glyph_v_advances(font:HarfBuzz.font_t, count:int, first_glyph:int, glyph_stride:int) -> first_advance:int, advance_stride:int """
    pass

def font_get_glyph_v_kerning(font, top_glyph, bottom_glyph): # real signature unknown; restored from __doc__
    """ font_get_glyph_v_kerning(font:HarfBuzz.font_t, top_glyph:int, bottom_glyph:int) -> int """
    return 0

def font_get_glyph_v_origin(font, glyph): # real signature unknown; restored from __doc__
    """ font_get_glyph_v_origin(font:HarfBuzz.font_t, glyph:int) -> int, x:int, y:int """
    return 0

def font_get_glyph_v_origins(font, count, first_glyph, glyph_stride, x_stride, y_stride): # real signature unknown; restored from __doc__
    """ font_get_glyph_v_origins(font:HarfBuzz.font_t, count:int, first_glyph:int, glyph_stride:int, x_stride:int, y_stride:int) -> int, first_x:int, first_y:int """
    return 0

def font_get_h_extents(font): # real signature unknown; restored from __doc__
    """ font_get_h_extents(font:HarfBuzz.font_t) -> int, extents:HarfBuzz.font_extents_t """
    return 0

def font_get_nominal_glyph(font, unicode): # real signature unknown; restored from __doc__
    """ font_get_nominal_glyph(font:HarfBuzz.font_t, unicode:int) -> int, glyph:int """
    return 0

def font_get_nominal_glyphs(font, count, first_unicode, unicode_stride, glyph_stride): # real signature unknown; restored from __doc__
    """ font_get_nominal_glyphs(font:HarfBuzz.font_t, count:int, first_unicode:int, unicode_stride:int, glyph_stride:int) -> int, first_glyph:int """
    return 0

def font_get_parent(font): # real signature unknown; restored from __doc__
    """ font_get_parent(font:HarfBuzz.font_t) -> HarfBuzz.font_t """
    pass

def font_get_ppem(font): # real signature unknown; restored from __doc__
    """ font_get_ppem(font:HarfBuzz.font_t) -> x_ppem:int, y_ppem:int """
    pass

def font_get_ptem(font): # real signature unknown; restored from __doc__
    """ font_get_ptem(font:HarfBuzz.font_t) -> float """
    return 0.0

def font_get_scale(font): # real signature unknown; restored from __doc__
    """ font_get_scale(font:HarfBuzz.font_t) -> x_scale:int, y_scale:int """
    pass

def font_get_serial(font): # real signature unknown; restored from __doc__
    """ font_get_serial(font:HarfBuzz.font_t) -> int """
    return 0

def font_get_synthetic_bold(font): # real signature unknown; restored from __doc__
    """ font_get_synthetic_bold(font:HarfBuzz.font_t) -> x_embolden:float, y_embolden:float, in_place:int """
    pass

def font_get_synthetic_slant(font): # real signature unknown; restored from __doc__
    """ font_get_synthetic_slant(font:HarfBuzz.font_t) -> float """
    return 0.0

def font_get_variation_glyph(font, unicode, variation_selector): # real signature unknown; restored from __doc__
    """ font_get_variation_glyph(font:HarfBuzz.font_t, unicode:int, variation_selector:int) -> int, glyph:int """
    return 0

def font_get_var_coords_design(font): # real signature unknown; restored from __doc__
    """ font_get_var_coords_design(font:HarfBuzz.font_t) -> float, length:int """
    return 0.0

def font_get_var_coords_normalized(font): # real signature unknown; restored from __doc__
    """ font_get_var_coords_normalized(font:HarfBuzz.font_t) -> int, length:int """
    return 0

def font_get_var_named_instance(font): # real signature unknown; restored from __doc__
    """ font_get_var_named_instance(font:HarfBuzz.font_t) -> int """
    return 0

def font_get_v_extents(font): # real signature unknown; restored from __doc__
    """ font_get_v_extents(font:HarfBuzz.font_t) -> int, extents:HarfBuzz.font_extents_t """
    return 0

def font_glyph_from_string(font, s): # real signature unknown; restored from __doc__
    """ font_glyph_from_string(font:HarfBuzz.font_t, s:list) -> int, glyph:int """
    return 0

def font_glyph_to_string(font, glyph): # real signature unknown; restored from __doc__
    """ font_glyph_to_string(font:HarfBuzz.font_t, glyph:int) -> s:list """
    pass

def font_is_immutable(font): # real signature unknown; restored from __doc__
    """ font_is_immutable(font:HarfBuzz.font_t) -> int """
    return 0

def font_is_synthetic(font): # real signature unknown; restored from __doc__
    """ font_is_synthetic(font:HarfBuzz.font_t) -> int """
    return 0

def font_list_funcs(): # real signature unknown; restored from __doc__
    """ font_list_funcs() -> list """
    return []

def font_make_immutable(font): # real signature unknown; restored from __doc__
    """ font_make_immutable(font:HarfBuzz.font_t) """
    pass

def font_paint_glyph(font, glyph, pfuncs, paint_data=None, palette_index, foreground): # real signature unknown; restored from __doc__
    """ font_paint_glyph(font:HarfBuzz.font_t, glyph:int, pfuncs:HarfBuzz.paint_funcs_t, paint_data=None, palette_index:int, foreground:int) """
    pass

def font_paint_glyph_or_fail(font, glyph, pfuncs, paint_data=None, palette_index, foreground): # real signature unknown; restored from __doc__
    """ font_paint_glyph_or_fail(font:HarfBuzz.font_t, glyph:int, pfuncs:HarfBuzz.paint_funcs_t, paint_data=None, palette_index:int, foreground:int) -> int """
    return 0

def font_set_face(font, face): # real signature unknown; restored from __doc__
    """ font_set_face(font:HarfBuzz.font_t, face:HarfBuzz.face_t) """
    pass

def font_set_funcs_using(font, name): # real signature unknown; restored from __doc__
    """ font_set_funcs_using(font:HarfBuzz.font_t, name:str) -> int """
    return 0

def font_set_parent(font, parent): # real signature unknown; restored from __doc__
    """ font_set_parent(font:HarfBuzz.font_t, parent:HarfBuzz.font_t) """
    pass

def font_set_ppem(font, x_ppem, y_ppem): # real signature unknown; restored from __doc__
    """ font_set_ppem(font:HarfBuzz.font_t, x_ppem:int, y_ppem:int) """
    pass

def font_set_ptem(font, ptem): # real signature unknown; restored from __doc__
    """ font_set_ptem(font:HarfBuzz.font_t, ptem:float) """
    pass

def font_set_scale(font, x_scale, y_scale): # real signature unknown; restored from __doc__
    """ font_set_scale(font:HarfBuzz.font_t, x_scale:int, y_scale:int) """
    pass

def font_set_synthetic_bold(font, x_embolden, y_embolden, in_place): # real signature unknown; restored from __doc__
    """ font_set_synthetic_bold(font:HarfBuzz.font_t, x_embolden:float, y_embolden:float, in_place:int) """
    pass

def font_set_synthetic_slant(font, slant): # real signature unknown; restored from __doc__
    """ font_set_synthetic_slant(font:HarfBuzz.font_t, slant:float) """
    pass

def font_set_variation(font, tag, value): # real signature unknown; restored from __doc__
    """ font_set_variation(font:HarfBuzz.font_t, tag:int, value:float) """
    pass

def font_set_variations(font, variations): # real signature unknown; restored from __doc__
    """ font_set_variations(font:HarfBuzz.font_t, variations:list) """
    pass

def font_set_var_coords_design(font, coords): # real signature unknown; restored from __doc__
    """ font_set_var_coords_design(font:HarfBuzz.font_t, coords:list) """
    pass

def font_set_var_coords_normalized(font, coords): # real signature unknown; restored from __doc__
    """ font_set_var_coords_normalized(font:HarfBuzz.font_t, coords:list) """
    pass

def font_set_var_named_instance(font, instance_index): # real signature unknown; restored from __doc__
    """ font_set_var_named_instance(font:HarfBuzz.font_t, instance_index:int) """
    pass

def font_subtract_glyph_origin_for_direction(font, glyph, direction, x, y): # real signature unknown; restored from __doc__
    """ font_subtract_glyph_origin_for_direction(font:HarfBuzz.font_t, glyph:int, direction:HarfBuzz.direction_t, x:int, y:int) -> x:int, y:int """
    pass

def free(ptr=None): # real signature unknown; restored from __doc__
    """ free(ptr=None) """
    pass

def ft_face_create_cached(ft_face): # real signature unknown; restored from __doc__
    """ ft_face_create_cached(ft_face:freetype2.Face) -> HarfBuzz.face_t """
    pass

def ft_face_create_from_blob_or_fail(blob, index): # real signature unknown; restored from __doc__
    """ ft_face_create_from_blob_or_fail(blob:HarfBuzz.blob_t, index:int) -> HarfBuzz.face_t """
    pass

def ft_face_create_from_file_or_fail(file_name, index): # real signature unknown; restored from __doc__
    """ ft_face_create_from_file_or_fail(file_name:str, index:int) -> HarfBuzz.face_t """
    pass

def ft_face_create_referenced(ft_face): # real signature unknown; restored from __doc__
    """ ft_face_create_referenced(ft_face:freetype2.Face) -> HarfBuzz.face_t """
    pass

def ft_font_changed(font): # real signature unknown; restored from __doc__
    """ ft_font_changed(font:HarfBuzz.font_t) """
    pass

def ft_font_create_referenced(ft_face): # real signature unknown; restored from __doc__
    """ ft_font_create_referenced(ft_face:freetype2.Face) -> HarfBuzz.font_t """
    pass

def ft_font_get_load_flags(font): # real signature unknown; restored from __doc__
    """ ft_font_get_load_flags(font:HarfBuzz.font_t) -> int """
    return 0

def ft_font_set_funcs(font): # real signature unknown; restored from __doc__
    """ ft_font_set_funcs(font:HarfBuzz.font_t) """
    pass

def ft_font_set_load_flags(font, load_flags): # real signature unknown; restored from __doc__
    """ ft_font_set_load_flags(font:HarfBuzz.font_t, load_flags:int) """
    pass

def ft_hb_font_changed(font): # real signature unknown; restored from __doc__
    """ ft_hb_font_changed(font:HarfBuzz.font_t) -> int """
    return 0

def glib_blob_create(gbytes): # real signature unknown; restored from __doc__
    """ glib_blob_create(gbytes:GLib.Bytes) -> HarfBuzz.blob_t """
    pass

def glib_get_unicode_funcs(): # real signature unknown; restored from __doc__
    """ glib_get_unicode_funcs() -> HarfBuzz.unicode_funcs_t """
    pass

def glib_script_from_script(script): # real signature unknown; restored from __doc__
    """ glib_script_from_script(script:HarfBuzz.script_t) -> GLib.UnicodeScript """
    pass

def glib_script_to_script(script): # real signature unknown; restored from __doc__
    """ glib_script_to_script(script:GLib.UnicodeScript) -> HarfBuzz.script_t """
    pass

def glyph_info_get_glyph_flags(info): # real signature unknown; restored from __doc__
    """ glyph_info_get_glyph_flags(info:HarfBuzz.glyph_info_t) -> HarfBuzz.glyph_flags_t """
    pass

def language_from_string(p_str): # real signature unknown; restored from __doc__
    """ language_from_string(str:list) -> HarfBuzz.language_t """
    pass

def language_get_default(): # real signature unknown; restored from __doc__
    """ language_get_default() -> HarfBuzz.language_t """
    pass

def language_matches(language, specific): # real signature unknown; restored from __doc__
    """ language_matches(language:HarfBuzz.language_t, specific:HarfBuzz.language_t) -> int """
    return 0

def language_to_string(language): # real signature unknown; restored from __doc__
    """ language_to_string(language:HarfBuzz.language_t) -> str """
    return ""

def malloc(size): # real signature unknown; restored from __doc__
    """ malloc(size:int) """
    pass

def map_allocation_successful(map): # real signature unknown; restored from __doc__
    """ map_allocation_successful(map:HarfBuzz.map_t) -> int """
    return 0

def map_clear(map): # real signature unknown; restored from __doc__
    """ map_clear(map:HarfBuzz.map_t) """
    pass

def map_copy(map): # real signature unknown; restored from __doc__
    """ map_copy(map:HarfBuzz.map_t) -> HarfBuzz.map_t """
    pass

def map_create(): # real signature unknown; restored from __doc__
    """ map_create() -> HarfBuzz.map_t """
    pass

def map_del(map, key): # real signature unknown; restored from __doc__
    """ map_del(map:HarfBuzz.map_t, key:int) """
    pass

def map_get(map, key): # real signature unknown; restored from __doc__
    """ map_get(map:HarfBuzz.map_t, key:int) -> int """
    return 0

def map_get_empty(): # real signature unknown; restored from __doc__
    """ map_get_empty() -> HarfBuzz.map_t """
    pass

def map_get_population(map): # real signature unknown; restored from __doc__
    """ map_get_population(map:HarfBuzz.map_t) -> int """
    return 0

def map_has(map, key): # real signature unknown; restored from __doc__
    """ map_has(map:HarfBuzz.map_t, key:int) -> int """
    return 0

def map_hash(map): # real signature unknown; restored from __doc__
    """ map_hash(map:HarfBuzz.map_t) -> int """
    return 0

def map_is_empty(map): # real signature unknown; restored from __doc__
    """ map_is_empty(map:HarfBuzz.map_t) -> int """
    return 0

def map_is_equal(map, other): # real signature unknown; restored from __doc__
    """ map_is_equal(map:HarfBuzz.map_t, other:HarfBuzz.map_t) -> int """
    return 0

def map_keys(map, keys): # real signature unknown; restored from __doc__
    """ map_keys(map:HarfBuzz.map_t, keys:HarfBuzz.set_t) """
    pass

def map_next(map, idx): # real signature unknown; restored from __doc__
    """ map_next(map:HarfBuzz.map_t, idx:int) -> int, idx:int, key:int, value:int """
    return 0

def map_set(map, key, value): # real signature unknown; restored from __doc__
    """ map_set(map:HarfBuzz.map_t, key:int, value:int) """
    pass

def map_update(map, other): # real signature unknown; restored from __doc__
    """ map_update(map:HarfBuzz.map_t, other:HarfBuzz.map_t) """
    pass

def map_values(map, values): # real signature unknown; restored from __doc__
    """ map_values(map:HarfBuzz.map_t, values:HarfBuzz.set_t) """
    pass

def ot_color_glyph_get_layers(face, glyph, start_offset): # real signature unknown; restored from __doc__
    """ ot_color_glyph_get_layers(face:HarfBuzz.face_t, glyph:int, start_offset:int) -> int, layers:list """
    return 0

def ot_color_glyph_has_paint(face, glyph): # real signature unknown; restored from __doc__
    """ ot_color_glyph_has_paint(face:HarfBuzz.face_t, glyph:int) -> int """
    return 0

def ot_color_glyph_reference_png(font, glyph): # real signature unknown; restored from __doc__
    """ ot_color_glyph_reference_png(font:HarfBuzz.font_t, glyph:int) -> HarfBuzz.blob_t """
    pass

def ot_color_glyph_reference_svg(face, glyph): # real signature unknown; restored from __doc__
    """ ot_color_glyph_reference_svg(face:HarfBuzz.face_t, glyph:int) -> HarfBuzz.blob_t """
    pass

def ot_color_has_layers(face): # real signature unknown; restored from __doc__
    """ ot_color_has_layers(face:HarfBuzz.face_t) -> int """
    return 0

def ot_color_has_paint(face): # real signature unknown; restored from __doc__
    """ ot_color_has_paint(face:HarfBuzz.face_t) -> int """
    return 0

def ot_color_has_palettes(face): # real signature unknown; restored from __doc__
    """ ot_color_has_palettes(face:HarfBuzz.face_t) -> int """
    return 0

def ot_color_has_png(face): # real signature unknown; restored from __doc__
    """ ot_color_has_png(face:HarfBuzz.face_t) -> int """
    return 0

def ot_color_has_svg(face): # real signature unknown; restored from __doc__
    """ ot_color_has_svg(face:HarfBuzz.face_t) -> int """
    return 0

def ot_color_palette_color_get_name_id(face, color_index): # real signature unknown; restored from __doc__
    """ ot_color_palette_color_get_name_id(face:HarfBuzz.face_t, color_index:int) -> int """
    return 0

def ot_color_palette_get_colors(face, palette_index, start_offset): # real signature unknown; restored from __doc__
    """ ot_color_palette_get_colors(face:HarfBuzz.face_t, palette_index:int, start_offset:int) -> int, colors:list """
    return 0

def ot_color_palette_get_count(face): # real signature unknown; restored from __doc__
    """ ot_color_palette_get_count(face:HarfBuzz.face_t) -> int """
    return 0

def ot_color_palette_get_flags(face, palette_index): # real signature unknown; restored from __doc__
    """ ot_color_palette_get_flags(face:HarfBuzz.face_t, palette_index:int) -> HarfBuzz.ot_color_palette_flags_t """
    pass

def ot_color_palette_get_name_id(face, palette_index): # real signature unknown; restored from __doc__
    """ ot_color_palette_get_name_id(face:HarfBuzz.face_t, palette_index:int) -> int """
    return 0

def ot_font_set_funcs(font): # real signature unknown; restored from __doc__
    """ ot_font_set_funcs(font:HarfBuzz.font_t) """
    pass

def ot_layout_collect_features(face, table_tag, scripts=None, languages=None, features=None): # real signature unknown; restored from __doc__
    """ ot_layout_collect_features(face:HarfBuzz.face_t, table_tag:int, scripts:list=None, languages:list=None, features:list=None) -> feature_indexes:HarfBuzz.set_t """
    pass

def ot_layout_collect_features_map(face, table_tag, script_index, language_index): # real signature unknown; restored from __doc__
    """ ot_layout_collect_features_map(face:HarfBuzz.face_t, table_tag:int, script_index:int, language_index:int) -> feature_map:HarfBuzz.map_t """
    pass

def ot_layout_collect_lookups(face, table_tag, scripts=None, languages=None, features=None): # real signature unknown; restored from __doc__
    """ ot_layout_collect_lookups(face:HarfBuzz.face_t, table_tag:int, scripts:list=None, languages:list=None, features:list=None) -> lookup_indexes:HarfBuzz.set_t """
    pass

def ot_layout_feature_get_characters(face, table_tag, feature_index, start_offset): # real signature unknown; restored from __doc__
    """ ot_layout_feature_get_characters(face:HarfBuzz.face_t, table_tag:int, feature_index:int, start_offset:int) -> int, characters:list """
    return 0

def ot_layout_feature_get_lookups(face, table_tag, feature_index, start_offset): # real signature unknown; restored from __doc__
    """ ot_layout_feature_get_lookups(face:HarfBuzz.face_t, table_tag:int, feature_index:int, start_offset:int) -> int, lookup_indexes:list """
    return 0

def ot_layout_feature_get_name_ids(face, table_tag, feature_index): # real signature unknown; restored from __doc__
    """ ot_layout_feature_get_name_ids(face:HarfBuzz.face_t, table_tag:int, feature_index:int) -> int, label_id:int, tooltip_id:int, sample_id:int, num_named_parameters:int, first_param_id:int """
    return 0

def ot_layout_feature_with_variations_get_lookups(face, table_tag, feature_index, variations_index, start_offset): # real signature unknown; restored from __doc__
    """ ot_layout_feature_with_variations_get_lookups(face:HarfBuzz.face_t, table_tag:int, feature_index:int, variations_index:int, start_offset:int) -> int, lookup_indexes:list """
    return 0

def ot_layout_get_attach_points(face, glyph, start_offset): # real signature unknown; restored from __doc__
    """ ot_layout_get_attach_points(face:HarfBuzz.face_t, glyph:int, start_offset:int) -> int, point_array:list """
    return 0

def ot_layout_get_baseline(font, baseline_tag, direction, script_tag, language_tag): # real signature unknown; restored from __doc__
    """ ot_layout_get_baseline(font:HarfBuzz.font_t, baseline_tag:HarfBuzz.ot_layout_baseline_tag_t, direction:HarfBuzz.direction_t, script_tag:int, language_tag:int) -> int, coord:int """
    return 0

def ot_layout_get_baseline2(font, baseline_tag, direction, script, language=None): # real signature unknown; restored from __doc__
    """ ot_layout_get_baseline2(font:HarfBuzz.font_t, baseline_tag:HarfBuzz.ot_layout_baseline_tag_t, direction:HarfBuzz.direction_t, script:HarfBuzz.script_t, language:HarfBuzz.language_t=None) -> int, coord:int """
    return 0

def ot_layout_get_baseline_with_fallback(font, baseline_tag, direction, script_tag, language_tag): # real signature unknown; restored from __doc__
    """ ot_layout_get_baseline_with_fallback(font:HarfBuzz.font_t, baseline_tag:HarfBuzz.ot_layout_baseline_tag_t, direction:HarfBuzz.direction_t, script_tag:int, language_tag:int) -> coord:int """
    pass

def ot_layout_get_baseline_with_fallback2(font, baseline_tag, direction, script, language=None): # real signature unknown; restored from __doc__
    """ ot_layout_get_baseline_with_fallback2(font:HarfBuzz.font_t, baseline_tag:HarfBuzz.ot_layout_baseline_tag_t, direction:HarfBuzz.direction_t, script:HarfBuzz.script_t, language:HarfBuzz.language_t=None) -> coord:int """
    pass

def ot_layout_get_font_extents(font, direction, script_tag, language_tag): # real signature unknown; restored from __doc__
    """ ot_layout_get_font_extents(font:HarfBuzz.font_t, direction:HarfBuzz.direction_t, script_tag:int, language_tag:int) -> int, extents:HarfBuzz.font_extents_t """
    return 0

def ot_layout_get_font_extents2(font, direction, script, language=None): # real signature unknown; restored from __doc__
    """ ot_layout_get_font_extents2(font:HarfBuzz.font_t, direction:HarfBuzz.direction_t, script:HarfBuzz.script_t, language:HarfBuzz.language_t=None) -> int, extents:HarfBuzz.font_extents_t """
    return 0

def ot_layout_get_glyphs_in_class(face, klass): # real signature unknown; restored from __doc__
    """ ot_layout_get_glyphs_in_class(face:HarfBuzz.face_t, klass:HarfBuzz.ot_layout_glyph_class_t) -> glyphs:HarfBuzz.set_t """
    pass

def ot_layout_get_glyph_class(face, glyph): # real signature unknown; restored from __doc__
    """ ot_layout_get_glyph_class(face:HarfBuzz.face_t, glyph:int) -> HarfBuzz.ot_layout_glyph_class_t """
    pass

def ot_layout_get_horizontal_baseline_tag_for_script(script): # real signature unknown; restored from __doc__
    """ ot_layout_get_horizontal_baseline_tag_for_script(script:HarfBuzz.script_t) -> HarfBuzz.ot_layout_baseline_tag_t """
    pass

def ot_layout_get_ligature_carets(font, direction, glyph, start_offset): # real signature unknown; restored from __doc__
    """ ot_layout_get_ligature_carets(font:HarfBuzz.font_t, direction:HarfBuzz.direction_t, glyph:int, start_offset:int) -> int, caret_array:list """
    return 0

def ot_layout_get_size_params(face): # real signature unknown; restored from __doc__
    """ ot_layout_get_size_params(face:HarfBuzz.face_t) -> int, design_size:int, subfamily_id:int, subfamily_name_id:int, range_start:int, range_end:int """
    return 0

def ot_layout_has_glyph_classes(face): # real signature unknown; restored from __doc__
    """ ot_layout_has_glyph_classes(face:HarfBuzz.face_t) -> int """
    return 0

def ot_layout_has_positioning(face): # real signature unknown; restored from __doc__
    """ ot_layout_has_positioning(face:HarfBuzz.face_t) -> int """
    return 0

def ot_layout_has_substitution(face): # real signature unknown; restored from __doc__
    """ ot_layout_has_substitution(face:HarfBuzz.face_t) -> int """
    return 0

def ot_layout_language_find_feature(face, table_tag, script_index, language_index, feature_tag): # real signature unknown; restored from __doc__
    """ ot_layout_language_find_feature(face:HarfBuzz.face_t, table_tag:int, script_index:int, language_index:int, feature_tag:int) -> int, feature_index:int """
    return 0

def ot_layout_language_get_feature_indexes(face, table_tag, script_index, language_index, start_offset): # real signature unknown; restored from __doc__
    """ ot_layout_language_get_feature_indexes(face:HarfBuzz.face_t, table_tag:int, script_index:int, language_index:int, start_offset:int) -> int, feature_indexes:list """
    return 0

def ot_layout_language_get_feature_tags(face, table_tag, script_index, language_index, start_offset): # real signature unknown; restored from __doc__
    """ ot_layout_language_get_feature_tags(face:HarfBuzz.face_t, table_tag:int, script_index:int, language_index:int, start_offset:int) -> int, feature_tags:list """
    return 0

def ot_layout_language_get_required_feature(face, table_tag, script_index, language_index): # real signature unknown; restored from __doc__
    """ ot_layout_language_get_required_feature(face:HarfBuzz.face_t, table_tag:int, script_index:int, language_index:int) -> int, feature_index:int, feature_tag:int """
    return 0

def ot_layout_language_get_required_feature_index(face, table_tag, script_index, language_index): # real signature unknown; restored from __doc__
    """ ot_layout_language_get_required_feature_index(face:HarfBuzz.face_t, table_tag:int, script_index:int, language_index:int) -> int, feature_index:int """
    return 0

def ot_layout_lookups_substitute_closure(face, lookups): # real signature unknown; restored from __doc__
    """ ot_layout_lookups_substitute_closure(face:HarfBuzz.face_t, lookups:HarfBuzz.set_t) -> glyphs:HarfBuzz.set_t """
    pass

def ot_layout_lookup_collect_glyphs(face, table_tag, lookup_index): # real signature unknown; restored from __doc__
    """ ot_layout_lookup_collect_glyphs(face:HarfBuzz.face_t, table_tag:int, lookup_index:int) -> glyphs_before:HarfBuzz.set_t, glyphs_input:HarfBuzz.set_t, glyphs_after:HarfBuzz.set_t, glyphs_output:HarfBuzz.set_t """
    pass

def ot_layout_lookup_collect_glyph_alternates(face, lookup_index, alternate_count, alternate_glyphs): # real signature unknown; restored from __doc__
    """ ot_layout_lookup_collect_glyph_alternates(face:HarfBuzz.face_t, lookup_index:int, alternate_count:HarfBuzz.map_t, alternate_glyphs:HarfBuzz.map_t) -> int, alternate_count:HarfBuzz.map_t, alternate_glyphs:HarfBuzz.map_t """
    return 0

def ot_layout_lookup_get_glyph_alternates(face, lookup_index, glyph, start_offset): # real signature unknown; restored from __doc__
    """ ot_layout_lookup_get_glyph_alternates(face:HarfBuzz.face_t, lookup_index:int, glyph:int, start_offset:int) -> int, alternate_glyphs:list """
    return 0

def ot_layout_lookup_get_optical_bound(font, lookup_index, direction, glyph): # real signature unknown; restored from __doc__
    """ ot_layout_lookup_get_optical_bound(font:HarfBuzz.font_t, lookup_index:int, direction:HarfBuzz.direction_t, glyph:int) -> int """
    return 0

def ot_layout_lookup_substitute_closure(face, lookup_index): # real signature unknown; restored from __doc__
    """ ot_layout_lookup_substitute_closure(face:HarfBuzz.face_t, lookup_index:int) -> glyphs:HarfBuzz.set_t """
    pass

def ot_layout_lookup_would_substitute(face, lookup_index, glyphs, glyphs_length, zero_context): # real signature unknown; restored from __doc__
    """ ot_layout_lookup_would_substitute(face:HarfBuzz.face_t, lookup_index:int, glyphs:int, glyphs_length:int, zero_context:int) -> int """
    return 0

def ot_layout_script_find_language(face, table_tag, script_index, language_tag, language_index): # real signature unknown; restored from __doc__
    """ ot_layout_script_find_language(face:HarfBuzz.face_t, table_tag:int, script_index:int, language_tag:int, language_index:int) -> int """
    return 0

def ot_layout_script_get_language_tags(face, table_tag, script_index, start_offset): # real signature unknown; restored from __doc__
    """ ot_layout_script_get_language_tags(face:HarfBuzz.face_t, table_tag:int, script_index:int, start_offset:int) -> int, language_tags:list """
    return 0

def ot_layout_script_select_language(face, table_tag, script_index, language_count, language_tags): # real signature unknown; restored from __doc__
    """ ot_layout_script_select_language(face:HarfBuzz.face_t, table_tag:int, script_index:int, language_count:int, language_tags:int) -> int, language_index:int """
    return 0

def ot_layout_script_select_language2(face, table_tag, script_index, language_count, language_tags): # real signature unknown; restored from __doc__
    """ ot_layout_script_select_language2(face:HarfBuzz.face_t, table_tag:int, script_index:int, language_count:int, language_tags:int) -> int, language_index:int, chosen_language:int """
    return 0

def ot_layout_table_choose_script(face, table_tag, script_tags): # real signature unknown; restored from __doc__
    """ ot_layout_table_choose_script(face:HarfBuzz.face_t, table_tag:int, script_tags:int) -> int, script_index:int, chosen_script:int """
    return 0

def ot_layout_table_find_feature_variations(face, table_tag, coords, num_coords): # real signature unknown; restored from __doc__
    """ ot_layout_table_find_feature_variations(face:HarfBuzz.face_t, table_tag:int, coords:int, num_coords:int) -> int, variations_index:int """
    return 0

def ot_layout_table_find_script(face, table_tag, script_tag): # real signature unknown; restored from __doc__
    """ ot_layout_table_find_script(face:HarfBuzz.face_t, table_tag:int, script_tag:int) -> int, script_index:int """
    return 0

def ot_layout_table_get_feature_tags(face, table_tag, start_offset): # real signature unknown; restored from __doc__
    """ ot_layout_table_get_feature_tags(face:HarfBuzz.face_t, table_tag:int, start_offset:int) -> int, feature_tags:list """
    return 0

def ot_layout_table_get_lookup_count(face, table_tag): # real signature unknown; restored from __doc__
    """ ot_layout_table_get_lookup_count(face:HarfBuzz.face_t, table_tag:int) -> int """
    return 0

def ot_layout_table_get_script_tags(face, table_tag, start_offset): # real signature unknown; restored from __doc__
    """ ot_layout_table_get_script_tags(face:HarfBuzz.face_t, table_tag:int, start_offset:int) -> int, script_tags:list """
    return 0

def ot_layout_table_select_script(face, table_tag, script_count, script_tags): # real signature unknown; restored from __doc__
    """ ot_layout_table_select_script(face:HarfBuzz.face_t, table_tag:int, script_count:int, script_tags:int) -> int, script_index:int, chosen_script:int """
    return 0

def ot_math_get_constant(font, constant): # real signature unknown; restored from __doc__
    """ ot_math_get_constant(font:HarfBuzz.font_t, constant:HarfBuzz.ot_math_constant_t) -> int """
    return 0

def ot_math_get_glyph_assembly(font, glyph, direction, start_offset): # real signature unknown; restored from __doc__
    """ ot_math_get_glyph_assembly(font:HarfBuzz.font_t, glyph:int, direction:HarfBuzz.direction_t, start_offset:int) -> int, parts:list, italics_correction:int """
    return 0

def ot_math_get_glyph_italics_correction(font, glyph): # real signature unknown; restored from __doc__
    """ ot_math_get_glyph_italics_correction(font:HarfBuzz.font_t, glyph:int) -> int """
    return 0

def ot_math_get_glyph_kerning(font, glyph, kern, correction_height): # real signature unknown; restored from __doc__
    """ ot_math_get_glyph_kerning(font:HarfBuzz.font_t, glyph:int, kern:HarfBuzz.ot_math_kern_t, correction_height:int) -> int """
    return 0

def ot_math_get_glyph_kernings(font, glyph, kern, start_offset): # real signature unknown; restored from __doc__
    """ ot_math_get_glyph_kernings(font:HarfBuzz.font_t, glyph:int, kern:HarfBuzz.ot_math_kern_t, start_offset:int) -> int, kern_entries:list """
    return 0

def ot_math_get_glyph_top_accent_attachment(font, glyph): # real signature unknown; restored from __doc__
    """ ot_math_get_glyph_top_accent_attachment(font:HarfBuzz.font_t, glyph:int) -> int """
    return 0

def ot_math_get_glyph_variants(font, glyph, direction, start_offset): # real signature unknown; restored from __doc__
    """ ot_math_get_glyph_variants(font:HarfBuzz.font_t, glyph:int, direction:HarfBuzz.direction_t, start_offset:int) -> int, variants:list """
    return 0

def ot_math_get_min_connector_overlap(font, direction): # real signature unknown; restored from __doc__
    """ ot_math_get_min_connector_overlap(font:HarfBuzz.font_t, direction:HarfBuzz.direction_t) -> int """
    return 0

def ot_math_has_data(face): # real signature unknown; restored from __doc__
    """ ot_math_has_data(face:HarfBuzz.face_t) -> int """
    return 0

def ot_math_is_glyph_extended_shape(face, glyph): # real signature unknown; restored from __doc__
    """ ot_math_is_glyph_extended_shape(face:HarfBuzz.face_t, glyph:int) -> int """
    return 0

def ot_meta_get_entry_tags(face, start_offset): # real signature unknown; restored from __doc__
    """ ot_meta_get_entry_tags(face:HarfBuzz.face_t, start_offset:int) -> int, entries:list """
    return 0

def ot_meta_reference_entry(face, meta_tag): # real signature unknown; restored from __doc__
    """ ot_meta_reference_entry(face:HarfBuzz.face_t, meta_tag:HarfBuzz.ot_meta_tag_t) -> HarfBuzz.blob_t """
    pass

def ot_metrics_get_position(font, metrics_tag): # real signature unknown; restored from __doc__
    """ ot_metrics_get_position(font:HarfBuzz.font_t, metrics_tag:HarfBuzz.ot_metrics_tag_t) -> int, position:int """
    return 0

def ot_metrics_get_position_with_fallback(font, metrics_tag): # real signature unknown; restored from __doc__
    """ ot_metrics_get_position_with_fallback(font:HarfBuzz.font_t, metrics_tag:HarfBuzz.ot_metrics_tag_t) -> position:int """
    pass

def ot_metrics_get_variation(font, metrics_tag): # real signature unknown; restored from __doc__
    """ ot_metrics_get_variation(font:HarfBuzz.font_t, metrics_tag:HarfBuzz.ot_metrics_tag_t) -> float """
    return 0.0

def ot_metrics_get_x_variation(font, metrics_tag): # real signature unknown; restored from __doc__
    """ ot_metrics_get_x_variation(font:HarfBuzz.font_t, metrics_tag:HarfBuzz.ot_metrics_tag_t) -> int """
    return 0

def ot_metrics_get_y_variation(font, metrics_tag): # real signature unknown; restored from __doc__
    """ ot_metrics_get_y_variation(font:HarfBuzz.font_t, metrics_tag:HarfBuzz.ot_metrics_tag_t) -> int """
    return 0

def ot_name_get_utf16(face, name_id, language): # real signature unknown; restored from __doc__
    """ ot_name_get_utf16(face:HarfBuzz.face_t, name_id:int, language:HarfBuzz.language_t) -> int, text:list """
    return 0

def ot_name_get_utf32(face, name_id, language): # real signature unknown; restored from __doc__
    """ ot_name_get_utf32(face:HarfBuzz.face_t, name_id:int, language:HarfBuzz.language_t) -> int, text:list """
    return 0

def ot_name_get_utf8(face, name_id, language): # real signature unknown; restored from __doc__
    """ ot_name_get_utf8(face:HarfBuzz.face_t, name_id:int, language:HarfBuzz.language_t) -> int, text:list """
    return 0

def ot_name_list_names(face): # real signature unknown; restored from __doc__
    """ ot_name_list_names(face:HarfBuzz.face_t) -> list """
    return []

def ot_shape_glyphs_closure(font, buffer, features): # real signature unknown; restored from __doc__
    """ ot_shape_glyphs_closure(font:HarfBuzz.font_t, buffer:HarfBuzz.buffer_t, features:list) -> glyphs:HarfBuzz.set_t """
    pass

def ot_shape_plan_collect_lookups(shape_plan, table_tag): # real signature unknown; restored from __doc__
    """ ot_shape_plan_collect_lookups(shape_plan:HarfBuzz.shape_plan_t, table_tag:int) -> lookup_indexes:HarfBuzz.set_t """
    pass

def ot_shape_plan_get_feature_tags(shape_plan, start_offset): # real signature unknown; restored from __doc__
    """ ot_shape_plan_get_feature_tags(shape_plan:HarfBuzz.shape_plan_t, start_offset:int) -> int, tags:list """
    return 0

def ot_tags_from_script(script): # real signature unknown; restored from __doc__
    """ ot_tags_from_script(script:HarfBuzz.script_t) -> script_tag_1:int, script_tag_2:int """
    pass

def ot_tags_from_script_and_language(script, language=None, script_count, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ ot_tags_from_script_and_language(script:HarfBuzz.script_t, language:HarfBuzz.language_t=None, script_count:int=<optional>, language_count:int=<optional>) -> script_count:int, script_tags:int, language_count:int, language_tags:int """
    pass

def ot_tags_to_script_and_language(script_tag, language_tag): # real signature unknown; restored from __doc__
    """ ot_tags_to_script_and_language(script_tag:int, language_tag:int) -> script:HarfBuzz.script_t, language:HarfBuzz.language_t """
    pass

def ot_tag_from_language(language): # real signature unknown; restored from __doc__
    """ ot_tag_from_language(language:HarfBuzz.language_t) -> int """
    return 0

def ot_tag_to_language(tag): # real signature unknown; restored from __doc__
    """ ot_tag_to_language(tag:int) -> HarfBuzz.language_t or None """
    pass

def ot_tag_to_script(tag): # real signature unknown; restored from __doc__
    """ ot_tag_to_script(tag:int) -> HarfBuzz.script_t """
    pass

def ot_var_find_axis(face, axis_tag, axis_index): # real signature unknown; restored from __doc__
    """ ot_var_find_axis(face:HarfBuzz.face_t, axis_tag:int, axis_index:int) -> int, axis_info:HarfBuzz.ot_var_axis_t """
    return 0

def ot_var_find_axis_info(face, axis_tag): # real signature unknown; restored from __doc__
    """ ot_var_find_axis_info(face:HarfBuzz.face_t, axis_tag:int) -> int, axis_info:HarfBuzz.ot_var_axis_info_t """
    return 0

def ot_var_get_axes(face, start_offset): # real signature unknown; restored from __doc__
    """ ot_var_get_axes(face:HarfBuzz.face_t, start_offset:int) -> int, axes_array:list """
    return 0

def ot_var_get_axis_count(face): # real signature unknown; restored from __doc__
    """ ot_var_get_axis_count(face:HarfBuzz.face_t) -> int """
    return 0

def ot_var_get_axis_infos(face, start_offset): # real signature unknown; restored from __doc__
    """ ot_var_get_axis_infos(face:HarfBuzz.face_t, start_offset:int) -> int, axes_array:list """
    return 0

def ot_var_get_named_instance_count(face): # real signature unknown; restored from __doc__
    """ ot_var_get_named_instance_count(face:HarfBuzz.face_t) -> int """
    return 0

def ot_var_has_data(face): # real signature unknown; restored from __doc__
    """ ot_var_has_data(face:HarfBuzz.face_t) -> int """
    return 0

def ot_var_named_instance_get_design_coords(face, instance_index): # real signature unknown; restored from __doc__
    """ ot_var_named_instance_get_design_coords(face:HarfBuzz.face_t, instance_index:int) -> int, coords:list """
    return 0

def ot_var_named_instance_get_postscript_name_id(face, instance_index): # real signature unknown; restored from __doc__
    """ ot_var_named_instance_get_postscript_name_id(face:HarfBuzz.face_t, instance_index:int) -> int """
    return 0

def ot_var_named_instance_get_subfamily_name_id(face, instance_index): # real signature unknown; restored from __doc__
    """ ot_var_named_instance_get_subfamily_name_id(face:HarfBuzz.face_t, instance_index:int) -> int """
    return 0

def ot_var_normalize_coords(face, coords_length, design_coords): # real signature unknown; restored from __doc__
    """ ot_var_normalize_coords(face:HarfBuzz.face_t, coords_length:int, design_coords:float) -> normalized_coords:int """
    pass

def ot_var_normalize_variations(face, variations, variations_length): # real signature unknown; restored from __doc__
    """ ot_var_normalize_variations(face:HarfBuzz.face_t, variations:HarfBuzz.variation_t, variations_length:int) -> coords:list """
    pass

def paint_color(funcs, paint_data=None, is_foreground, color): # real signature unknown; restored from __doc__
    """ paint_color(funcs:HarfBuzz.paint_funcs_t, paint_data=None, is_foreground:int, color:int) """
    pass

def paint_color_glyph(funcs, paint_data=None, glyph, font): # real signature unknown; restored from __doc__
    """ paint_color_glyph(funcs:HarfBuzz.paint_funcs_t, paint_data=None, glyph:int, font:HarfBuzz.font_t) -> int """
    return 0

def paint_custom_palette_color(funcs, paint_data=None, color_index): # real signature unknown; restored from __doc__
    """ paint_custom_palette_color(funcs:HarfBuzz.paint_funcs_t, paint_data=None, color_index:int) -> int, color:int """
    return 0

def paint_funcs_create(): # real signature unknown; restored from __doc__
    """ paint_funcs_create() -> HarfBuzz.paint_funcs_t """
    pass

def paint_funcs_get_empty(): # real signature unknown; restored from __doc__
    """ paint_funcs_get_empty() -> HarfBuzz.paint_funcs_t """
    pass

def paint_funcs_is_immutable(funcs): # real signature unknown; restored from __doc__
    """ paint_funcs_is_immutable(funcs:HarfBuzz.paint_funcs_t) -> int """
    return 0

def paint_funcs_make_immutable(funcs): # real signature unknown; restored from __doc__
    """ paint_funcs_make_immutable(funcs:HarfBuzz.paint_funcs_t) """
    pass

def paint_funcs_set_color_func(funcs, func, user_data=None): # real signature unknown; restored from __doc__
    """ paint_funcs_set_color_func(funcs:HarfBuzz.paint_funcs_t, func:HarfBuzz.paint_color_func_t, user_data=None) """
    pass

def paint_funcs_set_color_glyph_func(funcs, func, user_data=None): # real signature unknown; restored from __doc__
    """ paint_funcs_set_color_glyph_func(funcs:HarfBuzz.paint_funcs_t, func:HarfBuzz.paint_color_glyph_func_t, user_data=None) """
    pass

def paint_funcs_set_custom_palette_color_func(funcs, func, user_data=None): # real signature unknown; restored from __doc__
    """ paint_funcs_set_custom_palette_color_func(funcs:HarfBuzz.paint_funcs_t, func:HarfBuzz.paint_custom_palette_color_func_t, user_data=None) """
    pass

def paint_funcs_set_image_func(funcs, func, user_data=None): # real signature unknown; restored from __doc__
    """ paint_funcs_set_image_func(funcs:HarfBuzz.paint_funcs_t, func:HarfBuzz.paint_image_func_t, user_data=None) """
    pass

def paint_funcs_set_linear_gradient_func(funcs, func, user_data=None): # real signature unknown; restored from __doc__
    """ paint_funcs_set_linear_gradient_func(funcs:HarfBuzz.paint_funcs_t, func:HarfBuzz.paint_linear_gradient_func_t, user_data=None) """
    pass

def paint_funcs_set_pop_clip_func(funcs, func, user_data=None): # real signature unknown; restored from __doc__
    """ paint_funcs_set_pop_clip_func(funcs:HarfBuzz.paint_funcs_t, func:HarfBuzz.paint_pop_clip_func_t, user_data=None) """
    pass

def paint_funcs_set_pop_group_func(funcs, func, user_data=None): # real signature unknown; restored from __doc__
    """ paint_funcs_set_pop_group_func(funcs:HarfBuzz.paint_funcs_t, func:HarfBuzz.paint_pop_group_func_t, user_data=None) """
    pass

def paint_funcs_set_pop_transform_func(funcs, func, user_data=None): # real signature unknown; restored from __doc__
    """ paint_funcs_set_pop_transform_func(funcs:HarfBuzz.paint_funcs_t, func:HarfBuzz.paint_pop_transform_func_t, user_data=None) """
    pass

def paint_funcs_set_push_clip_glyph_func(funcs, func, user_data=None): # real signature unknown; restored from __doc__
    """ paint_funcs_set_push_clip_glyph_func(funcs:HarfBuzz.paint_funcs_t, func:HarfBuzz.paint_push_clip_glyph_func_t, user_data=None) """
    pass

def paint_funcs_set_push_clip_rectangle_func(funcs, func, user_data=None): # real signature unknown; restored from __doc__
    """ paint_funcs_set_push_clip_rectangle_func(funcs:HarfBuzz.paint_funcs_t, func:HarfBuzz.paint_push_clip_rectangle_func_t, user_data=None) """
    pass

def paint_funcs_set_push_group_func(funcs, func, user_data=None): # real signature unknown; restored from __doc__
    """ paint_funcs_set_push_group_func(funcs:HarfBuzz.paint_funcs_t, func:HarfBuzz.paint_push_group_func_t, user_data=None) """
    pass

def paint_funcs_set_push_transform_func(funcs, func, user_data=None): # real signature unknown; restored from __doc__
    """ paint_funcs_set_push_transform_func(funcs:HarfBuzz.paint_funcs_t, func:HarfBuzz.paint_push_transform_func_t, user_data=None) """
    pass

def paint_funcs_set_radial_gradient_func(funcs, func, user_data=None): # real signature unknown; restored from __doc__
    """ paint_funcs_set_radial_gradient_func(funcs:HarfBuzz.paint_funcs_t, func:HarfBuzz.paint_radial_gradient_func_t, user_data=None) """
    pass

def paint_funcs_set_sweep_gradient_func(funcs, func, user_data=None): # real signature unknown; restored from __doc__
    """ paint_funcs_set_sweep_gradient_func(funcs:HarfBuzz.paint_funcs_t, func:HarfBuzz.paint_sweep_gradient_func_t, user_data=None) """
    pass

def paint_image(funcs, paint_data=None, image, width, height, format, slant, extents=None): # real signature unknown; restored from __doc__
    """ paint_image(funcs:HarfBuzz.paint_funcs_t, paint_data=None, image:HarfBuzz.blob_t, width:int, height:int, format:int, slant:float, extents:HarfBuzz.glyph_extents_t=None) """
    pass

def paint_linear_gradient(funcs, paint_data=None, color_line, x0, y0, x1, y1, x2, y2): # real signature unknown; restored from __doc__
    """ paint_linear_gradient(funcs:HarfBuzz.paint_funcs_t, paint_data=None, color_line:HarfBuzz.color_line_t, x0:float, y0:float, x1:float, y1:float, x2:float, y2:float) """
    pass

def paint_pop_clip(funcs, paint_data=None): # real signature unknown; restored from __doc__
    """ paint_pop_clip(funcs:HarfBuzz.paint_funcs_t, paint_data=None) """
    pass

def paint_pop_group(funcs, paint_data=None, mode): # real signature unknown; restored from __doc__
    """ paint_pop_group(funcs:HarfBuzz.paint_funcs_t, paint_data=None, mode:HarfBuzz.paint_composite_mode_t) """
    pass

def paint_pop_transform(funcs, paint_data=None): # real signature unknown; restored from __doc__
    """ paint_pop_transform(funcs:HarfBuzz.paint_funcs_t, paint_data=None) """
    pass

def paint_push_clip_glyph(funcs, paint_data=None, glyph, font): # real signature unknown; restored from __doc__
    """ paint_push_clip_glyph(funcs:HarfBuzz.paint_funcs_t, paint_data=None, glyph:int, font:HarfBuzz.font_t) """
    pass

def paint_push_clip_rectangle(funcs, paint_data=None, xmin, ymin, xmax, ymax): # real signature unknown; restored from __doc__
    """ paint_push_clip_rectangle(funcs:HarfBuzz.paint_funcs_t, paint_data=None, xmin:float, ymin:float, xmax:float, ymax:float) """
    pass

def paint_push_font_transform(funcs, paint_data=None, font): # real signature unknown; restored from __doc__
    """ paint_push_font_transform(funcs:HarfBuzz.paint_funcs_t, paint_data=None, font:HarfBuzz.font_t) """
    pass

def paint_push_group(funcs, paint_data=None): # real signature unknown; restored from __doc__
    """ paint_push_group(funcs:HarfBuzz.paint_funcs_t, paint_data=None) """
    pass

def paint_push_inverse_font_transform(funcs, paint_data=None, font): # real signature unknown; restored from __doc__
    """ paint_push_inverse_font_transform(funcs:HarfBuzz.paint_funcs_t, paint_data=None, font:HarfBuzz.font_t) """
    pass

def paint_push_transform(funcs, paint_data=None, xx, yx, xy, yy, dx, dy): # real signature unknown; restored from __doc__
    """ paint_push_transform(funcs:HarfBuzz.paint_funcs_t, paint_data=None, xx:float, yx:float, xy:float, yy:float, dx:float, dy:float) """
    pass

def paint_radial_gradient(funcs, paint_data=None, color_line, x0, y0, r0, x1, y1, r1): # real signature unknown; restored from __doc__
    """ paint_radial_gradient(funcs:HarfBuzz.paint_funcs_t, paint_data=None, color_line:HarfBuzz.color_line_t, x0:float, y0:float, r0:float, x1:float, y1:float, r1:float) """
    pass

def paint_sweep_gradient(funcs, paint_data=None, color_line, x0, y0, start_angle, end_angle): # real signature unknown; restored from __doc__
    """ paint_sweep_gradient(funcs:HarfBuzz.paint_funcs_t, paint_data=None, color_line:HarfBuzz.color_line_t, x0:float, y0:float, start_angle:float, end_angle:float) """
    pass

def realloc(ptr=None, size): # real signature unknown; restored from __doc__
    """ realloc(ptr=None, size:int) """
    pass

def script_from_iso15924_tag(tag): # real signature unknown; restored from __doc__
    """ script_from_iso15924_tag(tag:int) -> HarfBuzz.script_t """
    pass

def script_from_string(p_str): # real signature unknown; restored from __doc__
    """ script_from_string(str:list) -> HarfBuzz.script_t """
    pass

def script_get_horizontal_direction(script): # real signature unknown; restored from __doc__
    """ script_get_horizontal_direction(script:HarfBuzz.script_t) -> HarfBuzz.direction_t """
    pass

def script_to_iso15924_tag(script): # real signature unknown; restored from __doc__
    """ script_to_iso15924_tag(script:HarfBuzz.script_t) -> int """
    return 0

def segment_properties_equal(a, b): # real signature unknown; restored from __doc__
    """ segment_properties_equal(a:HarfBuzz.segment_properties_t, b:HarfBuzz.segment_properties_t) -> int """
    return 0

def segment_properties_hash(p): # real signature unknown; restored from __doc__
    """ segment_properties_hash(p:HarfBuzz.segment_properties_t) -> int """
    return 0

def segment_properties_overlay(p, src): # real signature unknown; restored from __doc__
    """ segment_properties_overlay(p:HarfBuzz.segment_properties_t, src:HarfBuzz.segment_properties_t) """
    pass

def set_add(set, codepoint): # real signature unknown; restored from __doc__
    """ set_add(set:HarfBuzz.set_t, codepoint:int) """
    pass

def set_add_range(set, first, last): # real signature unknown; restored from __doc__
    """ set_add_range(set:HarfBuzz.set_t, first:int, last:int) """
    pass

def set_add_sorted_array(set, sorted_codepoints): # real signature unknown; restored from __doc__
    """ set_add_sorted_array(set:HarfBuzz.set_t, sorted_codepoints:list) """
    pass

def set_allocation_successful(set): # real signature unknown; restored from __doc__
    """ set_allocation_successful(set:HarfBuzz.set_t) -> int """
    return 0

def set_clear(set): # real signature unknown; restored from __doc__
    """ set_clear(set:HarfBuzz.set_t) """
    pass

def set_copy(set): # real signature unknown; restored from __doc__
    """ set_copy(set:HarfBuzz.set_t) -> HarfBuzz.set_t """
    pass

def set_create(): # real signature unknown; restored from __doc__
    """ set_create() -> HarfBuzz.set_t """
    pass

def set_del(set, codepoint): # real signature unknown; restored from __doc__
    """ set_del(set:HarfBuzz.set_t, codepoint:int) """
    pass

def set_del_range(set, first, last): # real signature unknown; restored from __doc__
    """ set_del_range(set:HarfBuzz.set_t, first:int, last:int) """
    pass

def set_get_empty(): # real signature unknown; restored from __doc__
    """ set_get_empty() -> HarfBuzz.set_t """
    pass

def set_get_max(set): # real signature unknown; restored from __doc__
    """ set_get_max(set:HarfBuzz.set_t) -> int """
    return 0

def set_get_min(set): # real signature unknown; restored from __doc__
    """ set_get_min(set:HarfBuzz.set_t) -> int """
    return 0

def set_get_population(set): # real signature unknown; restored from __doc__
    """ set_get_population(set:HarfBuzz.set_t) -> int """
    return 0

def set_has(set, codepoint): # real signature unknown; restored from __doc__
    """ set_has(set:HarfBuzz.set_t, codepoint:int) -> int """
    return 0

def set_hash(set): # real signature unknown; restored from __doc__
    """ set_hash(set:HarfBuzz.set_t) -> int """
    return 0

def set_intersect(set, other): # real signature unknown; restored from __doc__
    """ set_intersect(set:HarfBuzz.set_t, other:HarfBuzz.set_t) """
    pass

def set_invert(set): # real signature unknown; restored from __doc__
    """ set_invert(set:HarfBuzz.set_t) """
    pass

def set_is_empty(set): # real signature unknown; restored from __doc__
    """ set_is_empty(set:HarfBuzz.set_t) -> int """
    return 0

def set_is_equal(set, other): # real signature unknown; restored from __doc__
    """ set_is_equal(set:HarfBuzz.set_t, other:HarfBuzz.set_t) -> int """
    return 0

def set_is_inverted(set): # real signature unknown; restored from __doc__
    """ set_is_inverted(set:HarfBuzz.set_t) -> int """
    return 0

def set_is_subset(set, larger_set): # real signature unknown; restored from __doc__
    """ set_is_subset(set:HarfBuzz.set_t, larger_set:HarfBuzz.set_t) -> int """
    return 0

def set_next(set, codepoint): # real signature unknown; restored from __doc__
    """ set_next(set:HarfBuzz.set_t, codepoint:int) -> int, codepoint:int """
    return 0

def set_next_many(set, codepoint, out): # real signature unknown; restored from __doc__
    """ set_next_many(set:HarfBuzz.set_t, codepoint:int, out:list) -> int """
    return 0

def set_next_range(set, last): # real signature unknown; restored from __doc__
    """ set_next_range(set:HarfBuzz.set_t, last:int) -> int, first:int, last:int """
    return 0

def set_previous(set, codepoint): # real signature unknown; restored from __doc__
    """ set_previous(set:HarfBuzz.set_t, codepoint:int) -> int, codepoint:int """
    return 0

def set_previous_range(set, first): # real signature unknown; restored from __doc__
    """ set_previous_range(set:HarfBuzz.set_t, first:int) -> int, first:int, last:int """
    return 0

def set_set(set, other): # real signature unknown; restored from __doc__
    """ set_set(set:HarfBuzz.set_t, other:HarfBuzz.set_t) """
    pass

def set_subtract(set, other): # real signature unknown; restored from __doc__
    """ set_subtract(set:HarfBuzz.set_t, other:HarfBuzz.set_t) """
    pass

def set_symmetric_difference(set, other): # real signature unknown; restored from __doc__
    """ set_symmetric_difference(set:HarfBuzz.set_t, other:HarfBuzz.set_t) """
    pass

def set_union(set, other): # real signature unknown; restored from __doc__
    """ set_union(set:HarfBuzz.set_t, other:HarfBuzz.set_t) """
    pass

def shape(font, buffer, features=None): # real signature unknown; restored from __doc__
    """ shape(font:HarfBuzz.font_t, buffer:HarfBuzz.buffer_t, features:list=None) """
    pass

def shape_full(font, buffer, features=None, shaper_list=None): # real signature unknown; restored from __doc__
    """ shape_full(font:HarfBuzz.font_t, buffer:HarfBuzz.buffer_t, features:list=None, shaper_list:list=None) -> int """
    return 0

def shape_list_shapers(): # real signature unknown; restored from __doc__
    """ shape_list_shapers() -> list """
    return []

def shape_plan_create(face, props, user_features, shaper_list): # real signature unknown; restored from __doc__
    """ shape_plan_create(face:HarfBuzz.face_t, props:HarfBuzz.segment_properties_t, user_features:list, shaper_list:list) -> HarfBuzz.shape_plan_t """
    pass

def shape_plan_create2(face, props, user_features, coords, shaper_list): # real signature unknown; restored from __doc__
    """ shape_plan_create2(face:HarfBuzz.face_t, props:HarfBuzz.segment_properties_t, user_features:list, coords:list, shaper_list:list) -> HarfBuzz.shape_plan_t """
    pass

def shape_plan_create_cached(face, props, user_features, shaper_list): # real signature unknown; restored from __doc__
    """ shape_plan_create_cached(face:HarfBuzz.face_t, props:HarfBuzz.segment_properties_t, user_features:list, shaper_list:list) -> HarfBuzz.shape_plan_t """
    pass

def shape_plan_create_cached2(face, props, user_features, coords, shaper_list): # real signature unknown; restored from __doc__
    """ shape_plan_create_cached2(face:HarfBuzz.face_t, props:HarfBuzz.segment_properties_t, user_features:list, coords:list, shaper_list:list) -> HarfBuzz.shape_plan_t """
    pass

def shape_plan_execute(shape_plan, font, buffer, features): # real signature unknown; restored from __doc__
    """ shape_plan_execute(shape_plan:HarfBuzz.shape_plan_t, font:HarfBuzz.font_t, buffer:HarfBuzz.buffer_t, features:list) -> int """
    return 0

def shape_plan_get_empty(): # real signature unknown; restored from __doc__
    """ shape_plan_get_empty() -> HarfBuzz.shape_plan_t """
    pass

def shape_plan_get_shaper(shape_plan): # real signature unknown; restored from __doc__
    """ shape_plan_get_shaper(shape_plan:HarfBuzz.shape_plan_t) -> str """
    return ""

def style_get_value(font, style_tag): # real signature unknown; restored from __doc__
    """ style_get_value(font:HarfBuzz.font_t, style_tag:HarfBuzz.style_tag_t) -> float """
    return 0.0

def tag_from_string(p_str): # real signature unknown; restored from __doc__
    """ tag_from_string(str:list) -> int """
    return 0

def tag_to_string(tag): # real signature unknown; restored from __doc__
    """ tag_to_string(tag:int) -> buf:list """
    pass

def unicode_combining_class(ufuncs, unicode): # real signature unknown; restored from __doc__
    """ unicode_combining_class(ufuncs:HarfBuzz.unicode_funcs_t, unicode:int) -> HarfBuzz.unicode_combining_class_t """
    pass

def unicode_compose(ufuncs, a, b): # real signature unknown; restored from __doc__
    """ unicode_compose(ufuncs:HarfBuzz.unicode_funcs_t, a:int, b:int) -> int, ab:int """
    return 0

def unicode_decompose(ufuncs, ab): # real signature unknown; restored from __doc__
    """ unicode_decompose(ufuncs:HarfBuzz.unicode_funcs_t, ab:int) -> int, a:int, b:int """
    return 0

def unicode_decompose_compatibility(ufuncs, u): # real signature unknown; restored from __doc__
    """ unicode_decompose_compatibility(ufuncs:HarfBuzz.unicode_funcs_t, u:int) -> int, decomposed:int """
    return 0

def unicode_eastasian_width(ufuncs, unicode): # real signature unknown; restored from __doc__
    """ unicode_eastasian_width(ufuncs:HarfBuzz.unicode_funcs_t, unicode:int) -> int """
    return 0

def unicode_funcs_create(parent=None): # real signature unknown; restored from __doc__
    """ unicode_funcs_create(parent:HarfBuzz.unicode_funcs_t=None) -> HarfBuzz.unicode_funcs_t """
    pass

def unicode_funcs_get_default(): # real signature unknown; restored from __doc__
    """ unicode_funcs_get_default() -> HarfBuzz.unicode_funcs_t """
    pass

def unicode_funcs_get_empty(): # real signature unknown; restored from __doc__
    """ unicode_funcs_get_empty() -> HarfBuzz.unicode_funcs_t """
    pass

def unicode_funcs_get_parent(ufuncs): # real signature unknown; restored from __doc__
    """ unicode_funcs_get_parent(ufuncs:HarfBuzz.unicode_funcs_t) -> HarfBuzz.unicode_funcs_t """
    pass

def unicode_funcs_is_immutable(ufuncs): # real signature unknown; restored from __doc__
    """ unicode_funcs_is_immutable(ufuncs:HarfBuzz.unicode_funcs_t) -> int """
    return 0

def unicode_funcs_make_immutable(ufuncs): # real signature unknown; restored from __doc__
    """ unicode_funcs_make_immutable(ufuncs:HarfBuzz.unicode_funcs_t) """
    pass

def unicode_funcs_set_combining_class_func(ufuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ unicode_funcs_set_combining_class_func(ufuncs:HarfBuzz.unicode_funcs_t, func:HarfBuzz.unicode_combining_class_func_t, user_data=None) """
    pass

def unicode_funcs_set_compose_func(ufuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ unicode_funcs_set_compose_func(ufuncs:HarfBuzz.unicode_funcs_t, func:HarfBuzz.unicode_compose_func_t, user_data=None) """
    pass

def unicode_funcs_set_decompose_compatibility_func(ufuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ unicode_funcs_set_decompose_compatibility_func(ufuncs:HarfBuzz.unicode_funcs_t, func:HarfBuzz.unicode_decompose_compatibility_func_t, user_data=None) """
    pass

def unicode_funcs_set_decompose_func(ufuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ unicode_funcs_set_decompose_func(ufuncs:HarfBuzz.unicode_funcs_t, func:HarfBuzz.unicode_decompose_func_t, user_data=None) """
    pass

def unicode_funcs_set_eastasian_width_func(ufuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ unicode_funcs_set_eastasian_width_func(ufuncs:HarfBuzz.unicode_funcs_t, func:HarfBuzz.unicode_eastasian_width_func_t, user_data=None) """
    pass

def unicode_funcs_set_general_category_func(ufuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ unicode_funcs_set_general_category_func(ufuncs:HarfBuzz.unicode_funcs_t, func:HarfBuzz.unicode_general_category_func_t, user_data=None) """
    pass

def unicode_funcs_set_mirroring_func(ufuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ unicode_funcs_set_mirroring_func(ufuncs:HarfBuzz.unicode_funcs_t, func:HarfBuzz.unicode_mirroring_func_t, user_data=None) """
    pass

def unicode_funcs_set_script_func(ufuncs, func, user_data=None): # real signature unknown; restored from __doc__
    """ unicode_funcs_set_script_func(ufuncs:HarfBuzz.unicode_funcs_t, func:HarfBuzz.unicode_script_func_t, user_data=None) """
    pass

def unicode_general_category(ufuncs, unicode): # real signature unknown; restored from __doc__
    """ unicode_general_category(ufuncs:HarfBuzz.unicode_funcs_t, unicode:int) -> HarfBuzz.unicode_general_category_t """
    pass

def unicode_mirroring(ufuncs, unicode): # real signature unknown; restored from __doc__
    """ unicode_mirroring(ufuncs:HarfBuzz.unicode_funcs_t, unicode:int) -> int """
    return 0

def unicode_script(ufuncs, unicode): # real signature unknown; restored from __doc__
    """ unicode_script(ufuncs:HarfBuzz.unicode_funcs_t, unicode:int) -> HarfBuzz.script_t """
    pass

def variation_from_string(p_str): # real signature unknown; restored from __doc__
    """ variation_from_string(str:list) -> int, variation:HarfBuzz.variation_t """
    return 0

def variation_to_string(variation): # real signature unknown; restored from __doc__
    """ variation_to_string(variation:HarfBuzz.variation_t) -> buf:list """
    pass

# classes

from .aat_layout_feature_selector_info_t import aat_layout_feature_selector_info_t
from .aat_layout_feature_selector_t import aat_layout_feature_selector_t
from .aat_layout_feature_type_t import aat_layout_feature_type_t
from .blob_t import blob_t
from .buffer_cluster_level_t import buffer_cluster_level_t
from .buffer_content_type_t import buffer_content_type_t
from .buffer_diff_flags_t import buffer_diff_flags_t
from .buffer_flags_t import buffer_flags_t
from .buffer_serialize_flags_t import buffer_serialize_flags_t
from .buffer_serialize_format_t import buffer_serialize_format_t
from .buffer_t import buffer_t
from .color_line_t import color_line_t
from .color_stop_t import color_stop_t
from .direction_t import direction_t
from .draw_funcs_t import draw_funcs_t
from .draw_state_t import draw_state_t
from .face_t import face_t
from .feature_t import feature_t
from .font_extents_t import font_extents_t
from .font_funcs_t import font_funcs_t
from .font_t import font_t
from .glyph_extents_t import glyph_extents_t
from .glyph_flags_t import glyph_flags_t
from .glyph_info_t import glyph_info_t
from .glyph_position_t import glyph_position_t
from .language_t import language_t
from .map_t import map_t
from .memory_mode_t import memory_mode_t
from .ot_color_layer_t import ot_color_layer_t
from .ot_color_palette_flags_t import ot_color_palette_flags_t
from .ot_layout_baseline_tag_t import ot_layout_baseline_tag_t
from .ot_layout_glyph_class_t import ot_layout_glyph_class_t
from .ot_math_constant_t import ot_math_constant_t
from .ot_math_glyph_part_flags_t import ot_math_glyph_part_flags_t
from .ot_math_glyph_part_t import ot_math_glyph_part_t
from .ot_math_glyph_variant_t import ot_math_glyph_variant_t
from .ot_math_kern_entry_t import ot_math_kern_entry_t
from .ot_math_kern_t import ot_math_kern_t
from .ot_meta_tag_t import ot_meta_tag_t
from .ot_metrics_tag_t import ot_metrics_tag_t
from .ot_name_entry_t import ot_name_entry_t
from .ot_name_id_predefined_t import ot_name_id_predefined_t
from .ot_var_axis_flags_t import ot_var_axis_flags_t
from .ot_var_axis_info_t import ot_var_axis_info_t
from .ot_var_axis_t import ot_var_axis_t
from .paint_composite_mode_t import paint_composite_mode_t
from .paint_extend_t import paint_extend_t
from .paint_funcs_t import paint_funcs_t
from .script_t import script_t
from .segment_properties_t import segment_properties_t
from .set_t import set_t
from .shape_plan_t import shape_plan_t
from .style_tag_t import style_tag_t
from .unicode_combining_class_t import unicode_combining_class_t
from .unicode_funcs_t import unicode_funcs_t
from .unicode_general_category_t import unicode_general_category_t
from .user_data_key_t import user_data_key_t
from .variation_t import variation_t
from .var_int_t import var_int_t
from .var_num_t import var_num_t
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x00000208a4df4440>'

__path__ = []

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.HarfBuzz', loader=<gi.importer.DynamicImporter object at 0x00000208a4df4440>)"

