class Solution:
    def isMaxHeap(self, arr, n):
        # Your code goes here
        for item in range(1, n):
            parentNode = (item + 1) // 2
            if arr[parentNode - 1] < arr[item]:
                return False
        return True


#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends