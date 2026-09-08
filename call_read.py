import sqlite3
from datetime import datetime

conn = sqlite3.connect("call.db")
cursor = conn.cursor()

# call.db에서 조회하고 통화 기록을 가져온다.
cursor.execute("SELECT name, phone_number, duration, call_date FROM calls")
rows = cursor.fetchall()

print(rows)
