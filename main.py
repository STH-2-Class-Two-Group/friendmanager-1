
#todo sqlite3 모듈을 사용하겠다.
import sqlite3

# todo SQlite 데이터베이스 ("call.db")에연결하라
# todo 파일이 없더라도 call.db 파일이 생성이 됩니다.
# todo conn은 connetion(연결) 객체를 의미합니다. 
conn = sqlite3.connect("call.db")

# todo cursor 객체를 생성해라
# todo cursor는 SQL문 명령어를 실행하기위함이다.
cursor = conn.cursor()

# todo SQL 명령어를 실행 execute() 
# TODO """ """를 사용하면 SQL을 여러 줄로 작성할 수 있다.
cursor.execute("""
CREATE TABLE IF NOT EXISTS calls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    call_date TEXT NOT NULL,
    duration INTEGER NOT NULL
)
""")

#todo 지금까지 쓴 내용을 데이터베이스에 최종 저장한다.
conn.commit()