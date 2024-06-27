def isToeplitz(mat):
    # Code here
    n = len(mat)
    m = len(mat[0])
    def isToeplitzValid(x, y):
        return x < n and y < m
    for i in range(0, n):
        for j in range(0, m):
            if isToeplitzValid(i + 1, j + 1) and mat[i][j] != mat[i + 1][j + 1]:
                return False
    return True


#{ 
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(m)] for j in range(n)]
        k = 0
        for i in range(n):
            for j in range(m):
                matrix[i][j] = arr[k]
                k += 1
        b = isToeplitz(matrix)

        if b == True:
            print("true")
        else:
            print("false")

# } Driver Code Ends