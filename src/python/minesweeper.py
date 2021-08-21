from kivy.app import App
from kivy.core.window import Window

from grid import Grid


class MinesweeperApp(App):
    def __init__(self, **kwargs):
        super(MinesweeperApp, self).__init__(**kwargs)

        self.window = Window
        self.window.fullscreen = 'auto'
        self.window.maximize()

    def build(self):
        return Grid().grid


if __name__ == '__main__':
    MinesweeperApp().run()
