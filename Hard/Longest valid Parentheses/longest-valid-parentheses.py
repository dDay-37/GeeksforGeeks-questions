# User function Template for Python3

class Solution:
    def maxLength(self, s):
        m=0
        st=[-1]
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    m=max(m,i-st[-1])
        return m


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        
        ob = Solution()
        print(ob.maxLength(S))
# } Driver Code Ends