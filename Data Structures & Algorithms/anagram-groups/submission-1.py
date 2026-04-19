class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}

        for string in strs:
            string_len = len(string)
            ord_sum = self.get_ord_sum(string)
            set_len = len(set(string))
            
            if (string_len, ord_sum, set_len) in result_dict:
                result_dict[(string_len, ord_sum, set_len)].append(string)
            else:
                result_dict[(string_len, ord_sum, set_len)] = [string]

        return list(result_dict.values())

    
    def get_ord_sum(self, string: str):
        sum_result = 0
        for ch in string:
            sum_result += ord(ch)
        
        return sum_result