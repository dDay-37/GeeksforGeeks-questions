class Solution:
    def myAtoi(self, s):
        # Code here
        s = s.lstrip()  # remove leading whitespaces
        sign = 1
        num = 0
        maxInt = (2 ** 31) - 1
        minInt = -(2 ** 31)

        if s and s[0] in ['+', '-']:
            if s[0] == '-':
                sign = -1
            s = s[1:]

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                break

        num *= sign

        if num > maxInt:
            return maxInt
        elif num < minInt:
            return minInt
        else:
            return num

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends