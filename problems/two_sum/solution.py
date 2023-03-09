class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            if (target-nums[i]) in nums:
                index = nums.index(target-nums[i])
                if index != i:
                    return [i,index]
        return [0,0]

