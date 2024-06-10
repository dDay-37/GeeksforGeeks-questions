#User function Template for python3
class Solution:

	def matchPairs(self, n, nuts, bolts):
		# code here
		a=['!','#','$','%','&','*','?','@','^']
		x=[]
		for i in a:
		    if i in nuts and i in bolts:
		        x.append(i)
# 		print(x)
		for j in range(len(x)):
	        nuts[j]=x[j]
            bolts[j]=x[j]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(n, nuts, bolts)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends