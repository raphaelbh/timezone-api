from datetime import datetime;
import timezone.timezone as timezone
from flask import Blueprint, make_response

api_blueprint = Blueprint("api_blueprint", __name__)

@api_blueprint.route('/timezones')
def timezones():
    return __response(200, timezone.timezones())

@api_blueprint.route('/now')
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
