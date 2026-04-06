class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r_dict = {}
        for s in strs:
            ar = [0] * 26
            for ch in s:
                ar[ord(ch) - 97] += 1
            
            s_tuple = tuple(ar)
            if s_tuple in r_dict:
                r_dict[s_tuple].append(s)
            else:
                r_dict[s_tuple] = [s]
        
        return list(r_dict.values())
