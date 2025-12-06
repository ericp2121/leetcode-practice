class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # rowCounter = 0

        # for i in range(1, n+1):
        #     # print('i', i)
        #     if n < i:
        #         # print('quitting because hit final row')
        #         return rowCounter
        #     n -= i
        #     # print('n', n)
        #     rowCounter += 1
        #     # print('row counter ', rowCounter)
        # return rowCounter
        # 
        # memory limit exceeded 

        # k * (k + 1) / 2 triangular number formula 

        left = 0
        right = n 

        found = False

        while left <= right:
            mid = (left + right) // 2   # middle index
            coinSum = mid*(mid+1)//2 # calculate total coins at the mid point

            if coinSum == n:
                return mid              # found it! if by case of equal to row 
            elif coinSum < n:
                left = mid + 1          # search right half
            else:
                right = mid - 1         # search left half

        return right   # not found




        