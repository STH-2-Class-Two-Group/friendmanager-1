
#* SQLite 연습


#! SQLite연결

#! SQLite 모듈 불러오기
import sqlite3

#! SQLite 모듈 안 클래스를 불러와 연결->친구 관리기 DB생성
conn = sqlite3.connect("friend_manager.db")

#! 명령전달을 위한 인스턴스 생성
cursor = conn.cursor()

