#User function Template for python3


class Solution:
    def optimalStrategyOfGame(self, n, arr):
        # Code here
        memory = {}
        def dfs(left, right):
            if(left, right) in memory:
                return memory[(left, right)]
            if left > right:
                return 0
            positionOne = arr[left] + min(dfs(left + 1, right - 1), dfs(left + 2, right))
            positionTwo = arr[right] + min(dfs(left, right - 2), dfs(left + 1, right - 1))
            
            maximum = max(positionOne, positionTwo)
            memory[(left, right)] = maximum
            return memory[(left, right)]
        return dfs(0, n - 1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        ob = Solution()
        print(ob.optimalStrategyOfGame(n,arr))

# } Driver Code Ends