from kivy.uix.screenmanager import ScreenManager

from game_screen import GameScreen
from options_screen import OptionsScreen


class MinesweeperManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.options_screen = OptionsScreen(name='intro')
        self.add_widget(self.options_screen)
        self.game_screen = GameScreen(name='game')
        self.add_widget(self.game_screen)
