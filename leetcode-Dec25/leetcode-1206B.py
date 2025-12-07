class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # missing = []
        # sortedArray = sorted(nums)
        
        # for i in range(1,len(nums)+1):
        #     # print(i, ' not in , adding ')
        #     if i not in nums:
        #         # print(i, ' not in , adding ')
        #         missing.append(i)

        # return missing

        missing = []
        setNums = set(nums)
        
        for i in range(1,len(nums)+1):
            # print(i, ' not in , adding ')
            if i not in setNums:
                # print(i, ' not in , adding ')
                missing.append(i)

        return missing 