import sqlite3
import time

conn = sqlite3.connect("call.db")
cursor = conn.cursor()

# call.db에서 조회하고 통화 기록을 가져온다.
cursor.execute("SELECT name, phone_number, duration, call_date FROM calls")
rows = cursor.fetchall()

def select():
    # todo 조회된 통화 기록을 1초마다 출력한다.
    for name, phone_number, duration, call_date in rows:
        print(f"이름: {name}, 전화번호: {phone_number}, 통화 시간: {duration}초, 통화 날짜: {call_date}")
        time.sleep(1)

# todo // 뒤에는 나눈 몫값 
# todo %는 나누고 남은 값 
# todo 파이썬 내장함수에 이방식을 이용한 divmod()가 있음 
def call_duration():
    Name = input("조회할 이름을 입력하세요")
    call_sum = 0
    call_count = 0

    for name, phone_number, duration, call_date in rows:
        if name == Name:
            call_sum += duration
            call_count += 1


    hours = call_sum // 3600
    minutes = (call_sum % 3600) // 60
    seconds = call_sum % 60
    print(f"{Name}님과 {hours}시간 {minutes}분 {seconds}초 동안 통화했고 {call_count}회 만큼 통화했습니다")

