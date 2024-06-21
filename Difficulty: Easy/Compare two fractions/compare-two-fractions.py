#User function Template for python3


class Solution:
    def compareFrac (self, str):
        a=str.strip().split(",")
        p=a[0].strip().split("/")
        q=a[1].strip().split("/")
        x=int(p[0])*int(q[1])
        y=int(q[0])*int(p[1])
        if x>y:
            return a[0]
        elif x<y:
            return a[1][1:]
        else:
            return "equal"
        # return ""



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends