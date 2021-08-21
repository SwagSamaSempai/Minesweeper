from kivy.uix.button import Button


class Cell(Button):
    def __init__(self, x, y, **kwargs):
        super(Cell, self).__init__(**kwargs)
        self.x = x
        self.y = y
