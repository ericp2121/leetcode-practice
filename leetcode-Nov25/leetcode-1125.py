class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # for i in range(len(nums)):
        #     print('checking ',nums[i])
        #     print(nums)
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         #pops index not value
        #         nums.append(0)

        # problem with above solutoin is that it only checks each index once

        occurences = nums.count(0)

        for i in range(occurences):
            nums.remove(0)
            nums.append(0)
    
        return nums

        