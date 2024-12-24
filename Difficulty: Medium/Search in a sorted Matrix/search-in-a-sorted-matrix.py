class Solution:
    def searchMatrix(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        
        # Binary search initialization
        low, high = 0, n * m - 1
        
        while low <= high:
            mid = (low + high) // 2
            row = mid // m
            col = mid % m
            
            # Access the element in the matrix
            mid_value = mat[row][col]
            
            if mid_value == x:
                return True
            elif mid_value < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return False


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.searchMatrix(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends