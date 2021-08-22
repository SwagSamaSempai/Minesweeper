from kivy.uix.screenmanager import Screen

from grid import Grid


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)

    def start(self, width, height, bombs_count):
        self.add_widget(Grid(width, height, bombs_count))
