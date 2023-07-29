class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        tmp = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in tmp:
                tmp[sorted_word].append(word)
            else:
                tmp[sorted_word] = [word]        
        return [tmp[key] for key in tmp]