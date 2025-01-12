
# class Solution:
#     def maxWater(self, arr):
#         # code here
#         cur=arr[0]
#         cur_ind=0
#         w=0
#         for i in range(len(arr)):
#             if arr[i]>=cur:
#                 w+=arr[i]*(i-cur_ind)
#                 cur_ind=i
#                 cur=arr[i]
#         if cur_ind<len(arr)-1:
#             w+=arr[-1]*(len(arr)-1-cur_ind)
#         return w

class Solution:
    def maxWater(self, arr):
        n = len(arr)
        if n < 3:
            return 0
        # Initialize arrays to store the left and right maximum heights
        left_max = [0] * n
        right_max = [0] * n
        # Fill left_max array
        left_max[0] = arr[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], arr[i])
        # Fill right_max array
        right_max[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i])
        # Calculate trapped water
        trapped_water = 0
        for i in range(n):
            trapped_water += max(0, min(left_max[i], right_max[i]) - arr[i])
        return trapped_water

#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends