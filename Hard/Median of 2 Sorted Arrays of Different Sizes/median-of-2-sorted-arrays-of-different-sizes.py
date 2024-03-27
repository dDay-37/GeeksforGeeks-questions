#User function Template for python3

class Solution:
    def MedianOfArrays(self, nums1, nums2):
            merged = []
            i = 0
            j = 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1
            merged.extend(nums1[i:])
            merged.extend(nums2[j:])
    
            total_length = len(merged)
            if total_length % 2 == 1:
                return merged[total_length // 2]
            else:
                mid_right = total_length // 2
                mid_left = mid_right - 1
                if ((merged[mid_left] + merged[mid_right]) / 2) // 1 == (merged[mid_left] + merged[mid_right]) / 2:
                    return int((merged[mid_left] + merged[mid_right]) / 2)
                return (merged[mid_left] + merged[mid_right]) / 2
       


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends