class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c=0
        for i in range(len(fruits)):
            grr=False
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j]:
                    grr=True
                    baskets.pop(j)
                    break
            if not grr: c+=1
        return c
            
