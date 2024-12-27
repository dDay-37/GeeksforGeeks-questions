#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    def countPairs(self, arr, target):
        # Initialize a hashmap to store frequencies
        freq = {}
        count = 0
        
        # Iterate through the array
        for num in arr:
            complement = target - num
            # Check if complement exists in hashmap
            if complement in freq:
                count += freq[complement]
            
            # Update the hashmap with the current number
            freq[num] = freq.get(num, 0) + 1
        
        return count
        #Your code here

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends