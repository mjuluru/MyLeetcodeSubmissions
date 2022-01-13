class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            if (target-nums[i]) in nums:
                index = nums.index(target-nums[i])
                if index != i:
                    result.append(i)
                    result.append(index)
                    break
        return result