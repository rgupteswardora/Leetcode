#User function Template for python3


class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        a,b=1,2
        rt=[-1]*n
        stack=[]
        stack.append(0)
        for i in range(1,n):
            if arr[i]<=arr[i-1]:
                stack.append(i)
            if arr[i]>arr[i-1]:
                po=stack[-1]
                while(b>a):
                    if(len(stack))>0:
                        po=stack.pop()
                        if(arr[po]>arr[i]):
                            stack.append(po)
                            stack.append(i)
                            break
                        rt[po]=arr[i]
                    else:
                        break
                stack.append(i)
        return rt
#{ 
#  Driver Code Starts
#Initial Template for Python 3
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
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends