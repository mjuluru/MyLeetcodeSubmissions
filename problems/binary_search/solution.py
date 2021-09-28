class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        mid = ( left + right )/2
        
        while left < right :
            mid = int(( left + right )/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = left + 1
            else:
                right = right - 1
        return -1
            
        