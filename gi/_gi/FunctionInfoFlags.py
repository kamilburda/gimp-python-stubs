# encoding: utf-8
# module gi._gi
# by generator 1.147
# no doc

# imports
from gobject import GBoxed, GInterface, GPointer, GType, Warning

import enum as __enum
import gi as __gi
import gobject as __gobject


from .type import type

class FunctionInfoFlags(type):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    IS_CONSTRUCTOR = 2
    IS_GETTER = 4
    IS_METHOD = 1
    IS_SETTER = 8
    WRAPS_VFUNC = 16


