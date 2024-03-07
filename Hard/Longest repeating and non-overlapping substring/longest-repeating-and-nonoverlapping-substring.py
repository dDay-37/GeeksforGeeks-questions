#User function Template for python3

# User function Template for python3

class Solution:
    def longestSubstring(self, s , n):
        # Code here
        maxLength = 0
        result = "-1"
        i = 0
        j = 0
        while i < n and j < n:
            subString = s[i: j + 1]
            if s.find(subString, j + 1) != -1:
                stringLength = len(subString)
                if stringLength > maxLength:
                    result = subString
                    maxLength = stringLength
            else:
                i += 1
            j += 1
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        S=input()
        
        ob = Solution()
        print(ob.longestSubstring(S , N))
# } Driver Code Ends