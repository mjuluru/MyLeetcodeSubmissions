class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(0, len(nums)):
            if (target-nums[n]) in nums:
                idx = nums.index(target-nums[n])
                if idx != n:
                    return [n, idx]