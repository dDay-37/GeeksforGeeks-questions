#User function Template for python3

from typing import List
import heapq
class Solution:
    def findCity(self, n : int, m : int, edges : List[List[int]], thres : int) -> int:
        adj=[[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        def dijk(src):
            dist=[float('inf')]*n
            dist[src]=0
            heap=[(0,src)]
            while heap:
                d,u=heapq.heappop(heap)
                if d>dist[u]:
                    continue
                for v,w in adj[u]:
                    if dist[u]+w<dist[v]:
                        dist[v]=dist[u]+w
                        heapq.heappush(heap,(dist[v],v))
            return dist

        mn=n
        ans=-1
        for i in range(n):
            c=sum(1 for h in dijk(i) if h<=thres)
            if c<=mn:
                mn=c
                ans=i
        return ans
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        
        n, m = map(int, input().strip().split())
        edges = []
        for i in range(m):
            u, v, wt = map(int, input().strip().split())
            edges.append([u, v, wt])
        distanceThreshold = int(input())
        obj = Solution()
        ans = obj.findCity(n, m, edges, distanceThreshold)
        print(ans)
            

# } Driver Code Ends