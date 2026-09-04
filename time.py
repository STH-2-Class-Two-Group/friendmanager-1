
#! datetime 내장함수를 불러와야 하기때문에 datetime이라는 파일을 만들면 안됩니다.
from datetime import datetime,timedelta

#Todo datetime.now()는 지금 시간을 나타내는 함수입니다.
now = datetime.now()
print(now)
