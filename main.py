from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas:Canvas, fill_color="black"):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2)
    
class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Game")
        self.canvas = Canvas(self.root, width=width, height=height)
        
        self.canvas.pack(fill=BOTH, expand=True)
        self.window_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()

    def close(self):
        self.window_running = False

    def draw_line(self, line:Line, fill_color="black"):
        line: Line
        line.draw(self.canvas, fill_color)

class Cell():
    def __init__(self, x1, y1, x2, y2, win:Window, walls=[True, True, True, True]):
        self._x1, self._x2 = x1, x2
        self._y1, self._y2 = y1, y2
        self.visited = False
        self.walls = walls # top, right, bottom, left
        self._win = win

    def draw(self):
        if self.walls[0]:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), fill_color="black")
        if self.walls[1]:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), fill_color="black")
        if self.walls[2]:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), fill_color="black")
        if self.walls[3]:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), fill_color="black")

    def draw_move(self, to_cell, undo=False):
        centerOrigin = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        centerDestination = Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)
        lineMove = Line(centerOrigin, centerDestination)
        fill_color = "red" if not undo else "gray"
        self._win.draw_line(lineMove, fill_color)
        
def main():
    win = Window(800, 600)
    c1 = Cell(10, 10, 100, 100, win, [True, True, False, True])
    c1.draw()
    c2 = Cell(100, 10, 200, 100, win, [True, False, True, True])
    c2.draw()
    c1.draw_move(c2, False)
    win.wait_for_close()




if __name__ == "__main__":
    main()
    
