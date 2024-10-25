class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        result = []
        leftElement, rightElement = 0, len(arr) - 1
        
        while leftElement <= rightElement:
            if leftElement <= rightElement:
                result.append(arr[rightElement])
                rightElement -= 1
                
            if leftElement <= rightElement:
                result.append(arr[leftElement])
                leftElement += 1
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends