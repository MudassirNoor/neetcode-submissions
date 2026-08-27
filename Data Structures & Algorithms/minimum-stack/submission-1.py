class MinStack:
    # Use the concept of State
    # In this design, each time we add a new value to the stack
    # we are tracking the minimum value within the stack at that specific length.
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
        
