from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_dict = defaultdict(set)
        super_trust_set = set()

        for x, y in trust:
            trust_dict[y].add(x)
            super_trust_set.add(x)

        for key, value in trust_dict.items():
            if len(value) == n - 1 and key not in super_trust_set:
                return key
        
        return -1