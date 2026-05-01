student_list = []
student_dict = {}

name = input("Enter your name: ")
age = input("Enter your age: ")
grade = input("Your grade: ")

student_list.append(name)
student_dict[name] = {"Age": age, "Grade": grade}

print("Student list:", student_list)
print("Student Dict:", student_dict)

search_name = input("Enter the name of the student you want to find: ")

if search_name in student_dict:
    print(f"Student present! Name: {search_name}, Age: {student_dict[search_name]['Age']}, Grade: {student_dict[search_name]['Grade']}")
else:
    print("Student not there!")

remove_name = input("Enter the name of the student you want to remove: ")

if remove_name in student_dict:
    student_list.remove(remove_name)
    del student_dict[remove_name]
    print(f"{remove_name} has been removed successfully!")
else:
    print("Student not there in the list!")
    