class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(not strs):
            return ""
        lens = [len(i) for i in strs]
        minLen = min(lens)

        longest = ""

        for i in range(0, minLen):
            prefix = set()
            for j in strs:
                prefix.add(j[i])
            if(len(prefix) == 1):
                longest+=prefix.pop()
            else:
                break

        return(longest)
