class Solution:
    # Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        # Your code here
        result = arrSum = -1e9
        for a in arr:
            arrSum = max(a, arrSum + a)
            result = max(result, arrSum)

        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends