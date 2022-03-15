class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        print(nums)
        for i in range(len(nums)-1):
            if nums[i] in nums[i+1: i+2]:
                return True
        return False