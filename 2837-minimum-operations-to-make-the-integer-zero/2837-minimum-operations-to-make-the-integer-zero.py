class Solution:
    def makeTheIntegerZero(self, a: int, b: int) -> int:
        for i in range(1,36):
            brr=a-i*b
            if brr<i:
                continue
            p=bin(brr).count("1")
            # if p<=i<=brr:
            if p<=i<=brr:
                return i
        return -1