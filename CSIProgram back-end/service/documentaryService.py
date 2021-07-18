from dao import documentaryDao
from fastapi.responses import JSONResponse
from datetime import datetime
from const import *
import os

def getAllDocumentaryService():
    documentaryResult = documentaryDao.getAllDocumentary()
    print(documentaryResult)
    return JSONResponse(
        content={
            'code': CODE_SUCCESSED,
            'message': MESSAGE_FLUSH_SUCCESSED,
            'data': documentaryResult
        }
    )

def appendDocumentaryService(url,title,initiatorName,departmentName):
    createDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    documentaryResult = documentaryDao.appendDocumentary(url,title,initiatorName,departmentName,createDate)
    code = CODE_FAILURE
    message = MESSAGE_FAILURE
    if (documentaryResult):
        code = CODE_SUCCESSED
        message = MESSAGE_APPEND_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': documentaryResult
        }
    )


def searchDocumentaryByEmployeeService(employee):
    documentaryResult = documentaryDao.searchDocumentaryByEmployee(employee)
    code = CODE_FAILURE
    message = MESSAGE_FAILURE
    if (documentaryResult):
        code = CODE_SUCCESSED
        message = MESSAGE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': documentaryResult
        }
    )

def searchDocumentaryByTitleService(documentary):
    documentaryResult = documentaryDao.searchDocumentaryByTitle(documentary)
    code = CODE_SUCCESSED
    message = MESSAGE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': documentaryResult
        }
    )

def deleteDocumentaryService(documentary):
    documentaryResult = documentaryDao.deleteDocumentary(documentary)
    #此处BUG高发
    os.remove("./userFile/"+documentary.title)
    code = CODE_FAILURE
    message = MESSAGE_DEPARTMENT_DELETE_FAILURE
    if (documentaryResult):
        code = CODE_SUCCESSED
        message = MESSAGE_DELETE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': documentaryResult
        }
    )
