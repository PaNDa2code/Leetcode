class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def helper(opened=0, closed=0):
                open_allowed = opened < n
                close_allowed = closed < opened

                if open_allowed and close_allowed:
                    return ['(' + p for p in helper(opened + 1, closed)] + \
                        [')' + p for p in helper(opened, closed + 1)]
                elif open_allowed:
                    return ['(' + p for p in helper(opened + 1, closed)]
                elif close_allowed:
                    return [')' + p for p in helper(opened, closed + 1)]
                else:
                    return ['']


        return helper()
        