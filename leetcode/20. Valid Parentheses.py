class Solution(object):
    def isValid(self, s):
        parenthesis = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                parenthesis.append(s[i])
            elif (len(parenthesis) != 0 and parenthesis[len(parenthesis) - 1] == '(' and s[i] == ')') or (
                    len(parenthesis) != 0 and parenthesis[len(parenthesis) - 1] == '{' and s[i] == '}') or (
                    len(parenthesis) != 0 and parenthesis[len(parenthesis) - 1] == '[' and s[i] == ']'):
                parenthesis.pop()
            else:
                return False
        return len(parenthesis) == 0


print(Solution().isValid("]("))
