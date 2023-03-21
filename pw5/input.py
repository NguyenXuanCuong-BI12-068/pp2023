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
with open('students.txt','w') as sf:
    with open('students.txt', 'r+') as rsf:
        rsf.truncate(0)
        # Create input of students
        n = int(input("Enter the number of student: "))
        for i in range(n):
            id_stu = int(input(f"ID of student {i+1}: "))
            sf.write(str(id_stu)+' ')
            name_stu = input(f"Name of student {i+1}: ")
            sf.write(name_stu+' ')
            dob_stu = input(f"DOB of student {i+1}: ")
            sf.write(dob_stu+'\n')
            stu = Student(id_stu,name_stu,dob_stu)
            students.append(name_stu)
            all_student.append(stu.get_student())
        sf.seek(0)
with open('subjects.txt','w') as suf:
    with open('subjects.txt', 'r+') as rsuf:
        rsuf.truncate(0)
        # Create input of subjects
        m = int(input("Enter the number of subject: "))
        for i in range(m):
            id_sub = input(f"ID of the subject {i+1}: ")
            suf.write(str(id_sub)+' ')
            name_sub = input(f"Name of the subject {i+1}: ")
            suf.write(name_sub+'\n')
            sub = Subject(id_sub,name_sub)
            subjects.append(name_sub)
            all_subject.append(sub.get_subject())
        suf.seek(0)
# Create input of credits
sum_credit = 0
for i in range(len(subjects)):
    cre = int(input(f"Credit of subject {subjects[i]}: "))
    sum_credit += cre
    credit.append(cre)
with open('marks.txt','w') as mf:
    with open('marks.txt', 'r+') as rmf:
        rmf.truncate(0)
    # Create input mark of students
        for i in range(len(students)):
            for j in range(len(subjects)):
                mark_stu = input(f"{subjects[j]} mark of student {students[i]}: ")
                mf.write(str(mark_stu)+ '\n')
                mark = Mark(mark_stu)
                marks.append(mark.get_mark())
        mf.seek(0)

with open('studens.dat', 'a') as af:
    with open('students.txt','r') as rs:
        read_student = rs.read()
    with open('subjects.txt','r') as rsub:
        read_subject = rsub.read()
    with open('marks.txt','r') as rm:
        read_mark = rm.read()
    rs.close()
    rsub.close()
    rm.close()

    af.write(str(read_student)+'\n')
    af.write(str(read_subject)+'\n')
    af.write(str(read_mark)+'\n')
