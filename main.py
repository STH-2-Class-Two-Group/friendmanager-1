from datetime import datetime, timedelta

now = datetime.now()
print(now)


#! 365일 이라는 것을 표현. 추가된 시간은 0:00:00으로 표기됨
day = timedelta(days=365)

print(day)
#! 2주 5일 12시간 10분 5초를 추가
add = timedelta(weeks = 2, days = 5, hours = 12, minutes = 10, seconds = 5)

print(add)
#! ->19 days, 12:10:05 표기됨. 2주->14일 + 5일
