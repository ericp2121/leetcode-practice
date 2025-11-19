class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        intA = self.convertBinaryToInt(a)
        intB = self.convertBinaryToInt(b)
        sumFinal = intA + intB

        if intA == 0 and intB == 0:
            return '0'
        print(sumFinal)
        biOutput = self.convertIntToBinary(sumFinal)

        return biOutput

    def convertBinaryToInt(self, num):
        sum = 0
        digits = [int(d) for d in str(num)]
        # converts into array of nums

        for i in reversed(range(len(digits))):

            sum = sum + int(digits[i])*(2**(len(digits)-1-i))
            # converts into int, reverse needed since index order is reversed for powers of 2
        print(' current sum is ', sum)
        return sum
    
    def convertIntToBinary(self, num):
        newNum = []
        newInt = num

        while newInt >= 1:
            newNum.append(newInt%2)
            newInt = newInt//2
            # divide by 2 until cannot, reverse for the int value. 
            # wait until quotient is 0

        biNum = [str(d) for d in reversed(newNum)]
        biNumJoin = "" .join(biNum)

        return biNumJoin