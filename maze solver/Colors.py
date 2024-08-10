from enum import Enum

class Colors(Enum):
    BLACK = "black"
    RED = "RED"

    def __str__(self) -> str:
        return self.value
