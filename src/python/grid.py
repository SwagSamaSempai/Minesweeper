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
                if y * width + x in bombs:
                    cell.value = 'B'
                self.add_widget(cell)
                row.append(cell)
            self.cells.append(row)
