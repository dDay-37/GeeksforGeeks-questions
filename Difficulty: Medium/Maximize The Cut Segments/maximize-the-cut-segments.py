#User function Template for python3

import sys
sys.setrecursionlimit(10 **  6)

class Solution:
    
    # Function to find the maximum number of cuts.
    def maximizeTheCuts(self, n, x, y, z):
        # Code here
        def execute(num):
            if num == 0:
                return 0
            
            if dp[num] != -1:
                return dp[num]
            takeX = takeY = takeZ = float('-inf')
            
            if num >= x:
                takeX = execute(num - x) + 1
            
            if num >= y:
                takeY = execute(num - y) + 1
            
            if num >= z:
                takeZ = execute(num - z) + 1
            
            dp[num] = max(takeX, takeY, takeZ)
            return dp[num]
        dp = [-1 for _ in range(n + 1)]
        result = execute(n)
        return max(0, result)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(Solution().maximizeTheCuts(n,x,y,z))
# } Driver Code Ends