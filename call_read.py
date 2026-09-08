import sqlite3
import time

class CallRead:
    def __init__(self):
        self.conn = sqlite3.connect("call.db")
        self.cursor = self.conn.cursor()

        # call.db에서 조회하고 통화 기록을 가져온다.
        self.cursor.execute("SELECT name, phone_number, duration, call_date FROM calls")
        self.rows = self.cursor.fetchall()

    def select(self):
        # todo 조회된 통화 기록을 1초마다 출력한다.
        for name, phone_number, duration, call_date in self.rows:
            print(f"이름: {name}, 전화번호: {phone_number}, 통화 시간: {duration}초, 통화 날짜: {call_date}")
            time.sleep(1)

    # todo // 뒤에는 나눈 몫값 
    # todo %는 나누고 남은 값 
    # todo 파이썬 내장함수에 이방식을 이용한 divmod()가 있음 
    #! for문 db를 불러올땐 name,phone_nuber,duration,call_date 가 세트이기때문에 4가지를 다 같이 설정해줘야함
    def call_duration(self):
        Name = input("조회할 이름을 입력하세요")
        call_sum = 0
        call_count = 0

        for name, phone_number, duration, call_date in self.rows:
            if name == Name:
                call_sum += duration
                call_count += 1


        hours = call_sum // 3600
        minutes = (call_sum % 3600) // 60
        seconds = call_sum % 60
        print(f"{Name}님과 {hours}시간 {minutes}분 {seconds}초 동안 통화했고 {call_count}회 만큼 통화했습니다")

        return Name,call_count

    def classify_frequency(self,name,call_count):
        
            if call_count < 30:
                frequency = "적은 빈도"

            elif call_count <= 70:
                frequency = "애매한 빈도"

            elif call_count <= 100:
                frequency = "많은 빈도"

            else:
                frequency = "그 이상"

            print(f"{name}님과의 통화 빈도는 {frequency} 입니다.")

call_read = CallRead()
name,call_count = call_read.call_duration()
call_read.classify_frequency(name,call_count)
