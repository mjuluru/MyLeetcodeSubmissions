class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sol = [n*n for n in nums]
        sol.sort()
        return sol
        