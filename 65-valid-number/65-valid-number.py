import re

class Solution:
    def isNumber(self, s: str) -> bool:


        prefix = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        
        return re.match(prefix,s)
