#User function Template for python3


class Solution:
    # Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        n = len(mat)
        
        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        # Step 2: Reverse each column
        for i in range(n):
            for j in range(n // 2):
                mat[j][i], mat[n - 1 - j][i] = mat[n - 1 - j][i], mat[j][i]
        
        # The matrix is now rotated 90 degrees anticlockwise
        return mat

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        n = int(data[index])
        index += 1
        matrix = []
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.rotateby90(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()

        print("~")

# } Driver Code Ends