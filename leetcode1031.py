from collections import Counter

class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        countChecker = Counter(nums)
        repeated = []

        for num, count in countChecker.items():
            # .items() iterates over key and value, where without it, it iterates only keys (ie only num and not count)
            if count >= 2:
                repeated.append(num)

        return repeated 
