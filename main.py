from tkinter import Tk, BOTH, Canvas

class Cell():
    def __init__(self, x1, y1, x2, y2, walls=[True, True, True, True]):
        self._x1, self._x2 = x1, x2
        self._y1, self._y2 = y1, y2
        self.visited = False
        self.walls = walls # top, right, bottom, left

    def draw(self, canvas:Canvas):
        if self.walls[0]:
            canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill="black", width=2)
        if self.walls[1]:
            canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill="black", width=2)
        if self.walls[2]:
            canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill="black", width=2)
        if self.walls[3]:
            canvas.create_line(self._x1, self._y1, self._x1, self._y2, fill="black", width=2)

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

    def draw_line(self, line, fill_color="black"):
        line: Line
        line.draw(self.canvas, fill_color)

def main():
    win = Window(800, 600)
    line = Line(Point(0,0), Point(800, 600))
    win.draw_line(line, "red")
    cell = Cell(10, 10, 100, 100, [False, True, True, True])
    cell.draw(win.canvas)

    win.wait_for_close()




if __name__ == "__main__":
    main()
    
