def binarySearch(arr,x):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            start = mid + 1
        else:
            end = mid - 1
    return -1    
arr = [int (x) for x in input("Enter the array: \n").split()]
x = int(input("Enter the element to be searched: \n"))
index = binarySearch(arr, x)
print("Element is at index:",index)
