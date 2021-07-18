
#!/usr/bin/python3

from const import DATABASE_LOCATION, DATABASE_PORT
import pymysql
import operator

def connect_db(uname="root", pwd="elysium"):
    # 打开数据库连接
    db = pymysql.connect(host=DATABASE_LOCATION, user=uname, database="testdb",port=DATABASE_PORT)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor(pymysql.cursors.DictCursor)
    return db, cursor



def appendAnnouncement(announcement):
    db, cursor = connect_db()
    sql = '''select * from announcement where announcement.title = '%s' ''' % announcement.title
    cursor.execute(sql)
    db.commit()
    result = cursor.fetchall()
    if result:
        print("公告已经存在")
        return False
    
    sql = """INSERT INTO announcement(title,initiatorName,createDate,content)
                VALUES('%s','%s','%s','%s')""" \
          % (announcement.title, announcement.initiatorName, announcement.createDate, announcement.content)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("插入公告成功")
        # 关闭数据库连接
        db.close()
        return True

    except:
        # 如果发生错误则回滚
        # Id是主键，不能插入相同Id
        db.rollback()
        print("插入公告失败")
        # 关闭数据库连接
        db.close()
        return False



def searchAnnouncementWithEmployee(employee):
    db, cursor = connect_db()
    sql = """select announcement.title,announcement.createDate from announcement WHERE announcement.announcementId
            = any(select employeeWithAnnouncement.announcementId from employeeWithAnnouncement
             where employeeWithAnnouncement.employeeId = '%s')""" % employee.id
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        results = cursor.fetchall()
        # 获取数据
        db.commit()
        if results:
            print("读取公告如下")
        else:
            print("没读取任何公告")
        # 关闭数据库连接
        sorted_result = sorted(results, key=operator.itemgetter('createDate'),reverse=True)
        for row in sorted_result:
            print(row)
        db.close()
        # 按照创建时间排序排序
        return sorted_result
        # 关闭数据库连接

    except:

        print("Error: unable to fetch data")
        # 返回None
        # 关闭数据库连接
        db.close()


def searchEmployeeWithAnnouncement(announcement):
    db, cursor = connect_db()
    sql = """select employee.name from employee where employee.id
    = any(select employeeWithAnnouncement.employeeId from employeeWithAnnouncement
    where employeeWithAnnouncement.announcementId
    =any(select announcement.announcementId from announcement
     where announcement.title = '%s'))""" % announcement.title
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        results = cursor.fetchall()
        # 获取数据
        db.commit()
        if results:
            print("如下员工读取了该公告")
        else:
            print("没有员工读取该公告")
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



def appendEmployeeWithAnnouncement(id, title):
    db, cursor = connect_db()
    sql = '''
    select * from employeeWithAnnouncement where
    employeeWithAnnouncement.employeeId = '%s'
    and employeeWithAnnouncement.announcementId = 
    (select announcement.announcementId from announcement
    where announcement.title = '%s')
    ''' % (id, title)
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    result = cursor.fetchall()
    if result:
        print("关系已经存在")
        sql = '''select announcement.title,announcement.initiatorName,announcement.createDate,announcement.content
                         from announcement where announcement.title = '%s'
                      ''' % title
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        result = cursor.fetchall()
        # 关闭数据库连接
        db.close()
        for row in result:
            print(row)
        return result
    else:
        sql = """insert into employeeWithAnnouncement
            (employeeId, announcementId)
            value
            ('%s', (select announcement.announcementId from announcement where announcement.title = '%s'))
            """ % (id, title)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            print("关系建立成功")
        except:
            print("关系建立失败")
        sql = '''select announcement.title,announcement.initiatorName,announcement.createDate,announcement.content
                                 from announcement where announcement.title = '%s'
                              ''' % title
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        result = cursor.fetchall()
        # 关闭数据库连接
        db.close()
        for row in result:
            print(row)
        return result


def getAllAnnouncement():
    db, cursor = connect_db()
    sql = """select announcement.title,announcement.initiatorName,
    announcement.createDate,announcement.content from announcement """
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 获取数据
        results = cursor.fetchall()
        sorted_result = sorted(results, key=operator.itemgetter('createDate'), reverse=True)
        for row in sorted_result:
            print(row)
        # 关闭数据库连接
        db.close()
        # 按照创建时间排序排序
        return sorted_result
        # 关闭数据库连接

    except:

        print("Error: unable to fetch data")
        # 返回None
        # 关闭数据库连接
        db.close()


def deleteAnnouncement(announcement):
    db, cursor = connect_db()
    sql = "DELETE FROM announcement WHERE announcement.title = '%s'" % announcement.title
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 关闭数据库连接
        db.close()
        print("删除公告成功")
        return True
        # 关闭数据库连接
    except:
        print("删除公告失败")
        # 返回None
        # 关闭数据库连接
        db.close()
        return False