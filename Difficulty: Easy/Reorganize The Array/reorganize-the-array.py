#{ 
 # Driver Code Starts

# } Driver Code Ends

class Solution:
    def rearrange(self, arr):
        result = [-1] * len(arr)
        for value in arr:
            if 0 <= value < len(arr):
                result[value] = value
        return result
        #Code here

#{ 
 # Driver Code Starts.
def main():
    t = int(input())
    for _ in range(t):
        input_str = input()
        arr = list(map(int, input_str.split()))
        solution = Solution()
        ans = solution.rearrange(arr)
        print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()
# } Driver Code Ends