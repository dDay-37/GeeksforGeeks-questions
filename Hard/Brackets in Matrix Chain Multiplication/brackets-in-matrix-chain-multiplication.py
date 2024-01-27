#User function Template for python3
class Solution:
    def matrixChainOrder(self, p, n):
        # Create a 2D table to store the minimum number of multiplications
        # and the position to split the chain for optimal parenthesization
        dp = [[0] * n for _ in range(n)]
        split = [[''] * n for _ in range(n)]

        # Fill the dp table using bottom-up dynamic programming
        for length in range(2, n):
            for i in range(1, n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')  # Initialize with infinity

                for k in range(i, j):
                    cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        split[i][j] = k

        # Build the optimal parenthesization string
        return self.constructParenthesis(split, 1, n - 1)

    def constructParenthesis(self, split, i, j):
        if i == j:
            return chr(ord('A') + i - 1)
        else:
            left = self.constructParenthesis(split, i, split[i][j])
            right = self.constructParenthesis(split, split[i][j] + 1, j)
            return '({}{})'.format(left, right)


#{ 
 # Driver Code Starts

def get(p, n):
    m = [[0] * n for _ in range(n)]
    for i in range(1, n):
        m[i][i] = 0

    for L in range(2, n):
        for i in range(1, n - L + 1):
            m[i][i + L - 1] = float('inf')
            for k in range(i, i + L - 1):
                q = m[i][k] + m[k + 1][i + L - 1] + p[i - 1] * p[k] * p[i + L - 1]
                if q < m[i][i + L - 1]:
                    m[i][i + L - 1] = q

    return m[1][n - 1]

def find(s, p):
    arr = []
    ans = 0
    for t in s:
        if t == '(':
            arr.append((-1, -1))
        elif t == ')':
            b = arr.pop()
            a = arr.pop()
            arr.pop()
            arr.append((a[0], b[1]))
            ans += a[0] * a[1] * b[1]
        else:
            arr.append((p[ord(t) - ord('A')], p[ord(t) - ord('A') + 1]))

    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    ob = Solution()
    result = ob.matrixChainOrder(p, n)
    
    if find(result, p) == get(p, n):
        print("True")
    else:
        print("False")

# } Driver Code Ends