from collections import Counter
from functools import lru_cache
from math import comb

MOD = 10**9 + 7

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        # Step 1: Count digit frequencies
        cnt = Counter(map(int, num))
        total_sum = sum(d * cnt[d] for d in cnt)
        n = len(num)

        # Step 2: Early exit if total sum is odd
        if total_sum % 2 != 0:
            return 0

        # Step 3: Precompute factorials and their modular inverses
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, 0, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        # Step 4: Define the DP function with memoization
        @lru_cache(None)
        def dp(i, remaining_sum, odd_left, even_left):
            if i == 10:
                return 1 if remaining_sum == 0 and odd_left == 0 and even_left == 0 else 0

            res = 0
            for odd_count in range(min(cnt.get(i, 0), odd_left) + 1):
                even_count = cnt.get(i, 0) - odd_count
                if 0 <= even_count <= even_left and odd_count * i <= remaining_sum:
                    res += (comb(odd_left, odd_count) * comb(even_left, even_count) *
                            dp(i + 1, remaining_sum - odd_count * i, odd_left - odd_count, even_left - even_count)) % MOD
                    res %= MOD

            return res

        # Step 5: Calculate the total number of balanced permutations
        return dp(0, total_sum // 2, n // 2, (n + 1) // 2)
