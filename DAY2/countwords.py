#WAP to count a word in a string using for loop
s = "yash patkar"
count = 0
for i in s:
    if i==" ":
        count += 1
print("Number of words in the string:", count + 1)