class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        Input: digits = [4,3,2,1]
        Output: [4,3,2,2]
        Explanation: The array represents the integer 4321.
        Incrementing by one gives 4321 + 1 = 4322.
        Thus, the result should be [4,3,2,2].
        """
        # newDigits = digits does NOT copy, just reference
        newDigits = list(digits)
        # this copies

        for i in reversed(range(len(digits))):
        # starts in reverse index
            newSum = digits[i]+1
            print('i is ',i)
            
            if newSum <= 9:
                newDigits[i] = newSum
                return newDigits
            elif newSum >= 10 and i == 0:
            # remember to use and
                newDigits[i] = 0
                newDigits = [1]+newDigits
                return newDigits
            else:
                newDigits[i] = 0
                newDigits[i-1] = newDigits[i-1]+1

                    
                
