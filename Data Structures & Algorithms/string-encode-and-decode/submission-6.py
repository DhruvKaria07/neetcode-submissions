class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))
            result += "#"
            result += s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find("#", i)

            length = int(s[i:j])
            i = j + 1

            word = s[i: i + length]
            result.append(word)

            i = length + j + 1
        return result
