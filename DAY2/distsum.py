# WAP to calculate and return the sum of distances between adjacent numbers in an array
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    val = int(input("Enter the element: "))
    arr.append(val)

total = 0
print(arr)
for i in range(n - 1):
    total += abs(arr[i] - arr[i + 1])

print("The sum of distances between adjacent numbers in the array is:", total)
