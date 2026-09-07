import sqlite3
from datetime import datetime

# 1. DB 연결(call_manager.db 파일이 없으면 자동 생성)해서 conn으로 생성
conn = sqlite3.connect("call_manager.db")

# 2. 커서(Cursor) 생성 - SQL문 실행 위한 객체
cursor = conn.cursor()

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS call_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- 고유ID(데이터 추가될 때 마다 자동으로 증가)
    name TEXT,                      -- 연락처 이름(문자)
    phone_number TEXT NOT NULL,     -- 전화번호(문자, 빈 값 허용하지 않음)
    call_type TEXT NOT NULL,        -- 통화 유형 (INCOMING, OUTGOING, MISSED) (문자, 빈 값 허용하지 않음)
    call_duration INTEGER,       -- 통화 시간 (초 단위)(정수형)
    call_timestamp DATETIME NOT NULL -- 통화 일시(날짜, 빈 값 허용하지 않음)
)
""")

def update_table(cursor, name, phone_number):
    cursor.execute("""
    UPDATE call_logs
    SET name = ?
    WHERE phone_number = ? 
    """, ('고객센터', '02-123-4567'))

# 3. 통화기록 테이블 생성
create_table(cursor)

# 4. 데이터 삽입 (Single Data Insert)
# single_log 튜플에 담긴 값들이 순서대로 ? 위치에 1:1로 대응되어 call_logs 테이블의 컬럼에 삽입.
# SQL 인젝션 방지를 위해 Parametric Query (?) 방식을 사용합니다.
#              name       phone_number   call_type  duration_seconds    call_timestamp
'''
single_log = ('홍길동', '010-1234-5678', 'INCOMING', 120 ,              datetime.now())

cursor.execute("""
INSERT INTO call_logs (name, phone_number, call_type, call_duration, call_timestamp)
VALUES (?, ?, ?, ?, ?)
""", single_log)
'''


# 5. 여러 개 데이터 한 번에 삽입 (Bulk Data Insert)

bulk_logs = [
    ('김철수', '010-9876-5432', 'OUTGOING', 45, datetime(2026, 9, 1, 10, 30, 0)),
    ('이영희', '010-5555-4444', 'MISSED', 0, datetime(2026, 9, 5, 14, 15, 0)),
    ('알수없음', '02-123-4567', 'INCOMING', 300, datetime(2026, 9, 7, 9, 0, 0)),
    ('박민수', '010-1111-2222', 'INCOMING', 150, datetime(2026, 8, 15, 11, 20, 0)),
    ('정수진', '010-3333-4444', 'OUTGOING', 80, datetime(2026, 8, 20, 16, 45, 0)),
    ('최동현', '010-6666-7777', 'MISSED', 0, datetime(2026, 8, 22, 9, 10, 0)),
    ('강지은', '010-8888-9999', 'INCOMING', 210, datetime(2026, 8, 25, 18, 5, 0)),
    ('조성민', '010-2222-3333', 'OUTGOING', 12, datetime(2026, 8, 28, 13, 50, 0)),
    ('윤서연', '010-4444-5555', 'INCOMING', 540, datetime(2026, 8, 30, 20, 30, 0)),
    ('임재현', '010-7777-8888', 'MISSED', 0, datetime(2026, 9, 2, 8, 40, 0)),
    ('한지민', '010-9999-0000', 'INCOMING', 95, datetime(2026, 9, 3, 15, 15, 0)),
    ('오태식', '010-1234-1111', 'OUTGOING', 330, datetime(2026, 9, 4, 12, 0, 0)),
    ('서유진', '010-2345-2222', 'INCOMING', 40, datetime(2026, 9, 6, 17, 25, 0)),
    ('권도현', '010-3456-3333', 'MISSED', 0, datetime(2026, 9, 7, 10, 5, 0)),
    ('황보경', '010-4567-4444', 'OUTGOING', 180, datetime(2026, 8, 10, 14, 30, 0)),
    ('송준서', '010-5678-5555', 'INCOMING', 60, datetime(2026, 8, 12, 19, 10, 0)),
    ('류지혜', '010-6789-6666', 'MISSED', 0, datetime(2026, 8, 14, 21, 0, 0)),
    ('전성호', '010-7890-7777', 'OUTGOING', 250, datetime(2026, 8, 16, 11, 40, 0)),
    ('홍길동', '010-1234-5678', 'INCOMING', 120, datetime(2026, 8, 18, 16, 15, 0)),
    ('고은지', '010-8901-8888', 'INCOMING', 310, datetime(2026, 8, 19, 10, 50, 0)),
    ('문태양', '010-9012-9999', 'OUTGOING', 15, datetime(2026, 8, 21, 15, 5, 0)),
    ('양소율', '010-0123-0000', 'MISSED', 0, datetime(2026, 8, 23, 12, 35, 0)),
    ('배준혁', '010-1122-3344', 'INCOMING', 420, datetime(2026, 8, 24, 17, 50, 0)),
    ('백지아', '010-2233-4455', 'OUTGOING', 90, datetime(2026, 8, 26, 9, 15, 0)),
    ('허재원', '010-3344-5566', 'INCOMING', 175, datetime(2026, 8, 27, 14, 40, 0)),
    ('유다은', '010-4455-6677', 'MISSED', 0, datetime(2026, 8, 29, 18, 20, 0)),
    ('남궁성', '010-5566-7788', 'OUTGOING', 500, datetime(2026, 8, 31, 11, 10, 0)),
    ('심수현', '010-6677-8899', 'INCOMING', 30, datetime(2026, 9, 1, 13, 0, 0)),
    ('노경민', '010-7788-9900', 'MISSED', 0, datetime(2026, 9, 2, 16, 45, 0)),
    ('하승우', '010-8899-0011', 'OUTGOING', 220, datetime(2026, 9, 3, 10, 25, 0)),
    ('곽지유', '010-9900-1122', 'INCOMING', 140, datetime(2026, 9, 4, 19, 35, 0)),
    ('성민준', '010-1010-2020', 'OUTGOING', 75, datetime(2026, 9, 5, 11, 50, 0)),
    ('차예린', '010-3030-4040', 'MISSED', 0, datetime(2026, 9, 6, 8, 15, 0)),
    ('주원석', '010-5050-6060', 'INCOMING', 280, datetime(2026, 9, 7, 14, 10, 0)),
    ('우지은', '010-7070-8080', 'OUTGOING', 105, datetime(2026, 8, 11, 15, 30, 0)),
    ('신동엽', '010-9090-0000', 'INCOMING', 65, datetime(2026, 8, 13, 10, 0, 0)),
    ('유재석', '010-1212-3434', 'MISSED', 0, datetime(2026, 8, 15, 17, 40, 0)),
    ('강호동', '010-5656-7878', 'OUTGOING', 480, datetime(2026, 8, 17, 12, 15, 0)),
    ('이수근', '010-9090-1212', 'INCOMING', 190, datetime(2026, 8, 18, 20, 5, 0)),
    ('하동훈', '010-3434-5656', 'OUTGOING', 35, datetime(2026, 8, 20, 9, 50, 0)),
    ('김종국', '010-7878-9090', 'MISSED', 0, datetime(2026, 8, 22, 14, 10, 0)),
    ('서장훈', '010-1111-3333', 'INCOMING', 320, datetime(2026, 8, 24, 18, 30, 0)),
    ('이상민', '010-2222-4444', 'OUTGOING', 115, datetime(2026, 8, 25, 11, 20, 0)),
    ('김희철', '010-3333-5555', 'INCOMING', 45, datetime(2026, 8, 27, 16, 0, 0)),
    ('민경훈', '010-4444-6666', 'MISSED', 0, datetime(2026, 8, 28, 21, 45, 0)),
    ('탁재훈', '010-5555-7777', 'OUTGOING', 230, datetime(2026, 8, 30, 10, 15, 0)),
    ('임원희', '010-6666-8888', 'INCOMING', 85, datetime(2026, 9, 1, 15, 40, 0)),
    ('김준호', '010-7777-9999', 'MISSED', 0, datetime(2026, 9, 2, 19, 10, 0)),
    ('김지민', '010-8888-0000', 'OUTGOING', 160, datetime(2026, 9, 3, 13, 25, 0)),
    ('박나래', '010-1234-9999', 'INCOMING', 270, datetime(2026, 9, 4, 17, 0, 0)),
    ('기안84', '010-2345-8888', 'OUTGOING', 50, datetime(2026, 9, 5, 22, 30, 0)),
    ('코드쿤스트', '010-3456-7777', 'MISSED', 0, datetime(2026, 9, 6, 12, 5, 0)),
    ('전현무', '010-4567-6666', 'INCOMING', 410, datetime(2026, 9, 7, 15, 30, 0)),
    ('이장우', '010-5678-5555', 'OUTGOING', 135, datetime(2026, 8, 10, 9, 45, 0)),
    ('박세리', '010-6789-4444', 'INCOMING', 290, datetime(2026, 8, 11, 14, 20, 0)),
    ('키', '010-7890-3333', 'MISSED', 0, datetime(2026, 8, 13, 18, 55, 0)),
    ('태연', '010-8901-2222', 'OUTGOING', 70, datetime(2026, 8, 14, 11, 10, 0)),
    ('한해', '010-9012-1111', 'INCOMING', 180, datetime(2026, 8, 16, 16, 35, 0)),
    ('문세윤', '010-0123-2222', 'MISSED', 0, datetime(2026, 8, 17, 20, 15, 0)),
    ('김동현', '010-1122-4455', 'OUTGOING', 200, datetime(2026, 8, 19, 13, 40, 0)),
    ('넉살', '010-2233-5566', 'INCOMING', 95, datetime(2026, 8, 21, 10, 0, 0)),
    ('피오', '010-3344-6677', 'OUTGOING', 125, datetime(2026, 8, 22, 15, 25, 0)),
    ('붐', '010-4455-7788', 'MISSED', 0, datetime(2026, 8, 24, 19, 50, 0)),
    ('입짧은햇님', '010-5566-8899', 'INCOMING', 360, datetime(2026, 8, 26, 12, 30, 0)),
    ('이말년', '010-6677-9900', 'OUTGOING', 40, datetime(2026, 8, 27, 17, 15, 0)),
    ('주호민', '010-7788-0011', 'INCOMING', 155, datetime(2026, 8, 29, 11, 0, 0)),
    ('기요시', '010-8899-1122', 'MISSED', 0, datetime(2026, 8, 30, 16, 40, 0)),
    ('침착맨', '010-9900-2233', 'OUTGOING', 310, datetime(2026, 9, 1, 21, 10, 0)),
    ('주우재', '010-1010-3030', 'INCOMING', 240, datetime(2026, 9, 2, 14, 5, 0)),
    ('조세호', '010-2020-4040', 'MISSED', 0, datetime(2026, 9, 3, 18, 30, 0)),
    ('남창희', '010-3030-5050', 'OUTGOING', 85, datetime(2026, 9, 4, 10, 15, 0)),
    ('양세형', '010-4040-6060', 'INCOMING', 170, datetime(2026, 9, 5, 15, 45, 0)),
    ('양세찬', '010-5050-7070', 'OUTGOING', 210, datetime(2026, 9, 6, 20, 20, 0)),
    ('유병재', '010-6060-8080', 'MISSED', 0, datetime(2026, 9, 7, 9, 55, 0)),
    ('조세빈', '010-7070-9090', 'INCOMING', 130, datetime(2026, 8, 10, 13, 10, 0)),
    ('장도연', '010-8080-0000', 'OUTGOING', 260, datetime(2026, 8, 12, 18, 0, 0)),
    ('안영미', '010-9090-1111', 'INCOMING', 75, datetime(2026, 8, 14, 10, 35, 0)),
    ('신봉선', '010-0000-2222', 'MISSED', 0, datetime(2026, 8, 16, 15, 20, 0)),
    ('김신영', '010-1111-4444', 'OUTGOING', 195, datetime(2026, 8, 17, 19, 45, 0)),
    ('송은이', '010-2222-5555', 'INCOMING', 330, datetime(2026, 8, 19, 11, 15, 0)),
    ('김숙', '010-3333-6666', 'OUTGOING', 110, datetime(2026, 8, 21, 16, 50, 0)),
    ('홍진경', '010-4444-7777', 'MISSED', 0, datetime(2026, 8, 23, 21, 30, 0)),
    ('조세호2', '010-5555-8888', 'INCOMING', 225, datetime(2026, 8, 25, 10, 5, 0)),
    ('남창희2', '010-6666-9999', 'OUTGOING', 90, datetime(2026, 8, 26, 14, 40, 0)),
    ('이국주', '010-7777-0000', 'INCOMING', 145, datetime(2026, 8, 28, 18, 15, 0)),
    ('신기루', '010-8888-1111', 'MISSED', 0, datetime(2026, 8, 30, 12, 50, 0)),
    ('풍자', '010-9999-2222', 'OUTGOING', 380, datetime(2026, 8, 31, 17, 25, 0)),
    ('곽튜브', '010-1234-0000', 'INCOMING', 205, datetime(2026, 9, 1, 22, 0, 0)),
    ('빠니보틀', '010-2345-1111', 'OUTGOING', 165, datetime(2026, 9, 2, 11, 35, 0)),
    ('원지', '010-3456-2222', 'MISSED', 0, datetime(2026, 9, 3, 16, 10, 0)),
    ('덱스', '010-4567-3333', 'INCOMING', 490, datetime(2026, 9, 4, 20, 45, 0)),
    ('이시언', '010-5678-4444', 'OUTGOING', 115, datetime(2026, 9, 5, 13, 20, 0)),
    ('빠니보틀2', '010-6789-5555', 'INCOMING', 80, datetime(2026, 9, 6, 17, 55, 0)),
    ('곽튜브2', '010-7890-6666', 'MISSED', 0, datetime(2026, 9, 7, 10, 30, 0)),
    ('고객센터', '02-123-4567', 'INCOMING', 300, datetime(2026, 9, 7, 11, 0, 0)),
    ('카드사', '1588-0000', 'INCOMING', 45, datetime(2026, 9, 7, 12, 15, 0)),
    ('택배기사', '010-0000-1234', 'OUTGOING', 25, datetime(2026, 9, 7, 13, 40, 0)),
    ('스팸차단', '070-1234-5678', 'MISSED', 0, datetime(2026, 9, 7, 14, 20, 0)),
    ('가족', '010-9999-8888', 'INCOMING', 600, datetime(2026, 9, 7, 15, 0, 0)),
]
'''
# 다중 인서트 실행
cursor.executemany("""
INSERT INTO call_logs (name, phone_number, call_type, call_duration, call_timestamp)
VALUES (?, ?, ?, ?, ?)
""", bulk_logs)
'''
# 단일 인서트 실행
for single_log in bulk_logs:
    cursor.execute("""
    INSERT INTO call_logs (name, phone_number, call_type, call_duration, call_timestamp)
    VALUES (?, ?, ?, ?, ?)
    """, single_log)


# --------------------------------------------------
# 6. 데이터 수정 (UPDATE)
# --------------------------------------------------
update_table(cursor, '고객센터', '02-123-4567')
'''
cursor.execute("""
UPDATE call_logs
SET name = ?
WHERE phone_number = ? 
""", ('고객센터', '02-123-4567'))
'''

# --------------------------------------------------
# 7. 데이터 삭제 (DELETE)
# Python sqlite3 모듈은 매핑할 파라미터를 튜플 형태로 받는다.
# 요소가 1개일 경우 (0)가 아니라 (0,)처럼 콤마를 붙여야 함.
# --------------------------------------------------
'''
cursor.execute("""
DELETE FROM call_logs

""", ) 
'''


# duration_seconds 컬럼명을 call_duration으로 변경
'''
cursor.execute("""
ALTER TABLE call_logs 
RENAME COLUMN duration_seconds TO call_duration
""")

conn.commit()
print("컬럼명이 성공적으로 변경되었습니다.")
'''


# call_logs 테이블 삭제
'''
cursor.execute("DROP TABLE IF EXISTS call_logs")

conn.commit()
print("테이블이 성공적으로 삭제되었습니다.")
'''

# 8. 변경 사항 저장 (Commit)
# commit을 호출해야 데이터가 실제 DB 파일에 최종적으로 저장됩니다.
conn.commit()

'''
end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"10000건 단일 인서트 총 소요 시간: {execution_time:.6f} 초")
'''
# rowcount는 Python sqlite3 모듈에서 cursor 객체가 기본적으로 가지괴 있는 객체.
# print(f"데이터 삽입 완료! 총 {cursor.rowcount}개의 행이 추가되었습니다.")

# 9. DB 연결 종료
conn.close()

# 10. 탐색기 생성된 DB 파일 확인하려면 "확장 프로그램" > "SQLite viewer" 설치 후 db파일 클릭하면 우측에 깔끔한 표 형태로 확인 가능.