class Solution:
    def nthPoint(self, N):
        if N == 1:
            return 1
        dp = [0] * (N + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, N + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % (10**9 + 7)
        
        return dp[N]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthPoint(n)
		print(ans)
# } Driver Code Ends