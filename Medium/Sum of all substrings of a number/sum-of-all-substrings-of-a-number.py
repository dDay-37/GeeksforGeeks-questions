#User function Template for python3
class Solution:
    def sumSubstrings(self,s):
        MOD = 10**9 + 7
        n = len(s)
        total_sum = 0

        multiplier = 1
        for i in range(n - 1, -1, -1):
            total_sum = (total_sum + int(s[i]) * multiplier * (i + 1)) % MOD
            multiplier = (multiplier * 10 + 1) % MOD

        return total_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        ob=Solution()
        print(ob.sumSubstrings(s))
# } Driver Code Ends