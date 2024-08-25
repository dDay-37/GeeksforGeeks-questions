# User function Template for python3

from bisect import bisect_right
from math import log

class Solution:
    
     # Function to count number of pairs such that x^y is greater than y^x.     
    def countPairs(self, arr, brr):
        # Code here
        """
            x^y > y^x
            y logx > x logy
            y / logy > x / logx
            logy / y < logx/x
        """
        arrLength = len(arr)
        brrLength = len(brr)
        a = [] * arrLength
        b = [] * brrLength
        count = 0
        for y in arr:
            a.append(log(y) / y)
            
        for x in brr:
            b.append(log(x) / x)
        
        a.sort()
        b.sort()
        
        for i in range(brrLength):
            index = bisect_right(a, b[i])
            count += arrLength - index
        
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

import atexit
import io
import sys
import bisect

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        # M, N = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countPairs(a, b))
        #code here

# } Driver Code Ends