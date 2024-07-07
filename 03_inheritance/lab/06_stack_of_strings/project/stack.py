from typing import List


class Stack:

    def __init__(self) -> None:
        self.data: List[str] = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> str:
        last_element = self.data.pop()
        return last_element

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return False if self.data else True

    def __str__(self):
        return "[" + ', '.join(reversed(self.data)) + "]"


s = Stack()
print(s.is_empty())
print(s.data)
s.push('koko')
s.push('bam')
s.push('pi4')
print(s.__str__())
s.pop()
print(s.__str__())
