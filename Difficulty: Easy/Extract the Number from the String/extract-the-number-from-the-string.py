class Solution:
    def ExtractNumber(self,sentence):
        words = sentence.split()
        ans =- 1
        for i in words:
            if i.isdigit():
                if '9' not in i:
                    ans = max(ans, int(i))
        return ans

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends