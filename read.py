import sqlite3
from call_list import dummy_call_logs 

class crudTest:

    def __init__(self, dbname = "call.db"):
        self.dbname = dbname

    def createTable(self):
        conn = sqlite3.connect(self.dbname)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS master_call(
                            name TEXT,
                            phone TEXT,
                            duration INTEGER,
                            call_date TEXT,
                            call_type TEXT
        )
        """)


        conn.commit()
        print(f"성공적으로 테이블이 만들어졌습니다.")

    def insertData(self):
        conn = sqlite3.connect(self.dbname)
        cursor = conn.cursor()

        cursor.executemany("""
                INSERT INTO master_call (name, phone, duration, call_date, call_type)
                VALUES (?, ?, ?, ?, ?)
        """, dummy_call_logs)

        conn.commit()

        print(f"{cursor.rowcount}건이 정상 등록되었습니다.")


    def selectTable(self):
        conn = sqlite3.connect(self.dbname)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM master_call
        """)

        rows = cursor.fetchall()

        for row in rows:
            print(row)


'''
test = crudTest()
test.createTable()
test.insertData()
test.selectTable()
'''
