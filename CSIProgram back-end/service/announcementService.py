from starlette.types import Message
from model.classModel import Department
from const import CODE_FAILURE, CODE_SUCCESSED, MESSAGE_APPEND_SUCCESSED, MESSAGE_DELETE_FAILURE, MESSAGE_DELETE_SUCCESSED, MESSAGE_DEPARTMENT_DELETE_FAILURE, MESSAGE_FAILURE, MESSAGE_FLUSH_SUCCESSED, MESSAGE_SUCCESSED, MESSAGE_UPDATE_FAILURE, MESSAGE_UPDATE_SUCCESSED
from fastapi.responses import JSONResponse
from datetime import datetime
from dao import announcementDao

def appendAnnouncementService(announcement):
    announcement.createDate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    announcementResult = announcementDao.appendAnnouncement(announcement)
    code = CODE_FAILURE
    message = MESSAGE_FAILURE
    if (announcementResult):
        code = CODE_SUCCESSED
        message = MESSAGE_APPEND_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': announcementResult
        }
    )

def deleteAnnouncementService(announcement):
    announcementResult = announcementDao.deleteAnnouncement(announcement)
    code = CODE_FAILURE
    message = MESSAGE_FAILURE
    if (announcementResult):
        code = CODE_SUCCESSED
        message = MESSAGE_DELETE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': announcementResult
        }
    )


def getAllAnnouncementService():
    announcementResult = announcementDao.getAllAnnouncement()
    code = CODE_SUCCESSED
    message = MESSAGE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': announcementResult
        }
    )

def searchAnnouncementWithEmployeeService(employee):
    announcementResult = announcementDao.searchAnnouncementWithEmployee(employee)
    code = CODE_FAILURE
    message = MESSAGE_FAILURE
    if (announcementResult):
        code = CODE_SUCCESSED
        message = MESSAGE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': announcementResult
        }
    )

def searchEmployeeWithAnnouncementService(announcement):
    announcementResult = announcementDao.searchEmployeeWithAnnouncement(announcement)
    code = CODE_FAILURE
    message = MESSAGE_FAILURE
    if (announcementResult):
        code = CODE_SUCCESSED
        message = MESSAGE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': announcementResult
        }
    )


def appendEmployeeWithAnnouncementService(id,title):
    departmentResult = announcementDao.appendEmployeeWithAnnouncement(id,title)
    code = CODE_FAILURE
    message = MESSAGE_FAILURE
    if (departmentResult):
        code = CODE_SUCCESSED
        message = MESSAGE_APPEND_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': departmentResult
        }
    )

def searchUnreadAnnouncementWithEmployeeService(employee):
    allAnnouncementResult = announcementDao.getAllAnnouncement()
    readAnnouncementResult = announcementDao.searchAnnouncementWithEmployee(employee)
    print(allAnnouncementResult)
    print(readAnnouncementResult)
    re = []
    for j in range(len(allAnnouncementResult)):
        flag = 0
        for i in range(len(readAnnouncementResult)):
            if(allAnnouncementResult[j]['title'] == readAnnouncementResult[i]['title']):
                flag = 1
        if(flag==0):
            re.append(allAnnouncementResult[j])
    code = CODE_FAILURE
    message = MESSAGE_FAILURE
    print(re)
    if (allAnnouncementResult):
        code = CODE_SUCCESSED
        message = MESSAGE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': re
        }
    )