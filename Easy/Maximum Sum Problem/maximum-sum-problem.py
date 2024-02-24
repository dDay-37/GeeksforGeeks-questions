#User function Template for python3

class Solution:
    def maxSum(self, n): 
        # code here 
        # print('n=',n)
        if n>=12 and n!= 0:
            return self.maxSum(n//2) + self.maxSum(n//3) + self.maxSum(n//4) 
        else:
            return n



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.maxSum(n))
# } Driver Code Ends