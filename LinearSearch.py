def LinearSearch(arr,x):
    for i in arr:
        if arr[i]==x:
            return i
    return -1
arr = [int (x) for x in input("Enter the array: \n").split()]
x = int(input("Enter the element to be searched: \n"))
index = LinearSearch(arr, x)
print("Element is at index:",index)
