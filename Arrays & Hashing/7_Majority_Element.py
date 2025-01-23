from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsMap = defaultdict(int)
        for num in nums:
            numsMap[num] += 1
        for key,val in numsMap.items():
            if val > len(nums) / 2:
                return key

if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,3]
    print(solution.majorityElement(nums))