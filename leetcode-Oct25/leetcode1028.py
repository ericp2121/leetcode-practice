class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Given an array nums of size n, return the majority element.

        The majority element is the element that appears more than ⌊n / 2⌋ times. 
        You may assume that the majority element always exists in the array.


        """

        # for num in nums:
        #     if nums.count(num) >= len(nums)/2:
        #         return num
        # run time too slow, O(n^2)

        noRepeat = set(nums)
        # extracts every value , once!

        for num in noRepeat:
            
            if nums.count(num) > len(nums)/2:
                # must be > , otherwise will round down if odd and put wrong answer
                return num


