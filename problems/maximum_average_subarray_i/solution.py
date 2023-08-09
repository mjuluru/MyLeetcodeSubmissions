class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        result = curr_avg = sum(nums[left:k])/k
        for right in range(k,len(nums)):
            curr_avg += nums[right]/k
            curr_avg -= nums[left]/k
            left += 1
            result = max(result, curr_avg)
        return result