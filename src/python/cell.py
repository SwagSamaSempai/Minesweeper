from kivy.lang import Builder
from kivy.uix.button import Button

Builder.load_file('../src/kivy/cell.kv')


class Cell(Button):
    def __init__(self, row, col, **kwargs):
        self.row = row
        self.col = col
        self.value = 0
        self.revealed = False

        super(Cell, self).__init__(**kwargs)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def inc_value(self):
        if isinstance(self.value, int):
            self.value += 1

    def reveal(self):
        self.revealed = True
        self.disabled = True
        if self.value:
            self.text = str(self.value)

    def is_revealed(self):
        return self.revealed

    def get_neighbors(self, height, width):
        for row in self.get_indices(self.row, height):
            for col in self.get_indices(self.col, width):
                if not (row == self.row and col == self.col):
                    yield row, col

    @staticmethod
    def get_indices(value, limit):
        indices = []
        if value > 0:
            indices.append(value - 1)
        indices.append(value)
        if value < limit - 1:
            indices.append(value + 1)
        return indices
