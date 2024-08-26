import re

class Solution:
    def wildCard(self, pattern, string):
        # Code here
        p = "^" + re.sub("\*+", "[a-z]*", pattern).replace("?", "[a-z]") + "$"
        return 1 if re.search(p, string) else 0
#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(pattern, string):
            print(1)
        else:
            print(0)

# } Driver Code Ends