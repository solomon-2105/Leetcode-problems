class Solution:
    def maxFreqSum(self, s: str) -> int:
        def is_vowel(char):
            return char.lower() in 'aeiou'
        a={}
        for i in s:
            if i in a: a[i]+=1
            else: a[i]=1
        maxv,maxc=0,0
        for k,v in a.items():
            if is_vowel(k):
                maxv=max(maxv,v)
            else:
                maxc=max(maxc,v)
        return maxv+maxc