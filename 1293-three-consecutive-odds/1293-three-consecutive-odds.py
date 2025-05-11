class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c=0
        for i in  arr: c+=1 #length of the array lol
        for i in range(c-2):
            if arr[i]%2==1 and arr[i+1]%2==1 and arr[i+2]%2==1: return True
        return False
