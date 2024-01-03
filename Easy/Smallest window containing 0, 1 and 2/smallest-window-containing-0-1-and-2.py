#User function Template for python3

class Solution:
    def smallestSubstring(self, S):
        dicti={}
        start=0
        mini=10**9
        for i in range(len(S)):
            dicti[S[i]]=dicti.get(S[i],0)+1
            while(start<i and dicti[S[start]]>1):
                dicti[S[start]]-=1
                start+=1
            if len(dicti)==3:
                mini=min(mini,i-start+1)
        return mini if mini!=10**9 else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends