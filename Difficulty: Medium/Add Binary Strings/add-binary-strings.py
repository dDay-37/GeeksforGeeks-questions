class Solution:
	def addBinary(self, s1, s2):
		# Code here
		stringOne = int(s1, 2)
		stringTwo = int(s2, 2)
		
		return bin(stringOne + stringTwo)[2:]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends