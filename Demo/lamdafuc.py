name=input("Enter your name:")
greet=lambda x:print("Hello", x)
greet(name)
print()
even_Odd=lambda x:"Even" if x%2==0 else "Odd"
num=int(input("Enter a number:"))
print(even_Odd(num))
arith=lambda x, y:(x+y, x-y, x*y, x/y)
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print(arith(num1,num2))
mylist= [1,2,3,4,5,6]
even=filter(lambda x: x%2==0, mylist)
print(list(even))
mylist=[1,2,3,4]
double=map(lambda x: x*2, mylist)
mynewlist=(list(double))
half=map(lambda x: x/2, mynewlist)
print(list(half))
print()
from functools import reduce
mylist=[1,2,3,4]
mul=reduce(lambda x,y: x*y,mylist)
print(mul)