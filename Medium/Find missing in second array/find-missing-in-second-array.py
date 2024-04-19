#User function Template for python3

from collections import defaultdict

class Solution:
    def findMissing(self, a, b, n, m):
        # Code here
        result = []
        dKaDict = defaultdict(int)
        for i in b:
            dKaDict[i] = 1
            
        for i in a:
            if dKaDict[i] == 0:
                result.append(i)
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
   # n=int(input())
    l = list(map(int, input().split()))
    n=l[0]
    m=l[1]
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    ob=Solution()
    ans=ob.findMissing(a,b,n,m)
    for each in ans:
        print(each,end=' ')
    print()
# } Driver Code Ends