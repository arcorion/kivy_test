from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.graphics import *
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from pathlib import Path
from random import choice
import platform


operating_system = platform.system()
match operating_system:
    case 'Linux':
        Config.set('graphic', 'fullscreen', 'auto')
        Config.set('graphics', 'width', '800')
        Config.set('graphics', 'height', '480')
        Config.set('graphics', 'borderless', '1')
        Window.show_cursor = False
    case 'Windows':
        Window.size = (800, 480)
    case _:
        Exception("Not a supported OS")

Builder.load_file('kivy_test.kv')

class TouchPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(TouchPanel, self).__init__(**kwargs)

    def get_background(self):
        match operating_system:
            case 'Linux':   
                image_directory = Path.cwd() / 'images' / 'backgrounds'
            case 'Windows':
                image_directory = Path.cwd() / 'images' / 'backgrounds'
                #  image_directory = Path('C:/Users/Christopher/Projects/kivy_test/images/backgrounds')
                # image_directory = Path('C:/Users/Christopher/OneDrive - UW/Documents/Projects/kivy_test/images/backgrounds')
            case _:
                Exception("Not a supported OS")        
        
        background_list = [x for x in image_directory.iterdir()]
        return str(choice(background_list))


class TopBar(ToggleButton):
    """
    Top informational bar
    """
    def __init__(self, **kwargs):
        super(TopBar, self).__init__(**kwargs)


class Desktop(BoxLayout):
    """
    Main desktop compopent - contains everything except
    the TopBar
    """
    pass


class PowerInput(BoxLayout):
    """
    Contains the PowerButton and InputButtons
    """
    pass


class PowerButton(ToggleButton):
    pass


class InputButtons(GridLayout):
    """
    Contains the different InputButton widgets.
    """
    
    pass


class InputButton(ToggleButton):
    """
    Buttons used to toggle input
    """
    pass


class BlankSpace(Label):
    """
    Empty Label - provides blank space to make the interface
    more "roomy"
    """
    pass


class ImageButtons(BoxLayout):
    """
    Contains BlankButton and FreezeButton, as well
    as a blank for later use.
    """


class LaterUseBlank(Label):
    """
    Blank space set aside for later use, probably for the
    camera toggle.
    """
    pass


class BlankButton(ToggleButton):
    pass


class FreezeButton(ToggleButton):
    pass


class SoundControls(BoxLayout):
    """
    Contains VolumeLabel, VolumeSlider, and MuteButton
    """
    pass


class VolumeLabel(Button):
    pass


class VolumeSlider(Slider):    
    pass


class MuteButton(ToggleButton):
    pass


class Huskontroller(App):
    def build(self):
        return TouchPanel()


if __name__ == "__main__":
    """
    Run me, my dear friend!
    """
    Huskontroller().run()