# WAP to calculate and return the sum of distances between adjacent numbers in an array

def sum_of_adjacent_distances(arr):
    total = 0
    for i in range(1, len(arr)):
        total += abs(arr[i] - arr[i - 1])
    return total


# Example
A = [1, 4, 2, 8, 5]
print(sum_of_adjacent_distances(A))
