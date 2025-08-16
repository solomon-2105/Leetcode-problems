class Solution:
    def maximum69Number (self, num: int) -> int:
        a=str(num)
        brr=""
        c=False
        for i in a:
            if i=="6" and not c:
                brr+="9"
                c=True
            else:
                brr+=i
        return int(brr)
            