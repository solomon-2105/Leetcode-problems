class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        
        def power(base, exp):
            if exp == 0:
                return 1
            half = power(base, exp // 2)
            half = (half * half) % mod
            if exp % 2 == 1:
                half = (half * base) % mod
            return half
        
        even_count = (n+1) // 2
        odd_count = n - even_count
        
        return (power(5, even_count) * power(4, odd_count)) % mod
