#User function Template for python3
from collections import defaultdict

class Solution:
    def minValue(self, s, k):
        # Code here
        charCount = defaultdict(int)
        for character in s:
            charCount[character] += 1
        valueList = list(charCount.values())
        valueList.sort()
        
        while k!= 0:
            valueList[-1] -= 1
            k -= 1
            valueList.sort()
        
        summ = 0
        for items in valueList:
            summ  += items ** 2
        return summ

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends