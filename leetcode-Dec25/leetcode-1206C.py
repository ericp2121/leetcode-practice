class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        quot = n//7
        remain = n%7

        maxSum = 0
        for i in range(quot):
            if quot >= 1:
                fullSum = 28 + (7*(i))
                maxSum  += fullSum
            else:
                maxSum += fullSum
                fullSum = (7*i)


        remainStart = quot
        remainSum = 0
        for x in range(remain):
            remainStart += 1
            remainSum = remainStart + remainSum

        return maxSum + remainSum
           
