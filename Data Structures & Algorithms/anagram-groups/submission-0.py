class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}

        for string in strs:
            string_len = len(string)
            ord_sum = self.get_ord_sum(string)
            
            if (string_len, ord_sum) in result_dict:
                result_dict[(string_len, ord_sum)].append(string)
            else:
                result_dict[(string_len, ord_sum)] = [string]

        return list(result_dict.values())

    
    def get_ord_sum(self, string: str):
        sum_result = 0
        for ch in string:
            sum_result += ord(ch)
        
        return sum_result