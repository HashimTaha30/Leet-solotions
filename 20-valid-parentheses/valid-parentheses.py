class Solution:
    def isValid(self, s: str) -> bool:


        stack = []

        for ch in s:
            if ch == '(':
                stack.append(')')
            elif ch == '[':
                stack.append(']')
            elif ch == '{':
                stack.append('}')
            else:
                if stack == [] or ch != stack.pop():
                    return False

        return stack == []




