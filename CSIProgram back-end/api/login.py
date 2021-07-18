from starlette.responses import JSONResponse
from toke import checkToken
from fastapi import APIRouter
from fastapi.param_functions import Header

#构建路由
router = APIRouter()

from service import loginService
from model import classModel
import hashlib


@router.post("/",tags=["login"])
async def loginWithPassword(employee:classModel.Employee):
    '''
    登录
    '''
    h1 = hashlib.md5()
    h1.update(employee.password.encode(encoding='utf-8'))
    employee.password = h1.hexdigest()
    return loginService.checkPasswordandIdService(employee)

@router.post("/changePassword",tags=["login"])
async def loginWithPassword(idWithPassword:classModel.IdWithPassword, token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    print(idWithPassword)
    h1 = hashlib.md5()
    h1.update(idWithPassword.password.encode(encoding='utf-8'))
    idWithPassword.password = h1.hexdigest()
    return loginService.changePasswordService(idWithPassword)

@router.post("/logout",tags=["login"])
async def logout(employee:classModel.Employee,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return loginService.logoutService(employee)

