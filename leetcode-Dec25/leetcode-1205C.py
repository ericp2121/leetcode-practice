class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        stringfy = str(num)
        listNum = list(stringfy)
        sum = False 

        while sum == False:
            checkSum = 0
            for i in range(len(listNum)):
                checkSum = checkSum + int(listNum[i])
            
            # print(checkSum)
            if checkSum < 10:
                sum = True
                return checkSum

            stringfy = str(checkSum)
            listNum = list(stringfy)


