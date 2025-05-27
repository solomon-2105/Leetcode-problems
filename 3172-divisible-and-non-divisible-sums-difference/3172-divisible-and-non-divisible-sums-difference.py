class Solution(object):
    def differenceOfSums(self, n, m):
        a=n*(n+1)//2
        b=m*(n//m)*(n//m+1)
        return a-b