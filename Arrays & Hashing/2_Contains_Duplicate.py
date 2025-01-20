from typing import List
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashm = defaultdict(int)
        for num in nums:
            hashm[num] += 1
        for val in hashm.values():
            if val >= 2:
                return True
        return False
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate([1,2,3,1]))