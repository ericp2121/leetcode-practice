class Solution(object):

    def firstUniqChar(self, s):

        """

        :type s: str

        :rtype: int

        """

        char_count = Counter(s)

        newS = list(s)


        for c in s:  # iterate in original order

            if char_count[c] == 1:

                return newS.index(c)

            

        return -1

        

