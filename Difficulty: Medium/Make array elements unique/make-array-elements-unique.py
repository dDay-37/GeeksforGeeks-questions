#User function Template for python3

class Solution:
    def minIncrements(self, arr): 
        arr.sort()
        cnt = 0
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                cnt += arr[i - 1] + 1 - arr[i]
                arr[i] = arr[i - 1] + 1
        return cnt
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr))

        T -= 1

# } Driver Code Ends