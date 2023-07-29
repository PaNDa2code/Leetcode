class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
                stack.append(int(token))
            else:
                second_elm = stack.pop()
                first_elm = stack.pop()              
                match token:
                    case '+':
                        stack.append(first_elm+second_elm)
                    case '-':
                        stack.append(first_elm-second_elm)
                    case '*':
                        stack.append(first_elm*second_elm)
                    case '/':
                        stack.append(int(first_elm/second_elm))

        return stack[0]