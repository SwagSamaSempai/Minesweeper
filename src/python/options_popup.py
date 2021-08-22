from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

Builder.load_file('../src/kivy/options_popup.kv')


class OptionsPopup(Popup):
    label = ObjectProperty()

    def __init__(self, invalid_inputs, **kwargs):
        super(OptionsPopup, self).__init__(**kwargs)

        self.label.text = f"These inputs are invalid:\n{''.join(invalid_inputs)}Use positive integers."
