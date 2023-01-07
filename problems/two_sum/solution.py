class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0,n):
            if target-nums[i] in nums:
                loc = nums.index(target-nums[i])
                if loc != i:
                    return [i,loc]
                
        return [0,0]

