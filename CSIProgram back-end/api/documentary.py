from toke import checkToken
from fastapi.param_functions import Header
from fastapi.responses import JSONResponse
from const import CODE_SUCCESSED, DATABASE_LOCATION_AND_PORT, MESSAGE_SUCCESSED
from starlette.responses import FileResponse
from service import documentaryService
from fastapi import APIRouter
from model import classModel

#创建路由
router = APIRouter()

@router.post("/delete",tags=["documentary"])
async def deleteDocumentary(documentary:classModel.Documentary,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return documentaryService.deleteDocumentaryService(documentary)

@router.post("/download",tags=["documentary"])
async def downloadDocumentary(documentary:classModel.Documentary,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return JSONResponse(
        content={
            'code': CODE_SUCCESSED,
            'message': MESSAGE_SUCCESSED,
            'data':DATABASE_LOCATION_AND_PORT+"/userFile/"+documentary.title
        }
        #以后检查选择那个文件夹
    )   

@router.get("/getAll",tags=["documentary"])
async def deleteDocumentary(token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    
    return documentaryService.getAllDocumentaryService()

@router.post("/searchByTitle",tags=["documentary"])
async def searchDocumentary(documentary:classModel.Documentary,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return documentaryService.searchDocumentaryByTitleService(documentary)

