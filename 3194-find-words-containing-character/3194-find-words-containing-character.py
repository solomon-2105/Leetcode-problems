class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        a=[]
        for i in range(len(words)):
            if x in list(words[i]):
                a.append(i)
        return a