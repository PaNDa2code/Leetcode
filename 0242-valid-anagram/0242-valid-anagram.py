class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not 1 <= len(s) <= 5 * 10**4 or not 1 <=  len(t) <= 5 * 10**4:
            raise Error('Big string')
        
        def counter(st:str)->dict:
            out =  {}
            for s in st:
                out[s] = out.get(s,0) + 1
            return out
        
        return counter(s) == counter(t)