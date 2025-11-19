class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """

        setNums = set(nums)
        flag = True


        if original in setNums: 
            while flag == True:
                # cannot be iterative through array because cannot assume that next value will be acceptable.
                for num in setNums:
                    original = original*2
                    if original in setNums:
                        flag = True
                    else:
                        flag = False
                        return original 
        else:
            return original 
        

