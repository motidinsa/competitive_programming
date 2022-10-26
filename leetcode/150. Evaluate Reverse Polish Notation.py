class Solution(object):
    def evalRPN(self, tokens):
        while True:
            for i in range(len(tokens)):
                if tokens[i] == '/' or tokens[i] == '*' or tokens[i] == '-' or tokens[i] == '+':
                    if tokens[i] == '/':
                        result = int(tokens[i - 2]) / int(tokens[i - 1])
                        del tokens[i]
                        del tokens[i - 1]
                        tokens[i - 2] = int(result)
                    elif tokens[i] == '*':
                        result = int(tokens[i - 2]) * int(tokens[i - 1])
                        del tokens[i]
                        del tokens[i - 1]
                        tokens[i - 2] = result
                    elif tokens[i] == '-':
                        result = int(tokens[i - 2]) - int(tokens[i - 1])
                        del tokens[i]
                        del tokens[i - 1]
                        tokens[i - 2] = result
                    elif tokens[i] == '+':
                        result = int(tokens[i - 2]) + int(tokens[i - 1])
                        del tokens[i]
                        del tokens[i - 1]
                        tokens[i - 2] = result
                    break
            if len(tokens) == 1:
                return tokens[0]


print(Solution().evalRPN(["0", "3", "/"]))
