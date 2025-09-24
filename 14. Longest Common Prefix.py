class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = [] #not the best solution
        idx = 0
        for i in range(len(strs[0])):
            first_word.append(strs[0][i])
        while idx < len(first_word):
            for j in range(len(strs)):
                if idx >= len(strs[j]):
                    return "".join(first_word[0:idx])
                elif strs[j][idx] != first_word[idx]:
                    return "".join(first_word[0:idx])
            idx += 1
        return "".join(first_word[0:idx])
