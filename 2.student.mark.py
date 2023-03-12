# Create class Person
class Person:
    def __init__(self,name):
        self.__name = name
    def get_person(self):
        return self.__name
#Create class Student inheritance Person
class Student(Person):
    def __init__(self, id,name,dob):
        super().__init__(name)
        self.__name = name
        self.__id = id
        self.__dob = dob
    def get_student(self):
        return f"ID: {self.__id}  Name: {self.__name}  DOB: {self.__dob}"

#Create class Subject
class Subject:
    def __init__(self,id_subject,name_subject):
        self.__id_subject = id_subject
        self.__name_subject = name_subject
    def get_subject(self):
        return f"ID: {self.__id_subject}  Name: {self.__name_subject}"

#Create class Mark
class Mark:
    def __init__(self,mark):
        self.__mark = mark
    def get_mark(self):
        return f"{self.__mark}"
    
# Create an array to store value
students = []
all_student = []
subjects = []
all_subject = []
marks = []
cnt = 0

# Create input of student
n = int(input("Enter the number of student: "))
for i in range(n):
    id_stu = int(input(f"ID of student {i+1}: "))
    name_stu = input(f"Name of student {i+1}: ")
    dob_stu = input(f"DOB of student {i+1}: ")
    stu = Student(id_stu,name_stu,dob_stu)
    students.append(name_stu)
    all_student.append(stu.get_student())

# Create input of subject
m = int(input("Enter the number of subject: "))
for i in range(m):
    id_sub = input(f"ID of the subject {i+1}: ")
    name_sub = input(f"Name of the subject {i+1}: ")
    sub = Subject(id_sub,name_sub)
    subjects.append(name_sub)
    all_subject.append(sub.get_subject())

# Create input mark of student
for i in range(len(students)):
    for j in range(len(subjects)):
        mark_stu = input(f"{subjects[j]} mark of student {students[i]}: ")
        mark = Mark(mark_stu)
        marks.append(mark.get_mark())

# Output list of student
print(" ")
print("List of the student: ")
for i in range(len(all_student)):
    print(all_student[i])

# Output list of subject
print(" ")
print("List of the subjects: ")
for i in range(len(all_subject)):
    print(all_subject[i])

# Output list mark of student
print(" ")
for i in range(len(students)):
    print(f"{students[i]}")
    for j in range(len(subjects)):
        print(f"        {subjects[j]}: {marks[cnt]}")
        cnt+=1