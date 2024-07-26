class Solution:
    def kPangram(self, string, k):
        # Code here
        totalCharacters, uniqueCharacters, isPresent = 0, 0, [False] * 26
        
        for value in string:
            if value.isalpha():
                totalCharacters += 1
                i = ord(value) - ord("a")
                
                if not isPresent[i]:
                    isPresent[i] = True
                    uniqueCharacters += 1
                    
        return 26 - uniqueCharacters <= k and totalCharacters >= 26

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends