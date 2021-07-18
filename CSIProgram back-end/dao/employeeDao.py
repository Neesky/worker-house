
#!/usr/bin/python3

from const import DATABASE_LOCATION, DATABASE_PORT
import pymysql

def connect_db(uname="root", pwd="elysium"):
    # 打开数据库连接
    db = pymysql.connect(host=DATABASE_LOCATION, user=uname, database="testdb",port=DATABASE_PORT)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor(pymysql.cursors.DictCursor)
    return db, cursor
  
def getAllEmployee():
    db, cursor = connect_db()
    sql = """select employee.id,employee.password,department.departmentName,
                    department.departmentRemark,
                    job.jobName,job.jobRemark,employee.name,employee.cardId,
                    employee.address,employee.postCode,
                    employee.tel,employee.phone,employee.QQNumber,employee.email,
                    employee.sex,party,employee.birthday,
                    employee.race,employee.education,employee.speciality,employee.hobby,
                    employee.remark,employee.createDate,employee.status

                    from employee,department,job
                    
                    WHERE
                    department.departmentId=employee.departmentId
                    and 
                    job.jobId=employee.jobId
                    """

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
        # for row in results:
        #     print(row)

        db.close()
        return results
        # 关闭数据库连接

    except:

        print("Error: unable to fetch data")
        # 返回None

        # 关闭数据库连接
        db.close()

def searchEmployee(employee):
    db, cursor = connect_db()
    if employee.departmentName != "%" and employee.jobName != "%":
        sql = """select employee.id,employee.password,department.departmentName,department.departmentRemark,
        job.jobName,job.jobRemark,employee.name,employee.cardId,employee.address,employee.postCode,
        employee.tel,employee.phone,employee.QQNumber,employee.email,employee.sex,party,employee.birthday,
        employee.race,employee.education,employee.speciality,employee.hobby,employee.remark,employee.createDate,employee.status
    
        from employee,department,job
     
        where 
        employee.jobId = (select job.jobId from job where job.jobName = '%s') 
        and job.jobName = '%s'
        and employee.sex like '%s' 
        and employee.name like '%s' 
        and employee.phone like '%s' 
        and employee.cardId like '%s' 
        and employee.departmentId
        = (select department.departmentId from department where department.departmentName = '%s')
        and department.departmentName = '%s' 
        """ % (employee.jobName, employee.jobName, employee.sex, employee.name, employee.phone, employee.cardId,
               employee.departmentName, employee.departmentName)
    elif employee.departmentName != "%":
        sql = """select employee.id,employee.password,department.departmentName,department.departmentRemark,
                job.jobName,job.jobRemark,employee.name,employee.cardId,employee.address,employee.postCode,
                employee.tel,employee.phone,employee.QQNumber,employee.email,employee.sex,party,employee.birthday,
                employee.race,employee.education,employee.speciality,employee.hobby,employee.remark,employee.createDate,employee.status

                from employee,department,job

                where 
               
                
                employee.sex like '%s' 
                and employee.name like '%s' 
                and employee.phone like '%s' 
                and employee.cardId like '%s' 
                and employee.departmentId
                = (select department.departmentId from department where department.departmentName = '%s')
                and department.departmentName = '%s' 
                
                and job.jobId = employee.jobId
                """ % (employee.sex, employee.name, employee.phone, employee.cardId,
                       employee.departmentName, employee.departmentName)
    elif employee.jobName != "%":
        sql = """select employee.id,employee.password,department.departmentName,department.departmentRemark,
                job.jobName,job.jobRemark,employee.name,employee.cardId,employee.address,employee.postCode,
                employee.tel,employee.phone,employee.QQNumber,employee.email,employee.sex,party,employee.birthday,
                employee.race,employee.education,employee.speciality,employee.hobby,employee.remark,employee.createDate,employee.status

                from employee,department,job

                where 
                employee.jobId = (select job.jobId from job where job.jobName = '%s') 
                and job.jobName = '%s'
                and employee.sex like '%s' 
                and employee.name like '%s' 
                and employee.phone like '%s' 
                and employee.cardId like '%s' 
                and department.departmentId = employee.departmentId
                
                """ % (employee.jobName, employee.jobName, employee.sex, employee.name, employee.phone, employee.cardId)
    else:
        sql = """select employee.id,employee.password,department.departmentName,department.departmentRemark,
                job.jobName,job.jobRemark,employee.name,employee.cardId,employee.address,employee.postCode,
                employee.tel,employee.phone,employee.QQNumber,employee.email,employee.sex,party,employee.birthday,
                employee.race,employee.education,employee.speciality,employee.hobby,employee.remark,employee.createDate,employee.status

                from employee,department,job

                where 
                
                employee.sex like '%s' 
                and employee.name like '%s' 
                and employee.phone like '%s' 
                and employee.cardId like '%s' 
                and department.departmentId = employee.departmentId
                and job.jobId = employee.jobId
                """ % (employee.sex, employee.name, employee.phone, employee.cardId)

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


