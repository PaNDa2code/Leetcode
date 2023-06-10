class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        
        output = [word1[i] + word2[i] for i in range(min(len1, len2))]
        output.extend(word1[min(len1, len2):] + word2[min(len1, len2):])
        
        return ''.join(output)

