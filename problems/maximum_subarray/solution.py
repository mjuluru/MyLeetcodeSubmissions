class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return sum(nums)
        
        sol = [[0 for j in range(2)] for i in range(len(nums))]
        result = -math.inf
        
        for i in range(len(nums)):
            sol[i][0] = nums[i]
            if i == 0:
                sol[i][1] = nums[i]
                result = max(result, sol[i][1])
            else:
                sol[i][1] = max(sol[i][0], sol[i-1][1]+sol[i][0], sol[i-1][0]+sol[i][0])
                result = max(result, sol[i][1])

        return int(result)

            
            