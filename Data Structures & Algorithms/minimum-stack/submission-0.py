class MinStack:

    def __init__(self):
        self._stack = []
        self._min_value_state = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        self._min_value_state.append(val if not self._min_value_state else min(self._min_value_state[-1], val))

    def pop(self) -> None:
        self._stack.pop()
        self._min_value_state.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_value_state[-1]
        
