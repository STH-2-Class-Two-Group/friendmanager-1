# TODO sqlite 사용
import sqlite3


# TODO "call.db"라는 SQLite 데이터베이스에 연결하라
# TODO conn이라는 변수명은 Connection, Connector 줄임말로 자주 사용됨
# TODO 밑에 코드를 작성하면 db파일을 만들겠다고 파이썬을 실행하면 파일이 만들어짐
conn = sqlite3.connect("call.db")


# TODO DB에 SQL 명령을 전달하고 실행하기 위한 커서 생성
cursor = conn.cursor()


# TODO 통화기록을 저장할 calls 테이블 생성
# TODO id: 통화기록마다 고유한 번호를 자동으로 부여
# TODO phone_number: 통화한 전화번호
# TODO call_date: 통화한 날짜
# TODO duration: 통화시간 (초 단위)


# TODO execute에서 CREATE TABLE = 표 만들기
# TODO             INSERT      = 표에 데이터 넣기
# TODO             SELECT      = 표에서 데이터 가져오기
# TODO             UPDATE      = 데이터 수정하기
# TODO             DELETE      = 데이터 삭제하기

cursor.execute("""
CREATE TABLE IF NOT EXISTS calls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phone_number TEXT,
    call_date TEXT,
    duration INTEGER
)
""")