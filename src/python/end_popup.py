from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

Builder.load_file('../src/kivy/end_popup.kv')


class EndPopup(Popup):
    label = ObjectProperty()

    def __init__(self, is_win, time, manager, **kwargs):
        super(EndPopup, self).__init__(**kwargs)
        self.manager = manager

        minutes, seconds = divmod(time, 60)
        if is_win:
            self.label.text = f"Congratulations! You won in {int(minutes)} minutes and {int(seconds)} seconds."
        else:
            self.label.text = f"Too bad! You lost after {int(minutes)} minutes and {int(seconds)} seconds."
