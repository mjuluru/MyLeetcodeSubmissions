class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k<=len(nums):
            temp = nums[-k:]
            nums[k:] = nums[:-k]
            nums[:k] = temp
        else:
            k = k%len(nums)
            temp = nums[-k:]
            nums[k:] = nums[:-k]
            nums[:k] = temp