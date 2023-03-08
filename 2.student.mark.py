# Create class Person
class Person:
    def __init__(self,name: str):
        self.name = name
        
#Create class Lecturer inheritance Person
class Lecturer(Person):
    def get_lecturer(self):
         return self.name
#Create class Student inheritance Person
class Student(Person):
    def __init__(self,name: str ,id: int ,dob:  str):
        super().__init__(name)
        self.id = id
        self.dob = dob
    def get_student(self):
        return f"ID: {self.id} Name: {self.name} DOB: {self.dob}"
        
#Create class Subject
class Subject:
    def __init__(self, subject_name: str,id_subject: int):
        self.subject_name = subject_name
        self.id_subject = id_subject
    def get_subject(self):
        return f"ID: {self.id_subject} Name: {self.subject_name}"
        
#Create class Mark
class Mark:
    def __init__(self,mark: int):
        self.mark = mark
    def get_mark(self):
        return f"{self.mark}"
        
# This class Information is useless because I don't khown how to use multiple inheritance
class Information(Student,Subject,Mark):
    def __init__(self, name: str, id: int, dob: str,subject_name: str,id_subject: int,mark: int):
        Student.__init__(self,name, id, dob)
        Subject.__init__(self,subject_name,id_subject)
        Mark.__init__(self,mark)
    def get_information(self):
        return f"{self.id} {self.name} {self.subject_name} {self.mark}"

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
    stu = Student(name_stu,id_stu,dob_stu)
    students.append(name_stu)
    all_student.append(stu.get_student())

# Create input of subject
m = int(input("Enter the number of subject: "))
for i in range(m):
    id_sub = input(f"ID of the subject {i+1}: ")
    name_sub = input(f"Name of the subject {i+1}: ")
    sub = Subject(name_sub,id_sub)
    subjects.append(name_sub)
    all_subject.append(sub.get_subject())

# Create input mark of student
for i in range(len(students)):
    for j in range(len(subjects)):
        mark_stu = input(f"{subjects[j]} mark of student {students[i]}: ")
        mark = Mark(mark_stu)
        marks.append(mark.get_mark())

# Output list of student
print("List of the student: ")
for i in range(len(all_student)):
    print(all_student[i])

# Output list of subject
print("List of the subjects: ")
for i in range(len(all_subject)):
    print(all_subject[i])

# Output list mark of student
for i in range(len(students)):
    print(f"{students[i]}")
    for j in range(len(subjects)):
        print(f"        {subjects[j]}: {marks[cnt]}")
        cnt+=1