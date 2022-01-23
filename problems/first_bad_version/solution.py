# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        mid = 0
        result = []
        result.append(n)
        while l < r :
            mid = l + (r-l)//2
            if mid == l or mid == r:
                break
            if isBadVersion(mid):
                result.append(mid)
                r = mid
            else:
                l = mid
        return min(result)