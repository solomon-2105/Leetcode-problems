class Solution:
    def canJump(self, a: List[int]) -> bool:
        count=0
        for i in range(len(a)):
            if i>count: return False
            count=max(i+a[i],count)
            if count>=len(a)-1:return True