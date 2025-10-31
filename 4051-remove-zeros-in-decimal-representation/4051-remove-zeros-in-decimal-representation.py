class Solution:
    def removeZeros(self, n: int) -> int:
        a=list(str(n))
        return int(''.join([x for x in a if x!='0']))