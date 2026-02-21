class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left , right+1):
            e = self.count_set_bits(i)
            if self.prime(e):
                count += 1
        return count

    def prime(self,n):
        s = 1
        for i in range(2,n+1) : 
            if n % i == 0:
                s += 1
        if s == 2:
            return True
        return False

    def count_set_bits(self,n):
        count = 0
        while n > 0:
            remainder = n % 2
            if remainder == 1:
                count += 1
            n = n // 2
        return count