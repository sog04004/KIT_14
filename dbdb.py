import pymysql

def dbcon():
    return pymysql.connect(host='sog04004.mysql.pythonanywhere-services.com', user='sog04004', password='root1234', db='sog04004$mydb', charset='utf8')

def create_table():
    try:
        db = dbcon()
        c = db.cursor()
        c.execute("CREATE TABLE users (id varchar(50), pw varchar(50), name varchar(50), PRIMARY KEY(id))")
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def insert_user(id, pw, name):
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id, pw, name)
        c.execute("INSERT INTO users VALUES (%s, %s, %s)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def select_all():
    ret = list()
    try:
        db = dbcon()
        c = db.cursor()
        c.execute('SELECT * FROM users')
        ret = c.fetchall()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret

def select_user(id, pw):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id, pw)
        c.execute('SELECT * FROM users WHERE id = %s AND pw = %s', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret

def check_id(id):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id,)
        c.execute('SELECT * FROM users WHERE id = %s', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret

create_table()