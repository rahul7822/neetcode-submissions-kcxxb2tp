class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "[]"

        encoded_str_result = []
        for s in strs:
            encoded_str = "+".join(list(map(lambda x : str(ord(x)), s)))
            encoded_str_result.append(encoded_str)
        
        return "-".join(encoded_str_result)

            

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        
        if s == "[]":
            return []

        result = []
        encoded_strs_by_del = s.split("-")
        for s in encoded_strs_by_del:
            decoded_str = "".join(list(map(lambda x : chr(int(x)) , s.split("+"))))
            result.append(decoded_str)

        return result