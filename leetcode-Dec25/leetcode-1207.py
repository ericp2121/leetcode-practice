class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        tmpArr = []
        newOutput = []


        for i in range(len(nums)-1,-1,-1):
            tmpArr.append(nums[i])
                  
            if (nums[i]-1) == (nums[i-1]):
                continue 
            else:

                if len(tmpArr) > 1:
                    smallOut = str(min(tmpArr)) + "->" + str(max(tmpArr))
                    newOutput.append(smallOut)
                else:
                    smallOut = str(tmpArr[0])
                    newOutput.append(smallOut)

                tmpArr = []

        newOutput.reverse()
        return newOutput
            
        