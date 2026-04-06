class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_d = {}
        for n in nums:
            num_d[n] = 1 + num_d.get(n, 0)
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in num_d.items():
            buckets[freq].append(num)

        result = []
        counter = 0
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            for num in bucket:
                result.append(num)
                counter += 1

                if counter == k:
                    break

            if counter == k:
                    break

        return result

        