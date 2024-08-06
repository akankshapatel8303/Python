def linear_search(arr, target):
    for i in range(len(arr)):
        if(arr[i] == target):
            return i
    return -1

arr = [11, 20, 8, 5, 23, 9, 1]
target = 40
print(linear_search(arr, target))