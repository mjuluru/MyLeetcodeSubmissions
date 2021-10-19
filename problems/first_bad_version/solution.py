# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

import random

class Solution:    
    
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = int(left + (right-left)/2)
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid
        return left