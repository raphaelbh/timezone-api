from flask import Blueprint

from flask import request
from datetime import datetime

from commons import api_utils
from services import timezone_service

blueprint = Blueprint("api", __name__)

@blueprint.route('/timezones')
def timezones():
    return api_utils.response(200, timezone_service.timezones())

@blueprint.route('/now')
def now():
    try:
        tz = request.args.get("timezone", default=None, type=str)
        dt = timezone_service.convert_datetime(datetime.now(), tz)
        return api_utils.response(200, dt)
    except Exception:
        return api_utils.response(400, 'Invalid timezone informed')