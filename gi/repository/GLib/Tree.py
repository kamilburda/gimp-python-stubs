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


class Tree(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new_full(key_compare_func:GLib.CompareDataFunc, key_compare_data=None, key_destroy_func:GLib.DestroyNotify) -> GLib.Tree
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def foreach(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, func:GLib.TraverseFunc, user_data=None) """
        pass

    def foreach_node(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_node(self, func:GLib.TraverseNodeFunc, user_data=None) """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def insert(self, key=None, value=None): # real signature unknown; restored from __doc__
        """ insert(self, key=None, value=None) """
        pass

    def insert_node(self, key=None, value=None): # real signature unknown; restored from __doc__
        """ insert_node(self, key=None, value=None) -> GLib.TreeNode or None """
        pass

    def lookup(self, key=None): # real signature unknown; restored from __doc__
        """ lookup(self, key=None) """
        pass

    def lookup_extended(self, lookup_key=None): # real signature unknown; restored from __doc__
        """ lookup_extended(self, lookup_key=None) -> bool, orig_key, value """
        return False

    def lookup_node(self, key=None): # real signature unknown; restored from __doc__
        """ lookup_node(self, key=None) -> GLib.TreeNode or None """
        pass

    def lower_bound(self, key=None): # real signature unknown; restored from __doc__
        """ lower_bound(self, key=None) -> GLib.TreeNode or None """
        pass

    @classmethod
    def new_full(cls, key_compare_func, key_compare_data=None, key_destroy_func): # real signature unknown; restored from __doc__
        """ new_full(key_compare_func:GLib.CompareDataFunc, key_compare_data=None, key_destroy_func:GLib.DestroyNotify) -> GLib.Tree """
        pass

    def nnodes(self): # real signature unknown; restored from __doc__
        """ nnodes(self) -> int """
        return 0

    def node_first(self): # real signature unknown; restored from __doc__
        """ node_first(self) -> GLib.TreeNode or None """
        pass

    def node_last(self): # real signature unknown; restored from __doc__
        """ node_last(self) -> GLib.TreeNode or None """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.Tree """
        pass

    def remove(self, key=None): # real signature unknown; restored from __doc__
        """ remove(self, key=None) -> bool """
        return False

    def remove_all(self): # real signature unknown; restored from __doc__
        """ remove_all(self) """
        pass

    def replace(self, key=None, value=None): # real signature unknown; restored from __doc__
        """ replace(self, key=None, value=None) """
        pass

    def replace_node(self, key=None, value=None): # real signature unknown; restored from __doc__
        """ replace_node(self, key=None, value=None) -> GLib.TreeNode or None """
        pass

    def search(self, search_func, user_data=None): # real signature unknown; restored from __doc__
        """ search(self, search_func:GLib.CompareFunc, user_data=None) """
        pass

    def search_node(self, search_func, user_data=None): # real signature unknown; restored from __doc__
        """ search_node(self, search_func:GLib.CompareFunc, user_data=None) -> GLib.TreeNode or None """
        pass

    def steal(self, key=None): # real signature unknown; restored from __doc__
        """ steal(self, key=None) -> bool """
        return False

    def traverse(self, traverse_func, traverse_type, user_data=None): # real signature unknown; restored from __doc__
        """ traverse(self, traverse_func:GLib.TraverseFunc, traverse_type:GLib.TraverseType, user_data=None) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def upper_bound(self, key=None): # real signature unknown; restored from __doc__
        """ upper_bound(self, key=None) -> GLib.TreeNode or None """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Tree), '__module__': 'gi.repository.GLib', '__gtype__': <GType GTree (2640518496)>, '__dict__': <attribute '__dict__' of 'Tree' objects>, '__weakref__': <attribute '__weakref__' of 'Tree' objects>, '__doc__': None, 'new_full': <classmethod(gi.FunctionInfo(new_full))>, 'destroy': gi.FunctionInfo(destroy), 'foreach': gi.FunctionInfo(foreach), 'foreach_node': gi.FunctionInfo(foreach_node), 'height': gi.FunctionInfo(height), 'insert': gi.FunctionInfo(insert), 'insert_node': gi.FunctionInfo(insert_node), 'lookup': gi.FunctionInfo(lookup), 'lookup_extended': gi.FunctionInfo(lookup_extended), 'lookup_node': gi.FunctionInfo(lookup_node), 'lower_bound': gi.FunctionInfo(lower_bound), 'nnodes': gi.FunctionInfo(nnodes), 'node_first': gi.FunctionInfo(node_first), 'node_last': gi.FunctionInfo(node_last), 'ref': gi.FunctionInfo(ref), 'remove': gi.FunctionInfo(remove), 'remove_all': gi.FunctionInfo(remove_all), 'replace': gi.FunctionInfo(replace), 'replace_node': gi.FunctionInfo(replace_node), 'search': gi.FunctionInfo(search), 'search_node': gi.FunctionInfo(search_node), 'steal': gi.FunctionInfo(steal), 'traverse': gi.FunctionInfo(traverse), 'unref': gi.FunctionInfo(unref), 'upper_bound': gi.FunctionInfo(upper_bound)})"
    __gtype__ = None # (!) real value is '<GType GTree (2640518496)>'
    __info__ = StructInfo(Tree)


