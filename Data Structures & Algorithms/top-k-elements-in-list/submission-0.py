class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequecy_dict = {}

        for num in nums:
            if num in frequecy_dict:
                frequecy_dict[num] += 1
            else:
                frequecy_dict[num] = 1

        sorted_frequecy_dict = dict(sorted(frequecy_dict.items(), key = lambda item : item[1], reverse=True))

        return list(islice(sorted_frequecy_dict.keys(), k))
