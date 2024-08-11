import time
from Cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self) -> None:
        self._cells = []
        for col in range(self.num_cols):
            new_col = []
            for row in range(self.num_rows):
                cell = Cell(window=self.win)
                new_col.append(cell)
            self._cells.append(new_col)

        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, I: int, J: int) -> None:
        start_x = self.x1 + I * self.cell_size_x
        end_x = start_x + self.cell_size_x
        start_y = self.y1 + J * self.cell_size_y
        end_y = start_y + self.cell_size_y
        self._cells[I][J].draw(start_x, start_y, end_x, end_y)
        if self.win:
            self._animate()

    def _animate(self) -> None:
        if self.win:
            self.win.redraw()
            time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
