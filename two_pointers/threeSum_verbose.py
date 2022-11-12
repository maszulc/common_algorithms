class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i, value in enumerate(nums):
            if i > 0 and value == nums[i - 1]:  # skip duplicates
                continue
            left_ptr, right_ptr = i, len(nums) - 1
            print(f'i = {i}, value = {value} left_ptr = {left_ptr}:')
            while left_ptr < right_ptr:
                triplet = value + nums[left_ptr] + nums[right_ptr]
                print(
                    f'{value} + {nums[left_ptr]} + {nums[right_ptr]} = {triplet}')
                if triplet > 0:
                    right_ptr -= 1
                elif triplet < 0:
                    left_ptr += 1
                else:
                    res.append([value, nums[left_ptr], nums[right_ptr]])
                    left_ptr += 1
                    # skip save values
                    while nums[left_ptr] == numbers_list[left_ptr - 1] and left_ptr < right_ptr:
                        left_ptr += 1
        return res


numbers_list = [-1, 0, 1, 2, -1, -4, 5, 3]
test_object = Solution()
res = test_object.threeSum(numbers_list)
print("Found triplets:")
print(res)
