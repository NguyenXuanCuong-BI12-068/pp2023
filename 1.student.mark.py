print("Number of student: ")
num_stu = int(input())
id_stu=[]
name_stu=[]
dob_stu=[]
for i in range(num_stu):
    id_sinhvien = input("ID of student "+str(i+1)+": ")
    id_stu.append(id_sinhvien)
    name_sinhvien = input("Name of student "+str(i+1)+": ")
    name_stu.append(name_sinhvien)
    dob = input("DOB of student "+str(i+1)+": ")
    dob_stu.append(dob)

print("Number of course")
num_cou = int(input())
id_cou =[]
name_cou=[]
mark_stu =[]
count = 0

for i in range(num_cou):
    id_course = input("ID of the course "+str(i+1)+": ")
    id_cou.append(id_course)
    name_course = input("Name of the course "+str(i+1)+": ")
    name_cou.append(name_course)

for i in range(num_cou):
    for j in range(num_stu): 
        mark=str(float(input(name_cou[i]+" mark of student "+ name_stu[j]+": ")))
        mark_stu.append(mark)

print("List of the student: ")
for i in range(num_stu):
    print("           "+id_stu[i]+" "+name_stu[i]+" "+dob_stu[i])
print("List of the course: ")
for k in range(num_cou):
    print("           "+id_cou[k]+" "+name_cou[k])
print("List of the mark student: ")
for j in range(num_cou):
    print("          "+name_stu[j]+": ")
    for i in range(num_cou):
        print("                  "+name_cou[i]+" "+mark_stu[count])
        count+=1
        

