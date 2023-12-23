#User function Template for python3


class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        a=n/k
        arr.sort()
        arr.append(-1)
        c=1
        s=0
        for i in range(n):
            if arr[i]==arr[i+1]:
                c+=1
            else:
                if c>a:
                    s+=1
                c=1
        return s
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(Solution().countOccurence(A, N, K))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends