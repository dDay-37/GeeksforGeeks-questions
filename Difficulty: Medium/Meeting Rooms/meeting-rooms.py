#User function Template for python3
class Solution:
    def canAttend(self, arr):
        # Sort meetings by their start times
        arr.sort(key=lambda x: x[0])
        
        # Check for overlaps in the sorted list
        for i in range(1, len(arr)):
            # If the current meeting starts before the previous one ends, return False
            if arr[i][0] < arr[i - 1][1]:
                return False
                
        # If no overlaps are found, return True
        return True

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.canAttend(arr)
        if ans:
            print("true")
        else:
            print("false")

# } Driver Code Ends