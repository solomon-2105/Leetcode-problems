class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0: return 0
        if n==1: return 1
        a=[0,1]
        for i in range(2,n+1):
            a.append(a[i-1]+a[i-2])
        return a[n]