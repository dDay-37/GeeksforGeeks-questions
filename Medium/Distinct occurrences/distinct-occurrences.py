class Solution:
    def sequenceCount(self,s, t):
        def solve(i,j,n,m):
            if i==n:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if s[i]==t[j]:
                if j==m-1:
                    dp[(i,j)]=(1+solve(i+1,j,n,m))%(10**9+7)
                    return dp[(i,j)]
                else:
                    ans=solve(i+1,j,n,m)%(10**9+7)
                    ans+=solve(i+1,j+1,n,m)%(10**9+7)
                    ans%=(10**9+7)
                    dp[(i,j)]=ans
                    return ans
            else:
                dp[(i,j)]=solve(i+1,j,n,m)%(10**9+7)
                return dp[(i,j)]

        dp={}
        return solve(0,0,len(s),len(t))


#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        print(Solution().sequenceCount(str(arr[0]), str(arr[1])))
# } Driver Code Ends