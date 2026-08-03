class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for num in tokens:
            if num == '+':
                stack.append(stack.pop() + stack.pop())
            elif num == '-':
                val1 = stack.pop()
                val2= stack.pop()
                stack.append(val2 - val1)
            elif num == '*':
                stack.append(stack.pop() * stack.pop())
            elif num == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/ a))
            else:
                stack.append(int(num))
        return stack[0]
        