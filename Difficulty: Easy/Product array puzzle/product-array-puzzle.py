#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        z=0
        id=-1
        p=1
        for i in range(len(nums)):
            if nums[i]==0:
                z+=1
                if z==1:
                    id=i
            else:
                p*=nums[i]
        if z>1:
            return [0]*len(nums)
        ans=[]
        # print(p)
        if z==1:
            ans=[0]*len(nums)
            ans[id]=p
            # print(ans[id])
        else:
            for i in nums:
                ans.append(p//i)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends