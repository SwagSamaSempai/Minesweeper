from time import perf_counter

from kivy.uix.screenmanager import Screen

from end_popup import EndPopup
from grid import Grid


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.timer = None
        self.grid = None

    def start(self, height, width, bombs_count):
        self.grid = Grid(height, width, bombs_count)
        self.add_widget(self.grid)
        self.timer = perf_counter()

    def end_game(self, is_win):
        time = perf_counter() - self.timer
        EndPopup(is_win, time, self.manager).open()
        self.remove_widget(self.grid)
        self.grid = None
