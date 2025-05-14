class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0: return False
        t=x
        sum=0
        while t:
            sum=sum*10 + t%10
            t//=10
        return sum==x