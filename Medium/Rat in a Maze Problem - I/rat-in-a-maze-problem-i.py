#User function Template for python3

class Solution:
    def findPath(self, m, n):
        dir='DLRU'
        dc=[0,-1,1,0]
        dr=[1,0,0,-1]
        def f(r,c,m,n,ans,cur):
            if r==n-1 and c==n-1:
                ans.append(cur)
                return
            m[r][c]=0
            for i in range(4):
                nr=r+dr[i]
                nc=c+dc[i]
                if 0<=nr<n and 0<=nc<n and m[nr][nc]==1:
                    cur+=dir[i]
                    f(nr,nc,m,n,ans,cur)
                    cur=cur[:-1]
            m[r][c]=1
            
        
        if m[0][0]!=0 and m[n-1][n-1]!=0:
            ans=[]
            cur=""
            f(0,0,m,n,ans,cur)
            # print(ans)
            return ans
        return [-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends