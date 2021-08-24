from random import sample

from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

from cell import Cell

Builder.load_file('../src/kivy/grid_layout.kv')


class Grid(GridLayout):
    def __init__(self, height, width, bombs_count, **kwargs):
        self.rows = height
        self.cols = width
        self.cells = []
        self.to_reveal = height * width - bombs_count

        super(Grid, self).__init__(**kwargs)

        bombs = sample(range(height * width), bombs_count)
        for row in range(height):
            temp = []
            for col in range(width):
                cell = Cell(row, col)
                self.add_widget(cell)
                temp.append(cell)
            self.cells.append(temp)

        for index in bombs:
            row, col = divmod(index, width)
            self.cells[row][col].set_value('B')
            for row, col in self.cells[row][col].get_neighbors(height, width):
                self.cells[row][col].inc_value()

    def reveal_cell_rec(self, row, col):
        self.cells[row][col].reveal()
        if self.cells[row][col].get_value() == 'B':
            self.parent.end_game(False)
        self.to_reveal -= 1
        if not self.to_reveal:
            self.parent.end_game(True)
        if not self.cells[row][col].get_value():
            for row, col in self.cells[row][col].get_neighbors(self.rows, self.cols):
                if not self.cells[row][col].is_revealed():
                    self.reveal_cell_rec(row, col)
