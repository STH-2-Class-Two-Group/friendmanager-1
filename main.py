from datetime import timedelta
import sqlite3


class Contact:

    def __init__(self, name, call_number):
        self.name = name
        self.call_number = call_number
        self.calls = []
        self.total_time = 0
        self.frequency = None

    # 통화 기록 추가
    def add_call(self, called_at, duration):
        call = {
            "called_at": called_at,
            "duration": duration
        }

        self.calls.append(call)
        self.total_time += duration

    # 1년이 지난 통화 기록 삭제
    def remove_old_calls(self, reference_time):
        one_year_ago = reference_time - timedelta(days=365)

        remaining_calls = []

        for call in self.calls:

            if call["called_at"] >= one_year_ago:
                remaining_calls.append(call)

            else:
                self.total_time -= call["duration"]

        self.calls = remaining_calls

    # 1년간 통화 횟수 계산
    def count_calls(self):
        return len(self.calls)

    # 연락 빈도 분류
    def classify_frequency(self):

        call_count = self.count_calls()

        if call_count < 30:
            self.frequency = "적은 빈도"

        elif call_count <= 70:
            self.frequency = "애매한 빈도"

        elif call_count <= 100:
            self.frequency = "많은 빈도"

        else:
            self.frequency = "그 이상"

        return self.frequency


class SQLite넣기(Contact):

    def __init__(self, name, call_number):

        # Contact의 __init__ 실행
        super().__init__(name, call_number)

        # SQLite 연결
        self.conn = sqlite3.connect("friend_manager.db")
        self.cursor = self.conn.cursor()

    # SQLite에 넣을 데이터 한 덩어리 생성
    def make_data(self):

        self.classify_frequency()

        self.data = {
            "name": self.name,
            "call_number": self.call_number,
            "count_calls": self.count_calls(),
            "total_time": self.total_time,
            "frequency": self.frequency
        }

        return self.data

    # 테이블 생성
    def sqlite_table_생성(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS call_data (

                managementnumber INTEGER PRIMARY KEY AUTOINCREMENT,

                name TEXT NOT NULL,

                call_number TEXT NOT NULL,

                count_calls INTEGER NOT NULL,

                total_time INTEGER NOT NULL,

                frequency TEXT NOT NULL,

                UNIQUE(name, call_number)
            )
        """)

        self.conn.commit()

    # 데이터 입력 / 기존 데이터 업데이트
    def sqlite_입력(self):

        self.make_data()

        self.cursor.execute("""
            INSERT INTO call_data (
                name,
                call_number,
                count_calls,
                total_time,
                frequency
            )

            VALUES (
                :name,
                :call_number,
                :count_calls,
                :total_time,
                :frequency
            )

            ON CONFLICT(name, call_number)

            DO UPDATE SET

                count_calls = excluded.count_calls,
                total_time = excluded.total_time,
                frequency = excluded.frequency

        """, self.data)

        self.conn.commit()

    def close(self):
        self.conn.close()