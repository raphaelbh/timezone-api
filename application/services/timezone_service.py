import pytz

def timezones(): 
    return pytz.all_timezones

def convert_datetime(datetime, timezone):

    if (timezone != None and timezone not in pytz.all_timezones):
        raise Exception('Invalid timezone')

    result = {}
    utc_datetime = __convert_datetime(datetime, 'UTC')
    result['UTC'] = __format_datetime(utc_datetime)

    if (timezone != None):
        utc_datetime = __convert_datetime(datetime, timezone)
        result[timezone] = __format_datetime(utc_datetime)

    return result

def __convert_datetime(datetime, zone):
    timezone = pytz.timezone(zone)
    return datetime.astimezone(timezone)

def __format_datetime(datetime): 
    return datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z')