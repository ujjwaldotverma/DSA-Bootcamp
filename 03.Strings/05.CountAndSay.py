#    https://leetcode.com/problems/count-and-say/
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        before = self.countAndSay(n-1)
        result = ""
        count = 1
        for i in range(len(before)):
            if i == len(before)-1 or before[i] != before[i+1]:
                result += str(count) + before[i]
                count = 1
            else:
                count += 1
        return result
