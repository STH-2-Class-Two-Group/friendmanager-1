from datetime import datetime, timedelta

import sqlite3
conn = sqlite3.connect("friend_manager.db")
cursor = conn.cursor()


#todo 관리 정보 연락처 추가

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

class sqlite넣기(Contact):
    def __init__(self,name,call_number): 
        super().__init__(self,name,call_number)  

    def data_add(self):
        self.data = {
            "name": self.name,
            "call_number": self.call_number,
            "count_calls": self.count_calls(),
            "total_time": self.total_time,
            "frequency": self.frequency
        }

    def sqlite_table_생성(self): 
        self.cursor.execute("""
            create table if not exists call_data( 
                managementnumber integer primary key autoincrement, 
                name text not null,
                call_number integer not null, 
                count_calls integer not null,
                total_time integer not null, 
                frequency text not null
                unique(name, call_number)
            )
        """) 
        conn.commit()
    def sqlite_입력(self):
        self.cursor.execute(""" 
            insert into call_data (
            name, 
            call_number, 
            count_calls,
            total_time, 
            frequency )
            values( :"name",
                    :"call_number, 
                    :"count_calls",
                    :"total_time", 
                    :"frequency")  

            on conflict(name, call_number)

            do update set
            count_calls = excluded.count_calls,
            total_time = excluded.total_time, 
            frequency = excluded.frequency

        """,self.data)
        conn.commit()
        conn.close()

#todo ui와 연동
    def sqlite_삭제(self, 사용자Y_N):
        self.cursor.execute(""" 
            delete from call_data
            if f{사용자Y_N}
            """)
        conn.commit()


        conn.close()