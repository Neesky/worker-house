from starlette.responses import JSONResponse
from toke import checkToken
from fastapi import APIRouter
from fastapi.param_functions import Header

#构建路由
router = APIRouter()

from service import announcementService
from model import classModel

@router.post("/append",tags=["announcement"])
async def appendAnnouncement(announcement:classModel.Announcement,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 200):
        return announcementService.appendAnnouncementService(announcement)
    else:
        return JSONResponse(
            content={
            'code': tokenResult[0],
            'message': tokenResult[1],
            'data': tokenResult[2]
        }
    )

@router.post("/delete",tags=["announcement"])
async def deleteAnnouncement(announcement:classModel.Announcement,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 200):
        return announcementService.deleteAnnouncementService(announcement)
    else:
        return JSONResponse(
            content={
            'code': tokenResult[0],
            'message': tokenResult[1],
            'data': tokenResult[2]
        }
    )

@router.get("/getAll",tags=["announcement"])
async def getAllAnnouncement(token:str = Header(None)):
    print(token)
    tokenResult = checkToken(token)
    if(tokenResult[0] == 200):
        return announcementService.getAllAnnouncementService()
    else:
        return JSONResponse(
            content={
            'code': tokenResult[0],
            'message': tokenResult[1],
            'data': tokenResult[2]
        }
    )

@router.post("/searchAnnouncementWithEmployee",tags=["announcement"])
async def searchAnnouncementWithEmployee(employee:classModel.Employee,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 200):
        return announcementService.searchAnnouncementWithEmployeeService(employee)
    else:
        return JSONResponse(
            content={
            'code': tokenResult[0],
            'message': tokenResult[1],
            'data': tokenResult[2]
        }
    )
@router.post("/searchUnreadAnnouncementWithEmployee",tags=["announcement"])
async def searchUnreadAnnouncementWithEmployee(employee:classModel.Employee,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 200):
        return announcementService.searchUnreadAnnouncementWithEmployeeService(employee)
    else:
        return JSONResponse(
            content={
            'code': tokenResult[0],
            'message': tokenResult[1],
            'data': tokenResult[2]
        }
    )

@router.post("/searchEmployeeWithAnnouncement",tags=["announcement"])
async def searchEmployeeWithAnnouncement(announcement:classModel.Announcement,token:str = Header(None)):
    print(announcement)
    tokenResult = checkToken(token)
    if(tokenResult[0] == 200):
        return announcementService.searchEmployeeWithAnnouncementService(announcement)
    else:
        return JSONResponse(
            content={
            'code': tokenResult[0],
            'message': tokenResult[1],
            'data': tokenResult[2]
        }
    )

@router.post("/appendEmployeeWithAnnouncement",tags=["announcement"])
async def appendEmployeeWithAnnouncement(userIdWithAnnouncement:classModel.UserIdWithAnnouncement,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 200):
        return announcementService.appendEmployeeWithAnnouncementService(userIdWithAnnouncement.id,userIdWithAnnouncement.title)
    else:
        return JSONResponse(
            content={
            'code': tokenResult[0],
            'message': tokenResult[1],
            'data': tokenResult[2]
        }
    )
