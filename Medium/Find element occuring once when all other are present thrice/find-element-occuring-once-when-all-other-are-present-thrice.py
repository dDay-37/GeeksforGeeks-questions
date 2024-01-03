#User function Template for python3

class Solution:
    def singleElement(self, arr, N):
        # code here 
        arr.sort()
        p=arr[0]
        c=1
        # print(arr)
        for i in arr[1:]:
            # print(p,i,c)
            if i==p:
                c+=1
            else:
                if c<3:
                    return p
                c=1
                p=i
        return arr[-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.singleElement(arr,N))
# } Driver Code Ends