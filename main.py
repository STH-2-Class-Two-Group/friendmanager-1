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