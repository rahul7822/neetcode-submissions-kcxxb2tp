class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(comb, cur_index, cur_sum):
            if cur_sum > target:
                return
            
            if cur_sum == target:
                result.append(comb.copy())

            for i in range(cur_index, len(candidates)):
                if i > cur_index and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] + cur_sum <= target:
                    comb.append(candidates[i])
                    backtrack(comb, i + 1, candidates[i] + cur_sum)
                    comb.pop()

        backtrack([], 0 , 0)
        return result