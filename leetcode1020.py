class Solution(object):
    def removeDuplicates(self, nums):
        tmpNums = []

        i = 0

        while i < len(nums):
            if nums[i] in tmpNums:
                nums.pop(i)
                # do not increment, otherwise will skip over this element 
                # if it is duplicate, will be ignored due to shifting index for list
                # hence, only increment if it is unique!
            else: 
                tmpNums.append(nums(i))
                i = i +1

                

        
        