from model.classModel import Department
from const import CODE_FAILURE, CODE_SUCCESSED, MESSAGE_APPEND_SUCCESSED, MESSAGE_DELETE_FAILURE, MESSAGE_DELETE_SUCCESSED, MESSAGE_DEPARTMENT_DELETE_FAILURE, MESSAGE_FAILURE, MESSAGE_FLUSH_SUCCESSED, MESSAGE_SUCCESSED, MESSAGE_UPDATE_FAILURE, MESSAGE_UPDATE_SUCCESSED
from fastapi.responses import JSONResponse
from dao import departmentDao, employeeDao

def getAllDepartmentService():
    departmentResult = departmentDao.getAllDepartment()
    print(departmentResult)
    return JSONResponse(
        content={
            'code': CODE_SUCCESSED,
            'message': MESSAGE_FLUSH_SUCCESSED,
            'data': departmentResult
        }
    )

def changeDepartmentService(department):
    departmentToChange = departmentDao.searchDepartment(department)
    #获得ID 
    code = CODE_FAILURE
    message = MESSAGE_UPDATE_FAILURE
    if(departmentToChange == None):#如果为空即返回
        return JSONResponse(content={'code': CODE_FAILURE,'message': MESSAGE_UPDATE_FAILURE,'data': False})
    ID = departmentToChange[0]["departmentId"]
    department.departmentId = ID
    department.departmentName = department.departmentNewName
    department.departmentNewName = None
    departmentResult = departmentDao.changeDepartment(department)
    code = CODE_SUCCESSED
    message = MESSAGE_UPDATE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': departmentResult
        }
    )

def deleteDepartmentService(department):
    departmentResult = departmentDao.deleteDepartment(department)
    code = CODE_FAILURE
    message = MESSAGE_DEPARTMENT_DELETE_FAILURE
    if(departmentResult):
        code = CODE_SUCCESSED
        message = MESSAGE_DELETE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': departmentResult
        }
    )

def searchDepartmentService(department):
    departmentResult = departmentDao.searchDepartment(department)
    code = CODE_FAILURE
    message = MESSAGE_FAILURE
    if(departmentResult):
        code = CODE_SUCCESSED
        message = MESSAGE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': departmentResult
        }
    )

def appendDepartmentService(department):
    departmentResult = departmentDao.appendDepartment(department)
    code = CODE_FAILURE
    message = MESSAGE_FAILURE
    if(departmentResult):
        code = CODE_SUCCESSED
        message = MESSAGE_APPEND_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': departmentResult
        }
    )
