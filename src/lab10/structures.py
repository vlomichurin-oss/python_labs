from collections import deque
from typing import Optional

class Stack: # LIFO data-structure - bigO: O(1) for any class-method
    def __init__(self):
        # internal storage for the stack
        self._data = []

    def push(self, item) -> None:
        self._data.append(item)

    def pop(self) -> any:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Optional[any]:
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)


class Queue: 
    def __init__(self):
        self._data = deque()

    def enqueue(self, item) -> None:
        self._data.append(item)

    def dequeue(self) -> any:
        if self.is_empty():
            raise IndexError('dequeue from empty queue')
        return self._data.popleft()

    def peek(self) -> Optional[any]:
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return not self._data
    def __len__(self):
        return len(self._data)