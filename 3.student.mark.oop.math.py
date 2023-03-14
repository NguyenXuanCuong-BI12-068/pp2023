import numpy as np
import array
import math
# Create class Person
class Person:
    def __init__(self,name: str):
        self.__name = name
    def get_person(self):
        return self.__name
 
#Create class Student inheritance Person
class Student(Person):
    def __init__(self, id: int,name: str,dob: str):
        super().__init__(name)
        self.__name = name
        self.__id = id
        self.__dob = dob
    def get_student(self):
        return f"ID: {self.__id}  Name: {self.__name}  DOB: {self.__dob}"
 
#Create class Subject
class Subject:
    def __init__(self,id_subject: int,name_subject: str):
        self.__id_subject = id_subject
        self.__name_subject = name_subject
    def get_subject(self):
        return f"ID: {self.__id_subject}  Name: {self.__name_subject}"
 
#Create class Mark
class Mark:
    def __init__(self,mark: float):
        self.__mark = mark
    def get_mark(self):
        return f"{self.__mark}"
 
# Create class Avarage GPA for student
class avg_gpa:
    def __init__(self,gpa: float):
        self.gpa = gpa
    def get_avg_gpa(self):
        return f"{round(self.gpa,2)}"
 
def main():
 
    # Create an array to store value
    students = []
    all_student = []
    subjects = []
    all_subject = []
    marks = []
    credit = []
    avarage_gpa = []
    mul_gpa = []
    cnt = 0
    count1 = 0
    count2 = 0

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
    
    
    # Output list of students
    print(" ")
    print("List of the student: ")
    for i in range(len(all_student)):
        print(all_student[i])
    
    # Output list of subjects
    print(" ")
    print("List of the subjects: ")
    for i in range(len(all_subject)):
        print(all_subject[i])
    
    # Output list mark of students
    print(" ")
    for i in range(len(students)):
        print(f"{students[i]}")
        for j in range(len(subjects)):
            print(f"        {subjects[j]}: {marks[cnt]}")
            cnt+=1
    
    # Output list round-down mark of students
    count = 0
    print("Round-down mark of student")
    for i in range(len(students)):
        print(f"{students[i]}")
        for j in range(len(subjects)):
            print(f"        {subjects[j]}: {math.floor(float(marks[count]))}")
            count+=1

    # Output of average gpa
    print("Avearge GPA:")
    for i in range(len(all_student)):
        avg=0
        k=0
        for j in range(len(credit)):
            avg+=float(marks[count1])*credit[k]
            k+=1
            count1+=1
            if k == len(credit):
                mul_gpa.append(avg)
                avg = 0
    for j in range(len(mul_gpa)):
        all_avg = avg_gpa(mul_gpa[j]/sum_credit)
        avarage_gpa.append(all_avg.get_avg_gpa())

    # Output list GPA of students
    for i in range(len(students)):
        print(f"GPA of student {students[i]}: {avarage_gpa[count2]}")
        count2+=1

    # Output list sorting GPA from top to bot
    print("GPA from top to bot")
    avarage_gpa.sort(reverse=True)
    print(avarage_gpa)

main()