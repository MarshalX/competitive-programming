class MinStack:
    def __init__(self):
        self._stack = []
        self._min = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        self._min.append(min(val, self._min[-1]) if self._min else val)

    def pop(self) -> None:
        self._stack.pop()
        self._min.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min[-1]
