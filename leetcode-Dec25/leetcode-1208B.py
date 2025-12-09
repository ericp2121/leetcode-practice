class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        longestCount = 0
        tmpCount = 0

        for num in nums:
            # print('checking ',num)
            if num == 1:
                tmpCount += 1
                # print('tmpCount',tmpCount)
                if tmpCount > longestCount:
                    # print('new largest count',tmpCount)
                    longestCount = tmpCount
            else:
                tmpCount = 0
        
        return longestCount 


        