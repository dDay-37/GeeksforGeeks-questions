# User function Template for Python3

class Solution:
    def maxGold(self, n, m, arr):
        for j in range(m-2, -1, -1):
            for i in range(n):
                if i == 0 and i == n-1:
                    arr[i][j] += arr[i][j+1]
                elif i == 0:
                    arr[i][j] += max(arr[i][j+1], arr[i+1][j+1])
                elif i == n-1:
                    arr[i][j] += max(arr[i][j+1], arr[i-1][j+1])
                else:
                    arr[i][j] += max(arr[i+1][j+1], max(arr[i][j+1], arr[i-1][j+1]))
        maxi = float('-inf')
        for i in range(n):
            if maxi < arr[i][0]:
                maxi = arr[i][0]
        return maxi

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends