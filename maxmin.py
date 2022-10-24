arr=[1,2,3,4,5]


minarr = float('inf')
maxarr = float('-inf')

for i in range(len(arr)):
    if arr[i]>maxarr:
        maxarr = arr[i]
    if arr[i]<minarr:
        minarr = arr[i]
print(minarr,maxarr)
