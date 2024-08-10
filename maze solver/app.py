from Window import Window
from Point import Point
from Line import Line
from Cell import Cell

point_a = Point(10,10)
point_b = Point(50, 50)
win = Window(800, 600)
cell = Cell(point_a, point_b, win)
cell.draw()
win.wait_for_close()
