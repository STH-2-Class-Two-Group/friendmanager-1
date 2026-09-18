'''
app.py
Flask 라우트 및 앱 구동
'''
from flask import Flask, render_template, request, jsonify
from read import crudTest
from datetime import datetime

app = Flask(__name__)
db = crudTest()

# 서버 시작 시 DB 테이블 생성 및 초기 더미데이터 삽입
with app.app_context():
    db.createTable()
    db.insertData()

@app.route("/")
def index():
    """메인 페이지: 전체 통화 기록 목록 출력"""
    logs = db.selectAllLogs()
    return render_template("index.html", logs=logs)

@app.route("/search")
def search():
    """이름으로 검색 및 Contact 로직 연동"""
    name = request.args.get("name", "")
    logs = db.selectByName(name) if name else []
    return render_template("index.html", logs=logs, search_name=name)

# RESTful API 형태 (JSON 응답)가 필요할 경우
@app.route("/api/calls/<name>")
def api_get_calls(name):
    logs = db.selectByName(name)
    return jsonify(logs)

if __name__ == "__main__":
    app.run(debug=True, port=5000)