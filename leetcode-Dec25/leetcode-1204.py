class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum = 0
        result = 0
        
        for i in range(len(nums)-1):
            # need to do -1 so it does not calculate left sum with entire array 
            leftSum += nums[i]
            rightSum = sum(nums) - leftSum
            print('checking right ',rightSum, ' left sum ', leftSum)
            checkSum = leftSum - rightSum

            if checkSum%2 == 0:
                result += 1
            
        return result 


        