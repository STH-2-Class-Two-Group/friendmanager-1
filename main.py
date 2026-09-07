
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