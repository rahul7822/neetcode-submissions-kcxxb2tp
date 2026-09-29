from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        balance_dict = defaultdict(int)

        for bill in bills:
            if bill == 5:
                balance_dict[5] += 1
            elif bill == 10 and balance_dict.get(5, -1) >= 1:
                balance_dict[5] -= 1
                balance_dict[10] += 1
            elif bill == 20:
                # make 15
                if balance_dict.get(10, -1) >= 1 and balance_dict.get(5, -1) >= 1:
                    balance_dict[10] -= 1
                    balance_dict[5] -= 1
                elif balance_dict.get(5, -1) >= 3:
                    balance_dict[5] -= 3
                else:
                    return False
            else:
                return False
        
        return True
