# class Solution(object):
#     def removeOccurrences(self, s, part):
#         """
#         :type s: str
#         :type part: str
#         :rtype: str
#         """
#         while part in s:
#             s=s.replace(part,"",1)
#         return s

class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        stack = []
        part_len = len(part)
        
        for char in s:
            stack.append(char) 
            if len(stack) >= part_len and "".join(stack[-part_len:]) == part:
                del stack[-part_len:] 
        
        return "".join(stack)