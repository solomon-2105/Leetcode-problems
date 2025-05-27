class Solution(object):
    def isHappy(self, n):
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            n=sum(int(digit)*int(digit) for digit in str(n))
        return n==1