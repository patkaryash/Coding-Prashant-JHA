mydict = {
    101: "yash",
    102: "siddharth",
    "103": "prashant",
    "104": "satyarth",
    101:"ashish", #when we have duplicate keys in a dictionary then the last value will be assigned to that key and the previous value will be overwritten
    104:"ashish"
}
print(mydict) #prints the whole dictionary
print(type(mydict)) #dictionary is a collection of key-value pairs which are unordered, changeable and indexed. No duplicate members.