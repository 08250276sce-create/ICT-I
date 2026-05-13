file=open('Students.xlsx','w')
file.write("Name,ID\n")
file.write("Namdel,1151\n")
file.write("Dechen,1152\n")
file.write("Pema,1153\n")
file.write("Ugyen,1154\n")
file.write("Phuntsho,1155\n")
file.close()
file=open('Students.xlsx','r')
students=file.read()
print(students)
file.close()
searchN=input("Enter a name to search:")
found=False
with open('students.xlsx','r') as file:
    for student in file:
        if searchN.lower()in student.lower():
            print(student)
            found=True
            break
if not found:
    print("Name not found in the file.")
print()