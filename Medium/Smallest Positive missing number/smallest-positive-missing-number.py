#User function Template for python3

class Solution:
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        arr=sorted(set(arr))
        counter=0
        for i in arr:
            if i >0 :
                counter+=1
                if i != counter :
                    return counter
        return counter+1

#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends