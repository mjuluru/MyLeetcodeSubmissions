class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = [1]*len(nums)
        pre = 1
        post = 1
        for i in range(len(nums)):
            r[i] = pre
            pre *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            r[i] *= post
            post *= nums[i]
        return r
        