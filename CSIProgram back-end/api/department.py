from starlette.responses import JSONResponse
from toke import checkToken
from fastapi.param_functions import Header
from pydantic.types import NoneBytes
from service import departmentService
from fastapi import APIRouter
from model import classModel

#创建路由
router = APIRouter()

@router.get("/getAll",tags=["department"])#tag的内容目前不清楚
async def getAllDepartment(token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return departmentService.getAllDepartmentService()

@router.post("/change",tags=["department"])
async def changeDepartment(department:classModel.Department,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    print(department)
    return departmentService.changeDepartmentService(department)

@router.post("/delete",tags=["department"])
async def deleteDepartment(department:classModel.Department,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return departmentService.deleteDepartmentService(department)

@router.post("/search",tags=["department"])
async def searchDepartment(department:classModel.Department,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return departmentService.searchDepartmentService(department)

@router.post("/append",tags=["department"])
async def appendDepartment(department:classModel.Department,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return departmentService.appendDepartmentService(department)