
class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        # Code here
        arr.sort(reverse = True)
        return sum(1 for i, x in enumerate(arr) if x > i)


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.hIndex(arr)

        print(result)
        print("~")

# } Driver Code Ends