from kivy.uix.screenmanager import ScreenManager

from game_screen import GameScreen
from options_screen import OptionsScreen


class MinesweeperManager(ScreenManager):
    def __init__(self, **kwargs):
        self.options_screen = OptionsScreen(name='options')
        self.game_screen = GameScreen(name='game')

        super().__init__(**kwargs)

        self.add_widget(self.options_screen)
        self.add_widget(self.game_screen)
