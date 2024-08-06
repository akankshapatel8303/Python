def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [23, 12, 40, 34, 11, 33, 2]
print(bubble_sort(arr))