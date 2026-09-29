from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10 and fives >= 1:
                fives -= 1
                tens += 1
            elif bill == 20:
                # make 15
                if tens >= 1 and fives >= 1:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
            else:
                return False
        
        return True
