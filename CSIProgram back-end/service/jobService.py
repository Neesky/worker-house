from dao import jobDao
from model.classModel import Job
from const import CODE_FAILURE, CODE_SUCCESSED, MESSAGE_APPEND_FAILURE, MESSAGE_APPEND_SUCCESSED, MESSAGE_DELETE_FAILURE, MESSAGE_DELETE_SUCCESSED, MESSAGE_FAILURE, MESSAGE_FLUSH_SUCCESSED, MESSAGE_JOB_DELETE_FAILURE, MESSAGE_SUCCESSED, MESSAGE_UPDATE_FAILURE, MESSAGE_UPDATE_SUCCESSED
from fastapi.responses import JSONResponse


def getAllJobService():
    jobResult = jobDao.getAllJob()
    return JSONResponse(
        content={
            'code': CODE_SUCCESSED,
            'message': MESSAGE_FLUSH_SUCCESSED,
            'data': jobResult
        }
    )

def changeJobService(job):
    jobToChange = jobDao.searchJob(job)
    print(jobToChange)
    #获得ID 
    code = CODE_FAILURE
    message = MESSAGE_UPDATE_FAILURE
    if(jobToChange):
        c = 1
    else:
        return JSONResponse(content={'code': CODE_FAILURE,'message': MESSAGE_UPDATE_FAILURE,'data': False})
    ID = jobToChange[0]["jobId"]
    job.jobId = ID
    job.jobName = job.jobNewName
    job.jobNewName = None
    jobResult = jobDao.changeJob(job)
    code = CODE_SUCCESSED
    message = MESSAGE_UPDATE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': jobResult
        }
    )

def deleteJobService(job):
    jobResult = jobDao.deleteJob(job)
    code = CODE_FAILURE
    message = MESSAGE_JOB_DELETE_FAILURE
    if(jobResult):
        code = CODE_SUCCESSED
        message = MESSAGE_DELETE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': jobResult
        }
    )

def searchJobService(job):
    jobResult = jobDao.searchJob(job)
    code = CODE_FAILURE
    message = MESSAGE_FAILURE
    if(jobResult):
        code = CODE_SUCCESSED
        message = MESSAGE_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': jobResult
        }
    )


def appendJobService(job):
    jobResult = jobDao.appendJob(job)
    code = CODE_FAILURE
    message = MESSAGE_APPEND_FAILURE
    if(jobResult):
        code = CODE_SUCCESSED
        message = MESSAGE_APPEND_SUCCESSED
    return JSONResponse(
        content={
            'code': code,
            'message': message,
            'data': jobResult
        }
    )

