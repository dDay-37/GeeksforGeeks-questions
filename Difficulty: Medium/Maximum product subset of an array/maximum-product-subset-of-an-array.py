#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def findMaxProduct(self, arr):
        MOD = 10**9 + 7

        if len(arr) == 1:
            return arr[0]

        max_neg = float('-inf')
        product = 1
        count_neg = 0
        count_zero = 0
        non_zero_count = 0

        for num in arr:
            if num == 0:
                count_zero += 1
            else:
                non_zero_count += 1
                if num < 0:
                    count_neg += 1
                    max_neg = max(max_neg, num)
                product = (product * num) % MOD

        # If the array has only zeros
        if non_zero_count == 0:
            return 0

        # If the count of negatives is odd, remove the largest negative number
        if count_neg % 2 != 0:
            if non_zero_count == 1 and count_zero > 0:
                return 0
            product = (product * pow(max_neg, MOD-2, MOD)) % MOD

        return product


#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        solution = Solution()
        ans = solution.findMaxProduct(arr)
        results.append(ans)
    
    for result in results:
        print(result)
# } Driver Code Ends