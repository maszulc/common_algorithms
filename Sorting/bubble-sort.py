class Solution():
    def bubbleSort(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j+1]:
                    tmp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = tmp
        return nums

    def bubbleSort2(self, nums: list[int]) -> list[int]:
        listLength = len(nums)
        for _ in range(listLength):
            for i in range(listLength - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums


arr = [4, 2, 6, 1, 8, 6, 5]
test = Solution()
print(test.bubbleSort(arr))
print(test.bubbleSort2(arr))
