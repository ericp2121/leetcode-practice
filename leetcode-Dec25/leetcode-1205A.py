class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # if n > 0:
        #     result = math.log(n, 3)
        #     if result%1 == 0:
        #         return True
        #     else:
        #         return False 
        # else:
        #     return False
        # python number issue


        while n >= 1:
            result = n%3
            print(result )

            if n == 1:
                return True
            elif result == 0:
                n = n/3
                print('new n: ',n)
            else:
                return False 

        return False