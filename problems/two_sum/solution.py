class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            if (target-nums[i]) in nums:
                idx = nums.index(target-nums[i])
                if idx != i:
                    return [i, idx]
        return [0,0]

