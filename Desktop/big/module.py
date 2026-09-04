# datetime이란?
# 특정 시점의 날짜 (년,월,일)과 시간 (시,분,초)를 나타내는 객체 또는 데이터 타입
# 사용하는 이유: 서로 따로 분리할수 있어서 데이터 관리가 편함.
# ex) 2026-09-04 12:49:00
# timedelta란?
# 이전 프레임에서 현재 프레임까지 걸린 시간, 1년전 날짜를 계산하기 위한 함수
# 사용하는 이유: 속도 유지 ex) 컴퓨터 성능이 달라도 게임 속도는 똑같이 유지됨.

from datetime import datetime, timedelta

# 오늘 날짜 (연,월,일)
today = datetime.now().date()
# 내일 날짜(오늘 +1일)
tomorrow = today + timedelta(days=1)
# 1년뒤 날짜(오늘 + 365일)
one_year_later = today + timedelta(days=365)

print(f"오늘: {today}")
print(f"내일: {tomorrow}")
print(f"1년뒤: {one_year_later}")