from collections import defaultdict
from typing import Any


class CallCount:
    def __init__(self) -> None:
        self._counts = defaultdict(int)
    
    def __call__(self, argument) -> Any:
        self._counts[argument] += 1
        return self._counts[argument]


cc = CallCount()

print(cc(1))
print(cc(2))
print(cc(1))
print(cc(1))
print(cc("something"))