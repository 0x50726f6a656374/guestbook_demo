import pymysql

db = pymysql.connect("192.168.64.2","dai yuchi","Dai12345","test")
cursor = db.cursor()

class database:
#addtion information to database
    @staticmethod
    def addDB(name,phone,birth):
        sql = "INSERT INTO INFORMATION(NAME, PHONE, BIRTHDAY) VALUE (%s,%s,%s)"
        data=(repr(name),repr(phone),repr(birth))
        cursor.execute(sql % data)
        db.commit()

#delete information from database
    @staticmethod
    def delete(name):
        sql = "DELETE FROM INFORMATION WHERE NAME = ('%s')"%(name)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
#update information from database
    @staticmethod
    def updateALL(phone,birth,name):
        sql = "UPDATE INFORMATION SET PHONE = '%s', BIRTHDAY = '%s'WHERE NAME = '%s' "%(phone,birth,name)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
    @staticmethod
    def updatePHONE(phone,name):
        sql = "update INFORMATION set PHONE = '%s' WHERE NAME = '%s'" % (phone, name)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
    @staticmethod
    def updateBIRTH(birth,name):
        sql = "update INFORMATION set BIRTHDAY = '%s'where NAME = '%s'" % (birth, name)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

#display the information from database
    @staticmethod
    def display():
        sql = "SELECT * FROM INFORMATION "
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
