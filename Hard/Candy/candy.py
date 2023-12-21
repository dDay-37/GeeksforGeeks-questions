#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minCandy(self, n, r):
        l = [1]*n
        for i in range(1, n):
            if r[i] > r[i-1]:
                l[i] = l[i-1]+1
            else:
                l[i]=1
                j=i
                while j>0 and r[j-1] > r[j] and l[j-1] <= l[j]:
                    l[j-1] = l[j]+1
                    j-=1

        return sum(l)
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ratings = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCandy(N, ratings)
        print(res)
# } Driver Code Ends