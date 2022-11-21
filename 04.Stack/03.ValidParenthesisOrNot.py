class Solution:
    def ispar(self,x):
        s=[]
        for char in x:
            if char in '({[':
                s.append(char)
            elif char is ')':
                if (not s or s[-1] !=  '('):
                    return False
                s.pop()
            elif char is '}':
                if (not s or s[-1] !=  '{'):
                    return False
                s.pop()
            elif char is ']':
                if (not s or s[-1] !=  '['):
                    return False
                s.pop()
        if (not s):
            return True
        return False
#DRIVER CODE
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends
