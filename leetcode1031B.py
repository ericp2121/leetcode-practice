class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        newList = sorted(nums)
        n = len(newList)



        if newList[len(newList)-1] != n:
            return n
            # for edge case where last digit != n
        if newList[0] != 0:
            return 0
            # edge case 0 missing

        for i in range(len(newList)-1):
            if (newList[i] + 1) != (newList[i+1]):
                return newList[i]+1
