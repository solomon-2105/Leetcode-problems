class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 1 1 1 2 2 3
        # foundTwo = False  #true
        # i = 0 #4
        # k = 0 #3
        # for i in range(1, len(nums)): #4
        #     if nums[i] != nums[j]:
        #         foundTwo = False
        #     if nums[j] == nums[i] and not foundTwo:
        #         foundTwo = True
        #         i += 1
        #         nums[k] = nums[j]
        #         k = j 
        #     else:
        #         nums[k] = nums[j]
        #         k += 1
        #         i += 1
        k = 2
        for i in range(2 , len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k+=1
        return k