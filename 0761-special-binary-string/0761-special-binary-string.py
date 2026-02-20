class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        b , start , sum = [] , 0 , 0
        for i in range(len(s)):
            sum += 1 if s[i] == '1' else -1
            if sum == 0 : 
                p = s[start + 1 : i]
                b.append("1" + self.makeLargestSpecial(p) + "0")
                start = i + 1
        b.sort(reverse = True)
        o =""
        for i in b:
            o += i
        return o 