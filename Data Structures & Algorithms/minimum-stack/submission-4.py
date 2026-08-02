class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
        

    def push(self, val: int) -> None:
        if len(self.stack):
            self.minStack.append(min(self.minStack[len(self.minStack) - 1], val))
        else:
            self.minStack.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        self.minStack.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        

    def getMin(self) -> int:
        return self.minStack[len(self.minStack) - 1]
        
