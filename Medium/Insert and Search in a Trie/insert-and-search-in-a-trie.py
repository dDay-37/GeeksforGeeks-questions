#User function Template for python3

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False


class Solution:
    def insert(self, root, key):
        for i in key:
            ind = ord(i) - ord('a')
            if not root.children[ind]:
                root.children[ind] = TrieNode()
            root = root.children[ind]
        root.isEndOfWord = True

    def search(self, root, key):
        for i in key:
            ind = ord(i) - ord('a')
            if not root.children[ind]:
                return False
            root = root.children[ind]
        return root.isEndOfWord


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
        

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=input().strip().split()
        strs=input()
        
        t=Trie()
        ob = Solution()
        
        for s in arr:
            ob.insert(t.root,s)
        
        if ob.search(t.root,strs):
            print(1)
        else:
            print(0)
# } Driver Code Ends