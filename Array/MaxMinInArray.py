arr=[1,2,3,4,5]


minarr = float('inf')        #min
maxarr = float('-inf')       #max

for i in range(len(arr)):    #main algo
    if arr[i]>maxarr:
        maxarr = arr[i]
    if arr[i]<minarr:
        minarr = arr[i]
print(minarr,maxarr)
