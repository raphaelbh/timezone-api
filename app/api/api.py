import api.timezone as timezone
from datetime import datetime;
from flask import Blueprint, make_response

api = Blueprint("api", __name__)

@api.route('/timezones')
def timezones():
    return __response(200, timezone.timezones())

@api.route('/now')
def now():
    return __response(200, timezone.now())

def __headers():
    return {"Content-Type": "application/json"}

def __response_body(status_code, body):
    return {
        'status_code': status_code,
        'data': body,
        'timestamp': datetime.now().timestamp()
    }

def __response(status_code, body):
    response_body = __response_body(status_code, body)
    response = make_response(response_body, status_code)
    response.headers = __headers()
    return response
