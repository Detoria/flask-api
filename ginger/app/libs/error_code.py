from app.libs.error import APIException


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006
