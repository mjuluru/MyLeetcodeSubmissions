class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            if i in count.keys():
                return True
                break
            else:
                count[i] = 1
        return False