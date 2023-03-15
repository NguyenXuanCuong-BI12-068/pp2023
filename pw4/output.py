from input import all_student,all_subject,students,subjects,marks,credit,sum_credit
from domains.gpa import avg_gpa
import math


avarage_gpa = []
mul_gpa = []
cnt = 0
count1 = 0
count2 = 0
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