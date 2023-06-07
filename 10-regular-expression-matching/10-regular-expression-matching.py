import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = "^" + p + "$"  # Add ^ at the beginning and $ at the end
        return bool(re.match(pattern, s))
        