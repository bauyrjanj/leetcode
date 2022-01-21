class MaxStack:

    def __init__(self):
        self.d = []

    def push(self, x: int) -> None:
        self.d.append(x)

    def pop(self) -> int:

        return self.d.pop()

    def top(self) -> int:
        return self.d[-1]

    def peekMax(self) -> int:
        return max(self.d)

    def popMax(self) -> int:
        max_element = max(self.d)
        idx = 0
        for i, e in enumerate(self.d):
            if e == max_element:
                idx = i

        return self.d.pop(idx)

    