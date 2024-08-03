class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self, n, m, s1, s2):
        dp=[[0]*(m+1) for _ in range(n+1)]
        # for row in dp:
        #     print(row)
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, m = map(int, input().strip().split())
        str1 = str(input())
        str2 = str(input())
        ob = Solution()
        print(ob.lcs(n, m, str1, str2))

# } Driver Code Ends