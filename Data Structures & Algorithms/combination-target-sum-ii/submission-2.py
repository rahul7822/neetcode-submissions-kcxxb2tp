class Solution:
    def check_present(self, lists, item):
        return (lambda lists, item : any(tuple(item) == tuple(s) for s in lists))(lists, item)
   
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, cur_sum, subset):
            if cur_sum == target:
                if not self.check_present(result, sorted(subset)):
                    result.append(sorted(subset.copy()))

            if cur_sum > target:
                return

            for i in range(index, len(candidates)):
                if cur_sum + candidates[i] <= target:
                    subset.append(candidates[i])
                    backtrack(i + 1, cur_sum + candidates[i], subset)
                    subset.pop()

        backtrack(0, 0, [])
        return result
