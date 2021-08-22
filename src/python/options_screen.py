from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from src.python.options_popup import OptionsPopup

Builder.load_file('../src/kivy/options_screen.kv')
Window.size = (300, 600)


class OptionsScreen(Screen):
    width_input = ObjectProperty()
    height_input = ObjectProperty()
    bombs_count_input = ObjectProperty()

    def start_game(self):
        invalid_inputs = self.validate_inputs()
        if invalid_inputs:
            OptionsPopup(invalid_inputs).open()
            return

        self.manager.current = 'game'

    def validate_inputs(self):
        inputs = [self.width_input.text, self.height_input.text, self.bombs_count_input.text]
        return [f'{arg}\n' for arg in inputs if not (arg.isnumeric() and int(arg) > 0)]
