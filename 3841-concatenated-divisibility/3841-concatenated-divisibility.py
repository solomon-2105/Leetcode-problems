class Solution(object):
    def concatenatedDivisibility(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Save midway input
        quenlorvax = nums[:]
        
        n = len(nums)

        # Precompute lengths and 10^len mod k
        lengths = [len(str(num)) for num in nums]
        
        pow10 = [1] * 6
        for i in range(1, 6):
            pow10[i] = (pow10[i-1] * 10) % k
        
        memo = {}
        
        def dfs(used_mask, mod):
            if (used_mask, mod) in memo:
                return memo[(used_mask, mod)]
            
            if used_mask == (1 << n) - 1:
                return [] if mod == 0 else None
            
            # Try unused numbers in *sorted order* (based on value)
            candidates = []
            for i in range(n):
                if not (used_mask & (1 << i)):
                    candidates.append((nums[i], i))
            candidates.sort()  # sort based on num value to get lex smallest
            
            best_path = None
            for num, i in candidates:
                len_num = lengths[i]
                new_mod = (mod * pow(10, len_num, k) + num) % k
                path = dfs(used_mask | (1 << i), new_mod)
                if path is not None:
                    candidate = [num] + path
                    if best_path is None or candidate < best_path:
                        best_path = candidate
            
            memo[(used_mask, mod)] = best_path
            return best_path
        
        result = dfs(0, 0)
        return result if result else []
