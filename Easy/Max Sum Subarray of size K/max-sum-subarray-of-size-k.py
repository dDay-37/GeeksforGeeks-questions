#User function Template for python3
class Solution:
    def maximumSumSubarray (self,k,arr,n):
        # code here 
        s=sum(arr[:k])
        c=sum(arr[:k])
        for i in range(0,n-k):
            c=c-arr[i]+arr[i+k]
            # print(i,c)
            s=max(s,c)
        return s

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends