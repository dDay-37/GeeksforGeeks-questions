class Solution:
    def findWinner(self, n, A):
        xor_value = 0
        for num in A:
            xor_value ^= num
        if xor_value == 0:
            return 1
        else:
            return 1 if n % 2 == 0 else 2

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        A = input().split()
        for itr in range(n):
            A[itr] = int(A[itr])

        ob = Solution()
        print(ob.findWinner(n, A))

# } Driver Code Ends