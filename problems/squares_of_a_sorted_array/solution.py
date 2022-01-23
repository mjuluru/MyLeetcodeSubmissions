class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [n**2 for n in nums]
        result.sort()
        return result