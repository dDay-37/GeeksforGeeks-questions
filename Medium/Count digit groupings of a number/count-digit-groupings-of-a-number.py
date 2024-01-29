#User function Template for python3

# User function Template for python3

class Solution:
    def __init__(self):
        self.dp = []
        
    def TotalCount(self, s):
		# Code here
        maxsum = (len(s) * (len(s) + 1)) // 2 * 9
        self.dp = [[-1]* (maxsum + 1) for _ in range(len(s))]
        return self.grouping(s, 0, 0)
    
    def grouping(self, s, index, sum):
	    if index == len(s):
	        return 1
	    if self.dp[index][sum] != -1:
	        return self.dp[index][sum]
	    currentSum = 0
	    result = 0
	    for i in range(index, len(s)):
	        currentSum += int(s[i])
	        if currentSum >= sum:
	            result += self.grouping(s, i + 1, currentSum)        
	    self.dp[index][sum] = result
	    return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.TotalCount(s)
		print(ans)
# } Driver Code Ends