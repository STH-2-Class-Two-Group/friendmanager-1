
#! datetime 내장함수를 불러와야 하기때문에 datetime이라는 파일을 만들면 안됩니다.
from datetime import datetime,timedelta

#Todo datetime.now()는 지금 날짜,시간을 나타내는 함수입니다.
now = datetime.now()
#print(now)

#todo one_days는 하루를 나타내는 timedelta 객체입니다.
one_days = timedelta(days=1)

#todo tomorrow 는 현재 시간에서 하루를 더한 객체 입니다.
tomorrow = now + one_days

#print(tomorrow)
#todo 위에서 now를 이용하여 오늘날짜와 현재시간을 출력하는 함수를 만들었습니다.
#todo now.strftime은 현재날짜,시간등을 문자열로 표시해주는 함수입니다.
#todo %Y = 연도(Year), %m = 월(month), %d = 일(day), %H = 시간(Hour), %M = 분(Minute), %S = 초(Second)
#! %m과 %M은 다르니 주의하세요
def now_datetime():
    print("오늘날짜는"+now.strftime("%Y-%m-%d") + "입니다.")
    print("현재시간은"+now.strftime("%H:%M:%S") + "입니다.")

#todo 입력받은 일수를 timedelta 객체로 반환해주는 함수
def timedelta_day():
    what_days = int(input("몇일을 계산할까요?"))
    return timedelta(days=what_days)


#todo timedelta_day()함수에서 반환받은 일수만큼 날짜를 더해주는 함수
def 일수계산기(days):
    result = now + days
    print(str(days.days),"일뒤 날짜는", result.strftime("%Y-%m-%d"), "입니다.")



now_datetime()
days = timedelta_day()
일수계산기(days)
