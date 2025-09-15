class Solution:
    def canBeTypedWords(self, text: str, bl: str) -> int:
        words = text.split()
        broken = set(bl)
        count = 0
        for word in words:
            bad = False
            for ch in word:
                if ch in broken:
                    bad = True
                    break  
            if not bad:
                count += 1
        return count