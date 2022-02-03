import pytz
from datetime import datetime;

def timezones(): 
    return pytz.all_timezones

def now():
    return datetime.now()