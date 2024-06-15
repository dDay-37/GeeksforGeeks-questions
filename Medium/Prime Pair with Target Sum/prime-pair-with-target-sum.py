from typing import List

class Solution:
    def getPrimes(self, n: int) -> List[int]:
        # Initialize a list to mark all numbers as prime initially
        is_prime = [True] * n

        # Sieve of Eratosthenes algorithm to find primes less than n
        for i in range(2, int(n ** 0.5) + 1): # Loop only up to the square root of n
            if is_prime[i]:
                # Mark all multiples of i as non-prime
                for j in range(i * i, n, i):
                    is_prime[j] = False

        # Initialize a list to store pairs of prime numbers
        prime_pairs = []

        # Find pairs of primes where both numbers add up to n
        for x in range(2, n // 2 + 1): # Only need to check up to n // 2
            y = n - x
            if is_prime[x] and is_prime[y]:
                # If both x and y are prime, add them as a pair
                return [x, y]
        return [-1,-1]


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.getPrimes(n)

        IntArray().Print(res)

# } Driver Code Ends