def appendEmployee(employee):
    db, cursor = connect_db()

    sql = """INSERT INTO employee(id,password,departmentId,jobId,name,cardId,
            address,postCode,tel,phone,QQNumber,email,sex,party,birthday,race,
            education,speciality,hobby,remark,createDate,status) 
            VALUES ('%s','%s', 
            (SELECT departmentId from department WHERE departmentName = '%s'),
            (SELECT jobId from job WHERE jobName = '%s'),
            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',
             '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % \
          (employee.id, employee.password, employee.departmentName, employee.jobName,
           employee.name, employee.cardId, employee.address, employee.postCode, employee.tel,
           employee.phone, employee.QQNumber, employee.email, employee.sex, employee.party,
           employee.birthday, employee.race, employee.education, employee.speciality,
           employee.hobby, employee.remark, employee.createDate, employee.status)
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

def insertDepartment(department):
    db, cursor = connect_db()
    sql = "INSERT INTO employee()"
    
def changeEmployee(employee):
    db, cursor = connect_db()
    sql = "UPDATE employee SET id = '%s',\
    departmentId = (SELECT departmentId from department WHERE departmentName = '%s')\
    ,jobId = (SELECT jobId from job WHERE jobName = '%s') \
    ,name = '%s',cardId = '%s', address = '%s',postCode = '%s',tel = '%s'\
    ,phone = '%s',QQNumber = '%s',email = '%s',sex = '%s',party = '%s',birthday = '%s'\
    ,race = '%s',education = '%s',speciality = '%s',hobby = '%s'\
    ,remark = '%s',createDate = '%s' ,status = '%s' WHERE id = '%s'" \
          % (employee.id, employee.departmentName, employee.jobName
             , employee.name, employee.cardId, employee.address, employee.postCode, employee.tel
             , employee.phone, employee.QQNumber, employee.email, employee.sex, employee.party
             , employee.birthday, employee.race, employee.education, employee.speciality, employee.hobby
             , employee.remark, employee.createDate, employee.status, employee.id)

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

def deleteEmployee(employee):
    db, cursor = connect_db()
    sql = "DELETE FROM employee WHERE id = '%s'" % employee.id

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




def getMyData(employee):

    db, cursor = connect_db()

    sql = """select employee.id,employee.password,department.departmentName,department.departmentRemark,
                job.jobName,job.jobRemark,employee.name,employee.cardId,employee.address,employee.postCode,
                employee.tel,employee.phone,employee.QQNumber,employee.email,employee.sex,party,employee.birthday,
                employee.race,employee.education,employee.speciality,employee.hobby,employee.remark,employee.createDate,employee.status

                from employee,department,job

                WHERE
                employee.id = '%s'
                and employee.departmentId = department.departmentId
                and employee.jobId = job.jobId""" % employee.id
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
        # for row in results:
        #     print(row)
        db.close()
        return results
        # 关闭数据库连接

    except:
        print("Error: unable to fetch data")
        # 返回None

        # 关闭数据库连接
        db.close()