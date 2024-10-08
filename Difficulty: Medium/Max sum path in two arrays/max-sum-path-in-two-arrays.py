#Your task is to complete this function
class Solution:
    def maxPathSum(self, arr1, arr2):
        i, j, m, n = 0, 0, len(arr1), len(arr2)
        s1, s2, ans = 0, 0, 0
        while i < m or j < n:
            if i == m:
                s2 += arr2[j]
                j += 1
                continue
            if j == n:
                s1 += arr1[i]
                i += 1
                continue

            if arr1[i] < arr2[j]:
                s1 += arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                s2 += arr2[j]
                j += 1
            else:
                s1 += arr1[i]
                i += 1
                s2 += arr2[j]
                j += 1
                ans += max(s1, s2)
                s1, s2 = 0, 0
        ans += max(s1, s2)
        return ans


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPathSum(arr1, arr2)
        print(ans)

# } Driver Code Ends