class Solution:
    def swapNibbles (self, n):
        # Code here
        binaryN = bin(n)[2:]
        if len(binaryN) < 8:
            binaryN = "".join(['0' for _ in range(8 - len(binaryN))]) + binaryN
        return int(binaryN[4:] + binaryN[0:4], 2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.swapNibbles(n))

# } Driver Code Ends