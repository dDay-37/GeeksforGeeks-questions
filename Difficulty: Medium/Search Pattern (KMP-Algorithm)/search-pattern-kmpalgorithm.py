class Solution:
    def search(self, pat, txt):
        # Code here
        patSize = len(pat)
        textSize = len(txt)
        listOne = []
        
        for i in range(0, patSize - 1 + textSize):
            s = txt[i:i + patSize]
            if s == pat:
                listOne.append(i)
        
        return listOne

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends