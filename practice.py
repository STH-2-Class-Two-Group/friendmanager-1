from datetime import datetime, timedelta
import sqlite3


class Contact:
    # 클래스가 만들어 질 때 자동으로 실행되는 메서드.
    def __init__(self, db_name = "call_manager.db"):
        # 파일 형태 데이터베이스에 연결.
        self.conn = sqlite3.connect(db_name)
        # SQL 쿼리문 수행할 cursor 객체 생성.
        self.cursor = self.conn.cursor()
        # Contact 클래스 객체 생성되는 시점에 1년 전 시간을 one_year_ago 변수에 할당.
        self.one_year_ago = datetime.now() - timedelta(days=365)
        # call_logs테이블 없으면 새로 만드는 SQL문 실행.
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS call_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 고유 번호 (자동 1씩 증가)
                name TEXT,                             -- 이름 (문자열)
                phone TEXT,                            -- 전화번호 (문자열)
                duration INTEGER,                      -- 통화 시간 (정수, 초 단위)
                call_date DATETIME                     -- 통화 날짜 및 시간
            )
        """)
        # 테이블 생성 변경사항을 DB에 최종 반영.
        self.conn.commit()

    # 기존 구현했던 함수 부분 대체~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''
    통화 기록 목록을 받아 DB에 한번에 저장하는 메서드.
    기존 구현했던 add_call(통화기록 추가) 함수 부분을 db에 insert하는 로직으로 대체.
    '''
    def save_calls(self, calls_list):
        # call_logs 테이블에 데이터 삽입할 insert문.
        sql  = "INSERT INTO call_logs (name, phone, duration, call_date) VALUES (?, ?, ?, ?)"
        # call_logs 테이블에 calls_list 안의 데이터들을 삽입.
        self.cursor.executemany(sql, calls_list)
        # 테이블 삽입 변경사항을 DB에 최종 반영.
        self.conn.commit()
        # 삽입한 calls_list 리스트 건 수 저장 완료됐다고 출력.
        print(f"{len(calls_list)}건 저장 완료")

    '''
    1년이 지난 통화 기록을 삭제하는 메서드.
    기존 구현했던 remove_old_calls(1년 경과한 기록 삭제) 함수 부분을 db에 delete하는 로직으로 대체.
    '''
    def delete_calls(self):
        # call_logs 테이블에 통화 날짜가 365일 전 날짜보다 작으면 삭제.
        self.cursor.execute("DELETE FROM call_logs WHERE call_date < ?", (self.one_year_ago, ))
        # 테이블 삭제 변경사항을 DB에 최종 반영.
        self.conn.commit()
        # 삭제 처리한 리스트 건 수 삭제 완료했다고 출력. rowcount는 cursor 객체의 기본 속성.
        print(f"{self.cursor.rowcount}건 삭제 완료!!")

    '''
    1년치 통화기록 건 수 조회
    기존 구현했던 count_calls(1년간 통화 횟수 계산) 함수 부분을 db에 select count하는 로직으로 대체.
    '''
    def show_calls_cnt(self):
        sql = "SELECT COUNT(*) FROM call_logs WHERE call_date > ?"
        self.cursor.execute(sql, (self.one_year_ago,))
        result = self.cursor.fetchone()
        print(f"총 {result[0]}건 조회됩니다.")


    # 새로 구현한 함수 부분~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # 통화 기록 목록 조회하는 메서드.
    def show_all(self):
        # call_logs 테이블에 name, phone, duration, call_date 컬럼 조회.
        self.cursor.execute("SELECT name, phone, duration, call_date FROM call_logs WHERE call_date > ?", (self.one_year_ago, ))
        # SELECT 쿼리의 실행 결과로 찾아낸 모든 행을 파이썬의 리스트 형태로 전부 가져옴.
        rows = self.cursor.fetchall()
        # SELECT 쿼리 실행 결과로 찾아낸 모든 행을 반복문으로 돌려서 한 줄씩 조회.
        for i in rows:
            print(i)

        '''
        fetchone() : 조회 결과 중 1개의 행만 가져옴.
        fetchmany(size) : 지정한 갯수(size)만큼 행 가져옴.
        '''
                            

manager = Contact()

calls_list = [
    ("홍길동", "010-1234-1234", 120, datetime.now()),
    ("TEST", "010-2222-2345", 45, datetime(2025, 12, 12)),
    ("쌉에이스", "010-9876-4567", 450, datetime(2025, 8, 1))
]

manager.save_calls(calls_list)

manager.delete_calls()

manager.show_all()

manager.show_calls_cnt()
