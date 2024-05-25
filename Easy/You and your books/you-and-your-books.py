class Solution:
    #Your task is to complete this function
    #Function should return an integer
    #a - list/array containing height of stack's respectively
     def max_Books(self, n, k, arr):
        #code here
        from itertools import groupby
        gs = groupby(arr, key=lambda x: x <= k)
        sums = [sum(e) for f, e in gs if f]
        return max(sums) if sums else 0

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        temp = list(map(int, input().strip().split()))
        n = temp[0]
        k = temp[1]
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.max_Books(n, k, arr))
# Contributed by:Harshit Sidhwa

# } Driver Code Ends