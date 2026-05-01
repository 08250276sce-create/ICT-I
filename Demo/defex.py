def calculate_total(x,y,z):
    return x+y+z

def calculate_average(total):
    return total/3

x = float(input("Enter marks for subject 1: "))
y = float(input("Enter marks for subject 2: "))
z = float(input("Enter marks for subject 3: "))

total = calculate_total(x, y, z)
average = calculate_average(total)

print("Total Marks:", total)
print(f"Average: {average:.2f}")
if average>=50:
    print("Result: Pass")
else:
    print("Result: Fail")
print()

def even_odd(num):
    if num %2 == 0:
        print(num, " is an even number.")
    else:
        print(num, " is an odd number.")
even_odd(int(input("Enter a number to check if it even or odd: ")))
print()