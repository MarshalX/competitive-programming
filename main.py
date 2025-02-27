class MinStack:
    def __init__(self):
        self._stack = []
        self._min = [float('inf')] * (10 ** 4)

    def push(self, val: int) -> None:
        self._stack.append(val)
        self._min[len(self._stack)] = min(val, self._min[len(self._stack) - 1])

    def pop(self) -> None:
        self._stack.pop()
        self._min[len(self._stack) + 1] = float('inf')

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min[len(self._stack)]
