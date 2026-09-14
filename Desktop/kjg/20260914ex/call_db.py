import sqlite3


class CallLogManager:

  def __init__(self, db_name="call_logs.db"):
    self.db_name = db_name
    self.create_table()

  def connect(self):
    return sqlite3.connect(self.db_name)

  def create_table(self):
    with self.connect() as conn:
      cursor = conn.cursor()
      cursor.execute("""
                CREATE TABLE IF NOT EXISTS call_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    call_number TEXT NOT NULL,
                    call_date TEXT NOT NULL,
                    call_count TEXT NOT NULL,
                    call_type TEXT NOT NULL
                )
            """)
      conn.commit()

  def insert_call(self, name, call_number, call_date, call_count, call_type):
    type_str = "수신" if str(call_type) == "1" else "발신"
    with self.connect() as conn:
      cursor = conn.cursor()
      cursor.execute(
          """
                INSERT INTO call_logs (name, call_number, call_date, call_count,"
          " call_type)
                VALUES (?, ?, ?, ?, ?)
            """,
          (name, call_number, call_date, str(call_count), type_str),
      )
      conn.commit()

  def get_all_calls(self):
    with self.connect() as conn:
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM call_logs")
      return cursor.fetchall()

  def update_call(self, log_id, name, call_number, call_date, call_count, call_type):
    type_str = "수신" if str(call_type) == "1" else "발신"
    with self.connect() as conn:
      cursor = conn.cursor()
      cursor.execute(
          """
                UPDATE call_logs 
                SET name = ?, call_number = ?, call_date = ?, call_count ="
          " ?, call_type = ?
                WHERE id = ?
            """,
          (name, call_number, call_date, str(call_count), type_str, log_id),
      )
      conn.commit()

  def delete_call(self, log_id):
    with self.connect() as conn:
      cursor = conn.cursor()
      cursor.execute("DELETE FROM call_logs WHERE id = ?", (log_id,))
      conn.commit()


if __name__ == "__main__":
  manager = CallLogManager()

  # Create (수신은 '1', 발신은 '2'로 입력받아 문자열로 저장)
  manager.insert_call(
      "홍길동", "010-1234-5678", "2026-06-06 14:30:00", "03:45", "1"
  )
  manager.insert_call(
      "김철수", "010-9876-5432", "2026-06-06 15:00:00", "01:12", "2"
  )

  # Read
  print("--- 전체 통화 기록 조회 ---")
  for row in manager.get_all_calls():
    print(row)

  # Update
  manager.update_call(
      1, "홍길동", "010-1234-5678", "2026-06-06 14:30:00", "04:00", "2"
  )

  # Delete
  # manager.delete_call(2)