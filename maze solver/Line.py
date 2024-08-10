from Point import Point
from tkinter import Canvas

class Line:
    def __init__(self, point_a: Point, point_b: Point) -> None:
        self.x1 = point_a.x
        self.y1 = point_a.y
        self.x2 = point_b.x
        self.y2 = point_b.y
    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2)

