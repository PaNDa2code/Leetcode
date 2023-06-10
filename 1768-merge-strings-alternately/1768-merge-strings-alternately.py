class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l = max(len(word1),len(word2))

        output = ''
        
        for i in range(l):
            if i >= len(word1):output += word2[i]
            elif i >= len(word2):output+= word1[i]
            else :output += word1[i]+word2[i]

        return output