name=input("Enter your name:")
for i in name:
    print(i)
print()
li=["Python Programming","Python Fundamentals","Python Interview Questions"]
for x in li:
    print(x)
print()
lenli=len(li)
for x in range(lenli):
    print(li[x])
print()
New_tuple=tuple(li)
for x in li:
    print(x)
print()
New_set=set(li)
for x in li:
    print(li)
print()
tup=("John Smith","Jane Doe","Alice Johnson")
for x in tup:
    print(x)
set1={10,30,20}
for x in set1:
    print(x)
BookDetails=dict({"Python Programming":"John Smith","Python Fundamentals":"Alice Johnson","Python Interview Question":"Jane Doe"})
for keys in BookDetails:
    print(keys, BookDetails[keys])
