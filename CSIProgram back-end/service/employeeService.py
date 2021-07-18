from dao import employeeDao
from model.classModel import Employee
from const import CODE_FAILURE, CODE_SUCCESSED, MESSAGE_APPEND_FAILURE, MESSAGE_APPEND_SUCCESSED, MESSAGE_DELETE_FAILURE
from const import MESSAGE_FAILURE, MESSAGE_FLUSH_SUCCESSED, MESSAGE_DELETE_SUCCESSED
from const import MESSAGE_SUCCESSED, MESSAGE_UPDATE_FAILURE, MESSAGE_UPDATE_SUCCESSED
from fastapi.responses import JSONResponse

import hashlib

def getAllEmployeeService():
    employeeResult = employeeDao.getAllEmployee()
    print(employeeResult)
    return JSONResponse(
        content={
            'code': CODE_SUCCESSED,
            'message': MESSAGE_FLUSH_SUCCESSED,
            'data': employeeResult
        }
    )

def getMyDataService(employee):
    employeeResult = employeeDao.getMyData(employee)
    code = CODE_FAILURE
    message = MESSAGE_FAILURE
    if(employeeResult):
        code = CODE_SUCCESSED
        message = MESSAGE_SUCCESSED
        employeeResult = employeeResult[0]
    else:
        employeeResult = {}
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': employeeResult
        }
    )

    



def changeEmployeeService(employee):
    employeeResult = employeeDao.changeEmployee(employee)
    code = CODE_FAILURE
    message = MESSAGE_UPDATE_FAILURE
    if(employeeResult):
        code = CODE_SUCCESSED
        message = MESSAGE_UPDATE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': employeeResult
        }
    )

def deleteEmployeeService(employee):
    employeeResult = employeeDao.deleteEmployee(employee)
    code = CODE_FAILURE
    message = MESSAGE_DELETE_FAILURE
    if(employeeResult):
        code = CODE_SUCCESSED
        message = MESSAGE_DELETE_SUCCESSED
    return JSONResponse(
        content={
            'code':code,
            'message': message,
            'data': employeeResult
        }
    )

def searchEmployeeService(employee):
    employeeResult = employeeDao.searchEmployee(employee)
    code = CODE_FAILURE
    message = MESSAGE_FAILURE
    print(employeeResult)
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

def appendEmployeeService(employee):
    code = CODE_FAILURE
    message = MESSAGE_APPEND_FAILURE
    h1 = hashlib.md5()
    print(employee)
    h1.update(employee.password.encode(encoding='utf-8'))
    employee.password = h1.hexdigest()
    employeeResult = employeeDao.appendEmployee(employee)
    print(employeeResult)
    if(employeeResult):
        code = CODE_SUCCESSED
        message = MESSAGE_APPEND_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': employeeResult
        }
    )
