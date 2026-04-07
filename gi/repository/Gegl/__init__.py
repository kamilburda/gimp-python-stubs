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


# Variables with simple values

AUTO_ROWSTRIDE = 0

CH_BACK_CENTER = 256
CH_BACK_LEFT = 16
CH_BACK_RIGHT = 32

CH_FRONT_CENTER = 4
CH_FRONT_LEFT = 1

CH_FRONT_LEFT_OF_CENTER = 64

CH_FRONT_RIGHT = 2

CH_FRONT_RIGHT_OF_CENTER = 128

CH_LAYOUT_2POINT1 = 0

CH_LAYOUT_2_1 = 0
CH_LAYOUT_2_2 = 0

CH_LAYOUT_3POINT1 = 0
CH_LAYOUT_4POINT0 = 0
CH_LAYOUT_4POINT1 = 0
CH_LAYOUT_5POINT0 = 0

CH_LAYOUT_5POINT0_BACK = 0

CH_LAYOUT_5POINT1 = 0

CH_LAYOUT_5POINT1_BACK = 0

CH_LAYOUT_6POINT0 = 0

CH_LAYOUT_6POINT0_FRONT = 0

CH_LAYOUT_6POINT1 = 0

CH_LAYOUT_6POINT1_BACK = 0
CH_LAYOUT_6POINT1_FRONT = 0

CH_LAYOUT_7POINT0 = 0

CH_LAYOUT_7POINT0_FRONT = 0

CH_LAYOUT_7POINT1 = 0

CH_LAYOUT_7POINT1_WIDE = 0

CH_LAYOUT_7POINT1_WIDE_BACK = 0

CH_LAYOUT_HEXADECAGONAL = 0
CH_LAYOUT_HEXAGONAL = 0
CH_LAYOUT_NATIVE = -1
CH_LAYOUT_OCTAGONAL = 0
CH_LAYOUT_QUAD = 0
CH_LAYOUT_STEREO = 0

CH_LAYOUT_STEREO_DOWNMIX = 0

CH_LAYOUT_SURROUND = 0

CH_LOW_FREQUENCY = 8

CH_LOW_FREQUENCY_2 = 0

CH_SIDE_LEFT = 512
CH_SIDE_RIGHT = 1024

CH_STEREO_LEFT = 536870912
CH_STEREO_RIGHT = 1073741824

CH_SURROUND_DIRECT_LEFT = 0
CH_SURROUND_DIRECT_RIGHT = 0

CH_TOP_BACK_CENTER = 65536
CH_TOP_BACK_LEFT = 32768
CH_TOP_BACK_RIGHT = 131072

CH_TOP_CENTER = 2048

CH_TOP_FRONT_CENTER = 8192
CH_TOP_FRONT_LEFT = 4096
CH_TOP_FRONT_RIGHT = 16384

CH_WIDE_LEFT = -2147483648
CH_WIDE_RIGHT = 0

FLOAT_EPSILON = 1e-05

LOOKUP_MAX_ENTRIES = 819200

MAJOR_VERSION = 0

MAX_AUDIO_CHANNELS = 8

MICRO_VERSION = 66

MINOR_VERSION = 4

PARAM_NO_VALIDATE = 64

_namespace = 'Gegl'

_version = '0.4'

# functions

def babl_variant(format, variant): # real signature unknown; restored from __doc__
    """ babl_variant(format:Babl.Object, variant:Gegl.BablVariant) -> Babl.Object """
    pass

def cl_disable(): # real signature unknown; restored from __doc__
    """ cl_disable() """
    pass

def cl_init(): # real signature unknown; restored from __doc__
    """ cl_init() -> bool """
    return False

def cl_is_accelerated(): # real signature unknown; restored from __doc__
    """ cl_is_accelerated() -> bool """
    return False

def config(): # real signature unknown; restored from __doc__
    """ config() -> Gegl.Config """
    pass

def create_chain(ops, op_start, op_end, time, rel_dim, path_root): # real signature unknown; restored from __doc__
    """ create_chain(ops:str, op_start:Gegl.Node, op_end:Gegl.Node, time:float, rel_dim:int, path_root:str) """
    pass

def create_chain_argv(ops, op_start, op_end, time, rel_dim, path_root): # real signature unknown; restored from __doc__
    """ create_chain_argv(ops:str, op_start:Gegl.Node, op_end:Gegl.Node, time:float, rel_dim:int, path_root:str) """
    pass

def exit(): # real signature unknown; restored from __doc__
    """ exit() """
    pass

def format(format_name): # real signature unknown; restored from __doc__
    """ format(format_name:str) -> GObject.Value or None """
    pass

