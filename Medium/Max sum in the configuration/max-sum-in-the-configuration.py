# User function Template for python3

def max_sum(a, n):
    # Code here
    arraySum = 0
    currentValue = 0

    for i in range(0, n):
        arraySum = arraySum + arr[i]
        currentValue = currentValue + (i * arr[i])

    maximumValue = currentValue

    for j in range(1, n):
        currentValue = currentValue + arraySum - n * arr[n - j]
        if (currentValue > maximumValue):
            maximumValue = currentValue

    return maximumValue
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends