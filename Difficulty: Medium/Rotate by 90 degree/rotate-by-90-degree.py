#User function Template for python3
def rotate(mat):
    arr1 = []
    for i in range(len(mat)):
        arr2 = []
        for j in range(len(mat) - 1, -1, -1):
            arr2.append(mat[j][i])
        arr1.append(arr2)
    mat[:] = arr1
    #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        matrix = []
        for i in range(N):
            arr = [int(x) for x in input().strip().split()]
            matrix.append(arr)

        rotate(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j], end=' ')
            print()
        print("~")

# } Driver Code Ends