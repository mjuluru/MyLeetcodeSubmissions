class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start, mid, end = 0, 0, len(nums)-1
        while (start <= end) and (end < len(nums)):
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1