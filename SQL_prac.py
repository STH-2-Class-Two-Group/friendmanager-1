import sqlite3
from call_list import bulk_logs

conn = sqlite3.connect("call3.db")
cursor = conn.cursor()


def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS calls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        duration INTEGER NOT NULL,
        call_date TEXT NOT NULL,
        call_type INTEGER NOT NULL
    )
    """)

    conn.commit()

# todo sqlite는 날짜 타입이 없어서 TEXT로 저장한다.
# todo datetime을 글자로 바꿨다가, 계산할 때 다시 datetime으로 되돌린다.
def insert_calls():
    for name, call_number, call_date, duration, call_type in bulk_logs:
        cursor.execute(
            """
            INSERT INTO calls (name, phone_number, duration, call_date, call_type)
            VALUES (?, ?, ?, ?, ?)
            """,
            (name, call_number, duration, str(call_date), call_type),
        )

    conn.commit()


create_table()
insert_calls()
conn.close()
