#Store the number of lecturers,students,subject and mark
lecturer = []
student = []
id_student = []
subject = []
id_sub = []
stu_mark = []

# Define the nubmer of lecturer
def number_of_lecturer():
    n =int(input("Number of the lecturer: "))
    while n<= 0:
        print("Number of lecturer must greater than 0!Try again")
        n =int(input("Number of the lecturer: "))
    for i in range(n):
        lec = input(f"Name of the lecturer {i+1}: ")
        lecturer.append(lec)
    
# Define the number of student
def number_of_student():
    n =int(input("Number of the student: "))
    while n<= 0:
        print("Number of student must greater than 0!Try again")
        n =int(input("Number of the student: "))
    for i in range(n):
        id = input(f"Id of the student {i+1}: ")
        id_student.append(id)
        stu = input(f"Name of the student {i+1}: ")
        student.append(stu)
    
    
# Define the number of subjects and marks of subject for each student
def number_of_course():
    n =int(input("Number of the subject: "))
    while n<= 0:
        print("Number of subject must greater than 0!Try again")
        n =int(input("Number of the subject: "))
    for i in range(n):
        id = input(f"Id of the subject {i+1}: ")
        id_sub.append(id)
        sub = input(f"Name of the subject {i+1}: ")
        subject.append(sub)
    
    
def mark_of_student():
    for i in range(len(student)):
        for j in range(len(subject)):
            mark = float(input(f"{subject[j]} mark of student {student[i]}: "))
            while mark <=0:
                print("Mark number must greater than 0!Try again")
                mark = float(input(f"{subject[j]} mark of student {student[i]}: "))
            stu_mark.append(mark)

# Define output
def list_output():
    cnt = 0
    print(" ")
    print("List of lecturers: ")
    print("Name")
    for i in range(len(lecturer)):
        print(f"{lecturer[i]}")
    print(" ")
    print("List of student: ")
    print("ID  Name")
    for i in range(len(student)):
        print(f"{id_student[i]}  {student[i]}")
    print(" ")
    print("List of subject: ")
    print("ID  Subject")
    for i in range(len(subject)):
        print(f"{id_sub[i]}  {subject[i]}")
    print(" ")
    print("Mark of student: ")
    print("Name   Subject   Mark")
    for i in range(len(student)):
        print(f"{student[i]}: ")
        for j in range(len(subject)):
            print(f"       {subject[j]}:    {stu_mark[cnt]}")
            cnt+=1

# Define main
def main():
    number_of_lecturer()
    number_of_student()
    number_of_course()
    mark_of_student()
    list_output()

main()
    