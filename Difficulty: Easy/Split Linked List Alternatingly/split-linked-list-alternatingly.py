#User function Template for python3
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def alternatingSplitList(self, head):
        # Create two dummy nodes to ease the splitting process
        list1_dummy = Node(0)  # Dummy node for the first list
        list2_dummy = Node(0)  # Dummy node for the second list
        
        # Pointers to build the two lists
        current1 = list1_dummy
        current2 = list2_dummy
        
        # Traverse the list alternately
        current = head
        index = 0
        while current:
            if index % 2 == 0:  # Even index goes to list1
                current1.next = current
                current1 = current1.next
            else:               # Odd index goes to list2
                current2.next = current
                current2 = current2.next
            # Move to the next node
            current = current.next
            index += 1
        
        # End the two lists
        current1.next = None
        current2.next = None
        
        # Return the heads of the two lists (without dummy nodes)
        return [list1_dummy.next, list2_dummy.next]
        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        head = Node(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next

        ob = Solution()
        result = ob.alternatingSplitList(head)
        printList(result[0])
        printList(result[1])

# } Driver Code Ends