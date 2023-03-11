class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        count1, count2 = Counter(nums1), Counter(nums2)
        for i in count1.keys():
            if i in count2.keys():
                result.extend([i]*min(count1[i], count2[i]))
        return result
        