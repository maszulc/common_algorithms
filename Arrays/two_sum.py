class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      prev_hashmap = {} # num : index
      for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_hashmap.keys():
            return [i, prev_hashmap[diff]]
        else:
            prev_hashmap[n] = i
nums = [2,7,11,15]
target = 22
test = Solution()
print(test.twoSum(nums, target))