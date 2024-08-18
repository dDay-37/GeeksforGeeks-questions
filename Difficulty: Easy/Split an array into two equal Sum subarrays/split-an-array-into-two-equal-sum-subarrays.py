class Solution:
    def canSplit(self, arr):
        # Code here
        arrLength = len(arr)
        leftSum = arr[0]
        rightSum = arr[arrLength - 1]
        
        pointerOne = 0
        pointerTwo = arrLength - 1
        
        while pointerOne < pointerTwo:
            if (leftSum == rightSum and pointerOne + 1 == pointerTwo):
                return True
            elif (leftSum > rightSum):
                pointerTwo -= 1
                rightSum += arr[pointerTwo]
            else:
                pointerOne += 1
                leftSum += arr[pointerOne]
        return False

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends