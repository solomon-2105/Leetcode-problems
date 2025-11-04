class Solution:
    def getRow(self, n: int) -> List[int]:
        a=[]
        for i in range(n+1):
            c=self.factorial(n)//((self.factorial(n-i))*self.factorial(i))
            a.append(c)
        return a
    def factorial(self,x):
        m=1
        for i in range(1,x+1):
            m*=i
        return m