def format_get_name(format): # real signature unknown; restored from __doc__
    """ format_get_name(format:GObject.Value) -> str or None """
    return ""

def get_version(): # real signature unknown; restored from __doc__
    """ get_version() -> major:int, minor:int, micro:int """
    pass

def graph_dump_outputs(node): # real signature unknown; restored from __doc__
    """ graph_dump_outputs(node:Gegl.Node) """
    pass

def graph_dump_request(node, roi): # real signature unknown; restored from __doc__
    """ graph_dump_request(node:Gegl.Node, roi:Gegl.Rectangle) """
    pass

def has_operation(operation_type): # real signature unknown; restored from __doc__
    """ has_operation(operation_type:str) -> bool """
    return False

def init(argv=None): # real signature unknown; restored from __doc__
    """ init(argv:list=None) -> argv:list """
    pass

def is_main_thread(): # real signature unknown; restored from __doc__
    """ is_main_thread() -> bool """
    return False

def list_operations(): # real signature unknown; restored from __doc__
    """ list_operations() -> list """
    return []

def load_module_directory(path): # real signature unknown; restored from __doc__
    """ load_module_directory(path:str) """
    pass

def parallel_distribute(max_n, func, user_data=None): # real signature unknown; restored from __doc__
    """ parallel_distribute(max_n:int, func:Gegl.ParallelDistributeFunc, user_data=None) """
    pass

def parallel_distribute_area(area, thread_cost, split_strategy, func, user_data=None): # real signature unknown; restored from __doc__
    """ parallel_distribute_area(area:Gegl.Rectangle, thread_cost:float, split_strategy:Gegl.SplitStrategy, func:Gegl.ParallelDistributeAreaFunc, user_data=None) """
    pass

def parallel_distribute_range(size, thread_cost, func, user_data=None): # real signature unknown; restored from __doc__
    """ parallel_distribute_range(size:int, thread_cost:float, func:Gegl.ParallelDistributeRangeFunc, user_data=None) """
    pass

