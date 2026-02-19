class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # If we pair one majority element with one different element,
        # they cancel each other.
        # Since majority element appears more than n/2 times,
        # it will still remain at the end.
        # 2 , 2 , 1 , 1 , 1 , 2 , 2 
        # here 2 is majority element as we can see , 
        # each element cancels out with 2 and 2 still remains at the end
        #thus it's the majority element

        count = 0
        el = None
        for i in nums:
            # If count becomes 0, choose current number as new candidate.
            if count == 0:
                el = i
            
            # If current number is same as candidate, increase count.
            # Otherwise decrease count (cancel out).
            if i == el:
                count += 1
            else:
                count -= 1
        
        # The remaining candidate must be the majority element.
        return el
