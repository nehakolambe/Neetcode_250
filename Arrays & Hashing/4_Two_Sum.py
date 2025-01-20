from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in numsMap:
                return [numsMap[difference],i]
            numsMap[nums[i]] = i
        return []

if __name__ == "__main__":
    solution = Solution()
    nums, target = [2,7,11,15], 9
    print(solution.twoSum(nums,target))