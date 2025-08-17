class Solution:
    def isPalindrome(self, s: str) -> bool:
        brr=[]
        for i in s:
            if i.isalnum():
                brr.append(i.lower())
        l,h=0,len(brr)-1
        while l<=h:
            if brr[l]==brr[h]:
                l+=1
                h-=1
            else:
                return False
        return True