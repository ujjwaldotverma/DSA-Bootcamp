arr = [ -1, 2, -3, 4, 5, 6, -7, 8, 9 ]

l=0
r=len(arr)-1

while l<r:
    if arr[l]<0 and arr[r]>0:
        l+=1 
        r-=1 
    elif arr[l]>0 and arr[r]<0:
        arr[l],arr[r]=arr[r],arr[l]
    elif arr[l]<0 and arr[r]<0:
        l+=1 
    else:
        r-=1
        
print(arr)
