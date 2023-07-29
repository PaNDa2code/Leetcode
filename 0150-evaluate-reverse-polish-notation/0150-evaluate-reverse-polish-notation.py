class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
                stack.append(int(token))
            else:
                second_elm = stack.pop()
                first_elm = stack.pop()
                stack.append(int(eval(f'{first_elm}{token}{second_elm}')))

        return stack[0]