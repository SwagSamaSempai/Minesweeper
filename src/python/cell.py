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
