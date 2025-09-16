class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self._backtrack(nums, 0, [], res)
        return res

    def _backtrack(self, nums, index, path, res):
        res.append(path.copy()) 
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self._backtrack(nums, i + 1, path, res)
            path.pop()
