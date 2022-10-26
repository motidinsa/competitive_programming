class Solution(object):
    def reverseParentheses(self, val):
        s = list(val)
        while True:
            parentheses = []
            for i in range(len(s)):
                if s[i] == '(':
                    parentheses.append(i)
                elif s[i] == ')':
                    currentVal = s[parentheses[len(parentheses) - 1] + 1:i]
                    reversedVal = ''
                    for j in range(len(currentVal)):
                        reversedVal = currentVal[j] + reversedVal
                    s = s[:parentheses[len(parentheses) - 1]] + list(reversedVal) + s[i + 1:]
                    break
            print(s)
            if '(' not in s:
                reversedWord = ''
                for i in range(len(s)):
                    reversedWord = reversedWord + s[i]
                return reversedWord


print(Solution().reverseParentheses("(ed(et(oc))el)"))
