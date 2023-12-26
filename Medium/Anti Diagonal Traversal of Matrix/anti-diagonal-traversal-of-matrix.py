#User function Template for python3

class Solution:
    def antiDiagonalPattern(self,m):
        a=[]
        n=len(m)
        x,y=0,0
        for i in range(n):
            x=i
            y=0
            while x>=0:
                a.append(m[y][x])
                x-=1
                y+=1
        for i in range(1,n):
            y=i
            x=n-1
            while y<=n-1:
                a.append(m[y][x])
                x-=1
                y+=1
        return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input()) 
        inp=list(map(int,input().split()))
        matrix=[]
        k = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(inp[k])
                k += 1
            matrix.append(row)
        ob = Solution()
        ans = ob.antiDiagonalPattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends