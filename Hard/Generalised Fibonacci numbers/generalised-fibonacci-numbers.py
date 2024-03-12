#User function Template for python3

# User function Template for python3

import numpy as np

class Solution:
    def genFibNum(self, a, b, c, n, m):
        # Code here
        if n <= 2:
            return 1
            
        result = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        
        genFibMatrix = np.array([
            [a, b, c],
            [1, 0, 0],
            [0, 0, 1]
        ])
        
        n -= 2
        
        while n:
            if n & 1:
                result = np.matmul(result, genFibMatrix) % m
            genFibMatrix = np.matmul(genFibMatrix, genFibMatrix) % m
                
            n >>= 1
        return sum(result[0]) % m
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b,c,n,m=map(int,input().split())
        
        ob = Solution()
        print(ob.genFibNum(a,b,c,n,m))
# } Driver Code Ends