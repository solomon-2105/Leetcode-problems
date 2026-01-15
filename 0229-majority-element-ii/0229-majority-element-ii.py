class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 , c2 , el1 , el2 = 0 , 0 , None , None
        for i in nums:
            if c1 == 0 and i != el2:
                c1 = 1
                el1 = i
            elif c2 == 0 and i != el1:
                c2 = 1
                el2 = i
            elif i == el1:
                c1 += 1
            elif i == el2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        a , b = 0 , 0
        for i in nums:
            if i == el1 : a += 1
            elif i == el2 : b += 1
        temp = []
        if a > len(nums)//3 : temp.append(el1)
        if b > len(nums)//3 : temp.append(el2)
        return temp