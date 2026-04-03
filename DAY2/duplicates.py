#WAP to remove duplicates from a string using for loop
s = "aabbcc"
result = ""
for i in s:
    if i not in result:
        result += i
print(s)
print(result)
