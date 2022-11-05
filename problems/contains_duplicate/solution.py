class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        items = {}
        for i in nums:
            if i not in items:
                items[i] = 0
            else:
                return True

        return False