from cell import Cell
import random
import time


class Maze:
    """
    Represents a maze.
    Args:
        x1 (int): The x-coordinate of the top-left corner of the maze.
        y1 (int): The y-coordinate of the top-left corner of the maze.
        num_rows (int): The number of rows in the maze.
        num_cols (int): The number of columns in the maze.
        cell_size_x (int): The width of each cell in the maze.
        cell_size_y (int): The height of each cell in the maze.
        win (object, optional): The window object to draw the maze on. Defaults to None.
        rnd_seed (int, optional): The random seed to use for generating the maze. Defaults to None.
    Methods:
        solve(): Solves the maze.
    """
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, rnd_seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if rnd_seed is not None:
            random.seed(rnd_seed)
            

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        
    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        # Check if i can go left
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        # Check if i can go right
        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        # Check if i can go up  
        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        # Check if i can go down
        if j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        return False

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            neighbors = self._get_neighbors(i, j)
            if len(neighbors) == 0:
                self._draw_cell(i, j)
                return
            next_i, next_j = random.choice(neighbors)
            if i < next_i:
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            elif i > next_i:
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            elif j < next_j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            elif j > next_j:
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            self._draw_cell(i, j)
            self._draw_cell(next_i, next_j)

            self._break_walls_r(next_i, next_j)

    def _get_neighbors(self, i, j):
        neighbors = []
        if i > 0 and not self._cells[i - 1][j].visited:
            neighbors.append((i - 1, j))
        if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
            neighbors.append((i + 1, j))
        if j > 0 and not self._cells[i][j - 1].visited:
            neighbors.append((i, j - 1))
        if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
            neighbors.append((i, j + 1))
        return neighbors