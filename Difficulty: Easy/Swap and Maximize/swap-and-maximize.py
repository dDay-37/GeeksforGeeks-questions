#User function Template for python3

class Solution:
    def maxSum(self, arr):
        # Sort the array to easily pick smallest and largest elements
        arr.sort()
        n = len(arr)
        
        # Arrange elements by alternating smallest and largest
        arranged = []
        for i in range(n // 2):
            arranged.append(arr[i])           # Pick from the start (smallest)
            arranged.append(arr[n - i - 1])   # Pick from the end (largest)
        
        if n % 2 != 0:  # If there is a middle element in an odd-length array, add it
            arranged.append(arr[n // 2])
        
        # Calculate the maximum sum of absolute differences
        max_sum = 0
        for i in range(1, n):
            max_sum += abs(arranged[i] - arranged[i - 1])
        
        # Add the circular difference (last element to the first)
        max_sum += abs(arranged[-1] - arranged[0])
        
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends