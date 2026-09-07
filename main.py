
#* SQLite 연습


#! SQLite연결

#! SQLite 모듈 불러오기
import sqlite3

#! SQLite 모듈 안 클래스를 불러와 연결->친구 관리기 DB생성
conn = sqlite3.connect("friend_manager.db")

#! 명령전달을 위한 인스턴스 생성
cursor = conn.cursor()

#! 명령을 실행하기.
#! 내부 문자는 꼭 대문자일 필요는 없지만 가독성을 위해 SQLite명령어는 대문자, id는 소문자로 쓴다.
#! 테이블 생성
#! create table 테이블을 생성해라
#! if not exists contacts contacts라는 이름이 없을때
#! integer 정수
#! primary key 고유번호
#! autoincrement 번호 자동 증가
#! not null 빈칸 허용 금지
#! unique 중복값 허용 금지
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts(
    contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone_number TEXT NOT NULL UNIQUE
    )""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS call_records(
    call_id INTEGER PRIMARY KEY AUTOINCREMENT,
    contacts INTEGER NOT NULL,
    call_at TEXT NOT NULL ,
    duration INTEGER NOT NULL
    )""")

#! 내부 목록 수정

#cursor.execute("""
#ALTER TABLE call_records
#RENAME COLUMN contacts to contact_id
#""")

#! 데이터 삽입

cursor.execute("""
INSERT INTO contacts(
    name,
    phone_number
)
VALUES(?,?)
""",("홍길동", "01011112222"))

cursor.execute("""
INSERT INTO call_records(
    contact_id,
    called_at,
    duration
)
VALUES(?,?,?)
""",(1,"2026-09-03 10:30:15", 300))

#! 데이터를 넣을때 반드시 commit을 해야지만 db에 적용이 된다
conn.commit()
