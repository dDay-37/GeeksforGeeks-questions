#User function Template for python3
class Solution:
    def countStrings(self, N):
        MOD = int(1e9) + 7
        dp0 = [0] * (N + 1)
        dp1 = [0] * (N + 1)
        dp0[1] = dp1[1] = 1
        for i in range(2, N + 1):
            dp0[i] = (dp0[i - 1] + dp1[i - 1]) % MOD
            dp1[i] = dp0[i - 1]
        return (dp0[N] + dp1[N]) % MOD

#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.countStrings( n)
        print(ans)
        tc=tc-1
# } Driver Code Ends