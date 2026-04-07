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


class DateTime(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(tz:GLib.TimeZone, year:int, month:int, day:int, hour:int, minute:int, seconds:float) -> GLib.DateTime or None
        new_from_iso8601(text:str, default_tz:GLib.TimeZone=None) -> GLib.DateTime or None
        new_from_timeval_local(tv:GLib.TimeVal) -> GLib.DateTime or None
        new_from_timeval_utc(tv:GLib.TimeVal) -> GLib.DateTime or None
        new_from_unix_local(t:int) -> GLib.DateTime or None
        new_from_unix_local_usec(usecs:int) -> GLib.DateTime or None
        new_from_unix_utc(t:int) -> GLib.DateTime or None
        new_from_unix_utc_usec(usecs:int) -> GLib.DateTime or None
        new_local(year:int, month:int, day:int, hour:int, minute:int, seconds:float) -> GLib.DateTime or None
        new_now(tz:GLib.TimeZone) -> GLib.DateTime or None
        new_now_local() -> GLib.DateTime or None
        new_now_utc() -> GLib.DateTime or None
        new_utc(year:int, month:int, day:int, hour:int, minute:int, seconds:float) -> GLib.DateTime or None
    """
    def add(self, timespan): # real signature unknown; restored from __doc__
        """ add(self, timespan:int) -> GLib.DateTime or None """
        pass

    def add_days(self, days): # real signature unknown; restored from __doc__
        """ add_days(self, days:int) -> GLib.DateTime or None """
        pass

    def add_full(self, years, months, days, hours, minutes, seconds): # real signature unknown; restored from __doc__
        """ add_full(self, years:int, months:int, days:int, hours:int, minutes:int, seconds:float) -> GLib.DateTime or None """
        pass

    def add_hours(self, hours): # real signature unknown; restored from __doc__
        """ add_hours(self, hours:int) -> GLib.DateTime or None """
        pass

    def add_minutes(self, minutes): # real signature unknown; restored from __doc__
        """ add_minutes(self, minutes:int) -> GLib.DateTime or None """
        pass

    def add_months(self, months): # real signature unknown; restored from __doc__
        """ add_months(self, months:int) -> GLib.DateTime or None """
        pass

    def add_seconds(self, seconds): # real signature unknown; restored from __doc__
        """ add_seconds(self, seconds:float) -> GLib.DateTime or None """
        pass

    def add_weeks(self, weeks): # real signature unknown; restored from __doc__
        """ add_weeks(self, weeks:int) -> GLib.DateTime or None """
        pass

    def add_years(self, years): # real signature unknown; restored from __doc__
        """ add_years(self, years:int) -> GLib.DateTime or None """
        pass

    def compare(self, dt2): # real signature unknown; restored from __doc__
        """ compare(self, dt2:GLib.DateTime) -> int """
        return 0

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def difference(self, begin): # real signature unknown; restored from __doc__
        """ difference(self, begin:GLib.DateTime) -> int """
        return 0

    def equal(self, dt2): # real signature unknown; restored from __doc__
        """ equal(self, dt2:GLib.DateTime) -> bool """
        return False

    def format(self, format): # real signature unknown; restored from __doc__
        """ format(self, format:str) -> str or None """
        return ""

    def format_iso8601(self): # real signature unknown; restored from __doc__
        """ format_iso8601(self) -> str or None """
        return ""

    def get_day_of_month(self): # real signature unknown; restored from __doc__
        """ get_day_of_month(self) -> int """
        return 0

    def get_day_of_week(self): # real signature unknown; restored from __doc__
        """ get_day_of_week(self) -> int """
        return 0

    def get_day_of_year(self): # real signature unknown; restored from __doc__
        """ get_day_of_year(self) -> int """
        return 0

    def get_hour(self): # real signature unknown; restored from __doc__
        """ get_hour(self) -> int """
        return 0

    def get_microsecond(self): # real signature unknown; restored from __doc__
        """ get_microsecond(self) -> int """
        return 0

    def get_minute(self): # real signature unknown; restored from __doc__
        """ get_minute(self) -> int """
        return 0

    def get_month(self): # real signature unknown; restored from __doc__
        """ get_month(self) -> int """
        return 0

    def get_second(self): # real signature unknown; restored from __doc__
        """ get_second(self) -> int """
        return 0

    def get_seconds(self): # real signature unknown; restored from __doc__
        """ get_seconds(self) -> float """
        return 0.0

    def get_timezone(self): # real signature unknown; restored from __doc__
        """ get_timezone(self) -> GLib.TimeZone """
        pass

    def get_timezone_abbreviation(self): # real signature unknown; restored from __doc__
        """ get_timezone_abbreviation(self) -> str """
        return ""

    def get_utc_offset(self): # real signature unknown; restored from __doc__
        """ get_utc_offset(self) -> int """
        return 0

    def get_week_numbering_year(self): # real signature unknown; restored from __doc__
        """ get_week_numbering_year(self) -> int """
        return 0

    def get_week_of_year(self): # real signature unknown; restored from __doc__
        """ get_week_of_year(self) -> int """
        return 0

    def get_year(self): # real signature unknown; restored from __doc__
        """ get_year(self) -> int """
        return 0

    def get_ymd(self): # real signature unknown; restored from __doc__
        """ get_ymd(self) -> year:int, month:int, day:int """
        pass

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def is_daylight_savings(self): # real signature unknown; restored from __doc__
        """ is_daylight_savings(self) -> bool """
        return False

    @classmethod
    def new(cls, tz, year, month, day, hour, minute, seconds): # real signature unknown; restored from __doc__
        """ new(tz:GLib.TimeZone, year:int, month:int, day:int, hour:int, minute:int, seconds:float) -> GLib.DateTime or None """
        pass

    @classmethod
    def new_from_iso8601(cls, text, default_tz=None): # real signature unknown; restored from __doc__
        """ new_from_iso8601(text:str, default_tz:GLib.TimeZone=None) -> GLib.DateTime or None """
        pass

    @classmethod
    def new_from_timeval_local(cls, tv): # real signature unknown; restored from __doc__
        """ new_from_timeval_local(tv:GLib.TimeVal) -> GLib.DateTime or None """
        pass

    @classmethod
    def new_from_timeval_utc(cls, tv): # real signature unknown; restored from __doc__
        """ new_from_timeval_utc(tv:GLib.TimeVal) -> GLib.DateTime or None """
        pass

    @classmethod
    def new_from_unix_local(cls, t): # real signature unknown; restored from __doc__
        """ new_from_unix_local(t:int) -> GLib.DateTime or None """
        pass

    @classmethod
    def new_from_unix_local_usec(cls, usecs): # real signature unknown; restored from __doc__
        """ new_from_unix_local_usec(usecs:int) -> GLib.DateTime or None """
        pass

    @classmethod
    def new_from_unix_utc(cls, t): # real signature unknown; restored from __doc__
        """ new_from_unix_utc(t:int) -> GLib.DateTime or None """
        pass

    @classmethod
    def new_from_unix_utc_usec(cls, usecs): # real signature unknown; restored from __doc__
        """ new_from_unix_utc_usec(usecs:int) -> GLib.DateTime or None """
        pass

    @classmethod
    def new_local(cls, year, month, day, hour, minute, seconds): # real signature unknown; restored from __doc__
        """ new_local(year:int, month:int, day:int, hour:int, minute:int, seconds:float) -> GLib.DateTime or None """
        pass

    @classmethod
    def new_now(cls, tz): # real signature unknown; restored from __doc__
        """ new_now(tz:GLib.TimeZone) -> GLib.DateTime or None """
        pass

    @classmethod
    def new_now_local(cls): # real signature unknown; restored from __doc__
        """ new_now_local() -> GLib.DateTime or None """
        pass

    @classmethod
    def new_now_utc(cls): # real signature unknown; restored from __doc__
        """ new_now_utc() -> GLib.DateTime or None """
        pass

    @classmethod
    def new_utc(cls, year, month, day, hour, minute, seconds): # real signature unknown; restored from __doc__
        """ new_utc(year:int, month:int, day:int, hour:int, minute:int, seconds:float) -> GLib.DateTime or None """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.DateTime """
        pass

    def to_local(self): # real signature unknown; restored from __doc__
        """ to_local(self) -> GLib.DateTime or None """
        pass

    def to_timeval(self, tv): # real signature unknown; restored from __doc__
        """ to_timeval(self, tv:GLib.TimeVal) -> bool """
        return False

    def to_timezone(self, tz): # real signature unknown; restored from __doc__
        """ to_timezone(self, tz:GLib.TimeZone) -> GLib.DateTime or None """
        pass

    def to_unix(self): # real signature unknown; restored from __doc__
        """ to_unix(self) -> int """
        return 0

    def to_unix_usec(self): # real signature unknown; restored from __doc__
        """ to_unix_usec(self) -> int """
        return 0

    def to_utc(self): # real signature unknown; restored from __doc__
        """ to_utc(self) -> GLib.DateTime or None """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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
        """ new(tz:GLib.TimeZone, year:int, month:int, day:int, hour:int, minute:int, seconds:float) -> GLib.DateTime or None """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DateTime), '__module__': 'gi.repository.GLib', '__gtype__': <GType GDateTime (2640518400)>, '__dict__': <attribute '__dict__' of 'DateTime' objects>, '__weakref__': <attribute '__weakref__' of 'DateTime' objects>, '__doc__': None, 'new': <classmethod(gi.FunctionInfo(new))>, 'new_from_iso8601': <classmethod(gi.FunctionInfo(new_from_iso8601))>, 'new_from_timeval_local': <classmethod(gi.FunctionInfo(new_from_timeval_local))>, 'new_from_timeval_utc': <classmethod(gi.FunctionInfo(new_from_timeval_utc))>, 'new_from_unix_local': <classmethod(gi.FunctionInfo(new_from_unix_local))>, 'new_from_unix_local_usec': <classmethod(gi.FunctionInfo(new_from_unix_local_usec))>, 'new_from_unix_utc': <classmethod(gi.FunctionInfo(new_from_unix_utc))>, 'new_from_unix_utc_usec': <classmethod(gi.FunctionInfo(new_from_unix_utc_usec))>, 'new_local': <classmethod(gi.FunctionInfo(new_local))>, 'new_now': <classmethod(gi.FunctionInfo(new_now))>, 'new_now_local': <classmethod(gi.FunctionInfo(new_now_local))>, 'new_now_utc': <classmethod(gi.FunctionInfo(new_now_utc))>, 'new_utc': <classmethod(gi.FunctionInfo(new_utc))>, 'add': gi.FunctionInfo(add), 'add_days': gi.FunctionInfo(add_days), 'add_full': gi.FunctionInfo(add_full), 'add_hours': gi.FunctionInfo(add_hours), 'add_minutes': gi.FunctionInfo(add_minutes), 'add_months': gi.FunctionInfo(add_months), 'add_seconds': gi.FunctionInfo(add_seconds), 'add_weeks': gi.FunctionInfo(add_weeks), 'add_years': gi.FunctionInfo(add_years), 'compare': gi.FunctionInfo(compare), 'difference': gi.FunctionInfo(difference), 'equal': gi.FunctionInfo(equal), 'format': gi.FunctionInfo(format), 'format_iso8601': gi.FunctionInfo(format_iso8601), 'get_day_of_month': gi.FunctionInfo(get_day_of_month), 'get_day_of_week': gi.FunctionInfo(get_day_of_week), 'get_day_of_year': gi.FunctionInfo(get_day_of_year), 'get_hour': gi.FunctionInfo(get_hour), 'get_microsecond': gi.FunctionInfo(get_microsecond), 'get_minute': gi.FunctionInfo(get_minute), 'get_month': gi.FunctionInfo(get_month), 'get_second': gi.FunctionInfo(get_second), 'get_seconds': gi.FunctionInfo(get_seconds), 'get_timezone': gi.FunctionInfo(get_timezone), 'get_timezone_abbreviation': gi.FunctionInfo(get_timezone_abbreviation), 'get_utc_offset': gi.FunctionInfo(get_utc_offset), 'get_week_numbering_year': gi.FunctionInfo(get_week_numbering_year), 'get_week_of_year': gi.FunctionInfo(get_week_of_year), 'get_year': gi.FunctionInfo(get_year), 'get_ymd': gi.FunctionInfo(get_ymd), 'hash': gi.FunctionInfo(hash), 'is_daylight_savings': gi.FunctionInfo(is_daylight_savings), 'ref': gi.FunctionInfo(ref), 'to_local': gi.FunctionInfo(to_local), 'to_timeval': gi.FunctionInfo(to_timeval), 'to_timezone': gi.FunctionInfo(to_timezone), 'to_unix': gi.FunctionInfo(to_unix), 'to_unix_usec': gi.FunctionInfo(to_unix_usec), 'to_utc': gi.FunctionInfo(to_utc), 'unref': gi.FunctionInfo(unref), '__new__': <staticmethod(gi.FunctionInfo(new))>, '__init__': <function nothing at 0x0000018e9fdc1010>})"
    __gtype__ = None # (!) real value is '<GType GDateTime (2640518400)>'
    __info__ = StructInfo(DateTime)


