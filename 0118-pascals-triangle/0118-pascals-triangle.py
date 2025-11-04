class Solution:
    def generate(self, n: int) -> List[List[int]]:
        b=[]
        for j in range(n):
            a=[]
            for i in range(j+1):
                c=self.factorial(j)//((self.factorial(j-i))*self.factorial(i))
                a.append(c)
            b.append(a)
        return b
    def factorial(self,x):
        m=1
        for i in range(1,x+1):
            m*=i
        return m