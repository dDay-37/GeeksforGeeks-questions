#User function Template for python3

class Solution:
    def anagrams(self, arr):
        from collections import defaultdict
        # Dictionary to group anagrams
        anagram_groups = defaultdict(list)
        # Iterate over each word in the array
        for word in arr:
            # Sort the characters of the word to create a key
            key = ''.join(sorted(word))
            # Append the word to the corresponding group
            anagram_groups[key].append(word)
        # Return the grouped anagrams as a list of lists
        return list(anagram_groups.values())
        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends