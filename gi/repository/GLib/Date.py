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


class Date(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Date()
        new() -> GLib.Date
        new_dmy(day:int, month:GLib.DateMonth, year:int) -> GLib.Date
        new_julian(julian_day:int) -> GLib.Date
    """
    def add_days(self, n_days): # real signature unknown; restored from __doc__
        """ add_days(self, n_days:int) """
        pass

    def add_months(self, n_months): # real signature unknown; restored from __doc__
        """ add_months(self, n_months:int) """
        pass

    def add_years(self, n_years): # real signature unknown; restored from __doc__
        """ add_years(self, n_years:int) """
        pass

    def clamp(self, min_date, max_date): # real signature unknown; restored from __doc__
        """ clamp(self, min_date:GLib.Date, max_date:GLib.Date) """
        pass

    def clear(self, n_dates): # real signature unknown; restored from __doc__
        """ clear(self, n_dates:int) """
        pass

    def compare(self, rhs): # real signature unknown; restored from __doc__
        """ compare(self, rhs:GLib.Date) -> int """
        return 0

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GLib.Date """
        pass

    def days_between(self, date2): # real signature unknown; restored from __doc__
        """ days_between(self, date2:GLib.Date) -> int """
        return 0

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_day(self): # real signature unknown; restored from __doc__
        """ get_day(self) -> int """
        return 0

    def get_days_in_month(self, month, year): # real signature unknown; restored from __doc__
        """ get_days_in_month(month:GLib.DateMonth, year:int) -> int """
        return 0

    def get_day_of_year(self): # real signature unknown; restored from __doc__
        """ get_day_of_year(self) -> int """
        return 0

    def get_iso8601_week_of_year(self): # real signature unknown; restored from __doc__
        """ get_iso8601_week_of_year(self) -> int """
        return 0

    def get_julian(self): # real signature unknown; restored from __doc__
        """ get_julian(self) -> int """
        return 0

    def get_monday_weeks_in_year(self, year): # real signature unknown; restored from __doc__
        """ get_monday_weeks_in_year(year:int) -> int """
        return 0

    def get_monday_week_of_year(self): # real signature unknown; restored from __doc__
        """ get_monday_week_of_year(self) -> int """
        return 0

    def get_month(self): # real signature unknown; restored from __doc__
        """ get_month(self) -> GLib.DateMonth """
        pass

    def get_sunday_weeks_in_year(self, year): # real signature unknown; restored from __doc__
        """ get_sunday_weeks_in_year(year:int) -> int """
        return 0

    def get_sunday_week_of_year(self): # real signature unknown; restored from __doc__
        """ get_sunday_week_of_year(self) -> int """
        return 0

    def get_weekday(self): # real signature unknown; restored from __doc__
        """ get_weekday(self) -> GLib.DateWeekday """
        pass

    def get_weeks_in_year(self, year, first_day_of_week): # real signature unknown; restored from __doc__
        """ get_weeks_in_year(year:int, first_day_of_week:GLib.DateWeekday) -> int """
        return 0

    def get_week_of_year(self, first_day_of_week): # real signature unknown; restored from __doc__
        """ get_week_of_year(self, first_day_of_week:GLib.DateWeekday) -> int """
        return 0

    def get_year(self): # real signature unknown; restored from __doc__
        """ get_year(self) -> int """
        return 0

    def is_first_of_month(self): # real signature unknown; restored from __doc__
        """ is_first_of_month(self) -> bool """
        return False

    def is_last_of_month(self): # real signature unknown; restored from __doc__
        """ is_last_of_month(self) -> bool """
        return False

    def is_leap_year(self, year): # real signature unknown; restored from __doc__
        """ is_leap_year(year:int) -> bool """
        return False

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> GLib.Date """
        pass

    @classmethod
    def new_dmy(cls, day, month, year): # real signature unknown; restored from __doc__
        """ new_dmy(day:int, month:GLib.DateMonth, year:int) -> GLib.Date """
        pass

    @classmethod
    def new_julian(cls, julian_day): # real signature unknown; restored from __doc__
        """ new_julian(julian_day:int) -> GLib.Date """
        pass

    def order(self, date2): # real signature unknown; restored from __doc__
        """ order(self, date2:GLib.Date) """
        pass

    def set_day(self, day): # real signature unknown; restored from __doc__
        """ set_day(self, day:int) """
        pass

    def set_dmy(self, day, month, y): # real signature unknown; restored from __doc__
        """ set_dmy(self, day:int, month:GLib.DateMonth, y:int) """
        pass

    def set_julian(self, julian_date): # real signature unknown; restored from __doc__
        """ set_julian(self, julian_date:int) """
        pass

    def set_month(self, month): # real signature unknown; restored from __doc__
        """ set_month(self, month:GLib.DateMonth) """
        pass

    def set_parse(self, p_str): # real signature unknown; restored from __doc__
        """ set_parse(self, str:str) """
        pass

    def set_time(self, time_): # real signature unknown; restored from __doc__
        """ set_time(self, time_:int) """
        pass

    def set_time_t(self, timet): # real signature unknown; restored from __doc__
        """ set_time_t(self, timet:int) """
        pass

    def set_time_val(self, timeval): # real signature unknown; restored from __doc__
        """ set_time_val(self, timeval:GLib.TimeVal) """
        pass

    def set_year(self, year): # real signature unknown; restored from __doc__
        """ set_year(self, year:int) """
        pass

    def strftime(self, s, slen, format, date): # real signature unknown; restored from __doc__
        """ strftime(s:str, slen:int, format:str, date:GLib.Date) -> int """
        return 0

    def subtract_days(self, n_days): # real signature unknown; restored from __doc__
        """ subtract_days(self, n_days:int) """
        pass

    def subtract_months(self, n_months): # real signature unknown; restored from __doc__
        """ subtract_months(self, n_months:int) """
        pass

    def subtract_years(self, n_years): # real signature unknown; restored from __doc__
        """ subtract_years(self, n_years:int) """
        pass

    def to_struct_tm(self, tm): # real signature unknown; restored from __doc__
        """ to_struct_tm(self, tm) """
        pass

    def valid(self): # real signature unknown; restored from __doc__
        """ valid(self) -> bool """
        return False

    def valid_day(self, day): # real signature unknown; restored from __doc__
        """ valid_day(day:int) -> bool """
        return False

    def valid_dmy(self, day, month, year): # real signature unknown; restored from __doc__
        """ valid_dmy(day:int, month:GLib.DateMonth, year:int) -> bool """
        return False

    def valid_julian(self, julian_date): # real signature unknown; restored from __doc__
        """ valid_julian(julian_date:int) -> bool """
        return False

    def valid_month(self, month): # real signature unknown; restored from __doc__
        """ valid_month(month:GLib.DateMonth) -> bool """
        return False

    def valid_weekday(self, weekday): # real signature unknown; restored from __doc__
        """ valid_weekday(weekday:GLib.DateWeekday) -> bool """
        return False

    def valid_year(self, year): # real signature unknown; restored from __doc__
        """ valid_year(year:int) -> bool """
        return False

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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new() -> GLib.Date """
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

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dmy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    julian = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    julian_days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Date), '__module__': 'gi.repository.GLib', '__gtype__': <GType GDate (2640519456)>, '__dict__': <attribute '__dict__' of 'Date' objects>, '__weakref__': <attribute '__weakref__' of 'Date' objects>, '__doc__': None, 'julian_days': <property object at 0x0000018e9ff884a0>, 'julian': <property object at 0x0000018e9ff883b0>, 'dmy': <property object at 0x0000018e9ff88630>, 'day': <property object at 0x0000018e9ff88720>, 'month': <property object at 0x0000018e9ff88810>, 'year': <property object at 0x0000018e9ff88900>, 'new': <classmethod(gi.FunctionInfo(new))>, 'new_dmy': <classmethod(gi.FunctionInfo(new_dmy))>, 'new_julian': <classmethod(gi.FunctionInfo(new_julian))>, 'add_days': gi.FunctionInfo(add_days), 'add_months': gi.FunctionInfo(add_months), 'add_years': gi.FunctionInfo(add_years), 'clamp': gi.FunctionInfo(clamp), 'clear': gi.FunctionInfo(clear), 'compare': gi.FunctionInfo(compare), 'copy': gi.FunctionInfo(copy), 'days_between': gi.FunctionInfo(days_between), 'free': gi.FunctionInfo(free), 'get_day': gi.FunctionInfo(get_day), 'get_day_of_year': gi.FunctionInfo(get_day_of_year), 'get_iso8601_week_of_year': gi.FunctionInfo(get_iso8601_week_of_year), 'get_julian': gi.FunctionInfo(get_julian), 'get_monday_week_of_year': gi.FunctionInfo(get_monday_week_of_year), 'get_month': gi.FunctionInfo(get_month), 'get_sunday_week_of_year': gi.FunctionInfo(get_sunday_week_of_year), 'get_week_of_year': gi.FunctionInfo(get_week_of_year), 'get_weekday': gi.FunctionInfo(get_weekday), 'get_year': gi.FunctionInfo(get_year), 'is_first_of_month': gi.FunctionInfo(is_first_of_month), 'is_last_of_month': gi.FunctionInfo(is_last_of_month), 'order': gi.FunctionInfo(order), 'set_day': gi.FunctionInfo(set_day), 'set_dmy': gi.FunctionInfo(set_dmy), 'set_julian': gi.FunctionInfo(set_julian), 'set_month': gi.FunctionInfo(set_month), 'set_parse': gi.FunctionInfo(set_parse), 'set_time': gi.FunctionInfo(set_time), 'set_time_t': gi.FunctionInfo(set_time_t), 'set_time_val': gi.FunctionInfo(set_time_val), 'set_year': gi.FunctionInfo(set_year), 'subtract_days': gi.FunctionInfo(subtract_days), 'subtract_months': gi.FunctionInfo(subtract_months), 'subtract_years': gi.FunctionInfo(subtract_years), 'to_struct_tm': gi.FunctionInfo(to_struct_tm), 'valid': gi.FunctionInfo(valid), 'get_days_in_month': <staticmethod(gi.FunctionInfo(get_days_in_month))>, 'get_monday_weeks_in_year': <staticmethod(gi.FunctionInfo(get_monday_weeks_in_year))>, 'get_sunday_weeks_in_year': <staticmethod(gi.FunctionInfo(get_sunday_weeks_in_year))>, 'get_weeks_in_year': <staticmethod(gi.FunctionInfo(get_weeks_in_year))>, 'is_leap_year': <staticmethod(gi.FunctionInfo(is_leap_year))>, 'strftime': <staticmethod(gi.FunctionInfo(strftime))>, 'valid_day': <staticmethod(gi.FunctionInfo(valid_day))>, 'valid_dmy': <staticmethod(gi.FunctionInfo(valid_dmy))>, 'valid_julian': <staticmethod(gi.FunctionInfo(valid_julian))>, 'valid_month': <staticmethod(gi.FunctionInfo(valid_month))>, 'valid_weekday': <staticmethod(gi.FunctionInfo(valid_weekday))>, 'valid_year': <staticmethod(gi.FunctionInfo(valid_year))>, '__new__': <staticmethod(gi.FunctionInfo(new))>, '__init__': <function nothing at 0x0000018e9fdc1010>})"
    __gtype__ = None # (!) real value is '<GType GDate (2640519456)>'
    __info__ = StructInfo(Date)


