class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
    
        digitsA = [int(a) for x in str(a)]
        digitsB = [int(b) for x in str(b)]
        newNum = []

        if len(digitsA) >= len(digitsB):
            execLen = len(digitsA)
        else:
            execLen = len(digitsB)

        carryOver = 0
        for i in reversed(range(execLen)):
            if digitsA[i] == 1 and digitsB[i] == 1 and carryOver == 0:
                newNum = [0]+newNum
                carryOver = 1
            if digitsA[i] == 1 and digitsB[i] == 1 and carryOver == 1:
                newNum = [1]+newNum
                carryOver = 1
            if (digitsA[i] == 1 and digitsB[i] == 0) or (digitsA[i] == 0 and digitsB[i] == 1) and carryOver == 1:
                newNum = [0]+newNum
                carryOver = 1
            if (digitsA[i] == 1 and digitsB[i] == 0) or (digitsA[i] == 0 and digitsB[i] == 1) and carryOver == 0:
                newNum = [1]+newNum
                carryOver = 0
            if (digitsA[i] == 0 and digitsB[i] == 0) and carryOver == 1:
                newNum = [1]+newNum
                carryOver = 0
            if (digitsA[i] == 0 and digitsB[i] == 0) and carryOver == 0:
                newNum = [0]+newNum
                carryOver = 0


        biNum = [str(d) for d in reversed(newNum)]
        biNumJoin = "" .join(biNum)
        newBiNum = int(biNumJoin)

        return newBiNum
        

        # contains logic errors 