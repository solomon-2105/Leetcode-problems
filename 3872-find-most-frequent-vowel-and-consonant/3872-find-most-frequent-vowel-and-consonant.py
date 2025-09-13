# class Solution:
#     def maxFreqSum(self, s: str) -> int:
#         a={}
#         b={}
#         c={'a','e','i','o','u'}
#         for i in s:
#             if i in c:
#                 a[i]=a.get(i,0)+1
#             else:
#                 b[i]=b.get(i,0)+1
#         return (max(a.values()) if a else 0)+(max(b.values()) if b else 0)
class Solution:
    def maxFreqSum(self, s: str) -> int:
        def is_vowel(char):
            return char in 'aeiou'
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