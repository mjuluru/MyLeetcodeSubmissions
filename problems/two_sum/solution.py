class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(enumerate(nums), key = lambda t:t[1])
        l,r = 0, len(nums)-1
        while l<=r :
            if nums[l][1]+nums[r][1] < target:
                l += 1
            elif nums[l][1]+nums[r][1] > target:
                r -= 1
            else:
                return nums[l][0],nums[r][0]