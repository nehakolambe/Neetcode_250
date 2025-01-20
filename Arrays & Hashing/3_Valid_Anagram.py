from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = defaultdict(int)
        hasht = defaultdict(int)
        for val in s:
            hashs[val] += 1
        for val in t:
            hasht[val] += 1
        if hashs == hasht:
            return True
        return False

if __name__ == "__main__":
    solution = Solution()
    s, t = "anagram", "nagaram"
    print(solution.isAnagram(s,t))