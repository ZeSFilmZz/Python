class person :
    # Constructor
    def __init__(self, Firstname, Lastname, Nickname, Age) :
        self.firstname = Firstname
        self.lastname = Lastname
        self.nickname = Nickname
        self.age = Age

    # Methode
    def say_hello(self):
        print(f'สวัสดี!! เราชื่อ{self.firstname} นามสกุล{self.lastname} ชื่อเล่น{self.nickname} อายุ{self.age}ปี ')

    def set_status(self,status):
        self.status = status

    def set_school(self,school):
        self.school = school

    def show_StatusAndSchool(self):
        print(f'ฉันเป็น{self.status}อยู่ที่{self.school}')

class student(person) :
    def __init__(self, Firstname, Lastname, Nickname, School, Age, Grade, MathScore, ScienceScore, EngScore, ThaiScore, SocialScore):
        super().__init__(Firstname, Lastname, Nickname, Age)
        self.grade = Grade
        self.math_score = MathScore
        self.science_score = ScienceScore
        self.eng_score = EngScore
        self.thai_score = ThaiScore
        self.social_score = SocialScore
        self.set_status('นักเรียน')
        self.set_school(School)

    def cal_average_score(self):
        self.avg_score = (self.math_score+ self.science_score+ self.eng_score+ self.thai_score+ self.social_score)/5
        print(f'{self.firstname} {self.lastname} มีคะแนนเฉลี่ย {self.avg_score} คะแนน')

class teacher(person) :
    def __init__(self, Firstname, Lastname, Nickname, Age, School, Subject):
        super().__init__(Firstname, Lastname, Nickname, Age)
        self.set_status('ครู')
        self.set_school(School)
        self.subject = Subject

    def show_Subject(self):
        print(f'ฉันเป็นครูสอนวิชา{self.subject}')

student1 = student('ตั้งใจ','เรียนดี','เก่ง', 'โรงเรียนลุงวิศวกร' ,16,11,85,82,80,90,78)
student1.say_hello()
student1.show_StatusAndSchool()
student1.cal_average_score()
print('=====================================')
teacher1 = teacher('สมร','สอนดี','หมอน',45,'โรงเรียนลุงวิศวกร','ภาษาอังกฤษ')
teacher1.say_hello()
teacher1.show_StatusAndSchool()
teacher1.show_Subject()