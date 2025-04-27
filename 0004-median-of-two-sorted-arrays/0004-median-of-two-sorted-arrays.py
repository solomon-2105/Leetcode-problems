class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # bruteforce TC- O(m+n)
        # i=j=0
        # merged=[]
        # while i<len(nums1) and j<len(nums2):
        #     if nums1[i]<=nums2[j]:
        #         merged.append(nums1[i])
        #         i+=1
        #     else:
        #         merged.append(nums2[j])
        #         j+=1
        # while i<len(nums1):
        #     merged.append(nums1[i])
        #     i+=1
        # while j<len(nums2):
        #     merged.append(nums2[j])
        #     j+=1
        # n=len(merged)
        # if n%2==1:
        #     return merged[n//2]
        # else:
        #     return (merged[n//2-1]+merged[n//2])/2.0

        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        total=m+n
        half=(total+1)//2 # Half size when merging both arrays
        left,right=0,m  # Binary search boundaries on nums1
        while left<=right:
            i=(left+right)//2  # Partition in nums1
            j=half-i         # Partition in nums2
            # Handle edges: If partition is at start or end
            nums1_left=float('-inf') if i == 0 else nums1[i-1]
            nums1_right=float('inf') if i == m else nums1[i]
            nums2_left=float('-inf') if j == 0 else nums2[j-1]
            nums2_right=float('inf') if j == n else nums2[j]
            # Check if the partition is correct
            if nums1_left<=nums2_right and nums2_left<=nums1_right:
                # If total number of elements is odd
                if total%2==1:
                    return float(max(nums1_left,nums2_left))
                else:
                    return (max(nums1_left,nums2_left)+min(nums1_right,nums2_right))/2.0
            elif nums1_left>nums2_right:
                # Move left in nums1
                right=i-1
            else:
                # Move right in nums1
                left=i+1