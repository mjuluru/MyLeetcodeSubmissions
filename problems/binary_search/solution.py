class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        l = 0
        r = len(nums)
        mid = 0
        while(l < r):
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = l + 1
            else:
                r = r - 1