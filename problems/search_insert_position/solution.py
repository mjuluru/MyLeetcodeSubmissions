class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result = 0
        start, end = 0,len(nums)-1
        mid = (start+end)//2
        if target in nums:
            return nums.index(target)
        while (start <= end) and (end < len(nums)):
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
                result = start
            else:
                end = mid - 1
                result = start
        return result