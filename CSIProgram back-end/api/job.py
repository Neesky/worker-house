from fastapi.param_functions import Header
from starlette.responses import JSONResponse
from toke import checkToken
from fastapi import APIRouter
from model import classModel
from service import jobService

#创建路由
router = APIRouter()

@router.get("/getAll",tags=["job"])#tag的内容目前不清楚
async def getAllJob(token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return jobService.getAllJobService()

@router.post("/change",tags=["job"])
async def changeJob(job:classModel.Job,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return jobService.changeJobService(job)

@router.post("/delete",tags=["job"])
async def deleteJob(job:classModel.Job,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return jobService.deleteJobService(job)

@router.post("/search",tags=["job"])
async def searchJob(job:classModel.Job,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return jobService.searchJobService(job)

@router.post("/append",tags=["job"])
async def appendJob(job:classModel.Job,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return jobService.appendJobService(job)