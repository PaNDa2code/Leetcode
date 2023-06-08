class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        processed = '#'.join('^{}$'.format(s))
        length = len(processed)
        p = [0] * length 
        center = right = 0 
        max_length = max_center = 0  

        for i in range(1, length - 1):
            if i < right:
                mirror = 2 * center - i
                p[i] = min(right - i, p[mirror])

          
            while processed[i + 1 + p[i]] == processed[i - 1 - p[i]]:
                p[i] += 1

           
            if i + p[i] > right:
                center, right = i, i + p[i]

                if p[i] > max_length:
                    max_length = p[i]
                    max_center = i

        
        start = (max_center - max_length) // 2
        return s[start: start + max_length]
