#!/usr/bin/python3

from const import DATABASE_LOCATION, DATABASE_PORT
import pymysql

def connect_db(uname="root", pwd="elysium"):
    # 打开数据库连接
    db = pymysql.connect(host=DATABASE_LOCATION, user=uname, database="testdb",port=DATABASE_PORT)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor(pymysql.cursors.DictCursor)
    return db, cursor


def getAllJob():
    db, cursor = connect_db()
    sql = """select job.jobName,job.jobRemark from job"""

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        results = cursor.fetchall()
        # 获取数据
        db.commit()
        if results:
            print("存在")
        else:
            print("不存在")
        # 关闭数据库连接
        for row in results:
            print(row)

        db.close()
        return results
        # 关闭数据库连接

    except:

        print("Error: unable to fetch data")
        # 返回None

        # 关闭数据库连接
        db.close()


def searchJob(job):
    db, cursor = connect_db()
    tmp = "%"
    for i in range(len(job.jobName)):
        tmp = tmp + job.jobName[i] + "%"
    sql = """select job.jobId,job.jobName,job.jobRemark


        from job

        where job.jobName like '%s'
        """ % tmp

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        results = cursor.fetchall()
        # 获取数据
        db.commit()
        if results:
            print("存在")
        else:
            print("不存在")
        # 关闭数据库连接
        print(results)
        db.close()
        return results
        # 关闭数据库连接

    except:

        print("Error: unable to fetch data")
        # 返回None

        # 关闭数据库连接
        db.close()



def appendJob(job):
    db, cursor = connect_db()

    sql = '''
        select * from job where job.jobName = '%s'
        ''' % job.jobName
    cursor.execute(sql)
    db.commit()
    result = cursor.fetchall()
    if result:
        print("职位已经存在")
        db.close()
        return False

    sql = """INSERT INTO job(jobName,jobRemark)
                VALUES('%s','%s')""" % (job.jobName, job.jobRemark)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("插入成功")
        # 关闭数据库连接
        db.close()
        return True

    except:
        # 如果发生错误则回滚
        # Id是主键，不能插入相同Id
        db.rollback()
        print("插入失败")
        # 关闭数据库连接
        db.close()
        return False


def changeJob(job):
    db, cursor = connect_db()
    sql = '''
            select * from job where job.jobName = '%s'
            ''' % job.jobName
    cursor.execute(sql)
    db.commit()
    result = cursor.fetchall()
    if result and result[0]['jobId'] != job.jobId:
        print("职位已经存在")
        db.close()
        return False

    sql = "UPDATE job SET jobName = '%s',jobRemark= '%s'\
           WHERE jobId = %d" \
          % (job.jobName, job.jobRemark, int(job.jobId))
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("更新成功")
        # 关闭数据库连接
        db.close()
        return True
    except:
        # 如果发生错误则回滚
        db.rollback()
        print("更新失败")
        # 关闭数据库连接
        db.close()
        return False

def deleteJob(job):
    db, cursor = connect_db()
    sql = '''UPDATE employee SET employee.jobId = 
    (select job.jobId from job where job.jobName = '无')
    WHERE employee.jobId = (select job.jobId from job
    WHERE job.jobName = '%s')
    ''' % job.jobName
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
    sql = "DELETE FROM job WHERE jobName = '%s'" % job.jobName

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
        print("删除成功")
        # 关闭数据库连接
        db.close()
        return True
    except:
        # 发生错误时回滚
        db.rollback()
        print("删除失败")
        # 关闭数据库连接
        db.close()
        return False