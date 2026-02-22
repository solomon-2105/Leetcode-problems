class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        mem = {}
        def  gcd(a , b):
            while b:
                a , b = b , a % b
            return a

        def solve(i , n , d):
            g = gcd(n , d)
            n //= g
            d //= g
            if i == len(nums):
                if d == 1 and n == k:
                    return 1
                return 0
            tup = (i , n , d)
            if tup in mem:
                return mem[tup]
            
            unch = solve(i+1 , n , d)
            mult = solve(i+1 , n * nums[i] , d)
            div = solve(i+1 , n, d * nums[i])
            
            mem[tup] = unch + mult + div
            return mem[tup]
        return solve(0 , 1 , 1)