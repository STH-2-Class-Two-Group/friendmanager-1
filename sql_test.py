from test import Contact

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
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS calls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        call_date TEXT NOT NULL,
        duration INTEGER NOT NULL,
        call_type INTEGER NOT NULL
    )
    """)

    #todo 지금까지 쓴 내용을 데이터베이스에 최종 저장한다.
    conn.commit()

#todo insert는 데이터를 추가하는 명령어 입니다.
#todo 테이블에서 데이터를 넣을 열을 지정하고, 그 열에 넣을 값을 values()에 작성한다.
def insert_call():
    cursor.execute("""
    insert into calls (name, phone_number, call_date, duration)
    values('박대성','010-1234-5678','2023-09-02',120)
    """)

    cursor.execute("""
    insert into calls (name, phone_number, call_date, duration)
    values('장승운','010-4231-4232','2025-10-23',600)
    """)

    conn.commit()

# TODO SELECT조회해라 FROM=위치는 calls에서
# TODO *는 모든 열을 의미한다.
def select_all():
    cursor.execute("SELECT * FROM calls")

    # TODO SELECT로 조회한 결과를 모두 가져온다.
    # TODO fetchall()은 조회된 모든 행(row)을 가져와서 리스트 형태로 반환한다.
    rows = cursor.fetchall()

    print(rows)

# todo 하나만 조회 하고 싶을때 fetchone()을 사용한다.
# todo fetchone()은 조회된 결과에서 첫 번째 행(row)만 가져온다.
# todo 만약에 2번 행을 가져오고 싶으면 fetchone()을 두 번 호출하면 된다.
def select_one():
    cursor.execute("SELECT * FROM calls")

    # TODO SELECT로 조회한 결과에서 하나의 행(row)을 가져온다.
    row1 = cursor.fetchone()
    row2 = cursor.fetchone()

    print(row1)
    print(row2)

#todo for in 반복문을 사용하여 조회 결과를 하나씩 출력한다
def select_for():
    cursor.execute("SELECT * FROM calls")

    for rows2 in cursor:
        print(rows2)

def select_many(count):

    cursor.execute("SELECT * FROM calls")
    # TODO 조회된 결과 중 최대 count개의 행을 가져온다.
    rows = cursor.fetchmany(count)

    #todo 리스트로 그대로 출력이 된다.
    print(rows)

    # TODO 가져온 여러 행을 하나씩 출력한다.
    for row in rows:
        print(row)

def update_call():
    cursor.execute("""
    UPDATE calls
    SET duration = 300
    WHERE id = 1
    """)

    conn.commit()

#todo delete는 데이터를 삭제하는 명령어 입니다.
#todo WHERE를 사용하여 삭제할 데이터를 지정한다.
#todo where뒤에 삭제하고 싶은걸 작성한다.
def delete_call():

    cursor.execute("""
    DELETE FROM calls
    WHERE name = ?
    
    """,('박대성',))

    #todo 지금까지 쓴 내용을 데이터베이스에 최종 저장한다.
    conn.commit()

 #todo rollback()은 지금까지 쓴 내용을 취소한다. 되돌린다.
 #! rollback()은 commit()을 호출했을땐 사용이 불가능하다.
def rollback_call():

    conn.rollback()




select_all()