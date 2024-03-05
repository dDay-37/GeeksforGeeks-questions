#User function Template for python3

class Solution:
    # Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self, a, n): 
        # Your code here
        left = [0]*(n)
        right = [0]*(n)
        
        left[0] = a[0]
        right[n-1] = a[n-1]
        for i in range(1, n):
            left[i] = min(a[i], left[i-1])
        for j in range(n-2, -1, -1):
            right[j] = max(a[j], right[j+1])
        
        i = 0
        j = 0
        maxx = -1
        while (i<n and j<n):
            if right[j] >= left[i]:
                maxx = max(maxx, j-i)
                j += 1
            else:
                i += 1
        return maxx

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends