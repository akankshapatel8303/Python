def binary_search(arr, target):
    start = 0
    end = len(arr)-1

    while(start<=end):
        mid = (start+end)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid] < target):
            start = mid+1
        else:
            end = mid-1
    return -1

arr = [1, 2, 4, 6, 9, 12]
target = 12
print(binary_search(arr, target))
