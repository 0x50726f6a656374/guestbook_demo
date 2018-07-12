import mysql.connector

TARGET_DATABASE_NAME = 'guestbook'
TARGET_TABLE_NAME = 'info'


class DatabaseCheck:
    def __init__(self):
        pass
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="403840308"
        )
        # disable lazy mode
        self.cursor = self.conn.cursor(buffered=True)

    def check_database(self):
        print("[INFO] Check database...")
        self.cursor.execute("SHOW DATABASES")
        for db in self.cursor:
            print("[INFO] Found database", db[0])
            if str(db[0]) == str(TARGET_DATABASE_NAME):
                print("[PASS] Database Found")
                return True

        print("[FAIL] Database " + TARGET_DATABASE_NAME + " not found")
        return False

    def check_table(self):
        print("[INFO] Check table...")
        self.cursor.execute("USE " + str(TARGET_DATABASE_NAME))
        print("[INFO] Use table", str(TARGET_DATABASE_NAME))
        self.cursor.execute("SHOW TABLES")
        for table in self.cursor:
            print("[INFO] Found table", table[0])
            if str(table[0]) == str(TARGET_TABLE_NAME):
                print("[PASS] Table Found", table[0])
                return True

        print("[FAIL] Table " + TARGET_TABLE_NAME + " not found")
        return False

    def create_database(self):
        print("[INFO] Creating Database....")
        try:
            self.cursor.execute("CREATE DATABASE " + str(TARGET_DATABASE_NAME))
            print("[SUCCESS] Database created")
            return True
        except mysql.connector.Error as err:
            print("[FAILED] Database create fail, ", err)
            return False

    def create_table(self):
        print("[INFO] Creating table...")
        try:
            self.cursor.execute(
                "CREATE TABLE " + TARGET_TABLE_NAME + " (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), birthday VARCHAR(255),phone VARCHAR(255))")
            print("[SUCCESS] Table Created")
            return True
        except mysql.connector.Error as err:
            print("[FAILED] Table create fail, ", err)
            return False

    def pre_check(self):
        for retry in range(0, 3):
            db_pass = self.check_database()
            if db_pass:
                table_pass = self.check_table()
                if table_pass:
                    print("[PASS] All Pre-Check Pass")
                    return True
                else:
                    self.create_table()
            else:
                self.create_database()
            print('[INFO] Retry...')
        print(['[FAIL] Pre-Check fail'])

    def create(self):
        pass


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="403840308",
            database=str(TARGET_DATABASE_NAME)
        )
        # disable lazy mode
        self.cursor = self.conn.cursor()

    def create(self, data_list):
        sql = "INSERT INTO " + TARGET_TABLE_NAME + " (name, birthday, phone) VALUES (%s, %s, %s)"
        val = (data_list["name"], data_list["birthday"], data_list["phone"])
        self.cursor.execute(sql, val)
        self.conn.commit()

    def read(self):
        self.cursor.execute("SELECT * FROM " + str(TARGET_TABLE_NAME))
        rows = self.cursor.fetchall()
        return rows

    def update(self, uid, name, birthday, phone):
        sql = "UPDATE " + str(
            TARGET_TABLE_NAME) + " SET name = '" + name + "',birthday = '" + birthday + "',phone = '" + phone + "' WHERE id = '" + str(
            uid) + "'"
        self.cursor.execute(sql)
        self.conn.commit()

    def delete(self, uid):
        sql = "DELETE FROM " + str(TARGET_TABLE_NAME) + " WHERE id = '" + str(uid) + "'"
        self.cursor.execute(sql)
        self.conn.commit()


def database():
    pass


if __name__ == "__main__":
    """ This is executed when run from the command line """
    database()
