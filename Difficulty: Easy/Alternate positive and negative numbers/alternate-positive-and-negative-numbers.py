#User function Template for python3

from itertools import zip_longest

class Solution:
    def rearrange(self, arr):
        positive = [item for item in arr if item >= 0]
        negative = [item for item in arr if item < 0]
        
        arr[:] = [x for pair in zip_longest(positive, negative)\
            for x in pair if x is not None]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends