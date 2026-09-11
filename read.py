import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect("call.db")
cursor = conn.cursor()


def input_name():
    return input("누구를 조회하시겠어요?")
#todo 1. 전체 통화 기록 조회
def select_all():
    cursor.execute("""
        SELECT *
        FROM calls
    """)

    rows = cursor.fetchall()

# todo 보기좋게 출력되라고 for문 사용 
    for row in rows:
        print(row)


#todo  2. 특정 사람의 통화 기록 조회
def select_person(name):

    cursor.execute("""
        SELECT *
        FROM calls
        WHERE name = ?
    """, (name,))

    rows = cursor.fetchall()
    print(f"{name}님과의 통화기록 ")
    for row in rows:
        print(row)
    return name


#todo  3. 특정 사람의 통화 횟수 조회
def call_count(name):
    cursor.execute("""
        SELECT COUNT(*)
        FROM calls
        WHERE name = ?
    """, (name,))

    row = cursor.fetchone()
    print(row[0])

    return row[0]


#todo  4. 특정 사람과의 총 통화시간 조회
def total_duration(name):
    cursor.execute("""
        SELECT SUM(duration)
        FROM calls
        WHERE name = ?
    """, (name,))

    row = cursor.fetchone()

    # todo 통화 기록이 없는 경우
    if row[0] is None:
        print(f"{name}님과의 통화 기록이 없습니다.")
        return 0

    call_sum = row[0]

    #todo 초를 시간, 분, 초로 변환
    hours = call_sum // 3600
    minutes = (call_sum % 3600) // 60
    seconds = call_sum % 60

    print(
        f"{name}님과 {hours}시간 {minutes}분 {seconds}초 동안 통화했습니다."
    )

    return call_sum


#todo  5. 최근 통화 기록 조회
def DESC_calls(name):
    cursor.execute("""
        SELECT *
        FROM calls
        WHERE name = ?
        ORDER BY call_date DESC
    """,(name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

#todo 6.오래된 기록 조회(하나만)
#todo 이부분으로 이사람이랑 얼마나 통화했는지 마지막 통화가 몇일이 지났어요, 이사람이랑 연락한지 3년이 되었어요 가능할거같음
def ASC_calls(name):
    cursor.execute("""
            SELECT *
            FROM calls
            WHERE name = ?
            ORDER BY call_date ASC
            LIMIT 2
        """,(name,))
    rows = cursor.fetchone()
    
    print(rows)





#todo 확인하는 용도로 while문 사용해서 메뉴식으로 확인
while(True):
    print("1.이름 입력   2.모든 통화기록 전부 검색   3.해당 사람 기록 검색  4.그 사람이랑 몇번 통화 했는지   5.해당 사람이랑 얼마나 통화했는지  6.최근에 통화한지 얼마나 됐는지 ")
    print("7.오래된 기록 조회")
    count = int(input("몇번 보실꺼에요"))
    if count == 1:
        name = input_name()
    elif count == 2:
        select_all()
    elif count == 3:
        select_person(name)
    elif count == 4:
        call_count(name)
    elif count == 5:
        total_duration(name)
    elif count == 6:
        DESC_calls(name)
    elif count == 7:
        ASC_calls(name)
