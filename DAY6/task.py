#WAP for arranging numbers such as all the even numbers are placed before odd numbers in a list
list = []
for i in range(int(input("Enter list size: "))):
    list.append(int(input("Enter a number: ")))
even=[]
for i in list:
    if i%2==0:
        even.append(i)
print("Even numbers:", even)
odd=[]
for i in list:
    if i%2!=0:
        odd.append(i)
print("Odd numbers:", odd)
print("Arranged list:", even + odd)
