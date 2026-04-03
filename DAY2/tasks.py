# for i in range(1,5):
#     if i==3:
#         continue #when i is equal to 3 then it will skip the rest of the code and move to the next iteration of the loop
#     print(i) #prints 1 and 2 and then breaks the loop when i is equal to 3

#WAP to print numbers 1,2,4,5 using for loop and then on side write it in descending order using continue statement
# for i in range(1,6):
#     if i==3:
#         continue #when i is equal to 3 then it will skip the rest of the code and move to the next iteration of the loop
#     print(i,6-i) #prints 1,2,4,5
            
# #zip () onsode we can takek multiple range function and print them together
# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue #when i is equal to 3 and j is equal to 3 then it will skip the rest of the code and move to the next iteration of the loop    
#     print(i,j) #prints 1,5 and then 2,4 and then 4,2 and then 5,1

#WAP to move * to start of string
# s= "yash*is*a*good*programmer"
# newstring=""
# for i in s:
#     if i=="*":
#         newstring = i + newstring 
#     else:
#         newstring = newstring + i
# print(newstring) 


# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y) #prints True because the values of x and y are same
# print(x==z) #prints False because the values of x and z are different
# print(x != z) #prints True because the values of x and z are different
    
    