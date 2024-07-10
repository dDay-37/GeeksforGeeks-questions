from typing import List

class Solution:
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:
        memo = {}
        def dp(i,j):
            if i >= n or j >= m:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if mat[i][j] == 1:
                ans = min(dp(i+1,j), dp(i,j+1), dp(i+1,j+1)) + 1
                memo[(i,j)] = ans
                return ans
            memo[(i,j)] = 0
            return 0

        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, dp(i,j))

        return ans


#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n, m = map(int, input().split())

        mat = IntMatrix().Input(n, m)

        obj = Solution()
        res = obj.maxSquare(n, m, mat)

        print(res)

# } Driver Code Ends