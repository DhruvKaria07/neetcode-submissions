class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for x in seen:
            if x - 1 not in seen:
                current = x
                length = 1
                while current + 1 in seen:
                    current = current + 1
                    length = length + 1
                longest = max(length, longest)
        return longest
        