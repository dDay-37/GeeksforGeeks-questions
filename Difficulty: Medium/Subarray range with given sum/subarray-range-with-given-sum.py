#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def subArraySum(self,arr, tar):
        cumulative_sum = 0
        sum_counts = {0: 1}  
        count = 0
        for num in arr:
            cumulative_sum += num
            if (cumulative_sum - tar) in sum_counts:
                count += sum_counts[cumulative_sum - tar]
            if cumulative_sum in sum_counts:
                sum_counts[cumulative_sum] += 1
            else:
                sum_counts[cumulative_sum] = 1
                
        return count
        #Your code here

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends