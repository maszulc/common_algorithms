class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        start = 0
        stop = len(nums) - 1
        while(start <= stop):
            if nums[start] == nums[stop]:
                print(f'indices {start} and {stop} are duplicates')
                return True
            else:
                start += 1
                stop  -= 1
        return False

    def containsDuplicate2(self, nums: list[int]) -> bool:
        hashSet = []
        for n in nums:
            if n in hashSet:
                print(f'found duplicates: {n}')
                return True
            else:
                hashSet.append(n)

nums = [1,7,8,3,3,4,3,2,4,2]
test = Solution()
print(test.containsDuplicate(nums))
print(test.containsDuplicate2(nums))
