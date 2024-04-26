#User function Template for python3

# User function Template for python3

class Solution:
	def FindExitPoint(self, n, m, matrix):
		# Code here
		row, col = 0, 0
		xDirection, yDirection = 0, 1
		while(0 <= row < n and 0 <= col < m):
		    if matrix[row][col] == 1:
		        matrix[row][col] = 0
		        if xDirection == 0:
		            xDirection, yDirection = yDirection, xDirection
		        else:
		            xDirection, yDirection = yDirection,-xDirection
		    row += xDirection
		    col += yDirection
		return [max(0, min(row, n - 1)), max(0, min(col, m - 1))]

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
        ans = ob.FindExitPoint(n, m, matrix)
        for _ in ans:
            print(_, end=" ")
        print()

# } Driver Code Ends