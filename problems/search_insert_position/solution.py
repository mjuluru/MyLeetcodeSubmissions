class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        l = 0
        r = len(nums)-1
        mid = 0
        if nums[r] < target:
            return r+1
        elif nums[l] > target:
            return l
        while l < r  and r < len(nums):
            mid = l + (r-l)//2
            if (nums[l] < target) and (nums[r] > target) and ((r-l) == 1):
                return r
            elif nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid