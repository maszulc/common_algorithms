class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue
            lp, rp = i, len(nums) - 1
            while lp < rp:
                triplet = v + nums[lp] + nums[rp]
                if triplet < 0:
                    lp += 1
                elif triplet > 0:
                    rp -= 1
                else:
                    res.append(
                        [v, nums[lp], nums[rp]]
                    )
                    lp += 1
                    while lp < rp and nums[lp] == nums[lp-1]:
                        lp += 1
        return res


numbers_list = [-1, 0, 1, 2, -1, -4, 5, 3]
test_object = Solution()
res = test_object.threeSum(numbers_list)
print("Found triplets:")
print(res)
