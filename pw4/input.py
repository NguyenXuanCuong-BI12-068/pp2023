from domains.students import Student
from domains.subjects import Subject
from domains.marks import Mark

    # Create an array to store value
students = []
all_student = []
subjects = []
all_subject = []
marks = []
credit = []
    
# Create input of students
n = int(input("Enter the number of student: "))
for i in range(n):
    id_stu = int(input(f"ID of student {i+1}: "))
    name_stu = input(f"Name of student {i+1}: ")
    dob_stu = input(f"DOB of student {i+1}: ")
    stu = Student(id_stu,name_stu,dob_stu)
    students.append(name_stu)
    all_student.append(stu.get_student())
    
# Create input of subjects
m = int(input("Enter the number of subject: "))
for i in range(m):
    id_sub = input(f"ID of the subject {i+1}: ")
    name_sub = input(f"Name of the subject {i+1}: ")
    sub = Subject(id_sub,name_sub)
    subjects.append(name_sub)
    all_subject.append(sub.get_subject())
    
# Create input of credits
sum_credit = 0
for i in range(len(subjects)):
    cre = int(input(f"Credit of subject {subjects[i]}: "))
    sum_credit += cre
    credit.append(cre)
    
# Create input mark of students
for i in range(len(students)):
    for j in range(len(subjects)):
        mark_stu = input(f"{subjects[j]} mark of student {students[i]}: ")
        mark = Mark(mark_stu)
        marks.append(mark.get_mark())


