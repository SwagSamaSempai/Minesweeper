from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

from cell import Cell

Builder.load_file('../src/kivy/gridlayout.kv')


class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)

        self.grid = GridLayout()
        self.cells = [Cell(x, y) for x in range(self.grid.cols) for y in range(self.grid.rows)]
        for cell in self.cells:
            self.grid.add_widget(cell)
