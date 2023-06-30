class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        neg = 1
        index = 0

        if s[0] == '+':
            index = 1
        elif s[0] == '-':
            neg = -1
            index = 1

        output = 0
        while index < len(s) and s[index].isdigit():
            output = output * 10 + int(s[index])
            index += 1

        output *= neg

        if output < -2 ** 31:
            return -2 ** 31
        elif output > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return output
