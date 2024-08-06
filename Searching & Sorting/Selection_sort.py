def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            while(arr[j] < arr[min_idx]):
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

arr = [12, 9, 30, 23, 11, 8, 10]
print(selection_sort(arr))
