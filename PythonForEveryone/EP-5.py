# สร้าง dictionary เพื่อเก็บคะแนนของนักเรียน
students = {
    "นักเรียน 1": {
        "คณิต": 95,
        "วิทยาศาสตร์": 88,
        "ภาษาอังกฤษ": 76
    },
    "นักเรียน 2": {
        "คณิต": 75,
        "วิทยาศาสตร์": 92,
        "ภาษาอังกฤษ": 85
    },
    "นักเรียน 3": {
        "คณิต": 88,
        "วิทยาศาสตร์": 78,
        "ภาษาอังกฤษ": 90
    },
}

# สร้างฟังก์ชันสำหรับเพิ่มข้อมูลเด็กนักเรียนใน dictionary
def add_student_data(student_name, math_scores , science_scores , english_scores):
    students[student_name] = { "คณิต": math_scores, "วิทยาศาสตร์": science_scores, "ภาษาอังกฤษ": english_scores }


# สร้างฟังก์ชันสำหรับหาคะแนนเฉลี่ยของแต่ละวิชา
def average_score_by_subject(subject):
    total_score = 0
    num_students = len(students)
    
    for s in students:
            total_score += students[s][subject]
    
    if num_students > 0:
        return total_score / num_students
    else:
        return 0

# โปรแกรมหลัก
while True:
    while True:
        Add = input("ต้องการเพิ่มนักเรียนหรือไม่(Y/N) : ")
        if Add == 'Y' :
            Name = input("ชื่อนักเรียน : ")
            Math_scores = int(input("คะแนนวิชาคณิต :"))
            Science_scores = int(input("คะแนนวิชาวิทยาศาสตร์ :"))
            English_scores = int(input("คะแนนวิชาภาษาอังกฤษ :"))
            add_student_data( Name, Math_scores, Science_scores, English_scores)
        else :
            break
    subject = input("ต้องการหาคะแนนเฉลี่ยของนักเรียนวิชา(คณิต,วิทยาศาสตร์,ภาษาอังกฤษ) :")
    average = average_score_by_subject(subject)
    print(f"คะแนนเฉลี่ยของวิชา{subject} คือ {average}")
    print('------------------------------------')
