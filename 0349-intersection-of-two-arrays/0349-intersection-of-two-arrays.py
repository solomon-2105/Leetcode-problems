class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res=[]
        i,j,x,y=0,0,len(nums1),len(nums2)
        while i<x and j<y:
            if nums1[i]==nums2[j] and (len(res)==0 or res[-1]!=nums1[i]):
                res.append(nums1[i])
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return res