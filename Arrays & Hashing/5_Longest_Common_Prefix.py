from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        sortStrs = sorted(strs)
        firstStr = sortStrs[0]
        lastStr = sortStrs[-1]
        for i in range(min(len(firstStr),len(lastStr))):
            if firstStr[i] != lastStr[i]:
                return lcp
            lcp += firstStr[i]
        return lcp

if __name__ == "__main__":
    solution = Solution()
    strs = ["flower","flow","flight"]
    print(solution.longestCommonPrefix(strs))