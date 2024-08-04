#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        zipped=zip(start,end)
        zipped=sorted(zipped,key=lambda x:x[1])
        # print(zipped)
        c=1
        t=zipped[0][1]
        for i in zipped[1:]:
            # print(i)
            if i[0]>t:
                c+=1
                t=i[1]
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends