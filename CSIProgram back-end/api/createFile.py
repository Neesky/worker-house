from const import MESSAGE_FAILURE
from toke import checkToken
from fastapi.param_functions import Header
from service.documentaryService import appendDocumentaryService
from service.departmentService import appendDepartmentService
from fastapi import APIRouter
from model import classModel

from typing import List
from starlette.requests import Request
from fastapi import FastAPI, Form, File, UploadFile
from starlette.templating import Jinja2Templates
#创建路由
router = APIRouter()
from service import employeeService
from model import classModel

templates = Jinja2Templates(directory="userFile")

@router.post("/upload")
async def files(file: UploadFile = File(...),initiatorName : str = Form(...), departmentName: str = Form(...), token:str = Header(None)):
        print(departmentName)
        tokenResult = checkToken(token)
        if(tokenResult[0] == 202):
            return False
        contents = await file.read()
        with open("./userFile/" + file.filename, "wb") as f:
            f.write(contents)  # 将写入文件路径存入数据库
        result = appendDocumentaryService("./userFile/"+file.filename,file.filename,initiatorName,departmentName)
        print(result)
        return result

@router.get("/")
async def main(request: Request):
    return templates.TemplateResponse('post.html', {'request': request})

