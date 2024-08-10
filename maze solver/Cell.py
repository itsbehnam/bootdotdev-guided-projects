from Point import Point
from Line import Line
from Window import Window
from Colors import Colors

class Cell:
    def __init__(self, start: Point, end: Point) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = start.x
        self._y1 = start.y
        self._x2 = end.x
        self._y2 = end.y

    def draw(self, window: Window) -> None:
        if self.has_top_wall:
            start_point = Point(self._x1, self._y1)
            end_point = Point(self._x2, self._y1)
            top_line = Line(start_point, end_point)
            window.draw_line(top_line, Colors.BLACK)
        if self.has_right_wall:
            start_point = Point(self._x2, self._y1)
            end_point = Point(self._x2, self._y2)
            left_line = Line(start_point, end_point)
            window.draw_line(left_line, Colors.BLACK)
        if self.has_bottom_wall:
            start_point = Point(self._x1, self._y2)
            end_point = Point(self._x2, self._y2)
            bottom_line = Line(start_point, end_point)
            window.draw_line(bottom_line, Colors.BLACK)
        if self.has_left_wall:
            start_point = Point(self._x1, self._y1)
            end_point = Point(self._x1, self._y2)
            left_line = Line(start_point, end_point)
            window.draw_line(left_line, Colors.BLACK)
