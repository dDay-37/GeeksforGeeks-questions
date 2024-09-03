#User function Template for python3
class Solution:
	def minOperations(self, str1, str2):
		s1=list(str1)
		s2=list(str2)
		n1=len(s1)
		n2=len(s2)
		dp=[[0]*(n2+1) for _ in range(n1+1)]
        for x in range(n1+1):
            dp[x][0]=x
        for y in range(n2+1):
            dp[0][y]=y
        # for row in dp:
        #     print(row)
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if s1[i-1]!=s2[j-1]:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1
                else:
                    dp[i][j]=dp[i-1][j-1]
        # for row in dp:
        #     print(row)
        return dp[-1][-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s1, s2 = input().split()
        ob = Solution()
        ans = ob.minOperations(s1, s2)
        print(ans)

# } Driver Code Ends