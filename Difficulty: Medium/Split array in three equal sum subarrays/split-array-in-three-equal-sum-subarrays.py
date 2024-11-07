#User function Template for python3
class Solution:
    
    def findSplit(self, arr):
        res = []
        total = 0
    
        for ele in arr:
            total += ele
    
        # If the total sum is not divisible by 3,
        # it's impossible to split the array
        if total % 3 != 0:
            res = [-1, -1]
            return res
    
        # Keep track of the sum of current segment
        currSum = 0
    
        for i in range(len(arr)):
            currSum += arr[i]
    
            # If the valid segment is found, store its index
            # and reset current sum to zero
            if currSum == total / 3:
                currSum = 0
                res.append(i)
    
                # If two valid segments are found and third non
                # empty segment is possible, return the index pair
                if len(res) == 2 and i < len(arr) - 1:
                    return res
    
        # If no index pair is possible
        res = [-1, -1]
        return res


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if (result == [-1, -1]) or len(result) != 2:
            print("false")
        else:
            sum1 = sum2 = sum3 = 0
            for i in range(len(arr)):
                if i <= result[0]:
                    sum1 += arr[i]
                elif i <= result[1]:
                    sum2 += arr[i]
                else:
                    sum3 += arr[i]

            if sum1 == sum2 == sum3:
                print("true")
            else:
                print("false")
        print("~")

# } Driver Code Ends