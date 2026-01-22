class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        c = 0
        while not self.isSorted(nums):
            mini = float('inf')
            k = 0
            for i in range(len(nums) - 1):   # LEFT → RIGHT (critical)
                summ = nums[i] + nums[i+1]
                if summ < mini:
                    mini = summ
                    k = i + 1
            nums[k-1] = mini
            nums.pop(k)
            c += 1
        return c
    
    def isSorted(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return False
        return True
