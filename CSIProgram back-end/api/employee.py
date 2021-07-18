from fastapi.param_functions import Header
from fastapi.responses import JSONResponse
from toke import checkToken
from fastapi import APIRouter
from model import classModel

#创建路由
router = APIRouter()
from service import employeeService
from model import classModel

@router.get("/getAll",tags=["employee"])
async def getAllEmployee(token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return employeeService.getAllEmployeeService()

@router.post("/change",tags=["employee"])
async def changeEmployee(employee:classModel.Employee,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return employeeService.changeEmployeeService(employee)

@router.post("/delete",tags=["employee"])
async def deleteEmployee(employee:classModel.Employee,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return employeeService.deleteEmployeeService(employee)

@router.post("/search",tags=["employee"])
async def searchEmployee(employee:classModel.Employee,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    if(employee.name == ''):
        employee.name = "%"
    if(employee.cardId == ''):
        employee.cardId = "%"
    if(employee.jobName == ''):
        employee.jobName = "%"
    if(employee.departmentName == ''):
        employee.departmentName = "%"
    if(employee.sex == '0'):
        employee.sex = "%"
    if(employee.phone == ''):
        employee.phone = "%"
    print(employee)
    return employeeService.searchEmployeeService(employee)

@router.post("/myId",tags=["employee"])
async def myId(employee:classModel.Employee,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return employeeService.getMyDataService(employee)

@router.post("/append",tags=["employee"])
async def appendEmployee(employee:classModel.Employee,token:str = Header(None)):
    tokenResult = checkToken(token)
    if(tokenResult[0] == 202):
        return JSONResponse(content={'code': tokenResult[0],'message': tokenResult[1],'data': tokenResult[2]})
    return employeeService.appendEmployeeService(employee)

#{"id": "20194056", "password": "123456", "departmentName": "挖矿部门", "departmentRemark": "天天挖矿", "jobName": "矿工", "jobRemark": "挥镐子", "name": "李放", "cardId": "500000200001010000", "address": "重庆沙坪坝", "postCode": "400000", "tel": "46464646", "phone": "13012345678", "QQNumber": "1313211", "email": "1313211@qq.com", "sex": "1", "party": "共青团员", "birthday": "20000101", "race": "汉族", "education": "本科", "speciality": "计算机科学与技术", "hobby": "摸鱼", "remark": "组长", "createDate": "20200101", "status": "1"}