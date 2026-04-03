#WAP to remove duplicates from a list using for loop
A = [1,2,2,3,4,4,5]
result = []
for i in A:
    if i not in result:
        result.append(i)
print(A)
print(result)