import itertools

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        if len(digits) < 1:
            return []

        digit_to_letter = {
            2: ('a', 'b', 'c'),
            3: ('d', 'e', 'f'),
            4: ('g', 'h', 'i'),
            5: ('j', 'k', 'l'),
            6: ('m', 'n', 'o'),
            7: ('p', 'q', 'r', 's'),
            8: ('t', 'u', 'v'),
            9: ('w', 'x', 'y', 'z')
        }
        

        return [''.join(comb) for comb in itertools.product(*tuple([digit_to_letter[int(dig)] for dig in digits]))]