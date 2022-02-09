import pytz

def timezones(): 
    return pytz.all_timezones

def convert_datetime(datetime, timezoneParam):

    if (timezoneParam != None and timezoneParam not in pytz.all_timezones):
        raise Exception('Invalid timezone')

    result = {}
    utc_datetime = __convert_datetime(datetime, 'UTC')
    result['UTC'] = _format_datetime(utc_datetime)

    if (timezoneParam != None):
        utc_datetime = __convert_datetime(datetime, timezoneParam)
        result[timezoneParam] = _format_datetime(utc_datetime)

    return result

def __convert_datetime(datetime, zone):
    timezone = pytz.timezone(zone)
    return datetime.astimezone(timezone)

def _format_datetime(datetime): 
    return datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z')