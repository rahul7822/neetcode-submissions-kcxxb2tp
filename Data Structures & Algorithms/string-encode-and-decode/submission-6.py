class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str_result = ""
        for s in strs:
            l = len(s)
            encode_str = str(l) + "#" + s
            encoded_str_result += encode_str

        return encoded_str_result

    def decode(self, s: str) -> List[str]:
        # 4#neet4#code4#love3#you
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#" and j < len(s):
                j += 1
            l = int(s[i : j])

            i = j

            item = s[i + 1 : i + l + 1]
            result.append(item)

            i = i + l + 1

        return result

