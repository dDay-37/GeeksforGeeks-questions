#User function Template for python3

class Solution:
    def maxVolume(self, p, a):
        x = (p - math.sqrt(p ** 2 - 24 * a)) / 12
        V = (p * x ** 2 - 8 * x ** 3) / 4
        return round(V, 2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        perimeter, area = [int(x) for x in input().split()]

        ob = Solution()
        print('%.2f' % ob.maxVolume(perimeter, area))

# } Driver Code Ends