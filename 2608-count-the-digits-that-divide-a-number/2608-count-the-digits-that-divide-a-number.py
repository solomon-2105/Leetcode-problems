class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        original = num
        count = 0
        
        while num > 0:
            r = num % 10 
            if r != 0 and original % r == 0:
                count += 1
            num //= 10  
        
        return count