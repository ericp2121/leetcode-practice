class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """

        zx_diff = abs(z-x)
        zy_diff = abs(z-y)

        if zx_diff == zy_diff:
            return 0
        elif zx_diff < zy_diff:
            return 1
        else:
            return 2
        