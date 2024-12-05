#{ 
 # Driver Code Starts

# } Driver Code Ends

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # Code here
        index = 0
        i = 0
        j = len(arr) - 1
        while index <= j and i <= j:
            if arr[index] == 1:
                index += 1
            elif arr[index] == 0:
                arr[index], arr[i] = arr[i], arr[index]
                i += 1
                index += 1    
            else:
                arr[index], arr[j] = arr[j], arr[index]
                j -= 1            
        return arr
        

#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")
        
if __name__ == "__main__":
    main()

# } Driver Code Ends