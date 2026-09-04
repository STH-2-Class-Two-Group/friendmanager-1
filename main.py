from datetime import datetime, timedelta

now = datetime.now()
reservation = datetime(2026,9,25,12,45,7)

#! 시간비교 예약 혹은 시간 비교후 처리시 사용
if now >= reservation:
    print(reservation)
else:
    print("notyet")