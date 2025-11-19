class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # should NOT use insert due to trailing zeros 
        for i in range(n):
            for x in range(m):
                if nums2[i] <= nums1[x]:
                    # otherwise will insert all big first!
                    for z in reversed(range(x, m)):
                        nums1[z+1] = nums1[z]
                        # since shift to right, replace right value with current
                        # otherwise, will risk overwriting current number 
                    nums1[x] = nums2[i]
                    # this will replace the value at current with the value needed
                    m+=1 
                    # so check more of the relevant nums
                    break
                    # stop checking
            else:
                nums1[m] = nums2[i]
                m += 1 
                
                # biggest num edge case; must insert at end 

                
        