#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        arr.sort()
        # print(arr)
        arr.append("-1")
        c=1
        m=1
        win=arr[0]
        curr=arr[0]
        for i in range(1,len(arr)):
            if arr[i]==curr:
                c+=1
            else:
                if c>m:
                    win=curr
                    m=c
                    # print('update winner')
                    # print(curr,c)
                c=1
                curr=arr[i]
        
        return win,m

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends