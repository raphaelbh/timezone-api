from datetime import datetime;
from flask import make_response

def response(status_code, body):
    response_body = __response_body(status_code, body)
    response = make_response(response_body, status_code)
    response.headers = __headers()
    return response

def __headers():
    return {"Content-Type": "application/json"}

def __response_body(status_code, body):
    return {
        'status_code': status_code,
        'data': body,
        'timestamp': datetime.now().timestamp()
    }