#User function Template for python3

import sys

class Solution:
    # Complete this function
    # Function to find the maximum occurred integer in all ranges.
    def maxOccured(self, n, l, r, maxx):
        # Your code here
        x = [0] * (maxx + 2)
        for i in range(n):
            x[l[i]] += 1
            x[r[i] + 1] -= 1

        result = sum = 0
        maxFrequency = -sys.maxsize - 1
        for i in range(maxx + 1):
            sum += x[i]
            if sum > maxFrequency:
                maxFrequency = sum
                result = i

        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

A = [0] * 1000000


def main():

    T = int(input())

    while (T > 0):

        global A
        A = [0] * 1000000

        n = int(input())

        l = [int(x) for x in input().strip().split()]
        r = [int(x) for x in input().strip().split()]

        maxx = max(r)
        ob = Solution()
        print(ob.maxOccured(n, l, r, maxx))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends