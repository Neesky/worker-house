import uvicorn
from fastapi import FastAPI
from api import createFile, department, documentary, employee, job, login, announcement
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()

#配置跨域
origins = ["*"]  

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"])  

# 注册api路由
app.include_router(login.router,prefix="/login")
app.include_router(employee.router,prefix="/employee")
app.include_router(department.router,prefix="/department")
app.include_router(job.router,prefix="/job")
app.include_router(createFile.router,prefix="/createFile")
app.include_router(announcement.router,prefix="/announcement")
app.include_router(documentary.router,prefix="/document")

app.mount("/userFile",StaticFiles(directory="./userFile"), name="static") 
if __name__ == '__main__':
    #执行主函数, 其IP端口
    uvicorn.run(app, host='0.0.0.0', port=23451)

 