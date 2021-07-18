from time import time
from starlette.types import Message
from toke import getToken
from const import CODE_FAILURE, CODE_SUCCESSED, MESSAGE_FAILURE, MESSAGE_LOGIN_FAILURE, MESSAGE_LOGIN_SUCCESSED, MESSAGE_SUCCESSED
from model.classModel import Employee
from dao import loginDao
from fastapi.responses import JSONResponse

def checkPasswordandIdService(employee:Employee):
    employeeResult = loginDao.searchPasswordById(employee)
    code = CODE_FAILURE
    message = MESSAGE_LOGIN_FAILURE
    data = ["2","NULL","NULL"]

    print(employee.oaid)
    if(employeeResult):
        employeeResult = employeeResult[0]
    else:
        return JSONResponse(content={'code': code,'message': message,'data': data})
    data[2] = employeeResult["loginErrorCount"]
    if(employee.oaid != employeeResult["oaid"]):
        if(employeeResult["mode"] == "1"):
            return JSONResponse(content={'code':code,'message': " 账号已在别处登录",'data': data})
    if(employeeResult["loginErrorCount"] > 5 and int(time())-employeeResult["loginErrorTime"] < 60): #读取时间相减，在add逻辑判断后。
        return JSONResponse(content={'code':code,'message': "登录超限，请稍后尝试",'data': data})
    elif (employeeResult["loginErrorTime"] <= 5 and int(time()) - employeeResult["loginErrorTime"] > 60):
        employee.loginErrorTime = int(time())
        loginDao.loginErrorCountUpdateSetOne(employee)
    #登录成功返回token
    token = getToken(employee)
    if(employeeResult["password"] == employee.password):
        code = CODE_SUCCESSED
        message = MESSAGE_LOGIN_SUCCESSED
        data[0],data[1] = employeeResult["status"],token
        loginDao.loginUpdate(employee)
        return JSONResponse(content={'code': code,'message': message,'data': data })
    else:
        loginDao.loginErrorCountUpdateAddOne(employee)
        if(employeeResult["loginErrorCount"] == 5):
            employee.loginErrorTime = int(time())
            loginDao.loginErrorTimeUpdate(employee)
            return JSONResponse(content={'code':code,'message': "登录超限，请在1分钟后尝试",'data': data})
        return JSONResponse(content={'code': CODE_FAILURE,'message': MESSAGE_LOGIN_FAILURE,'data': ["2",data[1],data[2]+1]})
    

def changePasswordService(idWithPassword):
    employeeResult = loginDao.changePassword(idWithPassword)
    code = CODE_FAILURE
    message = MESSAGE_FAILURE
    if(employeeResult):
        code = CODE_SUCCESSED
        message = MESSAGE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': employeeResult
        }
    )

def logoutService(employee):
    employeeResult = loginDao.logoutUpdate(employee)
    code = CODE_FAILURE
    message = MESSAGE_FAILURE
    if(employeeResult):
        code = CODE_SUCCESSED
        message = MESSAGE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': employeeResult
        }
    )
