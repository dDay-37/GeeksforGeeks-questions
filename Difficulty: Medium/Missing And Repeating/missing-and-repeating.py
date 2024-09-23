#User function Template for python3
from collections import Counter
class Solution:
    def findTwoElement( self,arr): 
        # code here
        x=Counter(arr)
        # print(x)
        twice=-1
        cur=1
        f1=0
        f2=0
        for i in x:
            if f1==0:
                if i==cur:
                    cur+=1
                else:
                    f1=1
            if f2==0:
                if x[i]==2:
                    twice=i
        return twice,cur


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends