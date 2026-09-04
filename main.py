from datetime import datetime

now = datetime.now()
print(now)

#! 오늘 날짜 불러오기
day = datetime.today()
print(day)
#! 2026-09-04 14:50:18.561270


#! 불러온 오늘 날짜 내부 시간 바꾸기
days = datetime.today().replace(hour = 1, minute = 15, second = 45, microsecond = 5)

print(days)

#! 2026-09-04 01:15:45.000005
#! 오늘 날짜   1시 15분 45.000005초
