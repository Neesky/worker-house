#!/usr/bin/python3

from const import DATABASE_LOCATION, DATABASE_PORT
import pymysql

def connect_db(uname="root", pwd="elysium"):
    # 打开数据库连接
    db = pymysql.connect(host=DATABASE_LOCATION, user=uname, database="testdb",port=DATABASE_PORT)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor(pymysql.cursors.DictCursor)
    
    return db, cursor

def searchPasswordById(employee):
    db, cursor = connect_db()
    sql = "select * from employee where employee.id = '%s'" % employee.id
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

def changePassword(idWithPassword):
    db, cursor = connect_db()
    sql = "UPDATE employee SET password = '%s' WHERE id = '%s'" \
          % (idWithPassword.password,idWithPassword.id)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("修改密码成功")
        # 关闭数据库连接
        db.close()
        return True
    except:
        # 如果发生错误则回滚
        db.rollback()
        print("修改密码失败")
        # 关闭数据库连接
        db.close()
        return False

def loginUpdate(employee):
    db, cursor = connect_db()
    sql = "UPDATE employee SET oaid = '%s',loginErrorCount = 0,mode = '1' WHERE id = '%s'" \
          % (employee.oaid, employee.id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("成功")
        # 关闭数据库连接
        db.close()
        return True
    except:
        # 如果发生错误则回滚
        db.rollback()
        print("失败")
        # 关闭数据库连接
        db.close()
        return False

def logoutUpdate(employee):

    db, cursor = connect_db()
    sql = "UPDATE employee SET mode = '%s' WHERE id = '%s'" \
          % ("0", employee.id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("成功")
        # 关闭数据库连接
        db.close()
        return True
    except:
        # 如果发生错误则回滚
        db.rollback()
        print("失败")
        # 关闭数据库连接
        db.close()
        return False

def loginErrorCountUpdateAddOne(employee):
    db, cursor = connect_db()
    sql = "UPDATE employee SET loginErrorCount = loginErrorCount+1 WHERE id = '%s'" \
          % (employee.id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("登录失败次数加一")
        # 关闭数据库连接
        db.close()
        return True
    except:
        # 如果发生错误则回滚
        db.rollback()
        print("执行错误")
        # 关闭数据库连接
        db.close()
        return False

def loginErrorCountUpdateSetOne(employee):
    db, cursor = connect_db()
    sql = "UPDATE employee SET loginErrorCount = 1,loginErrorTime = %d WHERE id = '%s'" \
          % (employee.loginErrorTime, employee.id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("次数置一")
        # 关闭数据库连接
        db.close()
        return True
    except:
        # 如果发生错误则回滚
        db.rollback()
        print("执行错误")
        # 关闭数据库连接
        db.close()
        return False

def loginErrorTimeUpdate(employee):
    db, cursor = connect_db()
    sql = "UPDATE employee SET loginErrorTime = %d WHERE id = '%s'" \
          % (employee.loginErrorTime, employee.id)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("锁定")
        # 关闭数据库连接
        db.close()
        return True
    except:
        # 如果发生错误则回滚
        db.rollback()
        print("执行错误")
        # 关闭数据库连接
        db.close()
        return False
