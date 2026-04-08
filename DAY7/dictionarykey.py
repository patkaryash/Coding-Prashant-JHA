# Dict = {"B":2,"A":1,"C":3}
# Asc = sorted(Dict.items())
# Des = sorted(Dict.items(),reverse=True)
# Asc = dict(Asc)
# Des = dict(Des)
# print("Ascending Order by key:",Asc)
# print("Descending Order by Value:",Des)

# #Remove all elements from a dictionary 
# a = {"A":1,"B":2,"C":3}
# a.clear()
# print(a)

#Count the number of non empty values in a dictionary 
dict1 = {"A":1,"B":"","C":"3","D":None,"E":"Five"}
count = 0
for i in dict1.values():
    if i:
        count+=1
print("Number of non empty values:",count)