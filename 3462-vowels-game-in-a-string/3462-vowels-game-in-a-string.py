class Solution:
    def doesAliceWin(self, s: str) -> bool:
        a={'a','e','i','o','u'}
        c=0
        for i in s:
            if i in a:
                return True
        return False