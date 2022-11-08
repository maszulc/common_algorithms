class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for _ in range(len(nums))]
        for n in nums:
            count[n] = count.get(n, 0) + 1
        print(f'count = {count}')
        for key, value in count.items():
            freq[value].append(key)
        print(f'freq = {freq}')
        res = []
        for x in range(len(freq) - 1 ,0, - 1):
            if (freq[x]):
                res.append(freq[x])
                if len(res) == 2:
                    return res





nums, k = [1,1,1,2,2,3], 2
print(f'nums = {nums} \nk = {k}')

test = Solution()
print(test.topKFrequent(nums, k))