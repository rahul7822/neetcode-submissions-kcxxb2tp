class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            tmp_result = []
            for item in result:
                tmp_result.append(item + [num])
                print(tmp_result)
            result = result + tmp_result

        return result