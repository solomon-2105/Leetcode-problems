class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        res = ['0']*n

        for i , j in enumerate(nums):
            if j[i] == '0':
                res[i] = '1'
            else:
                res[i] = '0'

        return "".join(res)