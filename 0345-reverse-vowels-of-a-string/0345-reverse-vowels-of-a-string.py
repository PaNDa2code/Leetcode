class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        hash_map = {}

        for x,c in enumerate(s):

            if c in hash_map:
                hash_map[c].append(x)
            else:
                hash_map[c] = [x]

        v_idxs = sorted([x for c in vowels for x in hash_map.get(c, [])])

        out = [c for c in s]

        for x,c in enumerate(out):

            if len(v_idxs)>1 and x == v_idxs[0]:

                right = v_idxs.pop()
                left = v_idxs.pop(0)

                out[left],out[right] = out[right],out[left]

        return ''.join(out)