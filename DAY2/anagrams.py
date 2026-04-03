#WAP to check if two strings are anagrams or not
s1 = "listen"
s2 = "silent"
if sorted(s1) == sorted(s2):

    print("Strings are anagrams")
else:
    print("Strings are not anagrams")
