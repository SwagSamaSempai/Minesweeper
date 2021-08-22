from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

from cell import Cell

Builder.load_file('../src/kivy/grid_layout.kv')


class Grid(GridLayout):
    def __init__(self, width, height, bombs_count, **kwargs):
        self.cols = width
        self.rows = height

        super(Grid, self).__init__(**kwargs)

        self.cells = [Cell(x, y) for x in range(width) for y in range(height)]
        for cell in self.cells:
            self.add_widget(cell)
