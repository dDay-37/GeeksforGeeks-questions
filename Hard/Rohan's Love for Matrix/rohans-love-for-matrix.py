#User function Template for python3
class Solution:
    def firstElement (self, n):
        # Code here
        mod = ((10 ** 9) + 7)
        result = [1, 1]
        for i in range(n - 1):
            result[0], result[1] = (result[0] + result[1]) % mod, result[0]
        return result[1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.firstElement(n))
# } Driver Code Ends