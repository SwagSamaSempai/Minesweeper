from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from src.python.cell import Cell

DEFAULT_BOMBS = 150
DEFAULT_WIDTH = 30
DEFAULT_HEIGHT = 30


class MinesweeperApp(App):
    def build(self):
        grid = GridLayout()
        grid.cols = DEFAULT_WIDTH
        grid.rows = DEFAULT_HEIGHT
        cells = [Cell(x, y) for x in range(grid.cols) for y in range(grid.rows)]
        for cell in cells:
            grid.add_widget(cell)
        return grid


if __name__ == '__main__':
    MinesweeperApp().run()
