class CQueue:

    def __init__(self):
        self.at_stack, self.dh_stack = [], []

    def appendTail(self, value: int) -> None:
        self.at_stack.append(value)

    def deleteHead(self) -> int:
        if self.dh_stack:
            return self.dh_stack.pop()
        if not len(self.at_stack):
            return -1
        while self.at_stack:
            self.dh_stack.append(self.at_stack.pop())
        return self.dh_stack.pop()
