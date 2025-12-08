class Solution(object):

    def countOdds(self, low, high):

        """

        :type low: int

        :type high: int

        :rtype: int

        """


        # for i in range(low, high+1):

        #     if i%2 != 0:

        #         oddCount += 1


        # return oddCount

        # O(n) too high

        

        baseCase = (high-low+1)/2

        if (high - low + 1)%2 == 0:

            return baseCase


        elif (high%2 != 0 and low%2 != 0):

            return baseCase + 1


        else:

            return baseCase