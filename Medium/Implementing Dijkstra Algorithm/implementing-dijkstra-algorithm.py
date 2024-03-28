import heapq
class Solution:
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, src):
        #code here
        pq=[]
        heapq.heappush(pq,(0,src))
        dist=[float('inf')]*V
        dist[src]=0
        while pq:
            d,u=heapq.heappop(pq)
            for v,weight in adj[u]:
                if dist[u]+weight<dist[v]:
                    dist[v]=dist[u]+weight
                    heapq.heappush (pq,(dist[v],v))
        return dist


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends