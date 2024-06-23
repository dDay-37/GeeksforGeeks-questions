class Solution:
	def bracketNumbers(self, str):
	    stack = [] 
	    c = 0
	    ans = []
	    for i in range(len(str)):
	        if(str[i] == '('):
	            c += 1 
	            ans.append(c)
	            stack.append(c)
	        elif(str[i] == ')'):
	            ans.append(stack[-1]) 
	            stack.pop() 
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends