class Solution:
    def removeDups(self, str):

        unique_alpha = [0] * 26
        result = ''

        for i in range(len(str)): 
            if unique_alpha[ord(str[i]) - 97] == 0: 
                result += str[i]
                unique_alpha[ord(str[i]) - 97] += 1

        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends