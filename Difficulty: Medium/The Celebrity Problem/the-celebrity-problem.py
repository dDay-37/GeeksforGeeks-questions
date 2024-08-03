class Solution:
    def celebrity(self, mat):
        n=len(mat)
        ar=[1]*n
        for i in range(n):
            if 1 in mat[i]:
                ar[i]=0
        # print(ar)
        for j in range(n):
            if ar[j]==1:
                for x in range(n):
                    if x!=j:
                    # print(mat[x][j])
                        if mat[x][j]==0:
                            ar[j]=0
                            # print("yabababa")
                            break
        # print(ar)
        if sum(ar)==1:
            for z in range(n):
                if ar[z]==1:
                    return z
        return -1

#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))

# } Driver Code Ends