from tkinter import Tk, BOTH, Canvas
from Line import Line

class Window:
    def __init__(self, width, height) -> None:
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("Root widget")
        self.__root.protocol('WM_DELETE_WINDOW', self.close)
        self.__canvas = Canvas()
        self.__canvas.pack()
        self.__is_running = False

    def redraw(self) -> None:
        self.__canvas.update()
        self.__canvas.update_idletasks()

    def wait_for_close(self) -> None:
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.__canvas, fill_color)

    def close(self) -> None:
        self.__is_running = False

