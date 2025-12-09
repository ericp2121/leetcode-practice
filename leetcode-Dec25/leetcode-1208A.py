class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # s = list(s)
        # t = list(t)

        # if len(s) == len(t):
        #     if len(s) < len(t):
        #         for char in s:
        #             if char not in t:
        #                 return False
        #             else:
        #                 t.remove(char)
        #     else:
        #         for char in t:
        #             if char not in s:
        #                 return False
        #             else:
        #                 s.remove(char)
        #     return True
        # else:
        #     return False

        # # slow run time

        s = Counter(s)
        t = Counter(t)
        
        return s == t