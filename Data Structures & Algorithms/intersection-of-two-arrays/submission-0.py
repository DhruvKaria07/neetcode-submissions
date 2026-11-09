class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        result = set()
        for x in nums1:
            seen.add(x)
        for y in nums2:
            if y in seen:
                result.add(y)
        return list(result)