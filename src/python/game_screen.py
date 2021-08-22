from kivy.uix.screenmanager import Screen


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.grid_width = None
        self.grid_height = None
        self.grid_bombs_count = None

    def start(self, width, height, bombs_count):
        self.grid_width = width
        self.grid_height = height
        self.grid_bombs_count = bombs_count
