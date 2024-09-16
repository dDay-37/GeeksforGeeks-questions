# User function Template for Python3

class Solution:
    def maxLength(self, str):
        # Initialize variables for left-to-right scan
        left = right = 0
        max_len = 0
        
        # Left to right scan
        for i in str:
            if i == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                max_len = max(max_len, 2 * right)  # Valid substring length
            elif right > left:
                left = right = 0  # Reset if invalid sequence
        
        # Initialize variables for right-to-left scan
        left = right = 0
        
        # Right to left scan
        for i in reversed(str):
            if i == ')':
                right += 1
            else:
                left += 1
            
            if left == right:
                max_len = max(max_len, 2 * left)  # Valid substring length
            elif left > right:
                left = right = 0  # Reset if invalid sequence
        
        return max_len



#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))

# } Driver Code Ends