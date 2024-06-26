class Solution:
    def findCoverage(self, matrix):
        # Code here
        countOne=0
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if(i - 1 >= 0 and matrix[i - 1][j] == 1):
                        countOne += 1
                    if(i + 1 < n and matrix[i + 1][j] == 1):
                        countOne += 1
                    if(j - 1 >= 0 and matrix[i][j - 1] == 1):
                        countOne += 1
                    if(j + 1 < m and matrix[i][j + 1] == 1):
                        countOne += 1
        return countOne


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.findCoverage(matrix)
        print(ans)

# } Driver Code Ends