from collections import deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        # Code here
        adjacentList = [[] for elements in range(n)]
        
        for leftEdge, rightEdge in edges:
            adjacentList[leftEdge].append(rightEdge)
            adjacentList[rightEdge].append(leftEdge)
            
        distance = [float('inf')] * n
        distance[src] = 0
        
        queue = deque([src])
        
        while queue:
            node = queue.popleft()
            for neighborNode in adjacentList[node]:
                if distance[neighborNode] == float('inf'):
                    distance[neighborNode] = distance[node] + 1
                    queue.append(neighborNode)
                    
        distance = [-1 if dist == float('inf') else dist for dist in distance]
        
        return distance


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends