from kivy.lang import Builder
from kivy.uix.button import Button

Builder.load_file('../src/kivy/cell.kv')


class Cell(Button):
    def __init__(self, x, y, **kwargs):
        super(Cell, self).__init__(**kwargs)
        self.x = x
        self.y = y
