#1st sol, O(n) S.C
class Solution:
    def sort012(self,arr,n):
        zero = 0
        one = 0
        two = 0
        for i in range(len(arr)):
            if arr[i]==0:
                zero+=1
            elif arr[i]==1:
                one+=1
            else:
                two+=1
        for i in range(len(arr)):
            if i<zero:
                arr[i]=0
            elif i<zero+one:
                arr[i]=1
            elif i<zero+one+two:
                arr[i]=2

#2nd sol, O(1) S.C
class Solution:
    def sort012(self,arr,n):
        # code here
        l, m, h = 0, 0, n-1
        
        while m <= h:
            if arr[m] == 0:
                arr[m],arr[l] = arr[l], arr[m]
                l += 1
                m += 1
            
            elif arr[m] == 1:
                m += 1
            
            else:
                arr[m], arr[h] = arr[h], arr[m]
                h -= 1
#main fn
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()
