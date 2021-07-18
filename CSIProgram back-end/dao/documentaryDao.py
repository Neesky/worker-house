import pymysql
from const import *
from  datetime import  datetime


def connect_db(uname="root", pwd="elysium"):
    # 打开数据库连接
    db = pymysql.connect(host=DATABASE_LOCATION, user=uname, database="testdb",port=DATABASE_PORT)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor(pymysql.cursors.DictCursor)
    return db, cursor

def getAllDocumentary():
    db, cursor = connect_db()
    sql = """select documentary.title, documentary.initiatorName,
     documentary.createDate, documentary.url
     from documentary
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


def appendDocumentary(url, title,initiatorName,departmentName,creatDate):
    db, cursor = connect_db()
    sql = '''select * from documentary
     where documentary.title = '%s'
     ''' % title
    cursor.execute(sql)

    db.commit()
    result = cursor.fetchall()

    if result:
        print("文件已经存在")
        return
    else:
        sql = """insert into documentary
        (departmentId,title,initiatorName, createDate, url)
        VALUES
        ((select department.departmentId from department where department.departmentName = '%s'), '%s', '%s', '%s', '%s')"""\
        % (departmentName,title, initiatorName, creatDate, url)

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
            db.rollback()
            print("插入失败")
        # 关闭数据库连接
            db.close()
            return False


def searchDocumentaryByemployee(employee):
    db, cursor = connect_db()
    sql = """select documentary.title, documentary.initiatorName,
    documentary.createDate, documentary.url
    from documentary where documentary.departmentName
    = (select departmentName from employee where employee.Id = '%s')
    or documentary.departmentName = '公共部门'
    """ % employee.Id

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


def searchDocumentaryByTitle(documentary):
    db, cursor = connect_db()
    tmp = "%"
    for i in range(len(documentary.title)):
        tmp = tmp + documentary.title[i] + "%"
    sql = """select documentary.title, documentary.initiatorName, documentary.createDate, documentary.url
        from documentary where documentary.title like '%s'
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


def deleteDocumentary(documentary):
    db, cursor = connect_db()
    sql = """delete from documentary where documentary.title = '%s'
    """ % documentary.title

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
