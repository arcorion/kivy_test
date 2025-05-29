from kivy import App
from kivy.uix.boxlayout import BoxLayout

class Panel(BoxLayout):
    pass

class Test(App):
    def build(self):
        return Panel()
    

if __name__ == "__main__":
    """
    Run me, my dear friend!
    """
    Test().run()