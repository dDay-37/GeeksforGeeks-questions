from typing import List

class Solution:
    def solve(self,dp,ind,coins,summ):
        if ind==len(coins):
            if summ==0:
                return False
            if  summ==2024 or summ%20==0 or summ%24==0:
                return True
            else:
                return False
        if dp[ind][summ]!=None:
            return dp[ind][summ]

        dp[ind][summ]=self.solve(dp,ind+1,coins,summ+coins[ind]) or self.solve(dp,ind+1,coins,summ)
        return dp[ind][summ]
    def isPossible(self, N : int, coins : List[int]) -> bool:
        # code here
        dp=[[None]*2025]*367
        return self.solve(dp,0,coins,0)

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
        
        N = int(input())
        
        
        coins=IntArray().Input(N)
        
        obj = Solution()
        res = obj.isPossible(N, coins)
        
        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends