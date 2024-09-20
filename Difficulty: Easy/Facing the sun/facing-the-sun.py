#User function Template for python3

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        c=0
        m=float('-inf')
        for i in height:
            if i>m:
                m=i
                c+=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        height = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(height)
        print(ans)

# } Driver Code Ends