class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        if len(nums) > 1:
            i = 0
            count = 0
            while (i < len(nums)):
                if count == counter[0] and (nums[-count] == 0 and nums[-1] == 0):
                    break
                if nums[i] == 0:
                    count += 1
                elif count>0:
                    nums[i-count] = nums[i]
                    nums[i] = 0
                
                i += 1