from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Panel(BoxLayout):
    def click_me(Button):
        print("I'm a button")

class Test(App):
    def build(self):
        return Panel()
    

if __name__ == "__main__":
    """
    Run me, my dear friend!
    """
    Test().run()