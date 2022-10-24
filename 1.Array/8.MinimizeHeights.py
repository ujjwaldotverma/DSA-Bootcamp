class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        if n==1:
            return 0
        arr.sort()
        diff = arr[n-1]-arr[0]
        intmin = intmax = 0
        for i in range(1,n):
            if arr[i]-k<0:
                continue
            intmax = max(arr[i-1]+k , arr[n-1]-k)
            intmin = min(arr[0]+k , arr[i]-k)
            
            diff = min(diff,intmax-intmin)
        return diff


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1
