# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        # You should minimize the number of calls to the API.
        # so, cannot run every single check 

        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid      # first bad is mid or before
            else:
                left = mid + 1   # first bad is after mid

        return left   # left points to the first bad version
