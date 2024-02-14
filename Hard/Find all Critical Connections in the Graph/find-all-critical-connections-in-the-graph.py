#User function Template for python3
class Solution:
    def criticalConnections(self, v, adj):
        # Function to find critical connections in a graph

        def Articulation_Point(u):
            # Function to find Articulation Point and critical connections

            low[u]=time[0]
            disc[u]=time[0]
            time[0]+=1
            visited[u]=True
            for v in adj[u]:
                if visited[v]==False:
                    parent[v]=u
                    Articulation_Point(v)

                    low[u]=min(low[u],low[v])

                    if low[v]>disc[u]:
                        ans.append(sorted([u,v]))

                elif parent[u]!=v:
                    low[u]=min(low[u],disc[v])



        ans=[]

        # Initializing low, disc, parent, time, and visited arrays
        low=[sys.maxsize for i in range(v)]
        disc=[sys.maxsize for i in range(v)]
        parent=[-1 for i in range(v)]
        time=[0]
        visited=[False for i in range(v)]

        # Calling Articulation_Point function for each unvisited vertex
        for i in range(v):
            if visited[i]==False:
                Articulation_Point(i)


        return sorted(ans)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.criticalConnections(V, adj)
		for i in range(len(ans)):
		    print(ans[i][0],ans[i][1])

# } Driver Code Ends