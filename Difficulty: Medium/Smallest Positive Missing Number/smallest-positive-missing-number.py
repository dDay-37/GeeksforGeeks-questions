#User function Template for python3
class Solution:
    
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        # Your code here
        visit = set(arr)
        i = 1
        while(i in visit):
            i += 1
        return i
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends