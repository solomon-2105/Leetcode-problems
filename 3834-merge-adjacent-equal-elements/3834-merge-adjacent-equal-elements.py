class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for i in nums:
            stack.append(i)
            while len(stack)>=2 and stack[-1] == stack[-2]:
                stack.pop()
                stack[-1] *= 2
        return stack