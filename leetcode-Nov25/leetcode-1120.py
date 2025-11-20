class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        repeated = []
        counterNum1 = Counter(nums1)
        counterNum2 = Counter(nums2)
        # prints list of values and occurences

        print(counterNum1)
        print(counterNum2)

        intersection = counterNum1&counterNum2
        # intersection of two counters

        for value in intersection:
            #check by value
            repeats = intersection[value]
            # fetch the associated count value 

            for i in range(repeats):
                repeated.append(value)
                # add to list per # times of count

        return repeated 
        