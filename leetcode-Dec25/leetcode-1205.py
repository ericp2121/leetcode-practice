import re
import string

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[' + re.escape(string.punctuation) + r'\s]', '', s)
        reversedStr = "".join(reversed(s))

        s = s.lower()
        reversedStr = reversedStr.lower()

        if reversedStr == s:
            # reversed returns array of individual chars
            return True

        else:
            return False