import jwt
import time
from model.classModel import Employee

lasttime = 24*60*60
codetype = 'HS256'
mixtype = 'NeeskyLF66'
# 使用 sanic 作为restful api 框架
def getToken(employee):
    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + lasttime,
        "id": employee.id,
    }
    token = jwt.encode(payload, mixtype, algorithm=codetype)
    return token


def checkToken(token):
    #  如果在生成token的时候使用了aud参数，那么校验的时候也需要添加此参数
    payload = None
    try:
        payload = jwt.decode(token, mixtype, algorithms=[codetype])
    except Exception as e:
        if str(e)=="Signature has expired":
            return 202,"身份过期",token
        else :
            return 202,"身份认证错误",token
    if payload:
        return 200,"成功", token
    return 202,"身份认证错误", token