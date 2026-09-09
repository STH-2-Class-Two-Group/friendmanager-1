from datetime import datetime, timedelta


class Contact:
    def __init__(self, name):
        self.name = name
        self.calls = []
        self.total_time = 0
        self.frequency = None
        '''
        2026.09.03 main_jangsg
        사용자 기준 분류 작업용 저장 공간 추가
        
        self.categories = {
            '가족': [],
            '친구': [],
            '지인': [],
            '비즈니스': []
        }
        '''

    # 통화 기록 추가
    '''
    2026.09.03 main_jangsg
    코드 리뷰 중 매개변수인 called_at, duration이
    무슨 의미를 가지고 있는지 코드만 가지고는 알기 어렵다는 의견이 있어서
    called_at(통화날짜), duration(통화시간)을 알기 쉽게 변수 변경.
    called_at -> call_date
    duration -> call_time
    '''
    def add_call(self, call_date, call_time):
        call = {
            "call_date": call_date,
            "call_time": call_time
        }

        self.calls.append(call)
        self.total_time += call_time

    # 1년이 지난 통화 기록 삭제
    def remove_old_calls(self, reference_time):
        '''
        2026.09.03 main_jangsg
        reference_time을 현재 일시로 설정하고, 365일 마이너스하는 로직을 설명하였으나
        구현된 코드를 보면 reference_time을 현재 일시로 값을 집어넣는 부분이 보이지 않아
        이 부분 추가.
        '''
        reference_time = datetime.now()
        one_year_ago = reference_time - timedelta(days=365)

        remaining_calls = []

        for call in self.calls:
            if call["call_date"] >= one_year_ago:
                remaining_calls.append(call)
            else:
                self.total_time -= call["call_time"]

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

    '''
    2026.09.03 main_jangsg
    사용자 분류 작업 함수 생성.
    4가지 분류(가족, 친구, 지인, 비즈니스) 중 하나를 선택하면
    선택한 분류항목에 이름을 추가하도록 구현.
    
    def user_category(self, category_name, name):
        if category_name in self.categories:
            self.categories[category_name].append(name)
    '''
        


    # 현재 정보 출력
    def show_info(self):
        print("이름:", self.name)
        print("1년간 통화 횟수:", self.count_calls())
        print("1년간 총 통화시간:", self.total_time, "초")
        print("연락 빈도:", self.frequency)