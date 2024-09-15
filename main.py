from graphics import Window
from maze import Maze
import argparse


def main():
    parser = argparse.ArgumentParser(description='Maze generator and solver')
    parser.add_argument('--seed', type=int, default=None, required=False)
    args = parser.parse_args()
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, args.seed)
    # ask the user to press enter to start the solving
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
