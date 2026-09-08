import sqlite3
from datetime import datetime
import time

conn = sqlite3.connect("call.db")
cursor = conn.cursor()

# call.db에서 조회하고 통화 기록을 가져온다.
cursor.execute("SELECT name, phone_number, duration, call_date FROM calls")
rows = cursor.fetchall()

# todo 조회된 통화 기록을 출력한다.
for name, phone_number, duration, call_date in rows:

    call_date = datetime.strptime(call_date, "%Y-%m-%d")
    print(f"이름: {name}, 전화번호: {phone_number}, 통화 시간: {duration}초, 통화 날짜: {call_date.strftime('%Y-%m-%d')}")
