#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from collections import Counter
class Solution:
    
    def getSingle(self,arr):
        # code here
        c=Counter(arr)
        for i in c:
            if c[i]%2==1:
                return i
        return -1


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        # k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getSingle(arr)
        print(res)
        t -= 1


# } Driver Code Ends