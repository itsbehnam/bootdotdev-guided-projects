from typing import Self
from Point import Point
from Line import Line
from Window import Window
from Colors import Colors

class Cell:
    def __init__(self, start: Point, end: Point, window: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = start.x
        self._y1 = start.y
        self._x2 = end.x
        self._y2 = end.y
        self._win = window

    def draw(self) -> None:
        if self.has_top_wall:
            start_point = Point(self._x1, self._y1)
            end_point = Point(self._x2, self._y1)
            top_line = Line(start_point, end_point)
            self._win.draw_line(top_line, Colors.BLACK.value)
        if self.has_right_wall:
            start_point = Point(self._x2, self._y1)
            end_point = Point(self._x2, self._y2)
            left_line = Line(start_point, end_point)
            self._win.draw_line(left_line, Colors.BLACK.value)
        if self.has_bottom_wall:
            start_point = Point(self._x1, self._y2)
            end_point = Point(self._x2, self._y2)
            bottom_line = Line(start_point, end_point)
            self._win.draw_line(bottom_line, Colors.BLACK.value)
        if self.has_left_wall:
            start_point = Point(self._x1, self._y1)
            end_point = Point(self._x1, self._y2)
            left_line = Line(start_point, end_point)
            self._win.draw_line(left_line, Colors.BLACK.value)

    def draw_move(self, to_cell: Self, undo: bool=False) -> None:
        color = Colors.GRAY.value if undo else Colors.RED.value

        src_center_x = int(self._x1 / self._x2)
        src_center_y = int(self._y1 / self._y2)

        dest_center_x = int(to_cell._x1 / to_cell._x2)
        dest_center_y = int(to_cell._y1 / to_cell._y2)

        src_point = Point(src_center_x, src_center_y)
        dest_point = Point(dest_center_x, dest_center_y)

        path_line = Line(src_point, dest_point)
        self._win.draw_line(path_line, color)
