#User function Template for python3

class Solution:
	def swapElements(self, arr, n):
	    #Code here
	    for i in range(n-2):
	       # print(arr[i],arr[i+2])
	        arr[i],arr[i+2]=arr[i+2],arr[i]
        return arr


#{ 
 # Driver Code Starts

#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        obj.swapElements(arr, n);
        for i in arr:
            print(i, end = " ")
        print()
# } Driver Code Ends