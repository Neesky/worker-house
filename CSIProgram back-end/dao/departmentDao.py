import pymysql
from const import *


def connect_db(uname="root", pwd="elysium"):
    # 打开数据库连接
    db = pymysql.connect(host=DATABASE_LOCATION, user=uname, database="testdb",port=DATABASE_PORT)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor(pymysql.cursors.DictCursor)
    return db, cursor
def getAllDepartment():
    db, cursor = connect_db()
    sql = """select department.departmentName,department.departmentRemark from department"""

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
        #for row in results:
           # print(row)

        db.close()
        return results
        # 关闭数据库连接

    except:

        print("Error: unable to fetch data")
        # 返回None

        # 关闭数据库连接
        db.close()


def searchDepartment(department):
    db, cursor = connect_db()
    tmp = "%"
    for i in range(len(department.departmentName)):
        tmp = tmp + department.departmentName[i] + "%"
    sql = """select department.departmentId,department.departmentName,department.departmentRemark
        
        from department

        where department.departmentName like '%s'
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
        # print(results)
        db.close()
        return results
        # 关闭数据库连接

    except:

        print("Error: unable to fetch data")
        # 返回None

        # 关闭数据库连接
        db.close()



def appendDepartment(department):
    db, cursor = connect_db()
    sql = '''
    select * from department where department.departmentName = '%s'
    ''' % department.departmentName
    cursor.execute(sql)
    db.commit()
    result = cursor.fetchall()
    if result:
        print("部门已经存在")
        db.close()
        return False

    sql = """INSERT INTO department(departmentName,departmentRemark)
            VALUES('%s','%s')""" % (department.departmentName, department.departmentRemark)
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


def changeDepartment(department):
    db, cursor = connect_db()
    sql = '''
        select * from department where department.departmentName = '%s'
        ''' % department.departmentName
    cursor.execute(sql)
    db.commit()
    result = cursor.fetchall()
    if result and result[0]['departmentId'] != department.departmentId:
        print("部门已经存在")
        db.close()
        return False

    sql = "UPDATE department SET departmentName = '%s',departmentRemark= '%s'\
           WHERE departmentId = %d" \
          % (department.departmentName, department.departmentRemark, int(department.departmentId))
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

def deleteDepartment(department):
    db, cursor = connect_db()
    sql = '''UPDATE employee SET employee.departmentId
     = (select department.departmentId from department where department.departmentName = '无')
    , employee.jobId = (select job.jobId from job where job.jobName = '无')
    WHERE employee.departmentId = (select department.departmentId from department
    WHERE department.departmentName = '%s')
    ''' % department.departmentName
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()

    sql = '''DELETE FROM department WHERE departmentName = '%s'  ''' \
          % department.departmentName

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
        print("删除部门成功")
        # 关闭数据库连接
        db.close()
        return True
    except:
        # 发生错误时回滚
        db.rollback()
        print("删除部门失败")
        # 关闭数据库连接
        db.close()
        return False
