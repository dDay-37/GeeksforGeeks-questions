class Solution:
    def countFreq(self, arr, target):
        cnt=0
        for i in range(len(arr)):
            if arr[i]>target:
                return cnt
            if arr[i]==target:
                cnt+=1
        return cnt
            
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countFreq(A, D)
        print(ans)
        print("~")

# } Driver Code Ends