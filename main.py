from datetime import datetime, timedelta

now = datetime.now()

day = timedelta(days=365*7)

#! 7년뒤 계산
sevenyears = now+day

print(sevenyears)
#! 2033-09-02 14:37:07.394412


#! 1년 50주 30일 전 계산

days = timedelta(weeks = 50, days = 365+30 )

onesatimeago = now-days
print(onesatimeago)

#! 2024-08-20 14:37:52.575804

print(now)



# datetime.now()는 컴퓨터 현재시각을 초 단위보다 더 정밀하게 가져옴.
# 시분초 뒤에 .383301 같은 숫자는 마이크로초를 의미.
# datetime.now() 기본 출력값은 2026-09-04 14:41:53.383301임.
# datetime은 현재 시각을 표현.
# .now() 메서드는 코드가 실행될 때 현재 날짜와 시간 정보를 가져옴.
now = datetime.now()

print("now에 대한 값은 ", now)

# datetime은 특정 날짜도 생성 가능.
# datetime(2026, 12, 25) 는 2026년 12월 25일 00시 00분 00초를 의미. 
# datetime(year, month, day, hour, minute, second) 형식이 기본적인 형식이나 최소한 year, month, day만 넣어도 정상적으로 출력됨.
xmas = datetime(2026, 12, 25)
print("xmas에 대한 값은 ", xmas)


print(f"오늘 날짜는 {now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초 입니다.")
# strftime() 메서드는 datetime -> 원하는 문자열로 치환
formatted_str = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_str)

# strptime() 메서드는 문자열 -> datetime 객체
date_str = "2026-10-01 09:00:00"
parsed_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("파싱된 datetime:", parsed_dt)

# timedelta 인자로는 days, hours, minutes, seconds, weeks 등 사용.
after_100_days = now + timedelta(days=100)
print("100일 후 날짜는 ", after_100_days.strftime("%Y-%m-%d %H:%M:%S"))

before_3_weeks = now - timedelta(weeks=3)
print("3주 전:", before_3_weeks.strftime("%Y-%m-%d"))

# 두 날짜 간 차이
# datetime 객체끼리 빼면 timedelta 객체가 반환될 수 있음.
target_date = datetime(2026, 12, 31)
today = datetime.now()

diff = target_date - today

print("남은 기간 객체:", diff)
print("남은 일수:", diff.days)