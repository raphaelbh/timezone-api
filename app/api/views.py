from flask import request
from datetime import datetime
from timezone import timezone
from commons import api_utils
from . import api_blueprint as api

@api.route('/timezones')
def timezones():
    return api_utils.response(200, timezone.timezones())

@api.route('/now')
def now():
    try:
        tz = request.args.get("timezone", default=None, type=str)
        dt = timezone.convert_datetime(datetime.now(), tz)
        return api_utils.response(200, dt)
    except Exception:
        return api_utils.response(400, 'Invalid timezone informed')

    