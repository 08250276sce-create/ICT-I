student_list=[] # Initialize an empty list to store student names
student_dict={} # Initialize an empty dictionary to store student information
name = input("enter the name of the student:    ") # Prompt the user to enter the name of the student and store it in the variable 'name'
age = int(input("enter the age of the student:    ")) # Prompt the user to enter the age of the student and store it in the variable 'age'
grade = input("enter the grade of the student:    ") # Prompt the user to enter the grade of the student and store it in the variable 'grade'
student_list.append(name) # Add the student's name to the student_list
student_dict[name] = {"age": age, "grade": grade} # Add the student's information to the student_dict with the name as the key and a dictionary containing age and grade as the value
print("Student List: ", student_list) # Print the list of student names
print("Student Dictionary: ", student_dict)  # Print the dictionary of student information
search_name = input("enter the name of the student to search:    ") # Prompt the user to enter the name of the student to search for and store it in the variable 'search_name'
if search_name in student_list:
    print(f"Student found! Name: {search_name}, Age: {student_dict[search_name]['age']}, Grade: {student_dict[search_name]['grade']}") # If the student is found in the student_list, print their information from the student_dict
else:
    print("student not found!") # If the student is not found in the student_list, print a message indicating that the student was not found
remove_name = input("enter the name of the student to remove:")
if remove_name in student_list:
    student_list.remove(remove_name) # If the student is found in the student_list, remove their name from the list
    del student_dict[remove_name] # Remove the student's information from the student_dict
    print(f"Student {remove_name} has been removed.") # Print a message indicating that the student has been removed 
else:
    print("student not found!") # If the student is not found in the student_list, print a message indicating that the student was not found