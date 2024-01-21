from typing import List

class Solution:
    def vertexCover(self, num_nodes: int, edges: List[List[int]]) -> int:
        if num_nodes == 0:
            return 0

        first_vertex, second_vertex = edges[0]
        first_vertex_edges = [(v1, v2) for v1, v2 in edges if v1 != first_vertex and v2 != first_vertex]
        second_vertex_edges = [(v1, v2) for v1, v2 in edges if v1 != second_vertex and v2 != second_vertex]

        return 1 + min(
            self.vertexCover(len(first_vertex_edges), first_vertex_edges),
            self.vertexCover(len(second_vertex_edges), second_vertex_edges)
        )


#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        m = int(input())
        
        
        edges=IntMatrix().Input(m, m)
        
        obj = Solution()
        res = obj.vertexCover(n, edges)
        
        print(res)
        

# } Driver Code Ends