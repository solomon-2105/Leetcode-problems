class Solution:
    def secondHighest(self, s: str) -> int:
        fmax=smax=float('-inf')
        for ch in s:
            if ch.isnumeric():
                num=int(ch)
                if num==fmax or num==smax:
                    continue
                if num>fmax:
                    smax=fmax
                    fmax=num
                elif num>smax:
                    smax=num
        return smax if smax!=float('-inf') else -1
