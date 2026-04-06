class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while start < end:
            value = numbers[start] + numbers[end]
            if value == target:
                break

            if value > target:
                end -= 1
                continue

            if value < target:
                start += 1
                continue
            
        return [start + 1, end + 1]