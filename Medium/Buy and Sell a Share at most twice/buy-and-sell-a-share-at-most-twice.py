from typing import List

class Solution:
    def maxProfit(self, n: int, prices: List[int]) -> int:
        if n <= 1:
            return 0

        # Initializing arrays to store the maximum profit at each day
        # for one transaction from left to right and from right to left
        max_profit_left = [0] * n
        max_profit_right = [0] * n

        # Forward pass to calculate the maximum profit from left to right
        min_price = prices[0]
        for i in range(1, n):
            max_profit_left[i] = max(max_profit_left[i-1], prices[i] - min_price)
            min_price = min(min_price, prices[i])

        # Backward pass to calculate the maximum profit from right to left
        max_price = prices[n-1]
        for i in range(n-2, -1, -1):
            max_profit_right[i] = max(max_profit_right[i+1], max_price - prices[i])
            max_price = max(max_price, prices[i])

        # Finding the maximum profit by combining the profits from left and right
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, max_profit_left[i] + max_profit_right[i])

        return max_profit



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.maxProfit(n, price)
        
        print(res)
        

# } Driver Code Ends