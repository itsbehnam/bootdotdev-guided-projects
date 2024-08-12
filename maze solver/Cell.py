from typing import Self, Optional
from Point import Point
from Line import Line
from Window import Window
from Colors import Colors

class Cell:
    def __init__(self, start: Point = Point(None, None), end: Point = Point(None, None), window: Optional[Window] = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = start.x
        self._y1 = start.y
        self._x2 = end.x
        self._y2 = end.y
        self._win = window
        self.visited = False

    def draw(self, x1: Optional[int] = None, y1: Optional[int] = None, x2: Optional[int] = None, y2: Optional[int] = None) -> None:
        if self._win is None:
            return

        start_point = Point(x1, y1) if x1 and y1 else Point(self._x1, self._y1)
        end_point = Point(x2, y1) if x2 and y1 else Point(self._x2, self._y1)
        top_line = Line(start_point, end_point)
        color = Colors.BLACK.value if self.has_top_wall else Colors.WHITE.value
        self._win.draw_line(top_line, color)

        start_point = Point(x2, y1) if x2 and y1 else Point(self._x2, self._y1)
        end_point = Point(x2, y2) if x2 and y2 else Point(self._x2, self._y2)
        left_line = Line(start_point, end_point)
        color = Colors.BLACK.value if self.has_right_wall else Colors.WHITE.value
        self._win.draw_line(left_line, color)

        start_point = Point(x1, y2) if x1 and y2 else Point(self._x1, self._y2)
        end_point = Point(x2, y2) if x2 and y2 else Point(self._x2, self._y2)
        bottom_line = Line(start_point, end_point)
        color = Colors.BLACK.value if self.has_bottom_wall else Colors.WHITE.value
        self._win.draw_line(bottom_line, color)

        start_point = Point(x1, y1) if x1 and y1 else Point(self._x1, self._y1)
        end_point = Point(x1, y2) if x1 and y2 else Point(self._x1, self._y2)
        left_line = Line(start_point, end_point)
        color = Colors.BLACK.value if self.has_left_wall else Colors.WHITE.value
        self._win.draw_line(left_line, color)

    def draw_move(self, to_cell: Self, undo: bool=False) -> None:
        color = Colors.RED.value if undo else Colors.GRAY.value

        if self._x1 and self._x2 and self._y1 and self._y2 and to_cell._x1 and to_cell._x2 and to_cell._y1 and to_cell._y2 and self._win:
            src_center_x = (self._x1 + self._x2) // 2
            src_center_y = (self._y1 + self._y2) // 2

            dest_center_x = (to_cell._x1 + to_cell._x2) // 2
            dest_center_y = (to_cell._y1 + to_cell._y2) // 2

            src_point = Point(src_center_x, src_center_y)
            dest_point = Point(dest_center_x, dest_center_y)

            path_line = Line(src_point, dest_point)
            self._win.draw_line(path_line, color)
