
class Solution:
    def search(self, pattern, text):
        occurrences = []  # List to store starting positions of pattern occurrences
        m, n = len(pattern), len(text)
        lps = self.calculate_lps(pattern)

        i, j = 0, 0  # Pointers for text and pattern
        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1

            if j == m:
                occurrences.append(i - j + 1)
                j = lps[j - 1]
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return occurrences


    def calculate_lps(self, pattern):
        m = len(pattern)
        lps = [0] * m
        length, i = 0, 1

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

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
        if len(ans)==0:
            print(-1,end="")
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends