class Solution:
    def removeKdigits(self, num_str, k):
        digit_stack = []

        for current_digit in num_str:
            while digit_stack and k > 0 and current_digit < digit_stack[-1]:
                k -= 1
                digit_stack.pop()

            digit_stack.append(current_digit)

        while k > 0:
            digit_stack.pop()
            k -= 1

        return "".join(digit_stack).lstrip('0') or '0'

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends