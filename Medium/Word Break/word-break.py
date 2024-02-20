#User function Template for python3

class Solution:
    def wordBreak(self, n, s, dictionary):
        # Complete this function
        def execute(s):
            if not s:
                return True
            for item in dictionary:
                if s.startswith(item) and execute(s[len(item):]):
                    return True
            return False
        return execute(s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends