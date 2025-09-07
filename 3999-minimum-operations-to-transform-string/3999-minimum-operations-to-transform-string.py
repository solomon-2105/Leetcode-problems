class Solution:
    def minOperations(self, s: str) -> int:
        # if s=='a': return 0
        # count=0
        # for i in s:
        #     if (ord(i)-96)<=(123-ord(i)):
        #         count+=ord(i)-96
        #     else:
        #         count+=123-ord(i)
        # return count
        a=set(s)
        a.discard('a')
        if len(a)==0: return 0
        c,d=min(a),max(a)
        return ord(d)-ord(c)+26-(ord(d)-ord('a'))