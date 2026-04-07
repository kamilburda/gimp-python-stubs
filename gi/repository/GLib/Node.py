# encoding: utf-8
# module gi.repository.GLib
# by generator 1.147
# no doc

# imports
from gi._gi import Pid, spawn_async

from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GLib as __gi_overrides_GLib
import gi._gi as __gi__gi


class Node(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Node()
    """
    def children_foreach(self, flags, func, data=None): # real signature unknown; restored from __doc__
        """ children_foreach(self, flags:GLib.TraverseFlags, func:GLib.NodeForeachFunc, data=None) """
        pass

    def child_index(self, data=None): # real signature unknown; restored from __doc__
        """ child_index(self, data=None) -> int """
        return 0

    def child_position(self, child): # real signature unknown; restored from __doc__
        """ child_position(self, child:GLib.Node) -> int """
        return 0

    def depth(self): # real signature unknown; restored from __doc__
        """ depth(self) -> int """
        return 0

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def is_ancestor(self, descendant): # real signature unknown; restored from __doc__
        """ is_ancestor(self, descendant:GLib.Node) -> bool """
        return False

    def max_height(self): # real signature unknown; restored from __doc__
        """ max_height(self) -> int """
        return 0

    def n_children(self): # real signature unknown; restored from __doc__
        """ n_children(self) -> int """
        return 0

    def n_nodes(self, flags): # real signature unknown; restored from __doc__
        """ n_nodes(self, flags:GLib.TraverseFlags) -> int """
        return 0

    def pop_allocator(self): # real signature unknown; restored from __doc__
        """ pop_allocator() """
        pass

    def push_allocator(self, allocator): # real signature unknown; restored from __doc__
        """ push_allocator(allocator:GLib.Allocator) """
        pass

    def reverse_children(self): # real signature unknown; restored from __doc__
        """ reverse_children(self) """
        pass

    def traverse(self, order, flags, max_depth, func, data=None): # real signature unknown; restored from __doc__
        """ traverse(self, order:GLib.TraverseType, flags:GLib.TraverseFlags, max_depth:int, func:GLib.NodeTraverseFunc, data=None) """
        pass

    def unlink(self): # real signature unknown; restored from __doc__
        """ unlink(self) """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Node), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Node' objects>, '__weakref__': <attribute '__weakref__' of 'Node' objects>, '__doc__': None, 'data': <property object at 0x0000018ea0079260>, 'next': <property object at 0x0000018ea0079350>, 'prev': <property object at 0x0000018ea0079440>, 'parent': <property object at 0x0000018ea0079530>, 'children': <property object at 0x0000018ea0079620>, 'child_index': gi.FunctionInfo(child_index), 'child_position': gi.FunctionInfo(child_position), 'children_foreach': gi.FunctionInfo(children_foreach), 'depth': gi.FunctionInfo(depth), 'destroy': gi.FunctionInfo(destroy), 'is_ancestor': gi.FunctionInfo(is_ancestor), 'max_height': gi.FunctionInfo(max_height), 'n_children': gi.FunctionInfo(n_children), 'n_nodes': gi.FunctionInfo(n_nodes), 'reverse_children': gi.FunctionInfo(reverse_children), 'traverse': gi.FunctionInfo(traverse), 'unlink': gi.FunctionInfo(unlink), 'pop_allocator': <staticmethod(gi.FunctionInfo(pop_allocator))>, 'push_allocator': <staticmethod(gi.FunctionInfo(push_allocator))>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Node)


