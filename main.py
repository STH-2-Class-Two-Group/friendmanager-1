from datetime import timedelta
import sqlite3


class Contact:

    def __init__(self, name, call_number):
        self.name = name
        self.call_number = call_number
        self.calls = []
        self.oldcalls = []
        self.total_time = 0
        self.one_time = 0
        self.frequency = None

    # 통화 기록 추가
    def add_call(self, called_at, duration):
        call = {
            "called_at": called_at,
            "duration": duration
        }

        self.calls.append(call)
        self.oldcalls.append(call)
        self.total_time += duration
        self.one_time += duration

    # 1년이 지난 통화 기록 삭제
    def remove_old_calls(self, reference_time):
        one_year_ago = reference_time - timedelta(days=365)

        remaining_calls = []

        for call in self.calls:

            if call["called_at"] >= one_year_ago:
                remaining_calls.append(call)

            else:
                self.one_time -= call["duration"]


        self.calls = remaining_calls

    # 1년간 통화 횟수 계산
    def count_calls(self, callcount):
        return len(callcount)

    # 연락 빈도 분류
    def classify_frequency(self,callcount):

        call_count = self.count_calls(callcount)

        if call_count < 30:
            self.frequency = "Adagio_아주_느리게"

        elif call_count <= 70:
            self.frequency = "Andante_느리게"

        elif call_count <= 100:
            self.frequency = "Allegro_빠르게"

        else:
            self.frequency = "Presto_아주_빠르게"

        return self.frequency


class SQLite넣기(Contact):

    def __init__(self, name, call_number, DBname):

        # Contact의 __init__ 실행
        super().__init__(name, call_number)

        # SQLite 연결
        self.conn = sqlite3.connect(f"{DBname}")
        self.cursor = self.conn.cursor()

    # SQLite에 넣을 데이터 한 덩어리 생성
    def make_data(self, callcount, calltime):

        self.classify_frequency()

        self.data = {
            "name": self.name,
            "call_number": self.call_number,
            "count_calls": callcount,
            "total_time": calltime,
            "frequency": self.frequency
        }

        return self.data

    # 테이블 생성
    def sqlite_table_생성(self, DBname):

        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {DBname} (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

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

        self.cursor.executemany("""
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

