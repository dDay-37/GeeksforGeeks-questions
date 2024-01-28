# User function Template for python3

from typing import List
from math import factorial,log2


class Solution:
    def findNthNumber(self, n : int, k : int ) -> int:
        # Code here
        def combination(n, r):
            return factorial(n) // (factorial(r) * factorial(n - r)) if n >= r else 0
        
        def countset(x, k):
            if k==0:
                return 1
            if x==0:
                return 0
            h = int(log2(x))
            if h < k - 1:
                return 0
            return combination(h, k) + countset(x ^ (1 << h), k - 1)
        
        def total(x, k):
            return sum(countset(x, i) for i in range(k + 1))
            
        lowest_num, highest_num = 0, 10**15
        while lowest_num < highest_num:
            middle_num = lowest_num + (highest_num - lowest_num) // 2
            if total(middle_num, k) >= n:
                highest_num = middle_num
            else:
                lowest_num = middle_num + 1
        return lowest_num



#{ 
 # Driver Code Starts



if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,k=map(int,input().split())
        
        obj = Solution()
        res = obj.findNthNumber(n,k)
        
        print(res)
        

# } Driver Code Ends