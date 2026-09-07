
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

#todo insert는 데이터를 추가하는 명령어 입니다.
#todo 테이블에서 데이터를 넣을 열을 지정하고, 그 열에 넣을 값을 values()에 작성한다.
cursor.execute("""
insert into calls (name, phone_number, call_date, duration) 
values('박대성','010-1234-5678','2023-09-02',120)
""")

conn.commit()

# TODO SELECT조회해라 FROM=위치는 calls에서
# TODO *는 모든 열을 의미한다.
cursor.execute("SELECT * FROM calls")

# TODO SELECT로 조회한 결과를 모두 가져온다.
# TODO fetchall()은 조회된 모든 행(row)을 가져와서 리스트 형태로 반환한다.
rows = cursor.fetchall()

print(rows)