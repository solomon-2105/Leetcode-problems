class Solution:
    def permute(self, nums):
        result = []
        used = [False] * len(nums)
        def backtrack(current):
            if len(current) == len(nums):
                result.append(current[:])  # Make a copy
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current.append(nums[i])
                    backtrack(current)
                    current.pop()       # Undo the choice
                    used[i] = False     # Mark as unused again
        backtrack([])
        return result