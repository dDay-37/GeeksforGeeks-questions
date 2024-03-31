#User function Template for python3


'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.key = value
        self.right = None
'''

class Solution:
    def findMaxForN(self, root, n):
        #Print the value of the element if it exists otherwise print -1.
        ans=-1
        def fun(root,n,ans):
            if root:
                # print(root.key,ans)
                if root.key==n:
                    ans=root.key
                    return ans
                if root.key>n:
                    return fun(root.left,n,ans)
                else:
                    ans=root.key
                    return fun(root.right,n,ans)
            else:
                return ans
        return fun(root,n,ans)
            # return ans
        # return -1
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.key = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    #Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        n = int(input())
        ob = Solution()
        print(ob.findMaxForN(root, n))

# } Driver Code Ends