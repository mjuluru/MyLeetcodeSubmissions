class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0 and n>0:
            nums1[0:] = nums2[0:]
        elif m>0 and n==0:
            nums1 = nums1
        else:
            i,j = 0,0
            while i<(m+j) and j<n:
                
                if nums1[i] < nums2[j]:
                    i += 1
                elif nums2[j] < nums1[i]:
                    nums1[i+1:] = nums1[i:-1]
                    nums1[i] = nums2[j]
                    j += 1
                else:
                    nums1[i+1:] = nums1[i:-1]
                    nums1[i] = nums2[j]
                    j += 1

            if j<n:
                nums1[i:] = nums2[j:]

