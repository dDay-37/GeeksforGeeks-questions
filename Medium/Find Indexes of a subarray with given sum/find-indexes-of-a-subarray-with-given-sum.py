#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self, arr, n, s): 
        start = 0
        end = 0
        current_sum = arr[0]  # Initialize current_sum with the first element
        found = False
        
        # Iterate through the array using two pointers
        while end < n:
            if current_sum == s:
                found = True
                break
            
            # Expand the window by moving the end pointer
            end += 1
            
            # If end reaches the end of the array, break the loop
            if end == n:
                break
            
            # Update the current sum
            current_sum += arr[end]
            
            # Check if the current sum is greater than or equal to s
            while current_sum > s and start < end:
                # Shrink the window by moving the start pointer
                current_sum -= arr[start]
                start += 1
            
            # If the current sum equals s, break the loop
            if current_sum == s:
                found = True
                break
                
        # If no subarray is found, return [-1]
        if not found:
            return [-1]
        
        # If s is 0, return the subarray consisting of a single element
        if s == 0:
            return [end + 1, end + 1]
        
        return [start + 1, end + 1]  # Adding 1 to convert to 1-based indexing



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends