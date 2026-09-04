from datetime import datetime, timedelta
import time

reservation = datetime(2026,9,4,15,38,50)

#! 시간비교 예약 혹은 시간 비교후 처리시 사용
while True:
    now = datetime.now()

    if now >= reservation:
        print("예약알람")
        break
    else:
        print(now)
        time.sleep(1)
        continue