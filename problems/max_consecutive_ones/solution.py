class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        sol = []
        for i in nums:
            if i == 1:
                count = count + 1
            else:
                sol.append(count)
                count = 0
        sol.append(count)
        count = 0
        return max(sol)
        