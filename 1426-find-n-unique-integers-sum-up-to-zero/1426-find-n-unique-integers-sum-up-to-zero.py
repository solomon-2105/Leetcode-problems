class Solution:
    def sumZero(self, n: int) -> List[int]:
        a=[]
        if n%2!=0: a.append(0)
        for i in range(1,n//2+1):
            a.append(-i)
            a.append(i)
        return a