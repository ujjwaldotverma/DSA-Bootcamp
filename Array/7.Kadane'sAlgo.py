#sol1
class Solution:
    def maxSubArraySum(self,arr,N):
        maxsofar = arr[0]
        maxhere = arr[0]
        for i in range(1,N):
            maxhere = max(arr[i], maxhere + arr[i])
            maxsofar = max(maxsofar,maxhere)
        return maxsofar

import math
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