def param_spec_audio_fragment(name, nick, blurb, flags): # real signature unknown; restored from __doc__
    """ param_spec_audio_fragment(name:str, nick:str, blurb:str, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_color(name, nick, blurb, default_color, flags): # real signature unknown; restored from __doc__
    """ param_spec_color(name:str, nick:str, blurb:str, default_color:Gegl.Color, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_color_from_string(name, nick, blurb, default_color_string, flags): # real signature unknown; restored from __doc__
    """ param_spec_color_from_string(name:str, nick:str, blurb:str, default_color_string:str, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_color_get_default(self): # real signature unknown; restored from __doc__
    """ param_spec_color_get_default(self:GObject.ParamSpec) -> Gegl.Color """
    pass

def param_spec_curve(name, nick, blurb, default_curve, flags): # real signature unknown; restored from __doc__
    """ param_spec_curve(name:str, nick:str, blurb:str, default_curve:Gegl.Curve, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_double(name, nick, blurb, minimum, maximum, default_value, ui_minimum, ui_maximum, ui_gamma, flags): # real signature unknown; restored from __doc__
    """ param_spec_double(name:str, nick:str, blurb:str, minimum:float, maximum:float, default_value:float, ui_minimum:float, ui_maximum:float, ui_gamma:float, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_enum(name, nick, blurb, enum_type, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_enum(name:str, nick:str, blurb:str, enum_type:GType, default_value:int, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_file_path(name, nick, blurb, no_validate, null_ok, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_file_path(name:str, nick:str, blurb:str, no_validate:bool, null_ok:bool, default_value:str, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_format(name, nick, blurb, flags): # real signature unknown; restored from __doc__
    """ param_spec_format(name:str, nick:str, blurb:str, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_get_property_key(pspec, key_name): # real signature unknown; restored from __doc__
    """ param_spec_get_property_key(pspec:GObject.ParamSpec, key_name:str) -> str """
    return ""

def param_spec_int(name, nick, blurb, minimum, maximum, default_value, ui_minimum, ui_maximum, ui_gamma, flags): # real signature unknown; restored from __doc__
    """ param_spec_int(name:str, nick:str, blurb:str, minimum:int, maximum:int, default_value:int, ui_minimum:int, ui_maximum:int, ui_gamma:float, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_path(name, nick, blurb, default_path, flags): # real signature unknown; restored from __doc__
    """ param_spec_path(name:str, nick:str, blurb:str, default_path:Gegl.Path, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_seed(name, nick, blurb, flags): # real signature unknown; restored from __doc__
    """ param_spec_seed(name:str, nick:str, blurb:str, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_set_property_key(pspec, key_name, value): # real signature unknown; restored from __doc__
    """ param_spec_set_property_key(pspec:GObject.ParamSpec, key_name:str, value:str) """
    pass

def param_spec_string(name, nick, blurb, no_validate, null_ok, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_string(name:str, nick:str, blurb:str, no_validate:bool, null_ok:bool, default_value:str, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_uri(name, nick, blurb, no_validate, null_ok, default_value, flags): # real signature unknown; restored from __doc__
    """ param_spec_uri(name:str, nick:str, blurb:str, no_validate:bool, null_ok:bool, default_value:str, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def rectangle_infinite_plane(): # real signature unknown; restored from __doc__
    """ rectangle_infinite_plane() -> Gegl.Rectangle """
    pass

def reset_stats(): # real signature unknown; restored from __doc__
    """ reset_stats() """
    pass

def serialize(start, end, basepath, serialize_flags): # real signature unknown; restored from __doc__
    """ serialize(start:Gegl.Node, end:Gegl.Node, basepath:str, serialize_flags:Gegl.SerializeFlag) -> str """
    return ""

def stats(): # real signature unknown; restored from __doc__
    """ stats() -> Gegl.Stats """
    pass

# classes

from .AbyssPolicy import AbyssPolicy
from .AccessMode import AccessMode
from .AudioFragment import AudioFragment
from .AudioFragmentClass import AudioFragmentClass
from .AudioFragmentPrivate import AudioFragmentPrivate
from .BablVariant import BablVariant
from .BlitFlags import BlitFlags
from .TileSource import TileSource
from .TileHandler import TileHandler
from .Buffer import Buffer
from .BufferIterator import BufferIterator
from .BufferIteratorItem import BufferIteratorItem
from .BufferIteratorPriv import BufferIteratorPriv
from .BufferMatrix2 import BufferMatrix2
from .CachePolicy import CachePolicy
from .Color import Color
from .ColorClass import ColorClass
from .ColorPrivate import ColorPrivate
from .Config import Config
from .Curve import Curve
from .CurveClass import CurveClass
from .DistanceMetric import DistanceMetric
from .DitherMethod import DitherMethod
from .Lookup import Lookup
from .MapFlags import MapFlags
from .Matrix3 import Matrix3
from .Metadata import Metadata
from .MetadataStore import MetadataStore
from .MetadataHash import MetadataHash
from .MetadataHashClass import MetadataHashClass
from .MetadataInterface import MetadataInterface
from .MetadataIter import MetadataIter
from .MetadataMap import MetadataMap
from .MetadataStoreClass import MetadataStoreClass
from .Node import Node
from .Operation import Operation
from .OperationContext import OperationContext
from .Orientation import Orientation
from .PadType import PadType
from .ParamAudioFragment import ParamAudioFragment
from .ParamColor import ParamColor
from .ParamCurve import ParamCurve
from .ParamDouble import ParamDouble
from .ParamEnum import ParamEnum
from .ParamFilePath import ParamFilePath
from .ParamFormat import ParamFormat
from .ParamInt import ParamInt
from .ParamPath import ParamPath
from .ParamSeed import ParamSeed
from .ParamSpecDouble import ParamSpecDouble
from .ParamSpecEnum import ParamSpecEnum
from .ParamSpecFilePath import ParamSpecFilePath
from .ParamSpecFormat import ParamSpecFormat
from .ParamSpecInt import ParamSpecInt
from .ParamSpecSeed import ParamSpecSeed
from .ParamSpecString import ParamSpecString
from .ParamSpecUri import ParamSpecUri
from .ParamString import ParamString
from .ParamUri import ParamUri
from .Path import Path
from .PathClass import PathClass
from .PathItem import PathItem
from .PathList import PathList
from .PathPoint import PathPoint
from .Processor import Processor
from .Random import Random
from .Rectangle import Rectangle
from .RectangleAlignment import RectangleAlignment
from .ResolutionUnit import ResolutionUnit
from .Sampler import Sampler
from .SamplerType import SamplerType
from .SerializeFlag import SerializeFlag
from .SplitStrategy import SplitStrategy
from .Stats import Stats
from .Tile import Tile
from .TileBackend import TileBackend
from .TileBackendClass import TileBackendClass
from .TileBackendPrivate import TileBackendPrivate
from .TileCommand import TileCommand
from .TileCopyParams import TileCopyParams
from .TileHandlerClass import TileHandlerClass
from .TileHandlerPrivate import TileHandlerPrivate
from .TileSourceClass import TileSourceClass
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x000001ebd98217c0>'

__path__ = []

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Gegl', loader=<gi.importer.DynamicImporter object at 0x000001ebd98217c0>)"

