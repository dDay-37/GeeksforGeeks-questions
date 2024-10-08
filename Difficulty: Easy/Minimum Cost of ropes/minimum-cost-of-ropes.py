import heapq
from typing import List

class Solution:
   def minCost(self, arr: List[int]) -> int:

        if len(arr) < 2: return 0

        heapq.heapify(arr)

        totalCost = 0

        while len(arr) > 1:
            x, y = heapq.heappop(arr), heapq.heappop(arr)
            min_cost = x + y
            totalCost += min_cost
            heapq.heappush(arr, min_cost)

        return totalCost

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import defaultdict
# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minCost(a))

# } Driver Code Ends