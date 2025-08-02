class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        c,d=0,len(nums)-1
        while c<=d:
            m=(c+d)//2
            if nums[m]==target:
                return True
            if nums[c]==nums[m] and nums[m]==nums[d]:
                c+=1
                d-=1
                continue
            if nums[c]<=nums[m]:
                if nums[c]<=target and target<=nums[m]:
                    d=m-1
                else:
                    c=m+1
            else:
                if nums[m]<=target and target<=nums[d]:
                    c=m+1
                else:
                    d=m-1
        return False
