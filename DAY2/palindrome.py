#WAP to check if a string is a palindrome or not
s = "racecar"
print(s) #left to right
print(s[::-1]) #right to left

if s == s[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")