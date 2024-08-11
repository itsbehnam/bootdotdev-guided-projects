from enum import Enum

class Colors(Enum):
    BLACK = "black"
    RED = "red"
    WHITE = "white"
    GRAY = "gray"

    BG = "white"

    def __str__(self) -> str:
        return self.value
