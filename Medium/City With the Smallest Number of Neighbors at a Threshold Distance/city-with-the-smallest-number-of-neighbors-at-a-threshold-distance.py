#User function Template for python3

from typing import List
import heapq
class Solution:
    def findCity(self, n : int, m : int, edges : List[List[int]], d : int) -> int:
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
            c=sum(1 for h in dijk(i) if h<=d)
            if c<=mn:
                mn=c
                ans=i
        return ans
        
        
"""
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3]
# mat=[[float('inf')]*n for _ in range(n)]
        # for x in range(n):
        #     mat[x][x]=0
        # for u,v,w in edges:
        #     mat[u][v]=w
        #     mat[v][u]=w
        # for via in range(n):
        #     for i in range(n):
        #         for j in range(n):
        #             mat[i][j]=min(mat[i][j],mat[i][via]+mat[via][j])
        # for _ in mat:
        #     print(_)
        
"""


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