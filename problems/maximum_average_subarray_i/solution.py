class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        averages = []
        start = 0
        end = k
        sum_k = sum(nums[start:end])
        averages.append((sum_k/k))
        for i in range(k, len(nums)):
            sum_k = sum_k + nums[i] - nums[start]
            averages.append((sum_k/k))
            start += 1
        return max(averages)
        
        