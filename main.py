class Person:
    def __init__(self, name, mbti, age, addr, hobby, concern, job, travel):
        self.name = name
        self.mbti = mbti
        self.age = age
        self.addr = addr
        self.hobby = hobby
        self.concern = concern
        self.job = job
        self.travel = travel
    # 자기 소개 함수
    def introduce(self):
        return f"안녕! 내 소개를 하자면 나는 {self.name}이고, MBTI는 {self.mbti}야. 나이는 {self.age}살이야. 집 주소는 {self.addr}이고 취미는 {self.hobby}야."
    # 걱정거리 함수
    def thinkConcern(self):
        return f"내가 최근에 걱정했던 내용은 {self.concern}야."
    # 직업 소개 함수
    def introduceJob(self):
        return f"나는 {self.job} 직장에서 일을 한 적이 있어."
    # 여행지 소개 함수
    def introduceTravel(self):
        return f"나는 {self.travel} 여행지를 최근 가본 적이 있어."
# 사용자 입력을 외부에서 받기
name = input("이름을 말해줘: ")
mbti = input("MBTI를 말해줘: ")
age = int(input("나이를 말해줘: "))
addr = input("집 주소를 말해줘: ")
hobby = input("취미를 말해줘: ")
concern = input("최근에 했던 걱정거리를 말해줘: ")
job = input("직업을 말해줘: ")
travel = input("여행지를 말해줘: ")

person1 = Person(name, mbti, age, addr, hobby, concern, job, travel)

# 결과 출력
print(person1.introduce())
print(person1.thinkConcern())
print(person1.introduceJob())
print(person1.introduceTravel())