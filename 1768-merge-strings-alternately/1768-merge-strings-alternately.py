class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        output = []

        for i in range(min(l1, l2)):
            output.append(word1[i])
            output.append(word2[i])

        output.extend(word1[min(l1, l2):])
        output.extend(word2[min(l1, l2):])

        return ''.join(output)
