from timezone import timezone
from commons import api_utils
from . import api_blueprint as api

@api.route('/timezones')
def timezones():
    return api_utils.response(200, timezone.timezones())

@api.route('/now')
def now():
    return api_utils.response(200, timezone.now())