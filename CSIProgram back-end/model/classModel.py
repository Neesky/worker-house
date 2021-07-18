from pydantic import BaseModel
from time import time


class IdWithPassword(BaseModel):
    id:str = "%"
    password:str = "%"
    class Config:
        schema_extra = {
            "example": {
                "id": "114514",
                "password": "1919810"
            }
        }
    
#本文件内，所有class的成员变量id均为主键
class Employee(BaseModel):
    
    id:str = None #成员id
    password:str = None #密码
    departmentName:str = "%" #部门名字
    departmentRemark:str = None #部门信息
    jobName:str = "%" #职位名字

    jobRemark:str = None #职业信息
    name:str = "%" #Employee.name员工名字
    cardId:str = "%" #身份证
    address:str = None #住址
    postCode:str = None #邮编

    tel:str = None #电话
    phone:str = "%" #手机
    QQNumber:str = None #qq号
    email:str = None #电子邮件
    sex:str = "%" # 1表示男，2表示女

    party:str = None #政治身份
    birthday:str = None #出生日期
    race:str = None #民族
    education:str = None #学历
    speciality:str = None #专业

    hobby:str = None #特长
    remark:str = None #员工备注
    createDate:str = None #创造日期
    status:str = None #1表示管理员，2表示员工
    oaid:str  = None 
    mode:str = "0" #0为未登录，1为登录

    loginErrorCount:int = 0
    loginErrorTime:int = None

    class Config:
        schema_extra = {
            "example": {
                "id":"20194100", #成员id
                "password":"str",  #密码
                "departmentName":"str" ,#部门名字
                "departmentRemark":"str",#部门信息
                "jobName":"str", #职位名字

                "jobRemark":"str",#职业信息
                "name":"str" ,#Employee.name员工名字
                "cardId":"str" ,#身份证
                "address":"str", #住址
                "postCode":"str" ,#邮编

                "tel":"str", #电话
                "phone":"str", #手机
                "QQNumber":"str" ,#qq号
                "email":"str", #电子邮件
                "sex":"str",# 1表示男，2表示女

                "party":"str", #政治身份
                "birthday":"str", #出生日期
                "race":"str", #民族
                "education":"str", #学历
                "speciality":"str", #专业

                "hobby":"str", #特长
                "remark":"str" ,#员工备注
                "createDate":"str", #创造日期
                "status":"str", #1表示管理员，2表示员工
            }
        }
    
class Job(BaseModel):
    jobId:str = None
    jobName:str #Job.name为职业名字
    jobNewName:str = None
    jobRemark:str = None #职业说明

    class Config:
        schema_extra = {
            "example": {
                "jobName": "str",
                "jobNewName": "清洁工",
                "jobRemark": "刷地板"
            }
        }
    
class Announcement(BaseModel):
    title:str
    initiatorName:str = None
    createDate:str = None
    content:str = None
    
    class Config:
        schema_extra = {
            "example": {
                "title":"A title of an announcement",
                "initiatorName":"冮泓波",
                "createDate": "20210730",
                "content":"知らない"
            }
        }

class UserIdWithAnnouncement(BaseModel):
    id:str
    title:str


class Documentary(BaseModel):
    title: str = None  #标题
    initiatorName: str = None   #发布人
    createDate: str = None #创建时间
    url: str = None

class Department(BaseModel):
    departmentId:str = None
    departmentName:str
    departmentNewName:str = None
    departmentRemark:str = None

    class Config:
        schema_extra = {
            "example":{
                "departmentName":"str",
                "departmentNewName":"手艺部门",
                "departmentRemark":"精通手艺"
            }
        }
    
class Notice(BaseModel):
    id:str
    

#................下面的类没有投入使用.................

class Student(BaseModel):#继承BaseModel类
    Id: int
    Name: str
    Age:int
    #Config为输入案例，在http:/xxx.xxx.xxx.xxx:xxxxx/docs可访问
    class Config:
        schema_extra = {
            "example": {
                "Id": "1919810",
                "Name": "Senpai",
                "Age": 24,
            }
        }
