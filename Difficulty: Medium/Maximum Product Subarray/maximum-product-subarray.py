#User function Template for python3
class Solution:
    # Function to find maximum
    # Product subarray
    def maxProduct(self, arr):
        # Code here
        maxProd = -float('inf')
        if len(arr) == 1:
            return arr[0]
        
        for i in range(len(arr) - 1):
            product = arr[i]
            maxProd = max(maxProd, product)
            if arr[i] != 0:
                for j in range(i + 1, len(arr)):
                    if arr[j] == 0:
                        break
                    product *= arr[j]
                    maxProd = max(maxProd, product)
        return maxProd

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends