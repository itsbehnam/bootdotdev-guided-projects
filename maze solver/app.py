from Window import Window
from Point import Point
from Line import Line

point_a = Point(0,0)
point_b = Point(50, 50)
line_a = Line(point_a, point_b)
win = Window(800, 600)
win.draw_line(line_a, "red")
win.wait_for_close()
