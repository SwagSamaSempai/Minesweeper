from kivy.app import App
from kivy.config import Config

Config.set('graphics', 'resizable', 0)


class MinesweeperApp(App):
    def build(self):
        from minesweeper_manager import MinesweeperManager
        return MinesweeperManager()


if __name__ == '__main__':
    MinesweeperApp().run()
