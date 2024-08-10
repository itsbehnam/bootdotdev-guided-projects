from enum import Enum

class Colors(Enum):
    BLACK = "black"
    RED = "red"
    GRAY = "gray"

    def __str__(self) -> str:
        return self.value
