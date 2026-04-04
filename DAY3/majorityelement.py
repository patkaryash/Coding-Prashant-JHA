#WAP to find the majority element in an array using for loop expected output: majority element is 4
s =int(input("Enter the size of the array: "))
A = []
count = 0
majority = None 
for i in range(s):
    A.append(int(input("Enter the element: ")))
print(A)
for i in A:
    if A.count(i)>count:
        count = A.count(i)
        majority = i
print("Majority element is: ",majority)


    


            