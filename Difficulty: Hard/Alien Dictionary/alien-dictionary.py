#User function Template for python3
from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, dict: List[str], n: int, k: int) -> str:
        # Your implementation here
        adjacent = defaultdict(set)
        inDegree = defaultdict(int)
        character = set()
        for index, value in enumerate(alien_dict):
            if index + 1 == n:
                continue
            
            currentElement = list(value)
            nextElement = list(alien_dict[index + 1])
            character.update(currentElement + nextElement)
            
            for a, b in zip(currentElement, nextElement):
                if a == b:
                    continue
                
                if b not in adjacent[a]:
                    inDegree[b] += 1
                    adjacent[a].add(b)
                break
            
        queue = []
        for c in character:
            if inDegree[c] == 0:
                queue.append(c)
                
        queueReturn = []
        while queue:
            currentElement = queue.pop()
            queueReturn.append(currentElement)
            for nextElement in adjacent[currentElement]:
                inDegree[nextElement] -= 1
                if inDegree[nextElement] == 0:
                    queue.append(nextElement)
        return queueReturn


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class sort_by_order:

    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word

    def sort_this_list(self, lst):
        lst.sort(key=self.transform)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1])

        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob = Solution()
        order = ob.findOrder(alien_dict, n, k)
        s = ""
        for i in range(k):
            s += chr(97 + i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)

            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)

# } Driver Code Ends