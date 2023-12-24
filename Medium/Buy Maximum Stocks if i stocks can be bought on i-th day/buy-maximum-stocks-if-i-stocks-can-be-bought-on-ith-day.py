

from typing import List
class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        # code here
        z=list(enumerate(price))
        z.sort(key=lambda x:x[1])
        stocks=0
        # print(z)
        for i in z:
            stocksLeft=i[0]+1
            while stocksLeft>0:
                if k>=i[1]:
                    stocksLeft-=1
                    stocks+=1
                    k-=i[1]
                    # print(f'stock bought worth {i[1]}')
                else:
                    return stocks
        return stocks
        # 1st val no of st, 2nd val price



#{ 
 # Driver Code Starts


class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,k = map(int,input().strip().split())
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.buyMaximumProducts(n, k, price)
        
        print(res)
        

# } Driver Code Ends