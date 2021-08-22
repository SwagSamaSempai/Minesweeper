from random import sample

from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

from cell import Cell

Builder.load_file('../src/kivy/grid_layout.kv')


class Grid(GridLayout):
    def __init__(self, width, height, bombs_count, **kwargs):
        self.cols = width
        self.rows = height
        self.cells = []

        super(Grid, self).__init__(**kwargs)

        bombs = sample(range(width * height), bombs_count)
        for y in range(height):
            row = []
            for x in range(width):
                cell = Cell(x, y)
                self.add_widget(cell)
                row.append(cell)
            self.cells.append(row)

        for index in bombs:
            y = index // width
            x = index % width
            self.cells[y][x].set_value('B')
            for x, y in self.cells[y][x].get_neighbors(width, height):
                self.cells[y][x].inc_value()

    def reveal_cell_rec(self, x, y):
        self.cells[y][x].reveal()
        if not self.cells[y][x].get_value():
            for col, row in self.cells[y][x].get_neighbors(self.cols, self.rows):
                if not self.cells[row][col].is_revealed():
                    self.reveal_cell_rec(col, row)
