#User function Template for python3

class Solution:
    def getMinDiff(self, k, arr):
        # Code here
        arr.sort()
        result = arr[-1] - arr[0]
        
        for i in range(1, len(arr)):
            minHeight = min(arr[0] + k, arr[i] - k)
            maxHeight = max(arr[i - 1] + k, arr[-1] - k)
            result = min(result, maxHeight - minHeight)
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.getMinDiff(k, arr)
        print(res)
        print("~")

# } Driver Code Ends