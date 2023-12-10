# Your task is to complete this function
# Function should return True/False or 1/0
def PalinArray(arr ,n):
    def p(x):
        m=len(x)
        i=0
        j=m-1
        while i<j:
            if x[i]==x[j]:
                i+=1
                j-=1
            else:
                return False
        return True
    for i in arr:
        if not p(str(i)):
            return 0
    return 1



#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends