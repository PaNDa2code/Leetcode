class Solution:
    def reverseWords(self, s: str) -> str:
        
        return ' '.join([c for c in s.strip().split(' ') if c != ''][::-1])