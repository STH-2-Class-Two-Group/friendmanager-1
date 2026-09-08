import sqlite3
from datetime import datetime

# --------------------------------------------------
# 1. DB 연결 및 커서 생성
# --------------------------------------------------
conn = sqlite3.connect("call_manager.db")
cursor = conn.cursor()

# --------------------------------------------------
# 2. 테이블 생성 (call_logs)
# --------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS call_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,                      -- 연락처 이름
    phone_number TEXT NOT NULL,     -- 전화번호
    call_type TEXT NOT NULL,        -- 통화 유형 (INCOMING, OUTGOING, MISSED)
    duration_seconds INTEGER,       -- 통화 시간 (초 단위)
    call_timestamp DATETIME NOT NULL -- 통화 일시
)
""")

# --------------------------------------------------
# 3. 데이터 삽입 (INSERT)
# --------------------------------------------------
# 단일 데이터 삽입
single_log = ('홍길동', '010-1234-5678', 'INCOMING', 120, datetime.now())

cursor.execute("""
INSERT INTO call_logs (name, phone_number, call_type, duration_seconds, call_timestamp)
VALUES (?, ?, ?, ?, ?)
""", single_log)

# 다중 데이터 삽입 (Bulk Insert)
bulk_logs = [
    ('김철수', '010-9876-5432', 'OUTGOING', 45, datetime(2026, 9, 1, 10, 30, 0)),
    ('이영희', '010-5555-4444', 'MISSED', 0, datetime(2026, 9, 5, 14, 15, 0)),
    ('알수없음', '02-123-4567', 'INCOMING', 300, datetime(2026, 9, 7, 9, 0, 0))
]

cursor.executemany("""
INSERT INTO call_logs (name, phone_number, call_type, duration_seconds, call_timestamp)
VALUES (?, ?, ?, ?, ?)
""", bulk_logs)

conn.commit()  # 저장
print("데이터 삽입 완료!")


# --------------------------------------------------
# 4. 데이터 수정 (UPDATE)
# 예시: '02-123-4567' 전화번호의 이름이 '알수없음'이었던 것을 '고객센터'로 수정
# --------------------------------------------------
update_data = ('고객센터', '02-123-4567')

cursor.execute("""
UPDATE call_logs
SET name = ?
WHERE phone_number = ?
""", update_data)

conn.commit()  # 저장
print(f"데이터 수정 완료! 총 {cursor.rowcount}개의 행이 수정되었습니다.")


# --------------------------------------------------
# 5. 데이터 삭제 (DELETE)
# 예시: 통화 시간이 0초인 기록(부재중 혹은 즉시 취소된 기록) 삭제
# --------------------------------------------------
delete_target_duration = (0,)

cursor.execute("""
DELETE FROM call_logs
WHERE duration_seconds = ?
""", delete_target_duration)

conn.commit()  # 저장
print(f"데이터 삭제 완료! 총 {cursor.rowcount}개의 행이 삭제되었습니다.")


# --------------------------------------------------
# 6. 최종 처리 결과 확인 (SELECT)
# --------------------------------------------------
cursor.execute("SELECT * FROM call_logs")
rows = cursor.fetchall()

print("\n--- [최종 call_logs 데이터 목록] ---")
for row in rows:
    print(row)

# --------------------------------------------------
# 7. DB 연결 종료
# --------------------------------------------------
conn.close()