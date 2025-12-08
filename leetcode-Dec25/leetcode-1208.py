class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        squareVals = []

        for i in range(1,n+1):
            squareVals.append((i**2))

        # for i in range(len(squareVals)):
        #     for x in range(len(squareVals)):
        #         for nums in squareVals:
        #             if (squareVals[i] + squareVals[x]) == nums:
        #                 count += 1

        squareVals = set(squareVals)

        for nums in squareVals:
            for numsA in squareVals:
                if (nums + numsA) in squareVals:
                    count += 1
                    continue

        return count

                
            



        