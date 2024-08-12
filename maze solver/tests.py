import unittest
from Maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows -1].has_bottom_wall,
            False
        )
        self.assertTrue(
            all(
                m1._cells[col][row].visited is False for col in range(m1.num_cols) for row in range(m1.num_rows)
            )
        )

if __name__ == "__main__":
    unittest.main()
