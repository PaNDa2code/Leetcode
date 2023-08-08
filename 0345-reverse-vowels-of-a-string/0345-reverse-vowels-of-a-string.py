class Solution:
    def reverseVowels(self, s: str) -> str:
        
        out = [c for c in s]

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        left = 0

        right = len(s) - 1

        def swap(l,r):
            out[l],out[r] = out[r],out[l]

        while left <= right:

            left_in_v = s[left] in vowels
            right_in_v = s[right] in vowels

            if left_in_v and right_in_v:

                swap(left,right)
                left += 1
                right -= 1

            elif left_in_v:
                right -= 1

            elif right_in_v:
                left += 1

            else:
                right -= 1
                left += 1

        return ''.join(out)