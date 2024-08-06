def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while(arr[j] > key) and (j>=0):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

arr = [11, 3, 30, 24, 12, 40]
print(insertion_sort(arr))