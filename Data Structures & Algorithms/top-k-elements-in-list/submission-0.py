class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for x in nums:
            freqMap[x] = freqMap.get(x, 0) + 1

        sortedItems = sorted(
            freqMap.items(),
            key= lambda x:x[1],
            reverse= True
        )

        result = []
        for x in sortedItems:
            if len(result) == k:
                break
            result.append(x[0])
        return result
