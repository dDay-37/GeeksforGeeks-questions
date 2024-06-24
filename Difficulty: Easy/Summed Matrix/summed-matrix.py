class Solution:
    def sumMatrix(self, n, q):
        # Code here
        if 2 <= q <= n + 1:
            return q - 1
        elif n + 1 < q <= 2 * n:
            return 2 * n - q + 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends