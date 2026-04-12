class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            subsets = []
            for sub in result:
                subsets.append(sub + [num])
            result += subsets

        return result
