#WAP to find common inputs
A= [1,2,3]
B = [2,3,4]
C = [3,4,5]
for i in A:
    if i in B and i in C: #checking if the element is present in both the lists
       print(i) #if the element is present in both the lists then it will be added to the result list and printed
        