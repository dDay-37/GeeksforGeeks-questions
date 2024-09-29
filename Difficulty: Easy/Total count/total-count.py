#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def totalCount(self, k, arr):
        c = 0
        for i in arr:
            if i % k == 0:
                c = c + (i // k)
            else:
                c = c + (i // k) + 1
        return c        # code here

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.totalCount(k,arr)
        print(res)
        t -= 1


# } Driver Code Ends