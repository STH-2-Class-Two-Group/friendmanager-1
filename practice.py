import sqlite3

conn = sqlite3.connect("call_record.db")
cursor = conn.cursor()

# create
cursor.execute("""
CREATE TABLE IF NOT EXISTS call_record(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    call_name TEXT,
    call_number TEXT,
    call_date TEXT,
    call_duration INTEGER,
    call_type TEXT
    )
""")

cursor.execute("""
INSERT INTO call_record(call_name, call_number, call_date, call_duration, call_type)
values(?,?,?,?,?)
""",(
    "박대성",
    "010-4054-2498",
    "2026-09-13",
    70,
    "2"))



# update

cursor.execute("""
update call_record
set call_number = '010-1234-5678', '010-2345-6785'
where call_name = '박대성'
""")
conn.commit()
