class Solution:
    def recamanSequence(self, n):
        # Code here
        sequence = [0]
        sequenceNumberAppeared = set()
        
        for i in range(1, n):
            previousTerm = sequence[-1]
            nextTerm = previousTerm - i
            
            if nextTerm > 0 and nextTerm not in sequenceNumberAppeared:
                sequence.append(nextTerm)
                sequenceNumberAppeared.add(nextTerm)
            else:
                nextTerm = previousTerm + i
                sequence.append(nextTerm)
                sequenceNumberAppeared.add(nextTerm)
                
        return sequence

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends