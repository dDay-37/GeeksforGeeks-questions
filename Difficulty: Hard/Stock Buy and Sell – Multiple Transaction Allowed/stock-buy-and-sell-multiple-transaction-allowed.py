from typing import List

class Solution:
    def maximumProfit(self, prices) -> int:
        # Code here
        n = len(prices)
        maxPrice = 0
        left, right = 0, 0
        while right < n - 1:
            if prices[right] <= prices[right + 1]:
                profit = prices[right + 1] - prices[left]
                maxPrice += profit
            right += 1
            left += 1
        return maxPrice
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)

# } Driver Code Ends