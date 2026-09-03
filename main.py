from datetime import datetime, timedelta


class Contact:
    def __init__(self, name):
        self.name = name
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

    # 현재 정보 출력
    def show_info(self):
        print("이름:", self.name)
        print("1년간 통화 횟수:", self.count_calls())
        print("1년간 총 통화시간:", self.total_time, "초")
        print("연락 빈도:", self.frequency)