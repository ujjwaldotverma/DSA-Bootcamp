class Solution:
    def getPairsCount(self, arr, n, k):
        unordered_map = {}
        count = 0
        for i in range(n):
            if k - arr[i] in unordered_map:
                count += unordered_map[k - arr[i]]
            if arr[i] in unordered_map:
                unordered_map[arr[i]] += 1
            else:
                unordered_map[arr[i]] = 1
        return count

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc-=1
