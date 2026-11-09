class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for word in strs:
            signature = tuple(sorted(word))
            if signature not in hashMap:
                hashMap[signature] = []
            hashMap[signature].append(word)
        return list(hashMap.values())