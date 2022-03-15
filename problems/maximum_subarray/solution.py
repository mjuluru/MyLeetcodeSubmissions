class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m_sum = nums[0]
        c_sum = nums[0]
        for i in nums[1:]:
            c_sum = max(i, c_sum+i)
            m_sum = max(m_sum, c_sum)
        return m_sum