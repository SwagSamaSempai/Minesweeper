from kivy.lang import Builder
from kivy.uix.button import Button

Builder.load_file('../src/kivy/cell.kv')


class Cell(Button):
    def __init__(self, x, y, **kwargs):
        self.x = x
        self.y = y
        self.value = 0

        super(Cell, self).__init__(**kwargs)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def set_value(self, value):
        self.value = value

    def inc_value(self):
        if isinstance(self.value, int):
            self.value += 1

    def show_value(self):
        self.text = str(self.value)

    def get_neighbors(self, width, height):
        for y in self.get_indices(self.y, height):
            for x in self.get_indices(self.x, width):
                yield x, y

    @staticmethod
    def get_indices(value, limit):
        indices = []
        if value > 0:
            indices.append(value - 1)
        indices.append(value)
        if value < limit - 1:
            indices.append(value + 1)
        return indices
