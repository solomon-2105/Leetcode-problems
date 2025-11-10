class Solution:
    def minOperations(self, nums: list[int]) -> int:
        stack=[]
        res=0
        for i in nums:
            while stack and stack[-1]>i:
                stack.pop()
            if i==0:
                continue
            if not stack or stack[-1]<i:
                res+=1
                stack.append(i)
        return res
