from collections import Counter

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # setList = set(nums)
        
        # for num in setList:
        #     if nums.count(num) >= 2:
        #         return True

        # return False
        # run time too long

        countList = Counter(nums)
        # counter counts apperances in list automatically 

        # for num, count in countList.items():
        #     print('num ',num , " appears times: ",count)
        #     if count >= 2:
        #         return True
        # return False
        # solution A, but slow

        count = {} # dict
        for num in nums: 
            if num in counts: 
                counts[num] += 1
                if counts[num] >= 2
                    return True
                    # should be faster, since do not need to check all elements
                # increments the key's value pair by 1 if already appears
            else:
                counts[num] = 1
                # if not in list, append