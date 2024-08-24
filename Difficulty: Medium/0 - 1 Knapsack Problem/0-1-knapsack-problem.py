class Solution:
    
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val):
        # Code here
        weightLength = len(wt)
        
        dp = [[0 for _ in range(W + 1)] for _ in range(weightLength + 1)]
        
        for i in range(1, weightLength + 1):
            for weight in range(1, W + 1):
                if wt[i - 1] <= weight:
                    dp[i][weight] = max(dp[i - 1][weight], dp[i - 1][weight - wt[i - 1]] + val[i - 1])
                else:
                    dp[i][weight] = dp[i - 1][weight]
        
        return dp[weightLength][W]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        # n = int(input())
        W = int(input())
        val = list(map(int, input().strip().split()))
        wt = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapSack(W, wt, val))

# } Driver Code Ends