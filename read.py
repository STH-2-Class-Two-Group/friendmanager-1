'''
read.py
SQLite DB 테이블 생성, CRUD 구현 담당.
'''
import sqlite3
from call_list import dummy_call_logs 
from datetime import datetime, timedelta

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

        conn.close()

    def insertData(self):
        conn = sqlite3.connect(self.dbname)
        cursor = conn.cursor()

        cursor.executemany("""
                INSERT INTO master_call (name, phone, duration, call_date, call_type)
                VALUES (?, ?, ?, ?, ?)
            """, dummy_call_logs)

        conn.commit()
        print(f"{cursor.rowcount}건이 정상 등록되었습니다.")

        conn.close()

    def deleteData(self):
        conn = sqlite3.connect(self.dbname)
        cursor = conn.cursor()

        one_year_ago = datetime.now() - timedelta(days=365)

        cursor.execute("""
            DELETE FROM master_call WHERE call_date < ?
        """, one_year_ago)

        conn.commit()

        print(f"{cursor.rowcount}건이 정상 삭제되었습니다.")

        conn.close()


    def selectTable(self, name):
        conn = sqlite3.connect(self.dbname)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT name, phone, duration, call_date, call_type 
            FROM master_call 
            WHERE name = ?
        """, (name,))

        rows = cursor.fetchall()

        conn.close()

        for row in rows:
            print(row)
        # 함수 호출 시 쿼리만 실행되고 구해온 데이터는 가져올 수 없어서 함수나 객체에서 가져오기 위함임.
        return row
    


'''
test = crudTest()
test.createTable()
test.insertData()
test.selectTable()
'''
