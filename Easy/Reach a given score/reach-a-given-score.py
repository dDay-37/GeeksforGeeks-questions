#User function Template for python3

class Solution:
    def count(self, n: int) -> int:
        #your code here
        ar=[0]*(n+1)
        ar[0]=1
        for i in range(3,n+1):
            ar[i]+=ar[i-3]
        for j in range(5,n+1):
            ar[j]+=ar[j-5]
        for k in range(10,n+1):
            ar[k]+=ar[k-10]
        # print(ar)
        return ar[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        ob = Solution()
        print(ob.count(n))
        
# } Driver Code Ends